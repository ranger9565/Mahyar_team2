from backend.core.task_engine import TaskEngine
from backend.core.planner import PlannerAgent

planner = PlannerAgent()
engine = TaskEngine()

user_input = "hello and sum"

plan = planner.create_plan(user_input)

print("PLAN:")
print(plan)

engine.load_tasks(plan)

result = engine.run()

print("\nRESULT:")
print(result)
