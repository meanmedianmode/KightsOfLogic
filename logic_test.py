import pytest
from logic import *


# Symbols -------------------------------------
def test_symbol_equality():
    propositional_symbol = Symbol('prop symbol')
    propositional_symbol2 = Symbol('prop symbols')

    assert propositional_symbol.__eq__(propositional_symbol)
    assert not propositional_symbol.__eq__(propositional_symbol2)


def test_symbol_repr():
    rain = Symbol('rain')
    assert repr(rain) == 'rain'


def test_symbol_class():
    prop_symbol = Symbol('prop')
    assert isinstance(prop_symbol, Sentence)
    assert isinstance(prop_symbol, Symbol)


def test_symbol_evaluate():
    rain = Symbol('rain')
    # evaluate returns bool(model[self.name])
    assert rain.evaluate({'rain': True, 'sunny': False}) == True
    assert rain.evaluate({'rain': False, 'sunny': True}) == False


def test_symbol_formula():
    rain = Symbol('rain')
    # returns string representation of symbol
    assert rain.formula() == 'rain'


def test_symbol_symbols():
    rain = Symbol('rain')
    assert isinstance(rain.symbols(), set)
    assert rain.symbols() == {'rain'}

# Not Logical Connective -------------------------------------


def test_not_repr():
    rain = Symbol('rain')
    not_connective = Not(rain)
    assert repr(not_connective) == 'Not(rain)'


def test_not_class():
    rain = Symbol('rain')
    not_connective = Not(rain)
    assert isinstance(not_connective, Sentence)
    assert isinstance(not_connective, Not)


def test_not_operand():
    rain = Symbol('rain')
    not_connective = Not(rain)
    assert not_connective.operand == rain


def test_not_evaluate():
    # TESTS Symbol FN
    rain = Symbol('rain')
    sunny = Symbol('sunny')
    not_connective = Not(rain)
    model = {'rain': True, 'sunny': False}
    # calls operands evaluate fn
    # operand = rain = Symbol('rain')
    # evaluate(self, model) --> bool(modes[rain.name])
    # inverses the logic !! evaluate(self, model)

    # Not(rain) == False
    assert not_connective.evaluate(model) == False

    model = {'rain': True, 'sunny': False}

    # calls operands evaluate fn
    # operand = rain = Symbol('rain')
    # operand = sunny = Symbol('sunny')
    # evaluate(self, model) --> bool(modes[rain.name])
    # rain = true, sun = false
    # true && false
    # inverses the logic !! evaluate(self, model)

    not_connective_with_and = Not(And(rain, sunny))
    assert not_connective_with_and.evaluate(model) == True


def test_not_formula():
    rain = Symbol('rain')
    not_connective = Not(rain)
    # returns string repr of connective and symbol
    assert not_connective.formula() == '¬rain'


def test_not_symbols():
    # TESTS Symbol FN
    rain = Symbol('rain')
    not_connective = Not(rain)
    # calls operands symbols fn
    assert isinstance(not_connective.symbols(), set)
    assert not_connective.symbols() == {'rain'}


# And Logical Connective -------------------------------------
# repr()
def test_and_connective_repr():
    rain = Symbol('rain')
    wet = Symbol('wet')
    and_connective = And(rain, wet)
    assert repr(and_connective) == 'And(rain, wet)'


# And class type
def test_and_connective_class():
    rain = Symbol('rain')
    wet = Symbol('wet')
    and_connective = And(rain, wet)
    assert isinstance(and_connective, Sentence)
    assert isinstance(and_connective, And)


# And conjuncts()
def test_and_connective_conjuncts():
    rain = Symbol('rain')
    wet = Symbol('wet')
    and_connective = And(rain, wet)
    assert and_connective.conjuncts == [rain, wet]


# And evaluate()
def test_and_connective_evaluate():
    # TESTS Symbol FN
    rain = Symbol('rain')
    sunny = Symbol('sunny')
    and_connective = And(rain, sunny)
    model = {'rain': True, 'sunny': False}
    # calls evaluate on each conjunct
    # ands them together

    # Rain and Sun
    assert and_connective.evaluate(model) == False

    wet = Symbol('wet')
    and_connective = And(rain, wet)
    model = {'rain': True, 'wet': True}
    # Rain and Wet
    assert and_connective.evaluate(model) == True

    and_connective = And(rain, Not(wet))
    model = {'rain': True, 'wet': True}
    # Rain and Not Wet
    assert and_connective.evaluate(model) == False


