"""Generate the synthetic example dataset in sample_data/.

All accounts, people and numbers are FICTIONAL. Distributions are shaped to look
like a mid-market B2B SaaS business (two product lines, a partner channel,
POC-heavy enterprise cycles) so the scripts in both role tracks have realistic
patterns to find. Seeded, so output is reproducible.

The lookup tables below are keyed by the segment and persona names in
config/example.yaml. When you change segments or personas in your company
config, update the tables here too (a check at the bottom of the tables fails
fast if they drift).

    python scripts/generate_sample_data.py
"""
from __future__ import annotations

import csv
import random
import sys
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from shared_core.config import AS_OF, DATA_DIR, fiscal_quarter, load_config  # noqa: E402

rng = random.Random(42)
cfg = load_config()

# ----------------------------------------------------------------------------- reference lists
PREFIX = ["Harborview", "Summit Ridge", "Cedar Valley", "Blue Mesa", "Northgate", "Ironwood", "Lakeshore",
          "Granite Peak", "Riverbend", "Silverline", "Oakmont", "Prairie First", "Bayfront", "Copper State",
          "Evergreen", "Keystone", "Maple Leaf", "Tidewater", "Stonebridge", "Westfield", "Pinecrest",
          "Crescent", "Highland", "Redwood", "Sterling", "Union Square", "Clearwater", "Falcon", "Meridian", "Arbor"]
SUFFIX = {
    "enterprise": ["Global", "Holdings", "Group"],
    "upper_mid_market": ["Corp", "Industries", "Partners"],
    "mid_market": ["Systems", "Solutions", "Works"],
    "small_business": ["Co", "Studio", "Labs"],
    "vertical_a": ["Pay", "Cloud", "Stack", "Flow", "Neo"],
    "vertical_b": ["Market", "Exchange", "Hub", "Network"],
    "vertical_c": ["Play", "Media", "Games", "Live"],
    "adjacent": ["Health", "Insurance", "Mutual", "County Services"],
    "other": ["Consulting", "Agency", "Studio", "Collective"],
}
FIRST = ["Avery", "Jordan", "Morgan", "Riley", "Casey", "Quinn", "Taylor", "Jamie", "Drew", "Reese",
         "Skyler", "Cameron", "Rowan", "Hayden", "Emerson", "Parker", "Sage", "Blake", "Logan", "Kendall"]
LAST = ["Alder", "Brooks", "Calloway", "Dunmore", "Ellery", "Fairbanks", "Garrow", "Hollis", "Ingram", "Jessup",
        "Kestrel", "Lowry", "Marlow", "Nash", "Orwell", "Pruitt", "Quill", "Rourke", "Sutter", "Thorne"]
TITLES = {
    "exec_buyer_primary": ["VP, Revenue Operations", "Head of Revenue", "Director, Revenue Strategy"],
    "exec_buyer_security": ["CISO", "Director, IT Security", "VP Information Security"],
    "exec_buyer_digital": ["SVP Digital", "Head of Digital Products", "Director, Digital Channels"],
    "influencer_risk": ["Chief Risk Officer", "Compliance Officer", "Director, Risk & Controls"],
    "exec_buyer_ops": ["Head of Operations", "Director, Operations"],
    "champion_product": ["VP Product", "Head of Product, Platform", "Group PM, Core Platform"],
    "champion_practitioner": ["Operations Analyst", "Senior Operations Manager", "Operations Lead"],
    "blocker_procurement": ["Vendor Risk Manager", "IT Procurement Lead", "Enterprise Architect"],
    "unknown": ["Marketing Coordinator", "Student", "Consultant", "Office Manager"],
}
SDRS = ["SDR - Alex Rivera", "SDR - Bri Okafor", "SDR - Chen Wu", "SDR - Dana Lopes", "SDR - Eli Novak", "SDR - Fran Moretti"]
AES = {"NA": ["AE - Grace Tan", "AE - Hugo Park", "AE - Iris Bell", "AE - Jon Reyes"],
       "EMEA": ["AE - Klara Weiss", "AE - Liam Byrne"], "APAC": ["AE - Mei Lin"], "LATAM": ["AE - Nico Duarte"]}
