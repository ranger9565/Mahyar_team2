class ModelRouter:

    def __init__(self, memory):
        self.memory = memory

    def route(self, content: str):

        text = content.lower()

        # 🧠 simple stable routing (no dependencies)
        if any(x in text for x in ["file", "read", "write", "list"]):
            model = "code_model"

        elif any(x in text for x in ["analyze", "design", "plan"]):
            model = "reasoning_model"

        else:
            model = "default"

        # 🧠 memory boost (optional logic)
        best = self.memory.best()

        if best and best.get("score", 0) > 5:
            model = "optimized_model"

        return {
            "model": model,
            "confidence": 0.7,
            "source": "stable_router"
        }
