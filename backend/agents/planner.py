class PlannerAgent:

    def run(self, task):
        text = task.get("input", "")

        return {
            "agent": "planner",
            "steps": [
                f"analyze: {text}",
                f"breakdown: {text}",
                f"plan execution: {text}"
            ]
        }

