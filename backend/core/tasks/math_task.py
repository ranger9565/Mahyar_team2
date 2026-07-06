def run(task: dict):
    expr = task.get("expression", "")
    try:
        return eval(expr)
    except Exception as e:
        return {"error": str(e)}

