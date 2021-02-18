from logic import *

# Puzzle 2
# A says "We are the same kind." Lie => Knave
# B says "We are of different kinds." Truth => Knight
# A is a knave
# B is a knight

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

# Initial Statment given by A
InitalStatement_SameKind = And(
  # If Aknight <=> Bknight
  Biconditional(AKnight, BKnight),
  # If Aknight <=> Not(Aknave)
  Biconditional(AKnight, Not(AKnave)),
  # If Aknight <=> Not(BKnave)
  Biconditional(AKnight, Not(BKnave))
)

# Initial Statment given by B
InitalStatement_DifferentKind = And(
  # If Aknight <=> Bknave
  Biconditional(AKnight, BKnave),
  # If BKnight <=> Aknave
  Biconditional(BKnight, AKnave),
  # If Aknight <=> Not(BKnight)
  Biconditional(AKnight, Not(BKnight)),
  # If AKnave <=> Not(Bknave)
  Biconditional(AKnave, Not(BKnave)),
)

knowledge = And(
  InitialKnowledge,
  # If A is a knight their initial statment must be true
  Biconditional(AKnight, InitalStatement_SameKind),
  # If B is a knight their initial statment must be true
  Biconditional(BKnight, InitalStatement_DifferentKind),
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
