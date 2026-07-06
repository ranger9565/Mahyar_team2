class Planner:

    def decompose(self, user_input: str):

        text = user_input.lower()
        tasks = []

        # 🧠 tool intent
        if any(x in text for x in ["list", "read", "write", "file"]):
            tasks.append({"type": "tool", "content": user_input})

        # 🧠 reasoning intent
        if any(x in text for x in ["analyze", "design", "build", "plan"]):
            tasks.append({"type": "print", "content": user_input})

        # 🧠 default fallback
        if not tasks:
            tasks.append({"type": "print", "content": user_input})

        return tasks

