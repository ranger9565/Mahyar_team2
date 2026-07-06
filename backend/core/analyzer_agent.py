class AnalyzerAgent:

    def run(self, task: dict):

        text = task.get("input", "")

        return {
            "length": len(text),
            "words": len(text.split())
        }

