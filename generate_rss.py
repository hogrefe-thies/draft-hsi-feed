import json
from datetime import datetime

# Load posts from the JSON file
with open('posts.json', 'r') as f:
    posts = json.load(f)

rss_header = """<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
    <channel>
        <title>Your RSS Feed Title</title>
        <link>https://username.github.io/my-rss-feed/</link>
        <description>Your feed description</description>
        <language>en-us</language>
        <lastBuildDate>{}</lastBuildDate>
""".format(datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT"))

rss_footer = """
    </channel>
</rss>
"""

rss_items = ""
for post in posts:
    rss_items += f"""
        <item>
            <title>{post['title']}</title>
            <link>{post['link']}</link>
            <description>{post['description']}</description>
            <pubDate>{post['pubDate']}</pubDate>
            <guid>{post['guid']}</guid>
        </item>
    """

# Write the RSS file
with open('rssfeed.xml', 'w') as f:
    f.write(rss_header + rss_items + rss_footer)
