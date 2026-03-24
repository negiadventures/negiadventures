"""
generate_stats.py
-----------------
Generates GitHub repository statistics and updates the README.md
STATS-START / STATS-END section with a summary.

Run by: .github/workflows/update-readme-stats.yml
"""

import os
import re
from datetime import datetime, timezone
from github import Github

# ── Configuration ───────────────────────────────────────────────────────────

GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
USERNAME = os.environ.get("GITHUB_USERNAME", "negiadventures")
README_PATH = "README.md"

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

# ── Helpers ──────────────────────────────────────────────────────────────────


def categorize(repo) -> str:
    text = (repo.name + " " + (repo.description or "")).lower()
    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(kw in text for kw in keywords):
            return category
    return "Backend & Infrastructure"


def build_stats_block(repos) -> str:
    categories: dict[str, list] = {k: [] for k in CATEGORY_KEYWORDS}
    categories["Other"] = []

    for repo in repos:
        cat = categorize(repo)
        categories.setdefault(cat, []).append(repo)

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    total_stars = sum(r.stargazers_count for r in repos)

    lines = [
        f"<!-- Auto-generated on {now} -->",
        "",
        "### 📊 Repository Statistics",
        "",
        f"**Total Public Repositories**: {len(repos)} &nbsp;|&nbsp; "
        f"**Total Stars**: {total_stars}",
        "",
        "**Distribution by Category**:",
        "",
    ]

    for cat, cat_repos in categories.items():
        if cat_repos:
            lines.append(f"- **{cat}**: {len(cat_repos)} repos")

    lines += [
        "",
        "**Recently Updated**:",
        "",
    ]

    recent = sorted(repos, key=lambda r: r.pushed_at or r.updated_at, reverse=True)[:5]
    for repo in recent:
        updated = (repo.pushed_at or repo.updated_at).strftime("%b %d, %Y")
        lines.append(f"- [`{repo.name}`]({repo.html_url}) — {updated}")

    lines.append("")
    return "\n".join(lines)


# ── Main ─────────────────────────────────────────────────────────────────────


def main() -> None:
    g = Github(GITHUB_TOKEN)
    user = g.get_user(USERNAME)
    repos = [r for r in user.get_repos(sort="updated", direction="desc") if not r.fork]

    stats_block = build_stats_block(repos)

    with open(README_PATH, "r", encoding="utf-8") as fh:
        content = fh.read()

    updated = re.sub(
        r"<!-- STATS-START -->.*?<!-- STATS-END -->",
        f"<!-- STATS-START -->\n{stats_block}\n<!-- STATS-END -->",
        content,
        flags=re.DOTALL,
    )

    with open(README_PATH, "w", encoding="utf-8") as fh:
        fh.write(updated)

    print(f"✅ README stats updated ({len(repos)} repos, {sum(r.stargazers_count for r in repos)} stars)")


if __name__ == "__main__":
    main()
