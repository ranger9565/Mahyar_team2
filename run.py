from backend.core.orchestrator import Orchestrator

orch = Orchestrator()

print(orch.run("list files"))
print(orch.run("read file backend/core/orchestrator.py"))
print(orch.run("write file hello world"))
