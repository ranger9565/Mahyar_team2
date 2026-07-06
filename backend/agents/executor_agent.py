class ExecutorAgent:

    def __init__(self, router, registry, tool_manager, memory):
        self.router = router
        self.registry = registry
        self.tool_manager = tool_manager
        self.memory = memory

    def run(self, task):

        ttype = task["type"]
        content = task["content"]

        # 🧠 TOOL PATH
        if ttype == "tool":
            return self.tool_manager.run(content, {})

        # 🧠 MODEL PATH (memory-aware routing)
        decision = self.router.route(content)

        model = self.registry.get(decision["model"])

        result = model.generate(
            prompt=content,
            context={
                "memory": self.memory.last(3),
                "evolution": decision
            }
        )

        return result["output"]

