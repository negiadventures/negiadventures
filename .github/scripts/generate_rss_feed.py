"""
generate_rss_feed.py
--------------------
Generates an Atom/RSS feed (feed.xml) from the user's public GitHub
repositories, sorted by most-recently pushed.

Run by: .github/workflows/generate-rss-feed.yml
"""

import os
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import format_datetime
from github import Github

# ── Configuration ────────────────────────────────────────────────────────────

GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
USERNAME = os.environ.get("GITHUB_USERNAME", "negiadventures")
FEED_PATH = "feed.xml"
MAX_ITEMS = 20

AUTHOR_NAME = "Anirudh Negi"
AUTHOR_EMAIL = "anirudh0993@gmail.com"
SITE_URL = "https://negiadventures.github.io"
GITHUB_URL = f"https://github.com/{USERNAME}"

# ── Helpers ───────────────────────────────────────────────────────────────────


def rfc2822(dt: datetime) -> str:
    """Return an RFC-2822 date string suitable for <pubDate>."""
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return format_datetime(dt)


def build_feed(repos) -> str:
    now = datetime.now(timezone.utc)

    rss = ET.Element("rss", version="2.0")
    rss.set("xmlns:atom", "http://www.w3.org/2005/Atom")

    channel = ET.SubElement(rss, "channel")

    ET.SubElement(channel, "title").text = f"{AUTHOR_NAME} — GitHub Projects"
    ET.SubElement(channel, "link").text = GITHUB_URL
    ET.SubElement(channel, "description").text = (
        "Latest public repositories and project updates from "
        f"{AUTHOR_NAME} ({USERNAME})"
    )
    ET.SubElement(channel, "language").text = "en-us"
    ET.SubElement(channel, "lastBuildDate").text = rfc2822(now)

    atom_link = ET.SubElement(channel, "atom:link")
    atom_link.set("href", f"{SITE_URL}/feed.xml")
    atom_link.set("rel", "self")
    atom_link.set("type", "application/rss+xml")

    for repo in repos[:MAX_ITEMS]:
        pushed = repo.pushed_at or repo.updated_at
        item = ET.SubElement(channel, "item")
        ET.SubElement(item, "title").text = repo.name
        ET.SubElement(item, "link").text = repo.html_url
        ET.SubElement(item, "guid", isPermaLink="true").text = repo.html_url
        ET.SubElement(item, "pubDate").text = rfc2822(pushed)
        desc_parts = [repo.description or "No description provided."]
        if repo.topics:
            desc_parts.append(f"Topics: {', '.join(repo.topics)}")
        if repo.language:
            desc_parts.append(f"Language: {repo.language}")
        desc_parts.append(f"Stars: {repo.stargazers_count}")
        ET.SubElement(item, "description").text = " | ".join(desc_parts)

    ET.indent(rss, space="  ")
    return '<?xml version="1.0" encoding="UTF-8"?>\n' + ET.tostring(
        rss, encoding="unicode"
    )


# ── Main ─────────────────────────────────────────────────────────────────────


def main() -> None:
    g = Github(GITHUB_TOKEN)
    user = g.get_user(USERNAME)
    repos = sorted(
        user.get_repos(type="public"),
        key=lambda r: r.pushed_at or r.updated_at,
        reverse=True,
    )

    feed_content = build_feed(repos)

    with open(FEED_PATH, "w", encoding="utf-8") as fh:
        fh.write(feed_content)

    print(f"✅ feed.xml generated with {min(len(repos), MAX_ITEMS)} items")


if __name__ == "__main__":
    main()
