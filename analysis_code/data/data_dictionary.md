# Data Dictionary

Dataset: `media_campaigns.csv`

Each row represents one advertising campaign for the fictional company Northstar Media.

| Column | Description | Example |
| --- | --- | --- |
| `campaign_id` | Unique campaign identifier | `CMP001` |
| `channel` | Media channel used by the campaign | `Streaming` |
| `cost_usd` | Campaign cost in US dollars | `8000` |
| `revenue_usd` | Revenue from the campaign in US dollars | `15200` |

The Python script adds one calculated field:

| Field | Formula |
| --- | --- |
| `profit_usd` | `revenue_usd - cost_usd` |
