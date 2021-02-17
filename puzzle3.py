from logic import *

# Puzzle 2
# A says "We are the same kind." => Knave
# B says "We are of different kinds." => Knight


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

InitialStatment1 = Or(And(AKnight, BKnight), And(AKnave, BKnave))
InitialStatment2 = Or(And(AKnight, BKnave), And(BKnave, AKnight))

knowledge = And(

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
