from puzzle import *


# <A knowledge0----------------------------------------------------------------->

# XOR = exclusive or
# Only a Knight or a Knave, not both or neither
# InitialKnowledge0 = And(
#     Or(AKnight, AKnave), # must be one of these
#     Not(And(AKnight, AKnave)), # but not both
# )
def test_a_initial_knowledge():
    # Cant have both a Knight and a Knave
    model1 = {'A is a Knight': True, 'A is a Knave': True}
    assert InitialKnowledge0.evaluate(model1) == False

    # Must have at least a knight or a knave
    model2 = {'A is a Knight': False, 'A is a Knave': False}
    assert InitialKnowledge0.evaluate(model2) == False

    # Only a Knight and not a Knave
    model3 = {'A is a Knight': True, 'A is a Knave': False}
    assert InitialKnowledge0.evaluate(model3) == True

    # Only a Knave and not a Knight
    model4 = {'A is a Knight': False, 'A is a Knave': True}
    assert InitialKnowledge0.evaluate(model4) == True

# InitialStatement = And(AKnight, AKnave)
def test_a_initial_statement():
    # And(True, True)
    model1 = {'A is a Knight': True, 'A is a Knave': True}
    assert InitialStatment0.evaluate(model1) == True

    # And(False, False)
    model2 = {'A is a Knight': False, 'A is a Knave': False}
    assert InitialStatment0.evaluate(model2) == False

    # And(True, False)
    model3 = {'A is a Knight': True, 'A is a Knave': False}
    assert InitialStatment0.evaluate(model3) == False

    # And(False, True)
    model4 = {'A is a Knight': False, 'A is a Knave': True}
    assert InitialStatment0.evaluate(model4) == False


# KnightTruth0 = Implication(AKnight, InitialStatment0)
# InitialStatment0 = And(AKnight, AKnave)
# Goal: implication(True, True)
def test_a_knight_truth():
    # implication(True, (True && True)) =>
    # implication(True, True)
    model1 = {'A is a Knight': True, 'A is a Knave': True}
    assert KnightTruth0.evaluate(model1) == True

    # A knight is false, so implication doesnt apply 
    model2 = {'A is a Knight': False, 'A is a Knave': False}
    assert KnightTruth0.evaluate(model2) == True
    
    # A knight is false, so implication doesnt apply
    model4 = {'A is a Knight': False, 'A is a Knave': True}
    assert KnightTruth0.evaluate(model4) == True
    
    # implication(True, (True && False))
    # implication(True, False)
    model3 = {'A is a Knight': True, 'A is a Knave': False}
    assert KnightTruth0.evaluate(model3) == False
    
# KnaveLie0 = Implication(AKnave, Not(InitialStatment0))
# InitialStatment0 = And(AKnight, AKnave)
# Goal: implication(True, True)
def test_a_knight_truth():
    # implication(True, !(False && True))
    # implication(True, True)
    model4 = {'A is a Knight': False, 'A is a Knave': True}
    assert KnaveLie0.evaluate(model4) == True
    
    # A Knave is false, so implication doesnt apply
    model2 = {'A is a Knight': False, 'A is a Knave': False}
    assert KnaveLie0.evaluate(model2) == True

    # A Knave is false, so implication doesnt apply
    model3 = {'A is a Knight': True, 'A is a Knave': False}
    assert KnaveLie0.evaluate(model3) == True
    
    # implication(True, !(True && True))
    # implication(True, False)
    model1 = {'A is a Knight': True, 'A is a Knave': True}
    assert KnaveLie0.evaluate(model1) == False
    


def test_knowledge_0():
    # should fail because not only a knave
    model1 = {'A is a Knight': True, 'A is a Knave': True}
    assert knowledge0.evaluate(model1) == False
    model2 = {'A is a Knight': False, 'A is a Knave': False}
    assert knowledge0.evaluate(model2) == False
    model3 = {'A is a Knight': True, 'A is a Knave': False}
    assert knowledge0.evaluate(model3) == False

    # should be the only one to pass as its only a knave
    model4 = {'A is a Knight': False, 'A is a Knave': True}
    assert knowledge0.evaluate(model4) == True
    
# def test_knowledge_1():
#     # should fail because not only a knave
#     model1 = {' is a Knight': True, ' is a Knave': True}
#     assert knowledge1.evaluate(model1) == False
#     model2 = {' is a Knight': False, ' is a Knave': False}
#     assert knowledge1.evaluate(model2) == False
#     model3 = {' is a Knight': True, ' is a Knave': False}
#     assert knowledge0.evaluate(model3) == False

#     # should be the only one to pass as its only a knave
#     model4 = {'A is a Knight': False, 'A is a Knave': True}
#     assert knowledge1.evaluate(model4) == True
