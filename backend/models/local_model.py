from backend.models.base_model import BaseModel


class LocalModel(BaseModel):

    def __init__(self):
        super().__init__("local")

    def generate(self, prompt: str, context=None):
        return {
            "model": self.name,
            "output": prompt
        }

    def is_available(self):
        return True