# And formula()
def test_and_connective_formula():
    rain = Symbol('rain')
    wet = Symbol('wet')
    and_connective = And(rain, wet)
    # returns string repr of connective and symbol
    assert and_connective.formula() == 'rain ∧ wet'

    and_connective = And(rain, Not(wet))
    assert and_connective.formula() == 'rain ∧ (¬wet)'


# And symbols()
def test_and_connective_symbols():
    # TESTS Symbol FN
    rain = Symbol('rain')
    wet = Symbol('wet')
    sunny = Symbol('sunny')
    and_connective = And(rain, wet, sunny)
    # calls symbols fn on each conjunctive
    assert isinstance(and_connective.symbols(), set)
    assert and_connective.symbols() == {'rain', 'wet', 'sunny'}


# And add()
def test_and_connective_add():
    # TESTS Symbol FN
    rain = Symbol('rain')
    wet = Symbol('wet')
    sunny = Symbol('sunny')
    and_connective = And(rain, wet)
    and_connective.add(sunny)
    assert and_connective.symbols() == {'rain', 'wet', 'sunny'}


# Or Logical Connective -------------------------------------
# repr()
def test_or_connective_repr():
    rain = Symbol('rain')
    wet = Symbol('wet')
    or_connective = Or(rain, wet)
    assert repr(or_connective) == 'Or(rain, wet)'
    or_connective = Or(rain, Not(wet))
    assert repr(or_connective) == 'Or(rain, Not(wet))'


# # class type
def test_or_connective_class():
    rain = Symbol('rain')
    wet = Symbol('wet')
    or_connective = Or(rain, wet)
    assert isinstance(or_connective, Sentence)
    assert isinstance(or_connective, Or)


# # disjuncts()
def test_or_connective_disjuncts():
    rain = Symbol('rain')
    wet = Symbol('wet')
    or_connective = Or(rain, wet)
    assert or_connective.disjuncts == [rain, wet]
    or_connective = Or(rain, Not(wet))
    assert or_connective.disjuncts == [rain, Not(wet)]


# # or evaluate()
def test_or_connective_evaluate():
    # TESTS Symbol FN
    rain = Symbol('rain')
    sunny = Symbol('sunny')
    or_connective = Or(rain, sunny)
    model = {'rain': True, 'sunny': False}
    # calls evaluate on each disjunct
    # ands them together

    # Rain or Sun
    assert or_connective.evaluate(model) == True

    wet = Symbol('wet')
    or_connective = Or(rain, wet)
    model = {'rain': False, 'wet': False}
    # Rain or Wet
    assert or_connective.evaluate(model) == False

    wet = Symbol('wet')
    or_connective = Or(rain, Not(wet))
    model = {'rain': False, 'wet': False}
    # Rain or Wet
    assert or_connective.evaluate(model) == True
    
    wet = Symbol('wet')
    or_connective = Or(rain, Not(wet))
    model = {'rain': True, 'wet': True}
    # Rain or Wet
    assert or_connective.evaluate(model) == True


# # or formula()
def test_or_connective_formula():
    rain = Symbol('rain')
    wet = Symbol('wet')
    or_connective = Or(rain, wet)
    # returns string repr of connective and symbol
    assert or_connective.formula() == 'rain ∨ wet'

    or_connective = Or(rain, Not(wet))
    # returns string repr of connective and symbol
    assert or_connective.formula() == 'rain ∨ (¬wet)'


# # or symbols()
def test_or_connective_symbols():
    # TESTS Symbol FN
    rain = Symbol('rain')
    wet = Symbol('wet')
    sunny = Symbol('sunny')
    or_connective = Or(rain, wet, sunny)
    # calls symbols fn on each conjunctive
    assert isinstance(or_connective.symbols(), set)
    assert or_connective.symbols() == {'rain', 'wet', 'sunny'}

    or_connective = Or(rain, wet, Not(sunny))
    assert or_connective.symbols() == {'rain', 'wet', 'sunny'}


# Implication Logical Connective -------------------------------------
# implication repr()
def test_implication_connective_repr():
    rain = Symbol('rain')
    wet = Symbol('wet')
    implication_connective = Implication(rain, wet)
    assert repr(implication_connective) == 'Implication(rain, wet)'
    implication_connective = Implication(rain, Not(wet))
    assert repr(implication_connective) == 'Implication(rain, Not(wet))'


