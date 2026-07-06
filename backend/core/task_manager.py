class TaskManager:

    def create_tasks(self, user_input: str):

        text = user_input.lower()

        tasks = []

        # --- TOOL MODE ---
        if any(w in text for w in ["list", "read", "write", "file"]):

            tasks.append({
                "type": "execution",
                "content": user_input
            })

        # --- MODEL MODE ---
        else:

            tasks.append({
                "type": "direct",
                "content": user_input
            })

        return tasks

