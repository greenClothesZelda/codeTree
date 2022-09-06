class Agent:
    def __init__(self, input_val):
        self.codeName = input_val[0]
        self.score = int(input_val[1])

agent = [
    Agent(tuple(input().split()))
    for _ in range(5)
]


min_index = 0

for i in range(5):
    if agent[i].score< agent[min_index].score:
        min_index = i
print(f"{agent[min_index].codeName} {agent[min_index].score}")