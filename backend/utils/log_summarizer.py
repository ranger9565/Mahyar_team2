class LogSummarizer:

    def summarize(self, log_text: str) -> dict:

        result = {
            "errors": [],
            "warnings": [],
            "success": [],
            "causes": []
        }

        for line in log_text.splitlines():

            l = line.lower().strip()

            if "error:" in l:
                result["errors"].append(l.split("error:")[1].strip())

            elif "failed" in l:
                result["errors"].append(l)

            elif "warning:" in l:
                result["warnings"].append(l)

            elif "successfully" in l:
                result["success"].append(l)

            elif "caused by" in l:
                result["causes"].append(l)

        return result
