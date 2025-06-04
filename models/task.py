from datetime import datetime

class Task:
    tasks = []
    id_counter = 1

    def __init__(self, title, description):
        self.id = Task.id_counter
        self.title = title
        self.description = description
        self.date_created = datetime.utcnow()
        Task.id_counter += 1

    @classmethod
    def create(cls, title, description):
        task = Task(title, description)
        cls.tasks.append(task)

    @classmethod
    def all(cls):
        return cls.tasks

    @classmethod
    def delete(cls, task_id):
        cls.tasks = [t for t in cls.tasks if t.id != task_id]

    @classmethod
    def get(cls, task_id):
        return next((t for t in cls.tasks if t.id == task_id), None)
