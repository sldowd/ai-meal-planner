# AI-Assisted Meal Planner CLI

A beginner-friendly Python project designed to help users create personalized weekly meal plans using AI (GPT-4). Built as a CLI application to demonstrate full-stack software engineering skills including data modeling, prompt design, API integration, and structured planning.

---

## 🎯 Project Goals
- Practice integrating AI with real-world logic
- Learn the SDLC from planning to implementation
- Showcase a CLI-first design with a long-term vision to migrate to web/mobile
- Build a professional-quality portfolio project

---

## ✅ MVP Scope (v1.0)
- [x] Create user profiles with dietary preferences
- [x] Generate meal plans via GPT-4 based on profile
- [x] Store plans locally in SQLite
- [x] View and regenerate past meal plans
- [x] Simple, intuitive CLI interface with `typer`

---

## 🧠 Technologies Used
| Layer         | Tool / Library         |
|---------------|------------------------|
| Language      | Python 3.10+           |
| CLI Interface | Typer or Rich          |
| Database      | SQLite + SQLAlchemy    |
| AI Engine     | OpenAI GPT-4 API       |
| Environment   | python-dotenv          |

---

## 📂 Folder Structure
```
meal-planner-cli/
├── main.py
├── cli/
│   └── interface.py
├── db/
│   └── models.py
├── services/
│   ├── ai.py
│   └── planner.py
├── requirements.txt
├── .env.example
├── planning/
│   ├── project_charter.md
│   ├── system_spec.md
│   └── ml_goals.md
└── tests/
    └── test_meal_planner.py
```

---

## 🚀 Getting Started
```bash
# Clone the repo
$ git clone https://github.com/YOUR_USERNAME/meal-planner-cli.git

# Create and activate a virtual environment
$ python -m venv venv
$ source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
$ pip install -r requirements.txt

# Run the app
$ python main.py
```

---

## 🌱 Future Scope (Post-MVP)
- Cloud-hosted backend (Supabase or Firebase)
- GUI app using Tauri or Tkinter
- Mobile-first version (React Native or Swift)
- Personalized meal scoring based on feedback
- Shopping list generation

---

## 📜 License
MIT License

---

> Built with ❤️ by [@sldowd](https://github.com/sldowd)

