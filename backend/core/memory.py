from datetime import datetime


class Memory:

    def __init__(self):
        self.logs = []
        self.goals = []

    def add(self, user_input, tasks, results):

        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "input": user_input,
            "tasks": tasks,
            "results": results,
            "score": self._score(results)
        }

        self.logs.append(entry)

        # 🧠 extract implicit goals
        self._extract_goal(user_input)

    def _extract_goal(self, text):

        text = text.lower()

        if "build" in text:
            self.goals.append("build_system")

        if "optimize" in text:
            self.goals.append("optimize_pipeline")

        if "analyze" in text:
            self.goals.append("analysis_mode")

    def _score(self, results):

        score = 0

        for r in results:

            if isinstance(r, dict) and "error" in r:
                score -= 2
            else:
                score += 1

        return score

    def last(self, n=3):
        return self.logs[-n:]

    def goals_state(self):
        return list(set(self.goals))

