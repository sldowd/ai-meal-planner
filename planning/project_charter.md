# Project Charter – AI-Assisted Meal Planner

## 🧭 Project Overview

Design and build a command-line application that generates personalized weekly meal plans using user preferences and OpenAI's GPT-4. The project aims to explore applied AI, data modeling, and full-stack CLI architecture.

---

## 🎯 Goals

* Create a user-friendly CLI app with persistent profiles
* Generate AI-based meal plans using prompt engineering
* Store plans locally with retrieval and regeneration
* Practice real software planning: architecture, requirements, testing

---

## 🔧 Project Scope (MVP)

* Single-user profiles stored in SQLite
* Profile preferences (diet, time, servings, skill level)
* GPT-4 used for natural language meal generation
* Store 7-day plans and allow review later
* CLI built using `typer` or `rich`

---

## ⛔ Out of Scope for MVP

* Shopping list generation
* Nutrition facts or calories
* Mobile or web frontend
* Multiple user accounts

---

## 🧑‍💻 Stakeholders

* Primary: You (Developer, Owner)
* Secondary: Recruiters, Reviewers (portfolio visibility)

---

## ⏳ Timeline Overview

* Week 1–2: Planning and CLI setup
* Week 3–4: AI integration and meal plan formatting
* Week 5–6: Plan history, error handling, polish

---

## ✅ Success Criteria

* Full CLI app runs locally and generates useful plans
* Clean codebase, modular structure, consistent CLI UX
* Planning folder with docs, Mermaid diagrams, and readme
* GitHub repo with milestone tags and clear commit history

---

## 🔮 Post-MVP Vision

* Cloud backend for hosting user data
* Shopping list exports
* Web frontend (Tauri or Flask)
* Feedback loop for plan scoring
