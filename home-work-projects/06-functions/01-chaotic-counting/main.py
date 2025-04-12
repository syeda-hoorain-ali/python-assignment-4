import random

DONE_LIKELIHOOD = 0.2

def done():
    """ Returns True with a probability of DONE_LIKELIHOOD """
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    """Prints numbers from 1 to 10, but stops early if done() returns True."""
    for i in range(1, 11):
        if done():
            return
        print(i)


def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done")

if __name__ == "__main__":
    main()
