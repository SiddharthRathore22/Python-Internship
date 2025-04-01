import Agent # type: ignore


Agent_1 = Agent.agent('shaktiman',32)
print(Agent_1.info())
Agent_1.health = Agent_1.health *100
print(Agent_1.health)
print('-'*30)

Agent_2 = Agent.agent('Sashi',200)
print(Agent_2.info())
print('-'*30)


Boss = Agent.agent('Shikhar',33)
print(Boss.info())
print('-'*30)
