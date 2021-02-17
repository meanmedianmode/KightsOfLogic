from logic import *

# Puzzle
# A says "I am both a knight and a knave."
# One character : A => A is a Knave
AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

# Facts about our world: XOR
InitialKnowledge = And(
    # Must be either a knight or a knave
    Or(AKnight, AKnave), 
    # Can't be both a knight and a knave
    Not(And(AKnight, AKnave)),
)

# What we're told by the character
InitialStatment = And(AKnight, AKnave)


# If the character is a knave, 
# we know there statement must be False
KnaveLie = Biconditional(AKnave, Not(InitialStatment))

knowledge = And(
    InitialKnowledge,
    KnaveLie,
)


def main():
    symbols = [AKnight, AKnave]
    if len(knowledge.conjuncts) == 0:
        print("Not yet implemented.")
    else:
        for symbol in symbols:
            if model_check(knowledge, symbol):
                print(f"    {symbol}")


if __name__ == "__main__":
    main()
