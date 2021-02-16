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
  assert rain.symbols() == { 'rain' }
  
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
  not_connective = Not(rain)
  model = {'rain': True, 'sunny': False}
  # calls operands evaluate fn 
  # operand = rain = Symbol('rain')
  # evaluate(self, model) --> bool(modes[rain.name])
  # inverses the logic !! evaluate(self, model)
  
  # Not(rain) == False
  assert not_connective.evaluate(model) == False


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


# class type
def test_and_connective_class():
  rain = Symbol('rain')
  wet = Symbol('wet')
  and_connective = And(rain, wet)
  assert isinstance(and_connective, Sentence)
  assert isinstance(and_connective, And)


# conjuncts()
def test_and_connective_conjuncts():
  rain = Symbol('rain')
  wet = Symbol('wet')
  and_connective = And(rain, wet)
  assert and_connective.conjuncts == [rain, wet]


# evaluate()
def test_and_connective_evaluate():
  # TESTS Symbol FN
  rain = Symbol('rain')
  wet = Symbol('wet')
  sunny = Symbol('sunny')
  and_connective = And(rain, sunny)
  model = {'rain': True, 'sunny': False }
  # calls evaluate on each conjunct 
  # ands them together

  # Rain and Sun 
  assert and_connective.evaluate(model) == False
  
  wet = Symbol('wet')
  and_connective = And(rain, wet)
  model = {'rain': True, 'wet': True}
  # Rain and Wet
  assert and_connective.evaluate(model) == True


# formula()
def test_and_connective_formula():
  rain = Symbol('rain')
  wet = Symbol('wet')
  and_connective = And(rain, wet)
  # returns string repr of connective and symbol
  assert and_connective.formula() == 'rain ∧ wet'


# symbols()
def test_and_connective_symbols():
  # TESTS Symbol FN
  rain = Symbol('rain')
  wet = Symbol('wet')
  sunny = Symbol('sunny')
  and_connective = And(rain, wet, sunny)
  # calls symbols fn on each conjunctive
  assert isinstance(and_connective.symbols(), set)
  assert and_connective.symbols() == {'rain', 'wet', 'sunny'}
 
 
# add() 
def test_and_connective_add():
  # TESTS Symbol FN
  rain = Symbol('rain')
  wet = Symbol('wet')
  sunny = Symbol('sunny')
  and_connective = And(rain, wet)
  and_connective.add(sunny)
  assert and_connective.symbols() == {'rain', 'wet', 'sunny'}
