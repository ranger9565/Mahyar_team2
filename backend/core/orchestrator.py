from backend.utils.log_summarizer import LogSummarizer


class Orchestrator:

    def __init__(self):
        self.log_summarizer = LogSummarizer()

    def run(self, input_data):
        return {
            "status": "ok",
            "input": input_data
        }

    def process_log(self, log_text: str):
        return self.log_summarizer.summarize(log_text)
