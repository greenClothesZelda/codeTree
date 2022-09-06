class Merchandise:
    def __init__(self, name = "codetree", code = 50):
        self.name = name
        self.code = code

merchandises = []
merchandises.append(Merchandise())
merchandises.append(Merchandise(*tuple(input().split())))

for i in range(2):
    print(f"product {merchandises[i].code} is {merchandises[i].name}")
