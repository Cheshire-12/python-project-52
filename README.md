# Task Manager
Task Manager is a task management system similar to Redmine. It allows users to create tasks, assign them to individuals, update task statuses, apply labels, and filter the task list based on any of these criteria. Using the system requires registration and authentication; guests can only view the home page and the list of users.

## 📊 Project status
| Tool | Status |
| :--- | :--- |
| **Hexlet tests** | [![Actions Status](https://github.com/Cheshire-12/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Cheshire-12/python-project-52/actions) |
| **Python CI and linter** | [![Python CI](https://github.com/Cheshire-12/python-project-52/actions/workflows/python-ci.yaml/badge.svg)](https://github.com/Cheshire-12/python-project-52/actions/workflows/python-ci.yaml) |
| **Quality gate status** | [![Quality gate status](https://sonarcloud.io/api/project_badges/measure?project=Cheshire-12_python-project-52&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=Cheshire-12_python-project-52) |
| **Coverage** | [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=Cheshire-12_python-project-52&metric=coverage)](https://sonarcloud.io/summary/new_code?id=Cheshire-12_python-project-52) |
| **Code smells** | [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=Cheshire-12_python-project-52&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=Cheshire-12_python-project-52) |

## 🌐 Public URL

The application is deployed and available online:
**[Task Manager on Render.com](https://python-project-52-xgjl.onrender.com/)**

---

## 🛠️ Tech Stack

* **Language & Core Framework:** Python 3.12+, Django
* **Package & Dependency Management:** `uv`
* **Database:** PostgreSQL (Production) / SQLite (Development)
* **Frontend & UI:** Bootstrap 5, `django-bootstrap5`
* **Static Files Serving:** WhiteNoise
* **Application Server:** Gunicorn
* **Filtering & Search:** `django-filter`
* **Error Tracking & Monitoring:** Rollbar (`rollbar`)
* **Linting & Code Formatting:** Ruff
* **Testing & Coverage:** Django TestCase Framework, Coverage.py
* **CI/CD & Code Quality:** GitHub Actions, SonarCloud / SonarQube Cloud
* **Deployment Platform:** Render.com

---

## Key Features

1. **User Management & Authentication**
   * Registration, Login, Logout.
   * Profile update and deletion with access permission checks (users can only manage their own profile).
2. **Task Management (CRUD)**
   * Creation, viewing, updating, and deletion of tasks.
   * Automatic assignment of task author upon creation.
   * Ability to assign an executor and set task descriptions.
3. **Statuses & Labels**
   * Customizable task statuses (e.g., *New*, *In Progress*, *Completed*).
   * Custom tags/labels for categorizing tasks.
   * Deletion protection: Statuses and labels linked to active tasks cannot be removed.
4. **Task Filtering**
   * Filter tasks by status, executor, label, or view only self-authored tasks ("My tasks only").
5. **Localization (i18n)**
   * Support for interface translation using Django's internationalization utilities.

---

## Prerequisites

Make sure you have the following installed on your local machine:
* **Python** (version 3.12 or higher)
* **uv** (fast Python package installer and dependency manager)

## Getting Started

### 1. Clone the repository
Choose one method:
1. SSH (Requires SSH key setup):
```bash
git clone git@github.com:Cheshire-12/python-project-52.git
```
2. HTTPS (universal):
```bash
git clone https://github.com/Cheshire-12/python-project-52.git
```
### 2. Install dependecies
```bash
uv sync
```
### 3. Environment variables configuration
Create a `.env` file in the root directory
Example configuration for `.env`:
```
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///db.sqlite3
ROLLBAR_ACCESS_TOKEN=your-rollbar-token
ROLLBAR_ENVIRONMENT=development
```
### 4. Apply database migrations
```bash
uv run python manage.py migrate
```
### 5. Run the development server
```bash
uv run python manage.py runserver
```
open http://127.0.0.1:8000 in your browser to access the application.

## Testing & Code Quality
### Running Tests
Execute the tests suite using Django test runner:
```bash
uv run python manage.py test
```
Or via Makefile
```bash
make test
```
### Checking Test Coverage
```bash
uv run coverage run manage.py test
uv run coverage report
```
### Lithing & Formatting with Ruff
Check code for issues
```bash
uv run ruff check .
```
Format code
```bash
uv run ruff format .
```