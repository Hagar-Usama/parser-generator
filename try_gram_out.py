import os
import sys


my_path = current_path = os.path.dirname(os.path.abspath(__file__))
my_path = my_path[:-16]
sys.path.insert(1, my_path)
import left_recursion
import left_factoring



grammar = {
    'M':



}
print("*.*.*"*15)
    # eliminating left recursion
    e_grammar = left_recursion.eliminate_lr(grammar_dict_sym)
    for i in e_grammar:
        print(f'{i}->{e_grammar[i]}')

    # eliminating left factoring
    el_grammar = left_factoring.eliminate_lf(e_grammar)


    grammar = {

    'METHOD_BODY': [['STATEMENT_LIST']],
    'STATEMENT_LIST': [['STATEMENT', 'STATEMENT_LIST_2']],
    'STATEMENT_LIST_2': [['STATEMENT', 'STATEMENT_LIST_2'], ['𝛆']],
    'STATEMENT': [['DECLARATION'], ['IF'], ['WHILE'], ['ASSIGNMENT']],
    'DECLARATION': [['PRIMITIVE_TYPE', "'id'", "';'"]],
    'PRIMITIVE_TYPE': [["'int'"], ["'float'"]],
    'IF': [["'if'", "'('", 'EXPRESSION', "')'", "'{'", 'STATEMENT', "'}'", "'else'", "'{'", 'STATEMENT', "'}'"]],
    'WHILE': [["'while'", "'('", 'EXPRESSION', "')'", "'{'", 'STATEMENT', "'}'"]],
    'ASSIGNMENT': [["'id'", "'assign'", 'EXPRESSION', "';'"]],
    'EXPRESSION': [['SIMPLE_EXPRESSION', 'EXPRESSION_2']],
    'EXPRESSION_2': [["'relop'", 'SIMPLE_EXPRESSION'], ['𝛆']],
    'SIMPLE_EXPRESSION': [['TERM', 'SIMPLE_EXPRESSION_2'], ['SIGN', 'TERM', 'SIMPLE_EXPRESSION_2']],
    'SIMPLE_EXPRESSION_2': [["'addop'", 'TERM', 'SIMPLE_EXPRESSION_2'], ['𝛆']],
    'TERM': [['FACTOR', 'TERM_2']],
    'TERM_2': [["'mulop'", 'FACTOR', 'TERM_2'], ['𝛆']],
    'FACTOR': [["'id'"], ["'num'"], ["'('", 'EXPRESSION', "')'"]],
    'SIGN': [["'addop'"]]
        
    }
