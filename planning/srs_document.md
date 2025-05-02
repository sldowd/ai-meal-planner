# Software Requirements Specification (SRS) – MVP

## 1. Introduction

### 1.1 Purpose
This document defines the functional and non-functional requirements for the AI-Assisted Meal Planner CLI application, built as an MVP for learning AI integration, data modeling, and CLI development.

### 1.2 Scope
The application will:
- Allow a single user to create and manage a dietary profile
- Generate a 7-day meal plan based on that profile
- Use the OpenAI GPT-4 API to generate plans in natural language
- Store meal plans in a local SQLite database
- Provide a CLI interface for interaction

### 1.3 Intended Audience
- Developer (you)
- Internship reviewers
- Future contributors (post-MVP)

---

## 2. Functional Requirements

### 2.1 User Profile
- User can input and update:
  - Name
  - Cooking skill level
  - Time per meal (in minutes)
  - Number of servings
  - Weekly budget
  - Dietary restrictions/preferences

### 2.2 Meal Plan Generation
- User selects "Generate Weekly Plan" from CLI menu
- System retrieves user preferences and formats an OpenAI prompt
- GPT-4 returns a natural-language meal plan for 7 days
- User can view and optionally save the plan to DB

### 2.3 Plan History
- User can view a list of previously saved meal plans
- User can select a plan to view full details

---

## 3. Non-Functional Requirements

- CLI-first, simple UX
- Uses `typer` or `rich` for CLI formatting
- SQLite used for local persistence
- GPT-4 prompt logic isolated in a service module
- Configurable `.env` file stores OpenAI key

---

## 4. External Interfaces

| Interface | Purpose |
|-----------|---------|
| `openai.ChatCompletion` | Meal plan generation |
| `sqlite3` / `sqlalchemy` | Local DB management |
| `dotenv` | API key config |
| `typer` | CLI framework |

---

## 5. Constraints
- Must run offline except for API calls
- Single-user only in MVP
- All data stored locally

---

## 6. Assumptions
- User has basic Python environment and API key setup
- Internet access available for GPT-4 usage

---

## 7. Future Features (Out of Scope for MVP)
- Multi-user profile support
- Nutrition scoring
- Shopping list generation
- Mobile or web frontend
- Plan export to PDF/Markdown

---

## 8. Glossary
- GPT: Generative Pre-trained Transformer
- API: Application Programming Interface
- CLI: Command Line Interface
- MVP: Minimum Viable Product

