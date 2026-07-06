class BaseAgent:
    def __init__(self, name):
        self.name = name

    def run(self, task, model):
        """
        Execution contract:
        هر agent باید واقعاً پردازش انجام بده
        """
        raise NotImplementedError

