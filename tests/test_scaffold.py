import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def test_scaffold_generates_runnable_repo():
    with tempfile.TemporaryDirectory() as tmp:
        dest = Path(tmp) / "acme"
        subprocess.run([sys.executable, str(ROOT / "scripts" / "new_company.py"), "Acme Corp",
                        "--dest", str(dest), "--fy-start-month", "1"], check=True, capture_output=True)
        cfg = (dest / "config" / "company.yaml").read_text()
        assert "name: Acme Corp" in cfg and "year_start_month: 1" in cfg
        assert not (dest / "config" / "example.yaml").exists()
        assert not (dest / "private-vault").exists()
        assert "Example Co" not in "".join(p.read_text() for p in dest.rglob("*.md"))
        r = subprocess.run([sys.executable, "-m", "gtm_engineer.lead_scoring.score_leads"],
                           cwd=dest, capture_output=True, text=True)
        assert r.returncode == 0 and "Acme Corp" in r.stdout
