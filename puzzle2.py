from logic import *

# Puzzle
# A says "We are both knaves." => A is a Knave
# B says nothing => B is a Knight (Because Knaves always lie part of what they said must be a lie)

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

# KB initial rules
InitialKnowledge = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Not(And(AKnight, AKnave)), 
    Not(And(BKnight, BKnave)),
)

# Statement given to us
InitialStatment = And(AKnave, BKnave)

knowledge = And(
    InitialKnowledge,
    # If A is a Knight his initial statment will be true
    Biconditional(AKnight, InitialStatment)
)

def main():
    symbols = [AKnight, AKnave, BKnight, BKnave]
    if len(knowledge.conjuncts) == 0:
        print("Not yet implemented.")
    else:
        for symbol in symbols:
            if model_check(knowledge, symbol):
                print(f"    {symbol}")


if __name__ == "__main__":
    main()
