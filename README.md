# A movie recommender

Need a suggestion for a movie tonight?

```
pip install -r requirements.txt
uvicorn main:app --reload
```

and then hit `http://127.0.0.1:8000/movie`.

The goal of this repo is to showcase how you can evolve a simple kind of `hello web` app to something that you can consider production-ready.

# Production-ready checklist

We define a production-ready application is this way:

- Develop and deploy reliably (ideally by anyone at anytime)
- Onboard new developers easily
- Introspect the application at runtime
- Dependencies are well known, software and infrastructure
- Other systems can rely on it (APIs and availability)

This checklist contains some qualitative indicators that you can use to evaluate your current situation.

**They are not absolute and things can always be improved**.

You can also find a list of actionables for each so called `pillar`.

1. [Developer experience](#developer-experience)
2. [Automation](#automation)
3. [Documentation](#documentation)
4. [Observability](#observability)
5. [Stability](#stability)

## Developer experience

### Evaluation

- How do I run PostgreSQL on my machine?
- How do install project dependencies?
- How do I run tests?
- How do I run this project?

### Actions

- Use Docker compose
- Add a How-to-start to your README
- Use a Makefile
- Pre-commit
- Use Poetry for dependency manangement

## Automation

### Evaluation

- You make manual releases
- You don’t know when a release is broken
- You don’t know what has been released
- You can’t easily roll back
- You don’t trust your release process

### Actions

- Manual processes are banned
- healthchecks
- Build & linters & tests merge flow
- 1 (or 2) click release process
- Each commit is a docker image
- Infrastructure as code

## Documentation

### Evaluation

- Who are the users of this application?
- Production is broken, how do I debug it?
- What are the steps to run the application locally?
- Which systems are relying on this application?
- How do I create a release?
- What happens if the application goes down?

## Observability

- Proper README.md
- Always onboard new members through your doc
- Some effort 💪
- How to operate your application: doc/runbook.md
- How to debug things: doc/playbook.md
- How to do a release: doc/release.md

### Evaluation

- Your users know before you when the application is not working like expected
- Logs are not giving you enough information (or context)
- You can’t answer simple metric related question about your application (throughput, req/s, average latency, …)

### Actions

- Structured logging
- Alerts on top of your metrics and logs
- Metrics, start with something easy
- Tracing (app & apps)

## Stability

### Evaluation

- You’re paged too often
- People complain about you breaking APIs
- Uptime is terrible
- Doing a release is scary

### Actions

- Linters (isort, flake8, black, mypy)
- Follow a code review process
- Standardized release process
- Orchestrator for deployments (k8s, nomad, …)
- Schema first (GraphQL, OpenAPI, protobuf)
- Improve test coverage
