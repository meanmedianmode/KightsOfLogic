from puzzle2 import *

model_1 = {'B is a Knight': True, 'B is a Knave': True,'A is a Knight': True, 'A is a Knave': True, 'initial_statement_filter': True}
model_2 = {'B is a Knight': True, 'B is a Knave': True,'A is a Knight': True, 'A is a Knave': False}
model_3 = {'B is a Knight': True, 'B is a Knave': True,'A is a Knight': False, 'A is a Knave': True, 'initial_statement_filter': True}
model_4 = {'B is a Knight': True, 'B is a Knave': True,'A is a Knight': False, 'A is a Knave': False}
model_5 = {'B is a Knight': True, 'B is a Knave': False,'A is a Knight': True, 'A is a Knave': True, 'knave_lie_filter': True}
model_6 = {'B is a Knight': True, 'B is a Knave': False,'A is a Knight': True, 'A is a Knave': False, 'initial_knowledge_filter': True} 
model_7 = {'B is a Knight': True, 'B is a Knave': False,'A is a Knight': False, 'A is a Knave': True, 'initial_knowledge_filter': True, 'knave_lie_filter': True, 'target': True}
model_8 = {'B is a Knight': True, 'B is a Knave': False,'A is a Knight': False, 'A is a Knave': False}
model_9 = {'B is a Knight': False, 'B is a Knave': True,'A is a Knight': True, 'A is a Knave': True, 'initial_statement_filter': True}
model_10 = {'B is a Knight': False, 'B is a Knave': True,'A is a Knight': True, 'A is a Knave': False, 'initial_knowledge_filter': True} 
model_11 = {'B is a Knight': False, 'B is a Knave': True, 'A is a Knight': False, 'A is a Knave': True, 'initial_knowledge_filter': True, 'initial_statement_filter': True} 
model_12 = {'B is a Knight': False, 'B is a Knave': True,'A is a Knight': False, 'A is a Knave': False}
model_13 = {'B is a Knight': False, 'B is a Knave': False, 'A is a Knight': True, 'A is a Knave': True, 'knave_lie_filter': True}
model_14 = {'B is a Knight': False, 'B is a Knave': False, 'A is a Knight': True, 'A is a Knave': False}
model_15 = {'B is a Knight': False, 'B is a Knave': False, 'A is a Knight': False, 'A is a Knave': True, 'knave_lie_filter': True}
model_16 = {'B is a Knight': False, 'B is a Knave': False,'A is a Knight': False, 'A is a Knave': False}
 
all_models = [ model_1, model_2, model_3, model_4, model_5, model_6, model_7, 
    model_8, model_9, model_10, model_11, model_12, model_13, model_14, model_15, model_16]           

# InitialKnowledge = And(
#     Or(AKnight, AKnave),
#     Or(BKnight, BKnave),
#     Not(And(AKnight, AKnave)), 
#     Not(And(BKnight, BKnave)),
# )
def test_initial_knowledge():
    for model in all_models:
      if InitialKnowledge.evaluate(model):
        assert model['initial_knowledge_filter'] == True

# InitialStatment = And(AKnave, BKnave)        
def test_initial_statement():
  for model in all_models:
      if InitialStatment.evaluate(model):
        assert model['initial_statement_filter'] == True

def test_knowledge():
  for model in all_models:
      if knowledge.evaluate(model):
        assert model['target'] == True
