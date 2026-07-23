<div align="center">

# 🚀 First API Endpoint

### A production-style Flask + SQLite backend built for the FlyRank Backend AI Engineering Internship

[![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Status](https://img.shields.io/badge/Status-Complete-2ea44f?style=for-the-badge)](#)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](#-license)

**A minimal, well-tested REST API that evolved from a two-endpoint demo into a full, database-backed CRUD service — built to demonstrate the core request → response → persistence loop with clean, professional engineering practices.**

[Overview](#-overview) •
[Endpoints](#️-api-reference) •
[Getting Started](#-getting-started) •
[Database](#️-database-integration-sqlite) •
[Testing](#-testing--verification) •
[Author](#-author)

</div>

---

## 📌 Overview

This project sits on the **server side** of the request–response cycle. It began as a lightweight Flask app exposing two simple JSON endpoints, and has since grown into a complete **Task Management CRUD API** backed by a real **SQLite database** — the same journey every backend engineer takes from "hello world" to a persistent, production-shaped service.

Every endpoint has been independently verified through **browser testing**, **`curl`**, and **manual SQL inspection** in DB Browser for SQLite, so the behavior documented here is proven, not assumed.

| | |
|---|---|
| 🧩 **Type** | REST API |
| 🐍 **Language** | Python 3.13 |
| 🌶️ **Framework** | Flask 3.1 |
| 🗄️ **Database** | SQLite (file-based, zero-config) |
| 🧪 **Verified via** | Browser, curl, DB Browser for SQLite |
| 🎓 **Built for** | FlyRank Backend AI Engineering Track |

---

## 🗺️ API Reference

### Core Endpoints

| Method | Route | Description |
|:------:|-------|-------------|
| `GET` | `/` | Returns a welcome message |
| `GET` | `/status` | Returns developer and service status info |

### Task Endpoints (SQLite-backed CRUD)

| Method | Route | Description | Success | Errors |
|:------:|-------|-------------|:-------:|:------:|
| `GET` | `/tasks` | Returns every task | `200` | — |
| `GET` | `/tasks/<id>` | Returns a single task by ID | `200` | `404` |
| `POST` | `/tasks` | Creates a new task | `201` | `400` |
| `PUT` | `/tasks/<id>` | Updates an existing task | `200` | `400` `404` |
| `DELETE` | `/tasks/<id>` | Deletes a task | `204` | `404` |

**Request body example (`POST` / `PUT`):**
```json
{
  "title": "Buy milk",
  "done": false
}
```

**Error response shape:**
```json
{
  "error": "Task not found"
}
```

All write operations use **parameterized queries** (`?` placeholders) — no user input is ever concatenated into raw SQL, which protects the API against SQL injection.

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Technology |
|---|---|
| **Language** | Python 3.13 |
| **Web Framework** | Flask 3.1 |
| **Database** | SQLite 3 (`tasks.db`) |
| **Database Tooling** | DB Browser for SQLite |
| **Manual Testing** | Browser · `curl` |
| **Version Control** | Git + GitHub |

</div>

---

## 🚦 Getting Started

### Prerequisites

- Python **3.10+** installed
- `pip` package manager

### Installation

```bash
git clone https://github.com/Numair-Iqbal/first-api-endpoint.git
cd first-api-endpoint
pip install -r requirements.txt
```

### Run the Server

```bash
python app.py
```

The server starts at **`http://127.0.0.1:5000`**.

> On first run, `tasks.db` is created automatically, the `tasks` table is created if missing, and **three example tasks are seeded** — this only happens once, even across restarts.

### Try It Out

**Browser**
```
http://127.0.0.1:5000/
http://127.0.0.1:5000/status
http://127.0.0.1:5000/tasks
```

**curl**
```bash
curl http://127.0.0.1:5000/
curl http://127.0.0.1:5000/status
curl http://127.0.0.1:5000/tasks

# Create a task
curl -X POST http://127.0.0.1:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn SQL"}'

# Update a task
curl -X PUT http://127.0.0.1:5000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy milk", "done": true}'

# Delete a task
curl -X DELETE http://127.0.0.1:5000/tasks/1
```

---

## 📂 Project Structure

```
first-api-endpoint/
├── app.py                          # Flask application — routes, DB logic, and server entry point
├── requirements.txt                # Project dependencies
├── .gitignore                      # Excludes tasks.db and Python cache files
├── README.md                       # Project documentation (this file)
└── screenshots/                    # Verification evidence
    ├── Browser-Test-Home.png
    ├── Browser-Test-Status.png
    ├── Curl-Test-Output-1.png
    ├── Curl-Test-Output-2.png
    └── db-browser-tasks.png
```

---

## 🧪 Testing & Verification

Every layer of this API was tested independently, so correctness is demonstrated rather than assumed.

### 1️⃣ Browser Testing

| `GET /` | `GET /status` |
|:---:|:---:|
| ![Home endpoint](screenshots/Browser-Test-Home.png) | ![Status endpoint](screenshots/Browser-Test-Status.png) |

### 2️⃣ Command-Line Testing (`curl`)

| Request 1 | Request 2 |
|:---:|:---:|
| ![Curl output 1](screenshots/Curl-Test-Output-1.png) | ![Curl output 2](screenshots/Curl-Test-Output-2.png) |

### 3️⃣ Persistence Test

1. Start the server and visit `/tasks` — three seeded tasks appear.
2. Stop the server (`Ctrl+C`) and start it again (`python app.py`).
3. Visit `/tasks` again — **the same three tasks are still there**, and no duplicates were created.

This confirms the core promise of Assignment 2: *data now survives a restart*, because it lives on disk instead of in memory.

---

## 🗄️ Database Integration (SQLite)

This project evolved from an in-memory, two-endpoint demo into a fully persistent, database-backed CRUD API.

### Why SQLite?

- ✅ **No separate server** — the entire database is a single file
- ✅ **Zero configuration** — no installation, no setup
- ✅ **Perfect for small/medium projects** and local development
- ✅ **True persistence** — data now survives server restarts, unlike the original in-memory version

### Where the Database Lives

The database file `tasks.db` is created **automatically** on first run. It is excluded from version control via `.gitignore`, so every fresh clone starts with a clean database that reseeds itself automatically.

### Exploring the Database Manually

The database was opened directly in **DB Browser for SQLite** to run queries by hand and confirm that the API and the database file always stay in sync — there is no separate "syncing" step; both read the exact same source of truth.

**Example query executed:**
```sql
SELECT COUNT(*) FROM tasks;
```
**Result:** `3` — confirming the seed data was inserted correctly, and only once, even across multiple restarts.

**A second query was run to test live sync:**
```sql
UPDATE tasks SET done = 1 WHERE id = 1;
```
After clicking **"Write Changes"** in DB Browser, refreshing `http://127.0.0.1:5000/tasks` in the browser **immediately** reflected the updated value — with no server restart required.

### 📸 Database Opened in DB Browser for SQLite

![DB Browser Screenshot](screenshots/db-browser-tasks.png)

---

## 🧠 What This Project Demonstrates

- Building and testing a REST API from scratch with Flask
- Designing clean, predictable JSON request/response contracts
- Moving a storage layer from in-memory to a persistent SQL database **without changing the API surface**
- Writing safe, parameterized SQL to prevent injection attacks
- Verifying behavior through multiple independent testing methods (browser, curl, direct DB inspection)
- Following a disciplined, stage-by-stage Git commit history

---

## 👨‍💻 Author

<div align="center">

**Numair Iqbal**
Backend AI Engineering Intern @ FlyRank
BS Computer Science · University of Layyah

[![GitHub](https://img.shields.io/badge/GitHub-Numair--Iqbal-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Numair-Iqbal)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/numair-iqbal)

</div>

---

<p align="center">
Built as part of the <b>FlyRank AI Internship</b> — Backend AI Engineering Track
</p>
