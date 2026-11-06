# DevLoot Harness

**Build up an agent harness one decision at a time.**

This Python notebook starts with a basic Deep Agents invocation, then adds the context, tools, execution limits, specialist delegation, approval examples, and persistence needed to study a more capable agent loop. The final example saves conversation checkpoints to SQLite and reads the state back using a stable thread ID.

The notebook is the application. There is no separate web interface or deployed agent service.

## Walk through the notebook

| Stage | What it explores |
| --- | --- |
| Base agent | Model setup and a first invocation |
| Context | Filesystem-backed instructions and company/team skills |
| Execution | Model-call limits and task-list middleware |
| Tools and delegation | A customer lookup tool and proposal-review specialist |
| Boundaries | Permission declarations and approval interrupts |
| Memory | SQLite checkpoints, stable conversation IDs, and summarization |

## Setup

Use **Python 3.14+**, **uv**, and a notebook editor such as VS Code or Jupyter.

```sh
git clone https://github.com/p2arthur/devloot-harness.git
cd devloot-harness
uv sync
cp .env.example .env
```

Configure `ZAI_API_KEY` locally. The first model cell reads it from the kernel environment, so make it available before executing that cell. Selecting a `.venv` kernel does not automatically load `.env` into the process environment.

Open [`devloot-harness.ipynb`](devloot-harness.ipynb), select the project's `.venv` Python kernel, and run cells in order from the repository root. Install an editor-compatible notebook kernel in your local environment if your editor needs one.

The notebook currently uses `glm-5.3-flash` through the Z.ai coding endpoint. Model calls send prompts and tool results to that configured provider.

## Customer lookup

[`tools/customer.py`](tools/customer.py) defines `user_brief`, a parameterized PostgreSQL query for a user's recorded profile evidence. It loads `DATABASE_URL` from `.env` and expects the existing DevLoot `User` and `ProfileJudgment` schema.

The base model examples can be explored independently. Customer-tool examples require a compatible database and access to the data being queried; this repository does not provision that schema.

## Persistence and approval examples

The final section writes to `checkpoint/notebook.sqlite`. Reusing `thread_id="notebook-chat"` resumes the same stored conversation. Treat the checkpoint as local conversation data and keep it out of source control.

Permission declarations are teaching examples and still require application wiring. An `interrupt_on` declaration alone does not supply an approval interface: the caller must inspect the interrupt, collect a decision, and resume using the same checkpointer and thread ID. The notebook discusses this boundary; it is not a complete enforcement or approval system.

## Repository map

- [`devloot-harness.ipynb`](devloot-harness.ipynb): the walkthrough and model invocations.
- [`context/`](context/): sample agent instructions and skill files.
- [`tools/customer.py`](tools/customer.py): PostgreSQL-backed evidence lookup.
- [`pyproject.toml`](pyproject.toml) and `uv.lock`: Python requirements and dependency versions.

Credentials, checkpoints, and execution outputs belong in your local environment. Publish the source notebook with outputs cleared.
