from logic import *

# Puzzle
# A says "We are both knaves." => A is a Knave
# B says nothing => B is a Knight (Because Knaves always lie part of what they said must be a lie)

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

InitialKnowledge = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Not(And(AKnight, AKnave)), 
    Not(And(BKnight, BKnave)),
)

InitialStatment = And(AKnave, BKnave)
KnaveLie = Biconditional(AKnave, Not(InitialStatment))

knowledge = And(
    InitialKnowledge,
    KnaveLie
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
