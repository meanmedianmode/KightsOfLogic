from logic import *

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'." => a Knave will never admit to being a Knave so this is a lie
# B says "C is a knave."
# C says "A is a knight."
# => A is a Knight
# => B is a Knave
# => C is a Knight

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# KB initial rules
InitialKnowledge = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    Not(And(AKnight, AKnave)), 
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),
)

knowledge = And(
  InitialKnowledge,
  # If B is a Knight A must be a Knave
  Biconditional(BKnight, Biconditional(AKnight, AKnave)),
  # If B is a Knight C must be a Knave
  Biconditional(BKnight, CKnave),
  # If C is a Knight A must be a Knight
  Biconditional(CKnight, AKnight)
)

def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    print('working')
    if len(knowledge.conjuncts) == 0:
        print("Not yet implemented.")
    else:
        for symbol in symbols:
            if model_check(knowledge, symbol):
                print(f"    {symbol}")

if __name__ == "__main__":
    main()