PARTNER_MGR = "Partner Mgr - Olu Adeyemi"
LEAD_SOURCES = ["Website Chat", "Demo Request", "Webinar", "Content Download", "Paid Social", "Event",
                "Outbound - Enrichment", "Outbound - Social Selling", "Partner Referral"]
COMPETITORS = ["Competitor A", "Competitor B", "Competitor C", "In-house build", "None known"]

SEG_WEIGHTS = {"enterprise": 3, "upper_mid_market": 12, "mid_market": 12, "small_business": 14, "vertical_a": 18,
               "vertical_b": 8, "vertical_c": 7, "adjacent": 6, "other": 12}
SEG_PERSONAS = {
    "enterprise": ["exec_buyer_primary", "exec_buyer_security", "exec_buyer_digital", "influencer_risk", "champion_practitioner", "blocker_procurement"],
    "upper_mid_market": ["exec_buyer_primary", "exec_buyer_digital", "influencer_risk", "champion_practitioner", "blocker_procurement"],
    "mid_market": ["exec_buyer_digital", "exec_buyer_primary", "influencer_risk", "champion_practitioner"],
    "small_business": ["exec_buyer_digital", "exec_buyer_primary", "influencer_risk", "champion_practitioner"],
    "vertical_a": ["champion_product", "exec_buyer_primary", "influencer_risk", "exec_buyer_security"],
    "vertical_b": ["exec_buyer_ops", "champion_product", "champion_practitioner"],
    "vertical_c": ["influencer_risk", "exec_buyer_ops", "champion_product"],
    "adjacent": ["exec_buyer_security", "influencer_risk", "blocker_procurement"],
    "other": ["unknown", "unknown", "blocker_procurement"],
}
SIZE = {  # employees range by segment
    "enterprise": (20000, 200000), "upper_mid_market": (1500, 20000), "mid_market": (50, 1500),
    "small_business": (10, 300), "vertical_a": (30, 3000), "vertical_b": (50, 5000),
    "vertical_c": (50, 4000), "adjacent": (200, 30000), "other": (5, 500),
}
ACV = {  # (min, max) new-logo ACV by segment. [ASSUME] illustrative only
    "enterprise": (250_000, 900_000), "upper_mid_market": (80_000, 300_000), "mid_market": (25_000, 70_000),
    "small_business": (20_000, 65_000), "vertical_a": (40_000, 220_000), "vertical_b": (35_000, 150_000),
    "vertical_c": (50_000, 200_000), "adjacent": (30_000, 120_000), "other": (15_000, 40_000),
}
CORE_SEGMENTS = ("enterprise", "upper_mid_market", "mid_market", "small_business")  # where the core product line is sold
assert set(SEG_WEIGHTS) == set(SUFFIX) == set(SIZE) == set(ACV) == set(cfg["segments"]), "update tables for your segments"
assert set(TITLES) == set(cfg["personas"]), "update TITLES for your personas"
SIGNALS = list(cfg["lead_scoring"]["intent_signals"].keys())
STAGES = [s["name"] for s in cfg["opportunity"]["stages"]]
OPEN_STAGES = STAGES[:5]


def d(day: date) -> str:
    return day.isoformat() if day else ""


def pick_weighted(weights: dict) -> str:
    keys, w = zip(*weights.items())
    return rng.choices(keys, weights=w)[0]


def region_for(seg: str) -> str:
    if seg in ("mid_market", "small_business"):
        return "NA"
    return rng.choices(["NA", "EMEA", "APAC", "LATAM"], weights=[70, 20, 6, 4])[0]


