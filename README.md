# Blog Project

This project is a simple blog application developed using **Django**. In this project, you can create, edit, and delete blog posts. You can also view each post. The front-end is built using only **HTML**, **CSS**, and **Bootstrap**. This is my first personal web application project.

## Features

- Create blog posts
- Edit blog posts
- Delete blog posts
- List and view blog posts
- User registration, login, and logout
- Commenting on blog posts

## Installation

To run this project on your local machine, follow these steps:

### 1. Clone the repository

```bash
git clone https://github.com/selimbugun/Django-Blog-App.git
cd blog
```

### 2. Create and Activate a Virtual Environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install the Required Packages

```bash
pip install -r requirements.txt
```

### 4. Set up the Database

To create the database, run the following commands:

```bash
python manage.py migrate
```

### 5. Start the Development Server

To run the project, use this command:

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

## Technologies Used

- **Backend:** Django
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite (Django's default database)
