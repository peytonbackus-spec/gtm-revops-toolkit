import os
import hmac
import hashlib
from fastapi import FastAPI, HTTPException, Depends, Request, Header
from pydantic import BaseModel
from build_gtm_system import SignalCaptureEngine, IntentSignal, setup_templates

app = FastAPI(title="GTM Signal Webhook Service")

HMAC_SECRET = os.getenv("GTM_HMAC_SECRET", "whsec_supersecretkey123")

async def verify_signature(request: Request, x_signature: str = Header(None)):
    if not x_signature:
        raise HTTPException(status_code=403, detail="Missing X-Signature header")

    body = await request.body()
    
    expected_signature = hmac.new(
        key=HMAC_SECRET.encode('utf-8'),
        msg=body,
        digestmod=hashlib.sha256
    ).hexdigest()

    provided_signature = x_signature.removeprefix("sha256=").strip()

    if not hmac.compare_digest(expected_signature, provided_signature):
        raise HTTPException(status_code=403, detail="Invalid HMAC signature")

vault_path = os.getcwd()
setup_templates(vault_path)
sig_engine = SignalCaptureEngine(vault_path)

class WebhookSignalPayload(BaseModel):
    company_name: str
    domain: str
    signal_type: str
    source: str
    raw_text: str
    impact_score: int

@app.post("/webhook/signal", dependencies=[Depends(verify_signature)])
async def receive_signal(payload: WebhookSignalPayload):
    try:
        signal = IntentSignal(
            company_name=payload.company_name,
            domain=payload.domain,
            signal_type=payload.signal_type,
            source=payload.source,
            raw_text=payload.raw_text,
            impact_score=payload.impact_score
        )
        file_path = sig_engine.process_signal(signal)
        return {"status": "success", "file_created": file_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