# ----------------------------------------------------------------------------- accounts
accounts = []
used = set()
for i in range(450):
    seg = pick_weighted(SEG_WEIGHTS)
    for attempt in range(50):
        name = f"{rng.choice(PREFIX)} {rng.choice(SUFFIX[seg])}"
        if attempt > 30:
            name += f" {rng.randint(2, 99)}"   # name space exhausted for this segment: disambiguate
        if name not in used:
            used.add(name)
            break
    emin, emax = SIZE[seg]
    accounts.append({
        "account_id": f"ACC-{1000 + i}", "account_name": name, "segment": seg, "region": region_for(seg),
        "employees": rng.randint(emin, emax),
        "is_customer": seg != "other" and rng.random() < (0.45 if seg in CORE_SEGMENTS else 0.15),
        "products_owned": "",
    })
for a in accounts:
    if a["is_customer"]:
        a["products_owned"] = rng.choice(["core", "core", "addon", "core;addon"])

# ----------------------------------------------------------------------------- leads
leads = []
start = date(2026, 1, 5)
for i in range(900):
    acct = rng.choice(accounts)
    seg = acct["segment"]
    persona = rng.choice(SEG_PERSONAS[seg])
    created = start + timedelta(days=rng.randint(0, (AS_OF - start).days - 1))
    source = rng.choice(LEAD_SOURCES)
    partner = rng.choice([p["name"] for p in cfg["partners"]]) if source == "Partner Referral" else ""
    # intent signals with dates
    n_sig = rng.choices([0, 1, 2, 3, 4], weights=[20, 35, 25, 13, 7])[0]
    if source in ("Demo Request", "Website Chat"):
        n_sig = max(n_sig, 1)
    sigs = []
    for _ in range(n_sig):
        s = rng.choice(SIGNALS)
        if source == "Demo Request" and not sigs:
            s = "demo_request"
        if source == "Website Chat" and not sigs:
            s = "chat_engaged"
        sigs.append(f"{s}@{d(min(AS_OF, created + timedelta(days=rng.randint(0, 20))))}")
    fn, ln = rng.choice(FIRST), rng.choice(LAST)
    domain = acct["account_name"].lower().replace(" ", "").replace("&", "") + ".example"
    email = f"{fn.lower()}.{ln.lower()}@{domain}"
    if rng.random() < 0.03:
        email = f"{fn.lower()}{ln.lower()}@gmail.example"  # personal email (DQ issue)
    if rng.random() < 0.02:
        email = ""  # missing email (DQ issue)
    product_interest = rng.choice(["core", "addon"]) if seg in CORE_SEGMENTS else "addon"

    # hidden propensity drives the funnel so scoring has real signal to find
    seg_pts = cfg["segments"][seg]["icp_points"]
    per_pts = cfg["personas"][persona]["points"]
    strong = sum(1 for s in sigs if s.split("@")[0] in ("demo_request", "chat_engaged", "email_reply_positive", "pricing_page_visit"))
    # "True" propensity the scoring model is trying to learn. Two segments deliberately behave
    # differently from their configured weights (small businesses convert better via partners,
    # upper-mid-market slower) so calibrate_scoring.py has a real finding to surface.
    truth = {"small_business": 1.35, "upper_mid_market": 0.8}.get(seg, 1.0)
    fitness = truth * (seg_pts / 30) * (0.35 + 0.65 * per_pts / 25)
    p_mql = min(0.90, 0.01 + 0.55 * fitness + 0.10 * strong + 0.02 * len(sigs))
    p_sql = min(0.80, 0.02 + 0.45 * fitness + 0.08 * strong)
    p_opp = min(0.85, 0.15 + 0.45 * fitness + 0.05 * strong)
    age = (AS_OF - created).days

    status, mql, sal, sql, conv, dq = "New", None, None, None, None, ""
    hours_to_sal = ""
    if age > 2:
        status = "Enriching" if age < 4 else "New"
        if seg == "other" and rng.random() < 0.7:
            status, dq = "Disqualified", rng.choice(["Not ICP", "Student/Job Seeker", "Bad Data"])
        elif rng.random() < p_mql:
            mql = created + timedelta(days=rng.randint(0, 3))
            status = "MQL"
            hours_to_sal = rng.choice([1, 2, 3, 4, 6, 8, 20, 30, 50])
            if age > 3:
                sal = mql + timedelta(days=hours_to_sal // 24)
                status = "Working"
                if rng.random() < p_sql and age > 10:
                    sql = sal + timedelta(days=rng.randint(2, 16))
                    status = "SQL"
                    if rng.random() < p_opp and age > 14:
                        conv = sql + timedelta(days=rng.randint(0, 5))
                        status = "Converted"
                    elif age > 45:
                        status = "Recycled"
                elif age > 60:
                    status = rng.choice(["Recycled", "Disqualified"])
                    dq = rng.choice(cfg["lead_lifecycle"]["disqualify_reasons"]) if status == "Disqualified" else ""
        elif age > 30:
            status = "Recycled" if rng.random() < 0.6 else "Disqualified"
            dq = rng.choice(["Not ICP", "No Use Case", "Competitor"]) if status == "Disqualified" else ""
    region = acct["region"] if rng.random() > 0.03 else ""  # missing region (DQ issue)
    leads.append({
        "lead_id": f"L-{5000 + i}", "created_date": d(created), "first_name": fn, "last_name": ln, "email": email,
        "title": rng.choice(TITLES[persona]), "persona": persona, "company": acct["account_name"],
        "account_id": acct["account_id"], "segment": seg, "region": region, "employees": acct["employees"],
        "lead_source": source, "partner": partner,
        "product_interest": product_interest, "is_existing_customer": acct["is_customer"],
        "intent_signals": "|".join(sigs), "status": status, "mql_date": d(mql), "sal_date": d(sal),
        "mql_to_sal_hours": hours_to_sal if sal else "", "sql_date": d(sql), "converted_date": d(conv), "opportunity_id": "", "disqualify_reason": dq,
        "owner": rng.choice(SDRS) if mql else "Marketing Queue",
    })
# duplicate a few leads (DQ issue)
for dup in rng.sample(leads, 6):
    leads.append({**dup, "lead_id": f"L-{9000 + len(leads)}", "status": "New", "mql_date": "", "sal_date": "",
                  "sql_date": "", "converted_date": "", "mql_to_sal_hours": "", "owner": "Marketing Queue"})

# ----------------------------------------------------------------------------- opportunities
opps = []
acct_by_id = {a["account_id"]: a for a in accounts}


def make_opp(acct, otype, created, source, partner="", product_line=None, amount=None):
    seg = acct["segment"]
    lo, hi = ACV[seg]
    amount = amount or round(rng.uniform(lo, hi) * (0.5 if otype == "Expansion" else 1.0), -3)
    product_line = product_line or ("addon" if seg in ("vertical_a", "vertical_b", "vertical_c", "adjacent")
                                    else rng.choice(["core", "addon"]))
    cycle = int(rng.uniform(60, 200) * (1.6 if seg == "enterprise" else 1.0) * (0.7 if otype == "Renewal" else 1.0))
    close = created + timedelta(days=cycle)
    fit = cfg["segments"][seg]["icp_points"]
    contacts = rng.randint(1, 7)
    eb = rng.random() < 0.55
    p_win = -0.05 + fit / 150 + (0.12 if eb else -0.08) + 0.03 * min(contacts, 5) + (0.12 if otype == "Expansion" else 0)
    p_win = max(0.05, min(0.92, p_win))
    is_closed = close < AS_OF and rng.random() < 0.92
    stage, fc, won, lost_reason, competitor = None, None, False, "", rng.choice(COMPETITORS)
    if is_closed:
        won = rng.random() < p_win
        stage = "Closed Won" if won else "Closed Lost"
        fc = "Closed" if won else "Omitted"
        if not won:
            lost_reason = rng.choices(cfg["opportunity"]["closed_lost_reasons"], weights=[14, 22, 26, 6, 9, 10, 9, 4])[0]
        stage_entered = close
    else:
        elapsed = (AS_OF - created).days
        idx = min(4, max(0, int(elapsed / max(cycle, 1) * 5)))
        if close < AS_OF:  # slipped past close date, still open: a hygiene problem to detect
            idx = rng.randint(2, 4)
        stage = OPEN_STAGES[idx]
        fc = ["Pipeline", "Pipeline", "Best Case", "Best Case", "Best Case"][idx]
        if (idx == 4 and rng.random() < 0.40) or (idx == 3 and rng.random() < 0.08):
            fc = "Commit"
        stage_entered = AS_OF - timedelta(days=rng.randint(1, 55))
    last_activity = (stage_entered if is_closed else AS_OF - timedelta(days=rng.choice([1, 2, 3, 5, 8, 12, 18, 25, 40])))
    return {
        "opportunity_id": f"OPP-{7000 + len(opps)}", "account_id": acct["account_id"], "account_name": acct["account_name"],
        "segment": seg, "region": acct["region"], "type": otype, "product_line": product_line, "source": source,
        "partner": partner, "owner": rng.choice(AES[acct["region"]]), "amount": int(amount), "stage": stage,
        "forecast_category": fc, "created_date": d(created), "close_date": d(close), "stage_entered_date": d(stage_entered),
        "last_activity_date": d(last_activity), "contacts_engaged": contacts, "economic_buyer_engaged": eb,
        "poc_status": rng.choice(["Not Started", "In Progress", "Passed", "N/A"]) if STAGES.index(stage) >= 2 or is_closed else "Not Started",
        "security_review": rng.choice(["Not Started", "In Progress", "Complete"]) if STAGES.index(stage) >= 3 or is_closed else "Not Started",
        "next_step": "" if rng.random() < 0.15 else rng.choice(["Exec alignment call", "POC readout", "Security questionnaire", "Pricing review", "Legal redlines"]),
        "is_closed": is_closed, "is_won": won, "closed_lost_reason": lost_reason, "competitor": competitor,
        "originating_lead_id": "",
    }


for lead in leads:
    if lead["status"] == "Converted":
        acct = acct_by_id[lead["account_id"]]
        otype = "Expansion" if acct["is_customer"] else "New Logo"
        src = "Partner" if lead["partner"] else ("SDR" if lead["lead_source"].startswith("Outbound") else "Marketing")
        o = make_opp(acct, otype, date.fromisoformat(lead["converted_date"]), src, lead["partner"], lead["product_interest"])
        o["originating_lead_id"] = lead["lead_id"]
        lead["opportunity_id"] = o["opportunity_id"]
        opps.append(o)
# AE- and partner-sourced opps that never were leads
for _ in range(110):
    acct = rng.choice([a for a in accounts if a["segment"] != "other"])
    created = date(2025, 10, 1) + timedelta(days=rng.randint(0, 350))
    if acct["is_customer"] and rng.random() < 0.5:
        otype = "Expansion"
        owned = acct["products_owned"]
        pl = "addon" if owned == "core" else ("core" if owned == "addon" else rng.choice(["core", "addon"]))
    else:
        otype, pl = "New Logo", None
    src = "Partner" if acct["segment"] in ("mid_market", "small_business") and rng.random() < 0.6 else "AE"
    partner = rng.choice([p["name"] for p in cfg["partners"]]) if src == "Partner" else ""
    opps.append(make_opp(acct, otype, created, src, partner, pl))

# Seed a realistic amount of CRM mess so the data-quality monitor has something to catch.
open_early = [o for o in opps if o["stage"] in OPEN_STAGES[:2]]
for o in rng.sample(open_early, min(3, len(open_early))):
    o["forecast_category"] = "Commit"            # O05: rep commits a stage-1 deal
lost = [o for o in opps if o["stage"] == "Closed Lost"]
for o in rng.sample(lost, min(4, len(lost))):
    o["closed_lost_reason"] = ""                 # O03: no loss reason captured
partner_opps = [o for o in opps if o["source"] == "Partner"]
for o in rng.sample(partner_opps, min(2, len(partner_opps))):
    o["partner"] = ""                            # O07: partner attribution lost
dq_leads = [l for l in leads if l["status"] == "Disqualified" and l["disqualify_reason"]]
for l in rng.sample(dq_leads, min(5, len(dq_leads))):
    l["disqualify_reason"] = ""                  # L05: DQ'd with no reason

# ----------------------------------------------------------------------------- renewals
renewals = []
for acct in [a for a in accounts if a["is_customer"]]:
    for pl in acct["products_owned"].split(";"):
        lo, hi = ACV[acct["segment"]]
        arr = int(round(rng.uniform(lo, hi), -3))
        renewal_date = AS_OF + timedelta(days=rng.randint(-20, 300))
        trend = round(rng.gauss(4 if pl == "addon" else -3, 14), 1)  # [ASSUME] core usage flat-to-down, add-on growing
        r = {
            "account_id": acct["account_id"], "account_name": acct["account_name"], "segment": acct["segment"],
            "region": acct["region"], "product_line": pl, "arr": arr, "renewal_date": d(renewal_date),
            "volume_trend_90d_pct": trend, "utilization_pct": max(5, min(160, round(rng.gauss(85, 25)))),
            "sev1_tickets_90d": rng.choices([0, 1, 2, 3], weights=[70, 18, 8, 4])[0],
            "exec_sponsor_active": rng.random() < 0.75, "competitor_signal": rng.random() < 0.18,
            "products_owned": acct["products_owned"], "owner": rng.choice(AES[acct["region"]]),
        }
        renewals.append(r)

# ----------------------------------------------------------------------------- forecast snapshots
# The three completed fiscal quarters before AS_OF, labelled with the configured fiscal calendar.
def _add_months(d0: date, n: int) -> date:
    m = d0.month - 1 + n
    return date(d0.year + m // 12, m % 12 + 1, 1)


_sm = int(cfg.get("fiscal", {}).get("year_start_month", 1))
_cur = _add_months(date(AS_OF.year, AS_OF.month, 1), -((AS_OF.month - _sm) % 3))   # start of the current quarter
QUARTERS = {}
for _k in (3, 2, 1):
    _qs = _add_months(_cur, -3 * _k)
    QUARTERS[fiscal_quarter(_qs, _sm)] = (_qs, _add_months(_qs, 3) - timedelta(days=1))
BIAS = {"NA": 0.92, "EMEA": 1.12, "APAC": 1.05, "LATAM": 1.0}  # NA sandbags commit, EMEA over-calls
snapshots = []
for q, (qs, qe) in QUARTERS.items():
    for region in cfg["regions"]:
        actual = sum(o["amount"] for o in opps if o["is_won"] and o["region"] == region
                     and qs <= date.fromisoformat(o["close_date"]) <= qe and o["type"] != "Renewal")
        if actual == 0:
            continue  # no bookings in this region-quarter, so there's no forecast to grade
        for wk in range(13):
            progress = wk / 12
            noise = rng.gauss(0, 0.12 * (1 - progress))
            commit = actual * (BIAS.get(region, 1.0) + noise) * (0.88 + 0.12 * progress)
            snapshots.append({
                "quarter": q, "week": wk + 1, "snapshot_date": d(qs + timedelta(weeks=wk)), "region": region,
                "commit": int(commit), "best_case": int(commit * rng.uniform(1.2, 1.45)),
                "pipeline": int(commit * rng.uniform(2.2, 3.4)), "actual_closed_won": int(actual),
            })


def write(name, rows):
    DATA_DIR.mkdir(exist_ok=True)
    with open(DATA_DIR / name, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {len(rows):>4} rows -> sample_data/{name}")


if __name__ == "__main__":
    write("accounts.csv", accounts)
    write("leads.csv", leads)
    write("opportunities.csv", opps)
    write("renewals.csv", renewals)
    write("forecast_snapshots.csv", snapshots)
