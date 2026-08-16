# Anirudh Negi | Backend & Distributed Systems Engineer

<div align="center">

![Profile Views](https://komarev.com/ghpvc/?username=negiadventures&color=0d7377&style=flat-square)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/anirudhnegi/)
[![Portfolio](https://img.shields.io/badge/-Portfolio-000000?style=flat-square&logo=github&logoColor=white)](https://negiadventures.github.io)
[![Email](https://img.shields.io/badge/-Email-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:anirudh0993@gmail.com)

**Distributed systems · Graph & relational data modeling · Large-scale ETL · AI-native engineering**

</div>

---

## About

Backend engineer, 8+ years, currently at **GoFundMe** building event-driven integration and the data
systems behind search and recommendations. I work on the parts that are expensive to get wrong: schema
and API contracts, failure semantics, and migration strategy.

Outside of work I architect and operate two live products, **[Utilix](https://utilix.tech)** and
**[Karyfy](https://karyfy.com)**, built almost entirely through agentic AI workflows with Claude Code.
I own the architecture, the data model, and the reliability; the agents write most of the code. It's the
most interesting engineering problem I've worked on lately: the bottleneck stops being implementation
speed and becomes the quality of your specification.

---

## Building

### 🛠️ [Utilix](https://utilix.tech) · the tool layer for developers and AI agents

One shared tool registry serving **six delivery surfaces** from a single implementation, so a tool is
specified once and its contract holds identically everywhere instead of drifting across per-surface
rewrites.

| | |
|---|---|
| **180+ tools** | one registry, one source of truth, growing daily |
| **6 surfaces** | web app · REST API · Node SDK · Python SDK · embeddable widget · MCP server |
| **130+ MCP tools** | Zod-validated, stdio · works in Claude Code, Claude Desktop, Cursor |
| **8K+** | npm downloads/month across published packages |

[![SDK](https://img.shields.io/npm/v/@utilix-tech/sdk?style=flat-square&label=%40utilix-tech%2Fsdk&color=22c55e)](https://www.npmjs.com/package/@utilix-tech/sdk)
[![MCP](https://img.shields.io/npm/v/@utilix-tech/mcp?style=flat-square&label=%40utilix-tech%2Fmcp&color=a855f7)](https://www.npmjs.com/package/@utilix-tech/mcp)
[![PyPI](https://img.shields.io/pypi/v/utilix-sdk?style=flat-square&label=utilix-sdk&color=3b82f6)](https://pypi.org/project/utilix-sdk/)

→ **[github.com/utilix-tech](https://github.com/utilix-tech)** · [docs](https://docs.utilix.tech)

### 🎯 [Karyfy](https://karyfy.com) · AI job-search platform *(live, beta)*

A hub-and-spoke multi-service system: a FastAPI hub exposing **250+ REST endpoints** and owning identity,
entitlement, and orchestration, in front of internal services for AI routing, resume curation, job
extraction, coaching, career planning, and a shared identity schema.

The piece I'd point at first is the **AI Gateway**. No product service calls a model provider directly.
It gives us provider abstraction over OpenAI and Anthropic with automatic failover, a versioned prompt
registry with a `draft → canary → active → deprecated` lifecycle, tier-aware model routing under timeout
budgets, structured-output schema validation with deterministic error codes, and per-request tracing and
cost estimation.

`FastAPI` · `React/TS` · `PostgreSQL` · `Redis` · `OpenSearch` · `Kubernetes/Helm` · `Clerk` · `Creem`

---

## Work

```
2016 ──────────────────────────────────────────────────────────── Present
 │
 ├─ 2016-2019 │ Software Engineer · Mediaocean · Pune, India
 │              ↳ ETL pipelines into Greenplum; incremental load + CDC
 │              ↳ SQL/query-plan optimization for live analytics dashboards
 │              ↳ Docker containerization of ETL workflows
 │              ↳ Awards: Rising Star, Brand Value
 │
 ├─ 2019-2021 │ Software Developer · SymphonyAI · Bangalore, India
 │              ↳ Decomposed sequential ETL into concurrent stages: hours to minutes
 │              ↳ Elasticsearch indexing strategy, custom analyzers & tokenizers
 │              ↳ Cluster sizing and shard optimization
 │              ↳ Mentored engineers on distributed search & indexing design
 │
 ├─ 2021-2022 │ MS Computer Science · Rutgers University, New Brunswick, NJ
 │              ↳ Award: Academic Excellence
 │
 ├─ 2022-2023 │ Senior Java Developer · Genentech (Roche) · Remote, US
 │              ↳ Salesforce → enterprise DB migration framework, idempotent + rollback
 │              ↳ Spring Batch optimization: 60% runtime reduction
 │              ↳ AWS infrastructure provisioning with Terraform
 │
 └─ 2023-NOW  │ Software Engineer II, Backend & Platform · GoFundMe · Remote, US
               ↳ Event-driven integration platform (schema, retry/DLQ, delivery guarantees)
               ↳ Neo4j property-graph data model + sync pipeline for a recommendation product
               ↳ ETL across 1.8M+ charities and 6M+ fundraisers
               ↳ Algolia search-index sync: 10+ hour run → 4 hours
               ↳ LLM-backed content generation shipped to production
               ↳ Award: SPOT
```

---

## Other Projects

| Project | Tech | Description |
|---------|------|-------------|
| [**openclaw-skills**](https://github.com/negiadventures/openclaw-skills) | Python | Reusable OpenClaw skills for agent workflows |
| [**devspace-microservices**](https://github.com/negiadventures/devspace-microservices) | TypeScript, K8s | Microservices deployment with DevSpace orchestration |
| [**slackbot_bedrock**](https://github.com/negiadventures/slackbot_bedrock) | AWS Bedrock, TS | LLM-powered Slack bot via AWS Bedrock |
| [**market-summary-ai**](https://github.com/negiadventures/market-summary-ai) | Python, LLM | Market summaries with AI-written news content |
| [**network-curl-extension**](https://github.com/negiadventures/network-curl-extension) | JavaScript | Browser extension for network debugging & curl generation |

---

## Stack

**Languages** &nbsp;
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![Kotlin](https://img.shields.io/badge/Kotlin-7F52FF?style=flat-square&logo=kotlin&logoColor=white)
![Java](https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-336791?style=flat-square&logo=postgresql&logoColor=white)

**Frameworks** &nbsp;
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Spring Boot](https://img.shields.io/badge/Spring%20Boot-6DB33F?style=flat-square&logo=spring-boot&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=next.js&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black)

**Data** &nbsp;
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=flat-square&logo=postgresql&logoColor=white)
![Neo4j](https://img.shields.io/badge/Neo4j-4581C3?style=flat-square&logo=neo4j&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white)
![Elasticsearch](https://img.shields.io/badge/Elasticsearch-005571?style=flat-square&logo=elasticsearch&logoColor=white)
![Kafka](https://img.shields.io/badge/Kafka-231F20?style=flat-square&logo=apache-kafka&logoColor=white)

**Cloud & Infra** &nbsp;
![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazon-aws&logoColor=FF9900)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=flat-square&logo=terraform&logoColor=white)
![Helm](https://img.shields.io/badge/Helm-0F1689?style=flat-square&logo=helm&logoColor=white)

**AI** &nbsp;
![Claude Code](https://img.shields.io/badge/Claude%20Code-D97757?style=flat-square&logo=anthropic&logoColor=white)
![MCP](https://img.shields.io/badge/MCP-000000?style=flat-square)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=openai&logoColor=white)
![AWS Bedrock](https://img.shields.io/badge/AWS%20Bedrock-FF9900?style=flat-square&logo=amazon-aws&logoColor=white)

---

## Stats

<div align="center">

[![GitHub Streak](https://github-readme-streak-stats.herokuapp.com?user=negiadventures&theme=github-dark-blue&hide_border=true)](https://github.com/negiadventures)

[![Top Languages](./stats/top-langs.svg)](https://github.com/negiadventures)

[![Anirudh's GitHub stats](./stats/github-stats.svg)](https://github.com/negiadventures)

</div>

<!-- STATS-START -->
<!-- Auto-generated on 2026-08-16 01:46 UTC -->

### 📊 Repository Statistics

**Total Public Repositories**: 40 &nbsp;|&nbsp; **Total Stars**: 11

**Distribution by Category**:

- **AI & Data Systems**: 8 repos
- **Backend & Infrastructure**: 16 repos
- **Educational & Research**: 8 repos
- **Client Work & Freelance**: 8 repos

**Recently Updated**:

- [`negiadventures`](https://github.com/negiadventures/negiadventures) — Aug 15, 2026
- [`negiadventures.github.io`](https://github.com/negiadventures/negiadventures.github.io) — Jul 26, 2026
- [`layover-games`](https://github.com/negiadventures/layover-games) — Apr 16, 2026
- [`openclaw-skills`](https://github.com/negiadventures/openclaw-skills) — Apr 10, 2026
- [`gamehub`](https://github.com/negiadventures/gamehub) — Apr 09, 2026

<!-- STATS-END -->

---

## Let's Connect

Happy to talk about backend architecture and scalability, graph and event-driven data systems, agentic
development workflows, or senior/staff engineering roles.

[![Email](https://img.shields.io/badge/anirudh0993@gmail.com-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:anirudh0993@gmail.com)
[![LinkedIn](https://img.shields.io/badge/linkedin.com/in/anirudhnegi-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/anirudhnegi/)
[![Portfolio](https://img.shields.io/badge/negiadventures.github.io-000000?style=flat-square&logo=github&logoColor=white)](https://negiadventures.github.io)
