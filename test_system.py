from backend.core.orchestrator import Orchestrator


def run_tests():

    orch = Orchestrator()

    test_cases = [
        "list files",
        "read file backend/core/orchestrator.py",
        "write file hello world",
        "analyze system structure",
        "design agent pipeline"
    ]

    for i, t in enumerate(test_cases):

        print("\n" + "="*50)
        print(f"TEST {i+1}: {t}")
        print("="*50)

        result = orch.run(t)

        print("\nRESULT:")
        print(result)


if __name__ == "__main__":
    run_tests()
