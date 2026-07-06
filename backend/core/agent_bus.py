class AgentBus:

    def __init__(self):
        self.agents = {}

    def register(self, name, agent):
        self.agents[name] = agent

    def run(self, name, payload):

        agent = self.agents.get(name)

        if not agent:
            return {"error": f"Agent {name} not found"}

        return agent.run(payload)
