---
type: area
category: revops
tags:
  - area
  - outbound
  - deliverability
  - email
status: active
last_updated: 2026-10-29
---

# Outbound Deliverability Checklist

Module: `gtm_engineer/marketing_ops`. Pre-launch and ongoing checks for cold and sequenced email from [COMPANY_NAME]. Pairs with the [Outbound Campaign Review](Outbound_Campaign_Review.md), which covers weekly review and diagnosis once sending is live. Authentication and sending-limit rules change; check each provider's current published requirements before configuring production domains `[VERIFY]`.

## Executive Summary

Fix infrastructure before copy. Authenticate every sending domain, keep outreach on secondary domains, warm each mailbox, cap sending per mailbox, and watch bounce, spam and reply rates from day one. Stop sending when a rate crosses its floor.

## Provider reference rules (Gmail and Yahoo bulk-sender requirements)

| Rule | Requirement |
|---|---|
| Authentication | SPF and DKIM, plus DMARC with alignment |
| Unsubscribe | One-click unsubscribe, honored within 2 days |
| Spam rate | Under 0.3%, ideally under 0.1% |

Read the provider pages for the full list, such as who counts as a bulk sender and the exceptions `[VERIFY]`.

## 1. Domains

- [ ] Outreach runs on secondary domains, separate from the primary brand domain, so a reputation problem stays contained.
- [ ] Each secondary domain looks legitimate to a recipient who checks it (redirect or landing page to the brand site).
- [ ] Domain age and registration are recorded in the sending inventory.

## 2. Authentication (per sending domain)

- [ ] **SPF** record published and covers only the senders actually used.
- [ ] **DKIM** keys published and signing enabled for every mailbox provider and sending tool.
- [ ] **DMARC** record published, with alignment between the From domain and the SPF and DKIM domains. Start at monitoring and tighten the policy as reports come back clean.
- [ ] Send a test to each major mailbox provider and read the authentication result in the message headers.
- [ ] Re-test after any DNS change or any change of sending tool.

## 3. Mailboxes and warmup

- [ ] Several mailboxes per domain rather than a few at high volume.
- [ ] **Warmup** before real sending: start with low volume and raise it in steps, using inbox-warmup tooling or real, low-volume conversation.
- [ ] **Per-mailbox sending limits** set in the [SEQUENCER] and enforced there. Starting value: `[ASSUME]`. Change it only with evidence from your own rates.
- [ ] New sequences and new lists start small and ramp.

## 4. List and message hygiene

- [ ] Verify addresses before sending; suppress known bounces and role accounts.
- [ ] Honor opt-outs and complaints across all sending domains and tools.
- [ ] Include a working unsubscribe path and honor it within 2 days.
- [ ] Plain, specific copy; no tracking-heavy templates that look like bulk mail.
- [ ] Consent and identification rules for the recipient's region are met. Authentication does not equal legal consent.

## 5. Monitoring

Track weekly at least, by domain and by mailbox:

| Metric | Why |
|---|---|
| Bounce rate | Domain damage; stop sending above the floor in the [Outbound Campaign Review](Outbound_Campaign_Review.md) |
| Spam-complaint rate | Provider thresholds above; use postmaster tools where the provider offers them |
| Reply rate | Early sign of placement or targeting trouble |
| Blocklist status | Check each sending domain and IP on a schedule |

- [ ] Alert the owner when any rate approaches its floor, before it crosses.
- [ ] A mailbox or domain that crosses a floor is paused, not tuned live.

## 6. Incident steps

1. Pause the affected mailbox or domain.
2. Check authentication results first, then list quality, then volume, then copy.
3. Resume at low volume and ramp again.
4. Log what happened and what changed.
