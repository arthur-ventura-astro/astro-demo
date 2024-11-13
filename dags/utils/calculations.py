from random import randint

batches = [i for i in range(5)]
bathces = [i for i in range(500)]

def compute_factor(factor=10):
    c, i = 0, 0
    while c < factor:
        h = hash(randint(0, 10_000_000))
        if str(h).startswith("0"):
            print("Tries:", i)
            c += 1
        i += 1

    return "Computation Ended!"
