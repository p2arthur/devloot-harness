# DevLoot Harness

A notebook walkthrough of agent harness engineering with Deep Agents and LangGraph.

## Setup

1. Install Python 3.14 and uv, then run `uv sync`.
2. Copy `.env.example` to `.env` and configure your credentials locally.
3. Open `devloot-harness.ipynb` in Jupyter or VS Code and select this project's `.venv` Python kernel.
4. Make `ZAI_API_KEY` available in the kernel environment before the first model cell. The customer tool loads `DATABASE_URL` from `.env` and requires the existing DevLoot PostgreSQL schema.
5. Run cells in order. Model calls use the configured Z.ai endpoint; customer lookups query your configured database.

The notebook progresses through a base agent, context and skills, middleware,
subagents, tool integration, permission examples, approval interrupts, SQLite
checkpointing, summarization, and persisted conversations. It is a working
walkthrough: permission declarations and interrupt handling require application
wiring; declaring them alone does not enforce a complete approval workflow.

The final example writes checkpoints to `checkpoint/notebook.sqlite`. Reuse the
same `thread_id` to continue a saved conversation. Credentials, databases, and
notebook execution outputs are excluded from the published source.
