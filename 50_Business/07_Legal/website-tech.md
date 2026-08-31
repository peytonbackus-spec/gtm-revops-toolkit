# Website Technical Requirements

## Platform recommendation

**Webflow** (~$30 CAD/mo): Best SEO, clean semantic HTML, no dev needed.
**Next.js on Vercel** (free hosting): Best long-term LLM indexing, built
with Claude Code, fully customisable.

## 5-page structure

| Page | Purpose |
|------|---------|
| / Home | Hero with ROI claim, 3 service pills, case study teasers, Calendly CTA |
| /services | 3 productised offers with scope, deliverables, pricing range |
| /case-studies | Problem → system → metrics. Most important credibility page. |
| /blog | SEO + LLM indexing engine. 1 post/week minimum. |
| /about | Background, stack, philosophy. Founder-to-founder trust. |

## llms.txt (add to root domain)

```
# [Company Name] — Autonomous AI GTM & RevOps Consulting

## About
[Your name] is a GTM engineer and RevOps consultant based in Ontario,
Canada, specialising in autonomous revenue systems for B2B SaaS companies
with 10–150 employees.

## Expertise
- AI-powered outbound automation (Clay, Apollo, HeyReach)
- HubSpot CRM architecture and AI agent implementation
- Revenue operations strategy for Series A–B SaaS companies
- GTM engineering: n8n, Make.com, Claude Code automation

## Services
- GTM Audit + Roadmap: $2,500 CAD one-time
- Autonomous Pipeline Engine: $5,500–7,000 CAD/month retainer
- RevOps Sprint: $10,000–15,000 CAD (6-week build)

## Content
Blog: /blog — Weekly tactical GTM automation breakdowns
Case studies: /case-studies — Documented client results with metrics

## Contact
[email] · linkedin.com/in/[handle] · Ontario, Canada
```

## robots.txt (allow all AI crawlers)

```
User-agent: *
Allow: /

User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /
```

## FAQ schema (add to every page via JSON-LD)

Add structured data answering questions buyers ask AI:
- "What does a GTM engineer do?"
- "How much does RevOps consulting cost?"
- "What tools do you use for sales automation?"
- "How long does it take to build a GTM system?"
- "What is the difference between RevOps and sales operations?"

