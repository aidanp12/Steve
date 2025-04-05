import random

def roll(input):
    input = input.lower().split("d")
    rolls = int(input[0])
    dice = int(input[1])
    results = []
    for i in range(rolls):
        match dice:
            case "d2":
                results.append(random.randint(1, 2))
            case "d4":
                results.append(random.randint(1, 4))
            case "d8":
                results.append(random.randint(1, 8))
            case "d6":
                results.append(random.randint(1, 6))
            case "d10":
                results.append(random.randint(1, 10))
            case "d20":
                results.append(random.randint(1, 20))
            case "d50":
                results.append(random.randint(1, 50))
            case "d100":
                results.append(random.randint(1, 100))
            case _:
                return 0
    return sum(results)