# implication class type
def test_implication_connective_class():
    rain = Symbol('rain')
    wet = Symbol('wet')
    implication_connective = Implication(rain, wet)
    assert isinstance(implication_connective, Sentence)
    assert isinstance(implication_connective, Implication)


# implication antecedent_consequent()
def test_implication_connective_antecedent_consequent():
    rain = Symbol('rain')
    wet = Symbol('wet')
    implication_connective = Implication(rain, wet)
    assert implication_connective.antecedent == rain
    assert implication_connective.consequent == wet
    implication_connective = Implication(rain, Not(wet))
    assert implication_connective.antecedent == rain
    assert implication_connective.consequent == Not(wet)


# evaluate()
def implication test_implication_connective_evaluate():
    # TESTS Symbol FN
    rain = Symbol('rain')
    wet = Symbol('wet')
    implication_connective = Implication(rain, wet)
    model = {'rain': True, 'wet': True}

    # Rain implies Wet ?
    # step one evaluate model:
    #   antecedent:rain=True, consequent:wet=True
    # invert and or together:
    #   !(antecedent:rain=True) or (wet=True)
    assert implication_connective.evaluate(model) == True

    # Rain implies not wet ?
    model = {'rain': True, 'wet': False}
    # step one evaluate model:
    #   antecedent:rain=True, consequent:wet=False
    # invert and or together:
    #   !(antecedent:rain=True) or (wet=False)
    assert implication_connective.evaluate(model) == False

    # Not rain implies wet
    # Returns true because its not raining so sentence is irrelavant
    model = {'rain': False, 'wet': True}
    # step one evaluate model:
    #   antecedent:rain=False, consequent:wet=True
    # invert and or together:
    #   !(antecedent:rain=False) or (wet=True)
    assert implication_connective.evaluate(model) == True


# implication formula()
def test_implication_connective_formula():
    rain = Symbol('rain')
    wet = Symbol('wet')
    implication_connective = Implication(rain, wet)
    # returns string repr of connective and symbol
    assert implication_connective.formula() == 'rain => wet'

    implication_connective = Implication(rain, Not(wet))
    # returns string repr of connective and symbol
    assert implication_connective.formula() == 'rain => (¬wet)'


# implication symbols()
def test_implication_connective_symbols():
    # TESTS Symbol FN
    rain = Symbol('rain')
    wet = Symbol('wet')
    sunny = Symbol('sunny')
    implication_connective = Implication(rain, wet)
    # calls symbols fn on each conjunctive
    assert isinstance(implication_connective.symbols(), set)
    assert implication_connective.symbols() == {'rain', 'wet'}

    implication_connective = Implication(rain, Not(wet))
    assert implication_connective.symbols() == {'rain', 'wet'}


# Implication Logical Connective -------------------------------------
# biconditional repr()
def test_biconditional_connective_repr():
    rain = Symbol('rain')
    wet = Symbol('wet')
    biconditional_connective = Biconditional(rain, wet)
    assert repr(biconditional_connective) == 'Biconditional(rain, wet)'
    biconditional_connective = Biconditional(rain, Not(wet))
    assert repr(biconditional_connective) == 'Biconditional(rain, Not(wet))'


# biconditional class type
def test_biconditional_connective_class():
    rain = Symbol('rain')
    wet = Symbol('wet')
    biconditional_connective = Biconditional(rain, wet)
    assert isinstance(biconditional_connective, Sentence)
    assert isinstance(biconditional_connective, Biconditional)


# biconditional antecedent_consequent()
def test_biconditional_connective_antecedent_consequent():
    rain = Symbol('rain')
    wet = Symbol('wet')
    biconditional_connective = Biconditional(rain, wet)
    assert biconditional_connective.left == rain
    assert biconditional_connective.right == wet
    biconditional_connective = Biconditional(rain, Not(wet))
    assert biconditional_connective.left == rain
    assert biconditional_connective.right == Not(wet)


