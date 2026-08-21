import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

APOLLO_API_KEY = os.getenv("APOLLO_API_KEY")
HUBSPOT_API_KEY = os.getenv("HUBSPOT_API_KEY")

@app.route("/webhook/enrich-lead", methods=["POST"])
def enrich_lead():
    data = request.json
    email = data.get("email")
    contact_id = data.get("hubspot_contact_id")

    if not email or not contact_id:
        return jsonify({"error": "Missing email or contact_id"}), 400

    # Query Apollo API for enrichment data
    apollo_url = "https://api.apollo.io/v1/people/match"
    apollo_res = requests.post(
        apollo_url,
        json={"api_key": APOLLO_API_KEY, "email": email}
    )
    
    if apollo_res.status_code == 200:
        person = apollo_res.json().get("person", {})
        org = person.get("organization", {})

        # Update HubSpot properties
        hubspot_url = f"https://api.hubapi.com/crm/v3/objects/contacts/{contact_id}"
        payload = {
            "properties": {
                "jobtitle": person.get("title"),
                "company": org.get("name"),
                "annualrevenue": org.get("estimated_num_employees")
            }
        }
        headers = {"Authorization": f"Bearer {HUBSPOT_API_KEY}", "Content-Type": "application/json"}
        requests.patch(hubspot_url, json=payload, headers=headers)
        return jsonify({"status": "success", "enriched": True}), 200

    return jsonify({"error": "Apollo match failed"}), 400

if __name__ == "__main__":
    app.run(port=5000)
