class DummyModel:

    def generate(self, prompt, context=None):
        return {
            "output": f"[MOCK_MODEL_RESPONSE] {prompt}",
            "context": context
        }


class ModelRegistry:

    def __init__(self):

        # 🧠 فقط برای تست سالم بودن سیستم
        self.models = {
            "default": DummyModel(),
            "code_model": DummyModel(),
            "reasoning_model": DummyModel(),
            "optimized_model": DummyModel()
        }

    def get(self, name: str):

        return self.models.get(name, self.models["default"])
