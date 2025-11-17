from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

TASKS_FILE = "tasks.json"


def load_tasks():
    """Load tasks from JSON file."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_tasks(tasks):
    """Save tasks list to JSON file."""
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


@app.route("/", methods=["GET"])
def index():
    tasks = load_tasks()
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task():
    tasks = load_tasks()

    title = request.form.get("title", "").strip()
    due = request.form.get("due", "").strip()
    category = request.form.get("category", "").strip()
    priority = request.form.get("priority", "").strip()

    if title:
        tasks.append({
            "title": title,
            "done": False,
            "due": due or None,
            "category": category or "General",
            "priority": priority or "Medium",
        })
        save_tasks(tasks)

    return redirect(url_for("index"))


@app.route("/complete/<int:index>", methods=["POST"])
def complete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = not tasks[index].get("done", False)
        save_tasks(tasks)
    return redirect(url_for("index"))


@app.route("/delete/<int:index>", methods=["POST"])
def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
