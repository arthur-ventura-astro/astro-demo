from random import randint

batches = [i for i in range(5)]
bathces = [i for i in range(50)]

def compute_factor(factor=2):
    expected = "0" * factor

    s, s_ = -1, 0
    while not str(s).startswith(expected):
        s = hash(randint(0, 10_000_000))
        if str(s).startswith("0"):
            print("Tries:", s_)
        s_ += 1

    return "Computation Ended!"
