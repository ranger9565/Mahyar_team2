from backend.core.tasks import print_task, math_task


class TaskEngine:

    def __init__(self):

        self.registry = {
            "print": print_task.run,
            "math": math_task.run
        }

        self.tasks = []

    def load_tasks(self, plan: dict):
        self.tasks = plan.get("tasks", [])

    def run(self):
        results = []

        for task in self.tasks:
            results.append(self.execute_task(task))

        return results

    def execute_task(self, task: dict, request=None):

        task_type = task.get("type")

        handler = self.registry.get(task_type)

        if not handler:
            return {"error": f"No handler for {task_type}"}

        return handler(task)

