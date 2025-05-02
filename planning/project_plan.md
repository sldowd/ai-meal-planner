# Project Plan – AI-Assisted Meal Planner (MVP Focus)

## 🎯 Goal
Deliver a functional CLI-based AI meal planning tool with user profiles, GPT-4 integration, and local data storage. The project is scoped for clarity, portfolio value, and personal growth in applied AI, software design, and CLI development.

---

## 🧭 MVP Timeline (6–8 Weeks Suggested)

### Week 1: Project Setup
- [x] Initialize repo, Git structure, and `.gitignore`
- [x] Write planning docs (SRS, user stories, DB schema)
- [x] Create `README.md` and planning folder

### Week 2: Core CLI Framework
- [x] Set up CLI with `typer`
- [x] Add main menu and routing logic
- [x] Implement profile creation and storage in DB

### Week 3: GPT Integration
- [ ] Build prompt generator from user preferences
- [ ] Connect to OpenAI API using `openai` lib
- [ ] Display results in clean format in CLI

### Week 4: Meal Plan Storage + Viewing
- [ ] Save meal plans to `meal_plans` table
- [ ] Add CLI view for past plans
- [ ] Enable plan regeneration

### Week 5: Error Handling + Polishing
- [ ] Add input validation, fallback messages
- [ ] Add color and layout polish using `rich`
- [ ] Create `.env.example` and usage docs

### Week 6: Testing + Wrap-Up
- [ ] Write minimal unit tests (DB logic, prompt formatting)
- [ ] Manual test user flow end-to-end
- [ ] Finalize `README.md` and project summary

---

## ✅ Key Deliverables
- `main.py` CLI entrypoint
- `cli/interface.py` for all user interaction
- `services/ai.py` for GPT logic
- `db/models.py` for SQLAlchemy ORM or raw SQL
- Planning folder with structured docs and diagrams

---

## 🧠 Stretch Goals (Optional)
- Auto-generate shopping list from plan
- Export plan to Markdown or PDF
- Support multiple profiles
- Add API test coverage

---

## 📌 Milestone Tags (Git)
| Tag | Description |
|-----|-------------|
| `v0.1.0-setup` | Repo initialized, docs written |
| `v0.2.0-cli` | CLI menu and profile complete |
| `v0.3.0-ai` | GPT-4 prompt integration functional |
| `v0.4.0-storage` | Plan save/view implemented |
| `v1.0.0-mvp` | Full CLI MVP done, polished, and documented |

---

## 🛠️ Tools
| Tool | Purpose |
|------|---------|
| `typer` | CLI interface management |
| `openai` | GPT-4 integration |
| `sqlite3` or `sqlalchemy` | Local database ORM |
| `python-dotenv` | Manage API key/env vars |
| `rich` | Styling output in CLI |
| `pytest` | Basic testing framework |

---

## ✅ Review Cycle
- Commit weekly progress to GitHub
- Use issues or a Notion doc to track feature work
- After MVP tag, decide: GUI next or feature expansion

