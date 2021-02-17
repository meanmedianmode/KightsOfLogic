from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")


InitialKnowledge0 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
)

InitialStatment0 = And(AKnight, AKnave)

KnightTruth0 = Implication(AKnight, InitialStatment0)
KnaveLie0 = Implication(AKnave, Not(InitialStatment0))
# Puzzle 
# A says "I am both a knight and a knave."
knowledge0 = And(
    InitialKnowledge0,
    KnightTruth0,
    KnaveLie0
)


# Aknight || Bknight
# AKave

InitialKnowledge1 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
)

InitialStatment1 = And(AKnave, BKnave)

KnightTruthA1 = Implication(AKnight, InitialStatment1)
KnaveLieA1 = Implication(AKnave, Not(InitialStatment1))

# Puzzle 1
# A says "We are both knaves.", Aknight && Aknave
# B says nothing., Bknight || Bknave
knowledge1 = And(
    InitialKnowledge1,
    KnightTruthA1,
    KnaveLieA1
)
# A is a Knave
# B is a Knight


InitialKnowledge1 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Or(AKnight, BKnight),
    Or(AKnave, BKnave),
    Not(And(AKnight, BKnight)),
    Not(And(AKnave, BKnave)),
)

InitialStatment1 = Or(And(AKnave, BKnave), And(AKnight, BKnight))
InitialStatment2 = Or(And(AKnave, BKnight), And(AKnight, BKnave))

KnightTruthA1 = Or(
    Implication(AKnight, InitialStatment1),
    Implication(AKnight, InitialStatment2),
)
KnaveLieA1 = Or(
    Implication(AKnave, Not(InitialStatment1)),
    Implication(AKnave, Not(InitialStatment2)),
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    InitialKnowledge1,
    KnightTruthA1,
    KnaveLieA1
)

# A is a Knave
# B is a Knight

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # TODO
)


def main():
    # symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    symbols = [AKnight, AKnave, BKnight, BKnave]
    puzzles = [
        # ("Puzzle 0", knowledge0),
        # ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        # ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
