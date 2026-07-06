import json
from datetime import datetime


class Logger:

    def log(self, event_type: str, data: dict):

        entry = {
            "time": datetime.utcnow().isoformat(),
            "type": event_type,
            "data": data
        }

        print(json.dumps(entry, ensure_ascii=False))
