"""
sync_portfolio_data.py
----------------------
Exports public GitHub repository metadata to projects.json so that
the negiadventures.github.io portfolio site can consume it directly.

Run by: .github/workflows/sync-portfolio.yml
"""

import json
import os
from datetime import datetime, timezone
from github import Github

# ── Configuration ────────────────────────────────────────────────────────────

GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
USERNAME = os.environ.get("GITHUB_USERNAME", "negiadventures")
OUTPUT_PATH = "projects.json"

# Projects to highlight at the top of the portfolio
FEATURED_SLUGS = [
    "market-summary-ai",
    "devspace-microservices",
    "slackbot_bedrock",
    "elasticsearch-helpers",
    "virtual-tryon",
    "network-curl-extension",
    "traffic-sign-detect-and-recognize",
    "predicting_hotel_availability",
]

# Category mapping (same logic as generate_stats.py)
CATEGORY_KEYWORDS: dict[str, list[str]] = {
    "AI & Data Systems": [
        "ai", "ml", "market", "bedrock", "slackbot", "analysis",
        "detection", "recognition", "predict", "pubmed", "neural",
    ],
    "Backend & Infrastructure": [
        "microservices", "elasticsearch", "devspace", "api",
        "kafka", "redis", "docker", "kubernetes",
    ],
    "Developer Tools": [
        "network", "extension", "cli", "readme", "dashboard", "tool",
    ],
    "Educational & Research": [
        "cs", "university", "algorithm", "pubmed", "getting",
        "course", "study", "learn",
    ],
    "Client Work & Freelance": [
        "fiverr", "zendesk", "challenge", "client",
    ],
}


def categorize(repo) -> str:
    text = (repo.name + " " + (repo.description or "")).lower()
    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(kw in text for kw in keywords):
            return category
    return "Backend & Infrastructure"


def serialize_repo(repo, featured: bool = False) -> dict:
    pushed = repo.pushed_at or repo.updated_at
    return {
        "name": repo.name,
        "full_name": repo.full_name,
        "description": repo.description or "",
        "url": repo.html_url,
        "homepage": repo.homepage or "",
        "language": repo.language or "",
        "topics": repo.topics,
        "stars": repo.stargazers_count,
        "forks": repo.forks_count,
        "open_issues": repo.open_issues_count,
        "is_fork": repo.fork,
        "is_archived": repo.archived,
        "created_at": repo.created_at.isoformat(),
        "updated_at": repo.updated_at.isoformat(),
        "pushed_at": pushed.isoformat(),
        "category": categorize(repo),
        "featured": featured,
    }


def main() -> None:
    g = Github(GITHUB_TOKEN)
    user = g.get_user(USERNAME)
    repos = list(user.get_repos(type="public", sort="updated", direction="desc"))

    featured_set = set(FEATURED_SLUGS)
    projects = [serialize_repo(r, featured=r.name in featured_set) for r in repos]

    # Sort: featured first, then by push date descending
    projects.sort(key=lambda p: (not p["featured"], p["pushed_at"]), reverse=False)

    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "username": USERNAME,
        "total_repos": len(projects),
        "projects": projects,
    }

    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2, ensure_ascii=False)

    featured_count = sum(1 for p in projects if p["featured"])
    print(
        f"✅ projects.json written — {len(projects)} repos "
        f"({featured_count} featured)"
    )


if __name__ == "__main__":
    main()
