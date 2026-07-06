class PlannerAgent:

    def run(self, user_input: str):

        text = user_input.lower()
        tasks = []

        if any(x in text for x in ["list", "read", "write", "file"]):
            tasks.append({"type": "tool", "content": user_input})

        if any(x in text for x in ["analyze", "design", "plan"]):
            tasks.append({"type": "model", "content": user_input})

        if not tasks:
            tasks.append({"type": "model", "content": user_input})

        return tasks

