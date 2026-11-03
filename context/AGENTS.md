# DevLoot

DevLoot helps people discover open source projects, find collaborators,
and contribute. AI tools support discovery, planning, and review.
Bounties let supporters fund specific GitHub issues through Algorand.

## Repository

- `client/`: React + Vite frontend.
- `server/`: NestJS API, Prisma/PostgreSQL, workers, and AI integrations.
- `contracts/`: Algorand bounty escrow contracts.
- `docs/`: Product, architecture, and operational documentation.

## Working conventions

- Read relevant code, docs, and local instructions before making changes.
- Keep solutions simple and focused. Avoid speculative abstractions and unrelated refactors.
- Follow existing patterns and preserve behavior unless the task requires changing it.
- Complete authorized work without repeatedly asking for confirmation.
- Ask when missing information materially affects scope or correctness.
- Preserve unrelated work. Never overwrite changes you did not make.
- Run checks appropriate to the change and report what was verified.
- Keep documentation aligned with behavior. Distinguish proposals, implemented code, and verified production behavior.
- Communicate clearly and concisely. Explain outcomes, meaningful tradeoffs, and remaining limitations.
- Never commit secrets, credentials, dumps, or generated execution reports.

## Services and integrations

- Reuse the existing `devloot` Docker Compose stack. Read
  `server/docs/local-docker.md` and inspect existing services first.
  Worktrees must use the canonical stack configuration.
- Start only necessary services. Do not create duplicate stacks or volumes,
  reset shared data, or stop services you did not start.
- Local work does not authorize production or Railway changes.
- For Stripe, use `--project-name devloot` and follow
  `docs/operations/stripe-access.md`. Verify account and mode before writes;
  live commands require explicit `--live`.
- Before discussing or changing GitHub authorization, read
  `docs/features/github-authorization.md`.
- For Slack, use only `slack_local`. Before every write, verify through a
  read-only identity call that the authenticated email is
  `arthur@letsroam.com`. Stop if verification fails.
- Send messages to others only when explicitly authorized.
