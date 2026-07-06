from backend.core.orchestrator import Orchestrator

orchestrator = Orchestrator()

result = orchestrator.route({
    "type": "plan",
    "input": "build AI orchestration system"
})

print(result)
