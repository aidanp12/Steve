import random

def diceRoll(input):
    input = input.lower().split("d")
    rolls = int(input[0])
    dice = int(input[1])
    results = []
    for i in range(rolls):
        match dice:
            case 2:
                results.append(random.randint(1, 2))
            case 4:
                results.append(random.randint(1, 4))
            case 6:
                results.append(random.randint(1, 6))
            case 8:
                results.append(random.randint(1, 8))
            case 10:
                results.append(random.randint(1, 10))
            case 20:
                results.append(random.randint(1, 20))
            case 50:
                results.append(random.randint(1, 50))
            case 100:
                results.append(random.randint(1, 100))
            case _:
                return 0
    return sum(results)
