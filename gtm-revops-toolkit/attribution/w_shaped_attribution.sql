-- W-Shaped Multi-Touch Attribution Model
-- Weights: 30% First Touch, 30% Lead Creation, 30% Opportunity Creation, 10% Middle Touches

WITH ranked_touches AS (
  SELECT
    opportunity_id,
    touchpoint_id,
    channel,
    touchpoint_type, -- 'first_touch', 'lead_creation', 'opp_creation', 'middle'
    created_at,
    COUNT(*) OVER (PARTITION BY opportunity_id) as total_touches
  FROM {{ ref('stg_marketing_touchpoints') }}
)
SELECT
  opportunity_id,
  touchpoint_id,
  channel,
  CASE
    WHEN touchpoint_type = 'first_touch' THEN 0.30
    WHEN touchpoint_type = 'lead_creation' THEN 0.30
    WHEN touchpoint_type = 'opp_creation' THEN 0.30
    ELSE 0.10 / NULLIF(total_touches - 3, 0)
  END AS w_shaped_weight
FROM ranked_touches;
