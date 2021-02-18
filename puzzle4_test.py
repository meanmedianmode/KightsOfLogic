from puzzle4 import *

model_1 = {'A is a Knight': True , 'A is a Knave': True, 'B is a Knave': True, 'B is a Knight': True, 'C is a Knight': True, 'C is a Knave': True}
model_2 = {'A is a Knight': False, 'A is a Knave': True, 'B is a Knave': True, 'B is a Knight': True, 'C is a Knight': True, 'C is a Knave': True}
model_3 = {'A is a Knight': True , 'A is a Knave': True, 'B is a Knave': True, 'B is a Knight': True, 'C is a Knight': True, 'C is a Knave': False}
model_4 = {'A is a Knight': False, 'A is a Knave': True, 'B is a Knave': True, 'B is a Knight': True, 'C is a Knight': True, 'C is a Knave': False}
model_5 = {'A is a Knight': True , 'A is a Knave': True, 'B is a Knave': True, 'B is a Knight': True, 'C is a Knight': False, 'C is a Knave': True}
model_6 = {'A is a Knight': False, 'A is a Knave': True, 'B is a Knave': True, 'B is a Knight': True, 'C is a Knight': False, 'C is a Knave': True}
model_7 = {'A is a Knight': True , 'A is a Knave': True, 'B is a Knave': True, 'B is a Knight': True, 'C is a Knight': False, 'C is a Knave': False}
model_8 = {'A is a Knight': False, 'A is a Knave': True, 'B is a Knave': True, 'B is a Knight': True, 'C is a Knight': False, 'C is a Knave': False}
model_9 = {'A is a Knight': True , 'A is a Knave': True, 'B is a Knave': True, 'B is a Knight': False, 'C is a Knight': True, 'C is a Knave': True}
model_10 = {'A is a Knight': False, 'A is a Knave': True, 'B is a Knave': True, 'B is a Knight': False, 'C is a Knight': True, 'C is a Knave': True}
model_11 = {'A is a Knight': True , 'A is a Knave': True, 'B is a Knave': True, 'B is a Knight': False, 'C is a Knight': True, 'C is a Knave': False}
model_12 = {'A is a Knight': False, 'A is a Knave': True, 'B is a Knave': True, 'B is a Knight': False, 'C is a Knight': True, 'C is a Knave': False, 'initial_knowledge': True}
model_13 = {'A is a Knight': True , 'A is a Knave': True, 'B is a Knave': True, 'B is a Knight': False, 'C is a Knight': False, 'C is a Knave': True}
model_14 = {'A is a Knight': False, 'A is a Knave': True, 'B is a Knave': True, 'B is a Knight': False, 'C is a Knight': False, 'C is a Knave': True, 'initial_knowledge': True}
model_15 = {'A is a Knight': True , 'A is a Knave': True, 'B is a Knave': True, 'B is a Knight': False, 'C is a Knight': False, 'C is a Knave': False}
model_16 = {'A is a Knight': False, 'A is a Knave': True, 'B is a Knave': True, 'B is a Knight': False, 'C is a Knight': False, 'C is a Knave': False}
model_17 = {'A is a Knight': True , 'A is a Knave': True, 'B is a Knave': False, 'B is a Knight': True, 'C is a Knight': True, 'C is a Knave': True}
model_18 = {'A is a Knight': False, 'A is a Knave': True, 'B is a Knave': False, 'B is a Knight': True, 'C is a Knight': True, 'C is a Knave': True}
model_19 = {'A is a Knight': True , 'A is a Knave': True, 'B is a Knave': False, 'B is a Knight': True, 'C is a Knight': True, 'C is a Knave': False}
model_20 = {'A is a Knight': False, 'A is a Knave': True, 'B is a Knave': False, 'B is a Knight': True, 'C is a Knight': True, 'C is a Knave': False, 'initial_knowledge': True}
model_21 = {'A is a Knight': True , 'A is a Knave': True, 'B is a Knave': False, 'B is a Knight': True, 'C is a Knight': False, 'C is a Knave': True}
model_22 = {'A is a Knight': False, 'A is a Knave': True, 'B is a Knave': False, 'B is a Knight': True, 'C is a Knight': False, 'C is a Knave': True, 'initial_knowledge': True}
model_23 = {'A is a Knight': True , 'A is a Knave': True, 'B is a Knave': False, 'B is a Knight': True, 'C is a Knight': False, 'C is a Knave': False}
model_24 = {'A is a Knight': False, 'A is a Knave': True, 'B is a Knave': False, 'B is a Knight': True, 'C is a Knight': False, 'C is a Knave': False}
model_25 = {'A is a Knight': True , 'A is a Knave': True, 'B is a Knave': False, 'B is a Knight': False, 'C is a Knight': True, 'C is a Knave': True}
model_26 = {'A is a Knight': False, 'A is a Knave': True, 'B is a Knave': False, 'B is a Knight': False, 'C is a Knight': True, 'C is a Knave': True}
model_27 = {'A is a Knight': True , 'A is a Knave': True, 'B is a Knave': False, 'B is a Knight': False, 'C is a Knight': True, 'C is a Knave': False}
model_28 = {'A is a Knight': False, 'A is a Knave': True, 'B is a Knave': False, 'B is a Knight': False, 'C is a Knight': True, 'C is a Knave': False}
model_29 = {'A is a Knight': True , 'A is a Knave': True, 'B is a Knave': False, 'B is a Knight': False, 'C is a Knight': False, 'C is a Knave': True}
model_30 = {'A is a Knight': False, 'A is a Knave': True, 'B is a Knave': False, 'B is a Knight': False, 'C is a Knight': False, 'C is a Knave': True}
model_31 = {'A is a Knight': True , 'A is a Knave': True, 'B is a Knave': False, 'B is a Knight': False, 'C is a Knight': False, 'C is a Knave': False}
model_32 = {'A is a Knight': False, 'A is a Knave': True, 'B is a Knave': False, 'B is a Knight': False, 'C is a Knight': False, 'C is a Knave': False}
model_33 = {'A is a Knight': True , 'A is a Knave': False, 'B is a Knave': True, 'B is a Knight': True, 'C is a Knight': True, 'C is a Knave': True}
model_34 = {'A is a Knight': False, 'A is a Knave': False, 'B is a Knave': True, 'B is a Knight': True, 'C is a Knight': True, 'C is a Knave': True}
model_35 = {'A is a Knight': True , 'A is a Knave': False, 'B is a Knave': True, 'B is a Knight': True, 'C is a Knight': True, 'C is a Knave': False}
model_36 = {'A is a Knight': False, 'A is a Knave': False, 'B is a Knave': True, 'B is a Knight': True, 'C is a Knight': True, 'C is a Knave': False}
model_37 = {'A is a Knight': True , 'A is a Knave': False, 'B is a Knave': True, 'B is a Knight': True, 'C is a Knight': False, 'C is a Knave': True}
model_38 = {'A is a Knight': False, 'A is a Knave': False, 'B is a Knave': True, 'B is a Knight': True, 'C is a Knight': False, 'C is a Knave': True}
model_39 = {'A is a Knight': True , 'A is a Knave': False, 'B is a Knave': True, 'B is a Knight': True, 'C is a Knight': False, 'C is a Knave': False}
model_40 = {'A is a Knight': False, 'A is a Knave': False, 'B is a Knave': True, 'B is a Knight': True, 'C is a Knight': False, 'C is a Knave': False}
model_41 = {'A is a Knight': True , 'A is a Knave': False, 'B is a Knave': True, 'B is a Knight': False, 'C is a Knight': True, 'C is a Knave': True}
model_42 = {'A is a Knight': False, 'A is a Knave': False, 'B is a Knave': True, 'B is a Knight': False, 'C is a Knight': True, 'C is a Knave': True}
model_43 = {'A is a Knight': True , 'A is a Knave': False, 'B is a Knave': True, 'B is a Knight': False, 'C is a Knight': True, 'C is a Knave': False, 'initial_knowledge': True, 'target': True}
model_44 = {'A is a Knight': False, 'A is a Knave': False, 'B is a Knave': True, 'B is a Knight': False, 'C is a Knight': True, 'C is a Knave': False}
model_45 = {'A is a Knight': True , 'A is a Knave': False, 'B is a Knave': True, 'B is a Knight': False, 'C is a Knight': False, 'C is a Knave': True, 'initial_knowledge': True}
model_46 = {'A is a Knight': False, 'A is a Knave': False, 'B is a Knave': True, 'B is a Knight': False, 'C is a Knight': False, 'C is a Knave': True}
model_47 = {'A is a Knight': True , 'A is a Knave': False, 'B is a Knave': True, 'B is a Knight': False, 'C is a Knight': False, 'C is a Knave': False}
model_48 = {'A is a Knight': False, 'A is a Knave': False, 'B is a Knave': True, 'B is a Knight': False, 'C is a Knight': False, 'C is a Knave': False}
model_49 = {'A is a Knight': True , 'A is a Knave': False, 'B is a Knave': False, 'B is a Knight': True, 'C is a Knight': True, 'C is a Knave': True}
model_50 = {'A is a Knight': False, 'A is a Knave': False, 'B is a Knave': False, 'B is a Knight': True, 'C is a Knight': True, 'C is a Knave': True}
model_51 = {'A is a Knight': True , 'A is a Knave': False, 'B is a Knave': False, 'B is a Knight': True, 'C is a Knight': True, 'C is a Knave': False, 'initial_knowledge': True}
model_52 = {'A is a Knight': False, 'A is a Knave': False, 'B is a Knave': False, 'B is a Knight': True, 'C is a Knight': True, 'C is a Knave': False}
model_53 = {'A is a Knight': True , 'A is a Knave': False, 'B is a Knave': False, 'B is a Knight': True, 'C is a Knight': False, 'C is a Knave': True, 'initial_knowledge': True}
model_54 = {'A is a Knight': False, 'A is a Knave': False, 'B is a Knave': False, 'B is a Knight': True, 'C is a Knight': False, 'C is a Knave': True}
model_55 = {'A is a Knight': True , 'A is a Knave': False, 'B is a Knave': False, 'B is a Knight': True, 'C is a Knight': False, 'C is a Knave': False}
model_56 = {'A is a Knight': False, 'A is a Knave': False, 'B is a Knave': False, 'B is a Knight': True, 'C is a Knight': False, 'C is a Knave': False}
model_57 = {'A is a Knight': True , 'A is a Knave': False, 'B is a Knave': False, 'B is a Knight': False, 'C is a Knight': True, 'C is a Knave': True}
model_58 = {'A is a Knight': False, 'A is a Knave': False, 'B is a Knave': False, 'B is a Knight': False, 'C is a Knight': True, 'C is a Knave': True}
model_59 = {'A is a Knight': True , 'A is a Knave': False, 'B is a Knave': False, 'B is a Knight': False, 'C is a Knight': True, 'C is a Knave': False}
model_60 = {'A is a Knight': False, 'A is a Knave': False, 'B is a Knave': False, 'B is a Knight': False, 'C is a Knight': True, 'C is a Knave': False}
model_61 = {'A is a Knight': True , 'A is a Knave': False, 'B is a Knave': False, 'B is a Knight': False, 'C is a Knight': False, 'C is a Knave': True}
model_62 = {'A is a Knight': False, 'A is a Knave': False, 'B is a Knave': False, 'B is a Knight': False, 'C is a Knight': False, 'C is a Knave': True}
model_63 = {'A is a Knight': True , 'A is a Knave': False, 'B is a Knave': False, 'B is a Knight': False, 'C is a Knight': False, 'C is a Knave': False}
model_64 = {'A is a Knight': False, 'A is a Knave': False, 'B is a Knave': False, 'B is a Knight': False, 'C is a Knight': False, 'C is a Knave': False}

all_models = [model_1, model_2, model_3, model_4, model_5, model_6, model_7, model_8, model_9, model_10, model_11, model_12, model_13, model_14, model_15, model_16, model_17, model_18, model_19, model_20, model_21, model_22, model_23, model_24, model_25, model_26, model_27, model_28, model_29, model_30, model_31, model_32, model_33, model_34, model_35, model_36, model_37, model_38, model_39, model_40, model_41, model_42, model_43, model_44, model_45, model_46, model_47, model_48, model_49, model_50, model_51, model_52, model_53, model_54, model_55, model_56, model_57, model_58, model_59, model_60, model_61, model_62, model_63, model_64] 

def test_initial_knowledge():
    for model in all_models:
      if InitialKnowledge.evaluate(model):
        assert model['initial_knowledge'] == True
    
def test_initial_knowledge():
    for model in all_models:
      if knowledge.evaluate(model):
        print(model)
    
    assert True == False
