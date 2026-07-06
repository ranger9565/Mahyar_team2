import os


class ToolRegistry:

    def __init__(self):

        self.tools = {
            "read_file": self.read_file,
            "write_file": self.write_file,
            "list_dir": self.list_dir
        }

    # --------------------
    # READ FILE
    # --------------------
    def read_file(self, path):
        try:
            with open(path, "r") as f:
                return f.read()
        except Exception as e:
            return {"error": str(e)}

    # --------------------
    # WRITE FILE
    # --------------------
    def write_file(self, data):

        try:
            path = data.get("path")
            content = data.get("content")

            with open(path, "w") as f:
                f.write(content)

            return {"status": "written", "path": path}

        except Exception as e:
            return {"error": str(e)}

    # --------------------
    # LIST DIR
    # --------------------
    def list_dir(self, path="."):
        try:
            return os.listdir(path)
        except Exception as e:
            return {"error": str(e)}

    # --------------------
    # RUN TOOL
    # --------------------
    def run(self, tool_name, payload=None):

        tool = self.tools.get(tool_name)

        if not tool:
            return {"error": "tool not found: " + tool_name}

        if payload:
            return tool(payload)

        return tool()
