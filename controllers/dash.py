from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from flask_login import login_required
from models.task import Task

dash_bp = Blueprint("dash", __name__)

@dash_bp.route("/", methods=["GET"])
@login_required
def dashboard():
    query = request.args.get("q", "").lower()
    tasks = Task.all()
    if query:
        tasks = [t for t in tasks if query in t.title.lower() or query in t.description.lower()]
    return render_template("dashboard.html", tasks=tasks, query=query)

@dash_bp.route("/create", methods=["POST"])
@login_required
def create_task():
    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip()
    if title:
        Task.create(title, description)
    return redirect(url_for("dash.dashboard"))

@dash_bp.route("/edit/<int:task_id>", methods=["GET", "POST"])
@login_required
def edit_task(task_id):
    task = Task.get(task_id)
    if not task:
        return redirect(url_for("dash.dashboard"))

    if request.method == "POST":
        task.title = request.form.get("title", "").strip()
        task.description = request.form.get("description", "").strip()
        return redirect(url_for("dash.dashboard"))

    return render_template("edit_task.html", task=task)

@dash_bp.route("/delete/<int:task_id>")
@login_required
def delete_task(task_id):
    Task.delete(task_id)
    return redirect(url_for("dash.dashboard"))

@dash_bp.route("/api/tasks")
@login_required
def api_tasks():
    return jsonify([
        {
            "id": t.id,
            "title": t.title,
            "description": t.description,
            "date_created": t.date_created.isoformat()
        }
        for t in Task.tasks
    ])
