# HouseAPP

<p align="center">
  **Making shared living easier, one household at a time.**
</p>

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-Framework-black)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue)
![Status](https://img.shields.io/badge/Project-In%20Development-orange)

---

## Table of Contents

1. [Overview](#overview)
2. [The Problem We Are Trying to Solve](#the-problem-we-are-trying-to-solve)
3. [Team Organization](#team-organization)
4. [MVP (Minimum Viable Product)](#mvp-minimum-viable-product)
5. [Tools and Technologies](#tools-and-technologies)
6. [Project Structure](#project-structure)
7. [Installation and Setup](#installation-and-setup)

---

## 1. Overview

Do you ever have problems with your roommates? You want to use the kitchen, but it is always busy and messy. You want to do your laundry, but someone is always using the washing machines. You want to take a shower in the morning, but the bathroom is always occupied.

It is crazy annoying, isn't it? It can make you not want to live with anyone at all.

With this app, we are going to try to give you the chance to solve all these problems, at least when it comes to the friction of living with other people.

## 2. The Problem We Are Trying to Solve

Housing is scarce and expensive nowadays, and not just in Eindhoven or the Netherlands. Most capitals and big cities around the world have a similar problem, and a lot of young people cannot afford an apartment on their own. They either have to share with someone or decide not to study.

With this app, we want to make sure that the decision to live with someone is not hard or stressful, but simply a choice, and a cheaper and simpler one.

About 90% of the problems of living with other people come down to organization. A house may have rules, but if nobody follows them, they are hard to enforce. Deciding who uses what and when can also take a lot of time and energy.

That is the problem this app tries to solve.

## 3. Team Organization

To organize the work, we are using Git and GitHub Projects. Everyone has their own version of the scheme we are working on, and each person works on a different part.

We created a backlog in GitHub Projects, and every week each person chooses what they want to work on. Once we finish the backlog, we discuss what we want to add and what ideas we have, and we add them to the backlog.

The goal is to reach an MVP by the end of this challenge. Nothing is static: if we want to change the colour or the design of the login page, we can always come back and make a version 2.

In general, the idea is to make progress on something new every week.

### Team Responsibilities

| Team Member | Responsibility |
|---|---|
| Malik | Frontend |
| Frank | Cybersecurity |
| David | Backend |
| Andres | Deployment and Backend |
| Linda | Database |

## 4. MVP (Minimum Viable Product)

For this 5-week sprint, we are aiming for a functional website where you can:

- Register and log in.
- Add rooms.
- Make complaints about other roommates.
- Make reservations for different spaces in the house.
- Make notes.

### Future Improvements

If we have time, we will build a mobile app and add more features related to the physical world, such as:

- Data from each room.
- Splitting the costs of utilities.

## 5. Tools and Technologies

We are all beginners in web development, but we have decided on the following tools:

| Area | Technology | Purpose |
|---|---|---|
| Backend | Python, Flask | Building the web application |
| Database | SQLite | Storing application data |
| Frontend | JavaScript, HTML, CSS, Bootstrap | Building the user interface |
| Prototyping | Figma | Designing and prototyping interfaces |
| Deployment | Fontys Edu Cloud | Hosting the website |

SQLite was chosen because it is easier for now to have a single file as the database in our project. If we have time, we might migrate to PostgreSQL.

We are going to host our website on Fontys Edu Cloud because it is free.

## 6. Project Structure

The project follows a modular structure using Flask Blueprints to separate different parts of the application.

```text
HouseAPP/
│
├── app/
│   ├── auth/
│   ├── dashboard/
│   ├── static/
│   ├── templates/
│   └── __init__.py
│
├── instance/
│   └── database.db
│
├── run.py
├── config.py
├── requirements.txt
└── README.md
```

### Application Modules

| Component | Description |
|---|---|
| `auth/` | Handles user authentication, including user registration, login and logout. |
| `dashboard/` | Manages the main dashboard and its functionality once users are logged in. |
| `static/` | Stores frontend assets such as CSS, JavaScript and images. |
| `templates/` | Contains the HTML templates rendered by Flask using Jinja2. |
| `__init__.py` | Initializes the Flask application, configures extensions and registers the application Blueprints. |

### Instance Folder

The `instance/` folder stores instance-specific application files.

- `database.db`: The SQLite database file where application data is stored, including user information and other records.

## 7. Installation and Setup

Follow these steps to run HouseAPP locally.

### Prerequisites

Make sure you have installed:

- Python 3.14.7
- Git

### 1. Clone the repository

```bash
git clone https://github.com/Andres-Fontys/Fontys-HousingAPP.git
cd HouseAPP
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python run.py
```

The application should now be running locally. Open the local address displayed in your terminal to access HouseAPP.

---

<p align="center">
  **HouseAPP — Better organization, better shared living.**
</p>
