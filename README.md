# TinyToDo Project

TinyToDo is a simple and clean to-do list web application built with **Flask**, **HTML**, and **CSS**. It allows users to create tasks, set due dates, assign categories and priority levels, mark tasks as completed, and delete them. All task data is stored locally in a JSON file so the app stays lightweight and easy to run.

---

##  Features

* Add tasks with:

  * Title
  * Due date
  * Category (School, Work, Home, Personal)
  * Priority (High, Medium, Low)
* Mark tasks as completed
* Delete tasks
* Persistent storage using `tasks.json`
* Modern, responsive UI
* Fully customizable CSS

---

##  Project Structure

project/
│── app.py
│── tasks.json
│── README.md
│
├── templates/
│   └── index.html
│
└── static/
  └── styles.css

---

##  Installation

### 1. Clone the repository

git clone <your-repo-url>
cd project

### 2. (Optional) Create a virtual environment

macOS / Linux:
python3 -m venv venv
source venv/bin/activate

Windows:
python3 -m venv venv
venv\Scripts\activate

### 3. Install dependencies

pip install flask

---

##  Running the Application

Start the Flask development server:
python3 app.py

Open your browser:
[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

##  Data Storage

All tasks are stored in **tasks.json**, automatically created when you run the app.


---

## 🚀 Future Improvements

* Edit task feature
* Search & filtering
* Drag-and-drop sorting
* User login system

<img width="1460" height="839" alt="Screenshot 2025-11-16 at 23 19 17" src="https://github.com/user-attachments/assets/33f90ebd-e409-466c-a2d3-190ba37681fe" />

---

## 📄 License

This project is for educational and personal use.
Feel free to modify and extend it.
