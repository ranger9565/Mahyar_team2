import os


class ToolManager:

    def __init__(self):

        # 🧠 Tool Registry (به جای if)
        self.tools = {
            "list_dir": self.list_dir,
            "read_file": self.read_file,
            "write_file": self.write_file
        }

    # ---------------- FILE OPS ----------------

    def list_dir(self, path="."):
        return os.listdir(path)

    def read_file(self, path):
        try:
            with open(path, "r") as f:
                return f.read()
        except Exception as e:
            return {"error": str(e)}

    def write_file(self, path, content):
        try:
            with open(path, "w") as f:
                f.write(content)
            return {"status": "written", "path": path}
        except Exception as e:
            return {"error": str(e)}

    # ---------------- SMART TOOL SELECTOR ----------------

    def detect_tool(self, text: str):

        t = text.lower()

        # 🧠 scoring system (بدون if مستقیم)
        scores = {
            "list_dir": sum(k in t for k in ["list", "dir", "folder"]),
            "read_file": sum(k in t for k in ["read", "show", "open"]),
            "write_file": sum(k in t for k in ["write", "create", "save"])
        }

        best = max(scores, key=scores.get)

        if scores[best] == 0:
            return None

        return best

    # ---------------- EXECUTOR ----------------

    def run(self, text: str, payload=None):

        tool_name = self.detect_tool(text)

        if not tool_name:
            return {"info": "no tool matched"}

        if tool_name == "list_dir":
            return self.list_dir(".")

        if tool_name == "read_file":
            return self.read_file(payload.get("path", "backend/core/orchestrator.py"))

        if tool_name == "write_file":
            return self.write_file(
                payload.get("path", "test.txt"),
                payload.get("content", "hello world")
            )

