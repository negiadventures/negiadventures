# Implementation Guide

This document explains how to set up and use the automated GitHub profile
enhancement workflows included in this repository.

---

## Overview

Three GitHub Actions workflows keep the profile README, RSS feed, and portfolio
data fresh automatically:

| Workflow | Schedule | Output |
|----------|----------|--------|
| `update-readme-stats.yml` | Weekly (Sun 00:00 UTC) | Updates the `STATS-START/END` block in `README.md` |
| `generate-rss-feed.yml` | Daily (06:00 UTC) | Regenerates `feed.xml` |
| `sync-portfolio.yml` | Weekly (Sun 01:00 UTC) | Regenerates `projects.json` |

All workflows can also be triggered manually via **Actions → Run workflow**.

---

## Prerequisites

No additional secrets are required — all three workflows use the built-in
`GITHUB_TOKEN` that GitHub provides automatically.

> **Note:** The `GITHUB_TOKEN` has read access to public repositories by
> default. If you want to include private repo stats, add a Personal Access
> Token (PAT) with `repo` scope as a repository secret named `GH_PAT`, and
> update the workflow env block:
>
> ```yaml
> env:
>   GITHUB_TOKEN: ${{ secrets.GH_PAT }}
> ```

---

## File Structure

```
.
├── README.md                          # GitHub profile — auto-updated stats block
├── feed.xml                           # RSS feed — regenerated daily
├── projects.json                      # Portfolio data — regenerated weekly
├── IMPLEMENTATION_GUIDE.md            # This file
└── .github/
    ├── workflows/
    │   ├── update-readme-stats.yml    # Weekly README stats update
    │   ├── generate-rss-feed.yml      # Daily RSS feed generation
    │   └── sync-portfolio.yml         # Weekly portfolio data sync
    └── scripts/
        ├── generate_stats.py          # Stats generation logic
        ├── generate_rss_feed.py       # RSS feed generation logic
        └── sync_portfolio_data.py     # Portfolio JSON export logic
```

---

## Customising the Scripts

### `generate_stats.py`

Edit `CATEGORY_KEYWORDS` to adjust how repositories are grouped into categories.
Add or remove keywords to match your own project naming conventions.

### `generate_rss_feed.py`

- Change `MAX_ITEMS` (default: `20`) to control how many entries appear in the feed.
- Update `AUTHOR_NAME`, `AUTHOR_EMAIL`, and `SITE_URL` if deploying under a
  different identity.

### `sync_portfolio_data.py`

- Add repository slugs to `FEATURED_SLUGS` to mark them as `"featured": true`
  in `projects.json`.
- The portfolio site at `negiadventures.github.io` can fetch `projects.json`
  directly to populate its project grid.

---

## README Stats Block

The `README.md` contains a pair of HTML comments that act as delimiters:

```markdown
<!-- STATS-START -->
<!-- STATS-END -->
```

`generate_stats.py` replaces everything between these markers on each run.
Do **not** delete or rename these markers, or the script will stop updating.

---

## RSS Feed

`feed.xml` is a standard RSS 2.0 file.  You can subscribe to it with any feed
reader, or reference it from your portfolio site:

```html
<link rel="alternate" type="application/rss+xml"
      title="Anirudh Negi — Projects"
      href="https://raw.githubusercontent.com/negiadventures/negiadventures/main/feed.xml">
```

---

## Portfolio Data (`projects.json`)

`projects.json` follows this schema:

```jsonc
{
  "generated_at": "<ISO-8601 timestamp>",
  "username": "negiadventures",
  "total_repos": 44,
  "projects": [
    {
      "name": "repo-name",
      "full_name": "negiadventures/repo-name",
      "description": "...",
      "url": "https://github.com/negiadventures/repo-name",
      "homepage": "https://...",
      "language": "Python",
      "topics": ["tag1", "tag2"],
      "stars": 3,
      "forks": 0,
      "open_issues": 0,
      "is_fork": false,
      "is_archived": false,
      "created_at": "...",
      "updated_at": "...",
      "pushed_at": "...",
      "category": "AI & Data Systems",
      "featured": true
    }
  ]
}
```

---

## Running Scripts Locally

```bash
# Install dependencies
pip install PyGithub requests

# Set your token
export GITHUB_TOKEN="ghp_your_token_here"
export GITHUB_USERNAME="negiadventures"

# Run any script
python .github/scripts/generate_stats.py
python .github/scripts/generate_rss_feed.py
python .github/scripts/sync_portfolio_data.py
```

---

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| Workflow fails with `401 Unauthorized` | Token expired or missing | Ensure `GITHUB_TOKEN` is available; for private repos use a PAT |
| README stats not updating | `STATS-START`/`STATS-END` markers removed | Re-add the HTML comment markers to `README.md` |
| `feed.xml` shows old data | Workflow did not commit | Check if `git diff` saw no changes — trigger manually via Actions |
| `projects.json` missing repos | Repos are private | Use a PAT with `repo` scope instead of `GITHUB_TOKEN` |
