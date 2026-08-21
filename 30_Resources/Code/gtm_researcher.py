import os
import xml.etree.ElementTree as ET
from urllib.request import Request, urlopen
from datetime import datetime

vault = os.path.expanduser("~/GTM 2nd Brain")
research_dir = os.path.join(vault, "30_Resources/Research")
os.makedirs(research_dir, exist_ok=True)

date_str = datetime.now().strftime("%Y-%m-%d")
file_path = os.path.join(research_dir, f"GTM_Research_{date_str}.md")

# GTM & RevOps RSS Feeds
FEEDS = {
    "Sales Hacker": "https://www.saleshacker.com/feed/",
    "OpenView Insights": "https://openviewpartners.com/feed/",
    "TechCrunch Enterprise": "https://techcrunch.com/category/enterprise/feed/"
}

def fetch_feed_items(url, max_items=3):
    items = []
    try:
        req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(req, timeout=10) as response:
            xml_data = response.read()
            root = ET.fromstring(xml_data)
            
            # Handle standard RSS 2.0 channel -> item structure
            channel = root.find("channel")
            if channel is not None:
                for item in channel.findall("item")[:max_items]:
                    title = item.findtext("title", "No Title").strip()
                    link = item.findtext("link", "").strip()
                    pub_date = item.findtext("pubDate", "").strip()
                    items.append({"title": title, "link": link, "date": pub_date})
    except Exception as e:
        items.append({"title": f"Failed to fetch feed: {str(e)}", "link": "", "date": ""})
    return items

# Gather insights from all feeds
feed_sections = []
for feed_name, feed_url in FEEDS.items():
    articles = fetch_feed_items(feed_url)
    section_md = f"### {feed_name}\n"
    if articles:
        for art in articles:
            if art["link"]:
                section_md += f"- [{art["title"]}]({art["link"]})\n"
            else:
                section_md += f"- {art["title"]}\n"
    else:
        section_md += "- No recent updates available.\n"
    feed_sections.append(section_md)

all_feeds_content = "\n".join(feed_sections)

content = f"""---
type: resource
category: research
tags:
  - gtm
  - revops
  - research
date: {date_str}
status: automated
---

# GTM & RevOps Automated Intelligence Digest - {date_str}

## Live RSS Feed Ingestion

{all_feeds_content}

## Strategic Takeaways
* Check recent articles above for changes in PLG thresholds, sales capacity models, and attribution strategies.
* Automated ingestion completed at {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}.
"""

with open(file_path, "w") as f:
    f.write(content)

print(f"Created live RSS research note at {file_path}")
