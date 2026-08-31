# Daily Outreach System

## The goal: 20 new contacts messaged every single day

At 20/day, 5 days/week = 400 prospects/month.
At 10% reply rate = 40 conversations.
At 25% call-book rate from replies = 10 discovery calls.
At 30% close rate = 3 new clients.

The math works — only if volume is consistent.

## Morning routine (90 min total)

### Step 1 — Signal scan (30 min)
- Check BetaKit Canada for this week's funding announcements
- Check TechCrunch Funding tag
- Search LinkedIn "Series A" posts from this week
- Check Crunchbase email alerts
- Any new B2B SaaS funding 10–100 employees = immediate outreach today

### Step 2 — Prospect research + HubSpot (45 min)
- Pull 10 prospects from LinkedIn Sales Nav or Apollo saved filters
- Find 5 with active buying signals
- Add all 10 to HubSpot with: company, title, signal noted, personalisation hook
- Note: Clay automates this entire step once the workflow is built

### Step 3 — Send today's outreach (45 min)
- 10 new contacts (from step 2) + 10 follow-ups (from HubSpot tasks)
- LinkedIn DMs for warm/signal-based contacts
- Email for cold contacts
- Max 30 LinkedIn DMs/day (restriction risk above this)
- Log every send in HubSpot immediately

## Midday (15 min) — Reply management
- Check LinkedIn + email for replies
- Positive reply: book call within 2 hours while they're warm
- Question: answer same day
- "Not now": move to 90-day nurture sequence in HubSpot
- "Not interested": mark closed, move on

## The Clay automation to build in week 2

Once first client is paying, build this workflow:
1. Source: Crunchbase webhook → new Series A/B funding, B2B SaaS, 10–150 employees
2. Enrich: Apollo → find CEO/CRO/VP Sales email + LinkedIn URL
3. Check: LinkedIn → does team have RevOps or SDR titles? (if not = hot signal)
4. Check: Apollo tech stack → confirm HubSpot in stack
5. AI: Claude API → write personalised first line from funding announcement
6. Push: HubSpot contact with all enrichment + personalised line in notes
7. Create: HubSpot task "Send outreach — [personalised line]" due today

Time saved: ~90 min/day. Cost: ~$30–50 CAD/mo in Clay credits.

