class ToolParser:

    def parse(self, text):

        text = text.lower()

        # list files
        if "list" in text and "file" in text:
            return {"tool": "list_dir", "args": {}}

        # read file
        if "read file" in text:
            parts = text.split()
            if "file" in parts:
                i = parts.index("file")
                if i + 1 < len(parts):
                    return {
                        "tool": "read_file",
                        "args": {"path": parts[i + 1]}
                    }

        # write file
        if "write file" in text:
            return {
                "tool": "write_file",
                "args": {
                    "path": "output.txt",
                    "content": text
                }
            }

        return None

