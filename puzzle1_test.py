from puzzle1 import *

# XOR = exclusive or
# Only a Knight or a Knave, not both or neither
# InitialKnowledge = And(
#     Or(AKnight, AKnave), # must be one of these
#     Not(And(AKnight, AKnave)), # but not both
# )
def test_a_initial_knowledge():
    # Cant have both a Knight and a Knave
    model1 = {'A is a Knight': True, 'A is a Knave': True}
    assert InitialKnowledge.evaluate(model1) == False

    # Must have at least a knight or a knave
    model2 = {'A is a Knight': False, 'A is a Knave': False}
    assert InitialKnowledge.evaluate(model2) == False

    # Only a Knight and not a Knave
    model3 = {'A is a Knight': True, 'A is a Knave': False}
    assert InitialKnowledge.evaluate(model3) == True

    # Only a Knave and not a Knight
    model4 = {'A is a Knight': False, 'A is a Knave': True}
    assert InitialKnowledge.evaluate(model4) == True

# InitialStatement = And(AKnight, AKnave)
def test_a_initial_statement():
    # And(True, True)
    model1 = {'A is a Knight': True, 'A is a Knave': True}
    assert InitialStatment.evaluate(model1) == True

    # And(False, False)
    model2 = {'A is a Knight': False, 'A is a Knave': False}
    assert InitialStatment.evaluate(model2) == False

    # And(True, False)
    model3 = {'A is a Knight': True, 'A is a Knave': False}
    assert InitialStatment.evaluate(model3) == False

    # And(False, True)
    model4 = {'A is a Knight': False, 'A is a Knave': True}
    assert InitialStatment.evaluate(model4) == False


# KnightTruth = Implication(AKnight, InitialStatment)
# KnightTruth = Implication(True, True)
# InitialStatment = And(AKnight, AKnave)
# Goal: implication(True, True)
def test_a_knight_truth():
    # implication(True, (True && True)) =>
    # implication(True, True)
    model1 = {'A is a Knight': True, 'A is a Knave': True}
    assert KnightTruth.evaluate(model1) == True

    # A knight is false, so implication doesnt apply 
    model2 = {'A is a Knight': False, 'A is a Knave': False}
    assert KnightTruth.evaluate(model2) == True
    
    # A knight is false, so implication doesnt apply
    model4 = {'A is a Knight': False, 'A is a Knave': True}
    assert KnightTruth.evaluate(model4) == True
    
    # implication(True, (True && False))
    # implication(True, False)
    model3 = {'A is a Knight': True, 'A is a Knave': False}
    assert KnightTruth.evaluate(model3) == False
    
# KnaveLie = implication(AKnave, Not(InitialStatment))
# InitialStatment = And(AKnight, AKnave)
# Goal: implication(True, Not(And(True, True)))
def test_a_knave_lie():
    
    # implication(True, !(False && True))
    # implication(True, True)
    model4 = {'A is a Knight': False, 'A is a Knave': True}
    assert KnaveLie.evaluate(model4) == True
    
    # A Knave is false, so implication doesnt apply
    model2 = {'A is a Knight': False, 'A is a Knave': False}
    assert KnaveLie.evaluate(model2) == True

    # A Knave is false, so implication doesnt apply
    model3 = {'A is a Knight': True, 'A is a Knave': False}
    assert KnaveLie.evaluate(model3) == True
    
    # implication(True, !(True && True))
    # implication(True, False)
    model1 = {'A is a Knight': True, 'A is a Knave': True}
    assert KnaveLie.evaluate(model1) == False
    


def test_knowledge_():
    # should fail because not only a knave
    model1 = {'A is a Knight': True, 'A is a Knave': True}
    assert knowledge.evaluate(model1) == False
    model2 = {'A is a Knight': False, 'A is a Knave': False}
    assert knowledge.evaluate(model2) == False
    model3 = {'A is a Knight': True, 'A is a Knave': False}
    assert knowledge.evaluate(model3) == False

    # should be the only one to pass as its only a knave
    model4 = {'A is a Knight': False, 'A is a Knave': True}
    assert knowledge.evaluate(model4) == True
