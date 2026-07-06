from backend.core.task_engine import TaskEngine
from backend.core.planner import Planner

planner = Planner()
engine = TaskEngine()

user_input = "hello and sum"

plan = planner.decompose(user_input)

print("PLAN:")
print(plan)

engine.load_tasks(plan)

result = engine.run()

print("\nRESULT:")
print(result)
