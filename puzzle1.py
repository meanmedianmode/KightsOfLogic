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

knowledge = And(
    InitialKnowledge,
    # If A is a Knight than the initial statement must be true
    Biconditional(AKnight, InitialStatment)
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