# biconditional evaluate()
def test_biconditional_connective_evaluate():
    # TESTS Symbol FN
    rain = Symbol('rain')
    wet = Symbol('wet')
    biconditional_connective = Biconditional(rain, wet)
    model = {'rain': True, 'wet': True}

    # Its only raining if its wet and its only wet if its raining
    # Its not raining unless it is wet
    # Its not wet unless it is wet

    # step one evaluate model:
    #   left:rain=True, right:wet=True
    # invert and or together:
    #   (left:rain=True) and (wet=True)
    #   or
    #   !(left:rain=True) and !(wet=True)
    assert biconditional_connective.evaluate(model) == True

    model = {'rain': False, 'wet': False}

    # Its only raining if its wet and its only wet if its raining
    # Its not raining unless it is wet
    # Its not wet unless it is wet

    # invert and or together:
    #   (left:rain=False) and (wet=False)
    #   or
    #   !(left:rain=False) and !(wet=False)
    assert biconditional_connective.evaluate(model) == True

    # Its only raining if its wet and its only wet if its raining
    # Its not raining unless it is wet
    # Its not wet unless it is wet
    model = {'rain': True, 'wet': False}
    # step one evaluate model:
    #   left:rain=True, right:wet=False
    # invert and or together:
    #   (left:rain=True) and (wet=False)
    #   or
    #   !(left:rain=True) and !(wet=False)
    assert biconditional_connective.evaluate(model) == False


# formula()
def test_biconditional_connective_formula():
    rain = Symbol('rain')
    wet = Symbol('wet')
    biconditional_connective = Biconditional(rain, wet)
    # returns string repr of connective and symbol
    assert biconditional_connective.formula() == 'rain <=> wet'

    biconditional_connective = Biconditional(rain, Not(wet))
    # returns string repr of connective and symbol
    assert biconditional_connective.formula() == 'rain <=> (¬wet)'


# symbols()
def test_biconditional_connective_symbols():
    # TESTS Symbol FN
    rain = Symbol('rain')
    wet = Symbol('wet')
    sunny = Symbol('sunny')
    biconditional_connective = Biconditional(rain, And(wet, sunny))
    # calls symbols fn on each conjunctive
    assert isinstance(biconditional_connective.symbols(), set)
    assert biconditional_connective.symbols() == {'rain', 'wet', 'sunny'}

    biconditional_connective = Biconditional(rain, Not(wet))
    assert biconditional_connective.symbols() == {'rain', 'wet'}


# Model Check -------------------------------------
# def test_cmodel_check():
#     # rain = Symbol('rain')
#     # wet = Symbol('wet')

#     # knowlege = And(
#     #   rain,
#     #   wet
#     # )
#     # assert model_check(knowlege, rain) == True

#     # knowlege = And(
#     #   Not(rain),
#     #   wet
#     # )
#     # assert model_check(knowlege, rain) == False
#     # assert model_check(knowlege, wet) == True

#     # knowlege = And(
#     #   Implication(rain, wet),
#     #   rain
#     # )
#     # assert model_check(knowlege, rain) == True
#     # assert model_check(knowlege, wet) == True

    


    
#     # one = Implication(And(knight, knave), Not(knight))
#     # two = Implication(And(knight, knave), knave)
    
    
#     # isKnave
#     # { 'is a knave': True, 'is a knight': True } => knave
#     # { 'is a knave': True, 'is a knight': False }
#     # { 'is a knave': False, 'is a knight': False }
#     # { 'is a knave': False, 'is a knight': True }
    
#     # knight = Symbol('is a knight')
#     # knave = Symbol('is a knave')
    
#     # knowlege = And(
#     #   Implication(And(knight, knave), knave),
#     #   And(knight, knave)
#     # )
#     # model_check(knowlege, knave)
#     # model_check(knowlege, knight)
    
#     rain = Symbol('rain')
#     sun = Symbol('sun')
#     wet = Symbol('wet')
    
#     knowlege = And(
#       Biconditional(rain, sun),
#       rain
#     )
    
#     knowlege = And(
#       Implication(And(sun, rain), rain),
#       # Implication(And(sun, rain), Not(sun)),
#       # sun,
#       # rain
#     )
#     # model_check(knowlege, sun)
#     print(model_check(knowlege, rain))
#     print(model_check(knowlege, sun))

#     assert True == False




def test_cmodel_check():
    knight = Symbol('is a knight')
    knave = Symbol('is a knave')

    knowlege = And(
      Not(And(knight, knave))
    )
    model_check(knowlege, knave)
    # model_check(knowlege, knight)
    
    assert True == False
