import os
import sys


my_path = current_path = os.path.dirname(os.path.abspath(__file__))
my_path = my_path[:-16]
sys.path.insert(1, my_path)
import left_recursion
import left_factoring


grammar_dict_sym = {
 '🤕': ['🤔'],
 '🤔': ['🤖', '🤔 🤖'],
 '🤖': ['🤙', '🤘', '🤚', '🤗'],
 '🤙': ['🤛 🤜 🤝'],
 '🤛': ['🤞', '🤟'],
 '🤘': ['🤠 🤥 🤤 🤣 🤦 🤖 🤡 🤢 🤦 🤖 🤡'],
 '🤚': ['🤧 🤥 🤤 🤣 🤦 🤖 🤡'],
 '🤗': ['🤜 🤨 🤤 🤝'],
 '🤤': ['🤪', '🤪 🤩 🤪'],
 '🤪': ['🤫', '🤬 🤫', '🤪 🤭 🤫'],
 '🤫': ['🤯', '🤫 🤮 🤯'],
 '🤯': ['🤜', '🤰', '🤥 🤤 🤣'],
 '🤬': ['🤭']}


""" 
STATEMENT_LIST ⟶  🤔
METHOD_BODY ⟶  🤕
STATEMENT ⟶  🤖
ASSIGNMENT ⟶  🤗
IF ⟶  🤘
DECLARATION ⟶  🤙
WHILE ⟶  🤚
PRIMITIVE_TYPE ⟶  🤛
'id' ⟶  🤜
';' ⟶  🤝
'int' ⟶  🤞
'float' ⟶  🤟
'if' ⟶  🤠
'}' ⟶  🤡
'else' ⟶  🤢
')' ⟶  🤣
EXPRESSION ⟶  🤤
'(' ⟶  🤥
'{' ⟶  🤦
'while' ⟶  🤧
'assign' ⟶  🤨
'relop' ⟶  🤩
SIMPLE_EXPRESSION ⟶  🤪
TERM ⟶  🤫
SIGN ⟶  🤬
'addop' ⟶  🤭
'mulop' ⟶  🤮
FACTOR ⟶  🤯
'num' ⟶  🤰
"""

print("*.*.*"*15)
    # eliminating left recursion
e_grammar = left_recursion.eliminate_lr(grammar_dict_sym)
print("*."*10)
print(e_grammar)
print("*."*10)
for i in e_grammar:
    print(f'*{i}->{e_grammar[i]}')

    # eliminating left factoring
    #el_grammar = left_factoring.eliminate_lf(e_grammar)


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




"""
STATEMENT_LIST ⟶ 🤔
METHOD_BODY ⟶ 🤕
STATEMENT ⟶ 🤖
WHILE ⟶ 🤗
IF ⟶ 🤘
ASSIGNMENT ⟶ 🤙
DECLARATION ⟶ 🤚
'id' ⟶ 🤛
PRIMITIVE_TYPE ⟶ 🤜
';' ⟶ 🤝
'float' ⟶ 🤞
'int' ⟶ 🤟
EXPRESSION ⟶ 🤠
'}' ⟶ 🤡
'if' ⟶ 🤢
'{' ⟶ 🤣
'(' ⟶ 🤤
'else' ⟶ 🤥
')' ⟶ 🤦
'while' ⟶ 🤧
'assign' ⟶ 🤨
SIMPLE_EXPRESSION ⟶ 🤩
'relop' ⟶ 🤪
* SIGN ⟶ 🤫
TERM ⟶ 🤬
'addop' ⟶ 🤭
'mulop' ⟶ 🤮
* FACTOR ⟶ 🤯
'num' ⟶ 🤰
'-' ⟶ 🤱
'+' ⟶ 🤲
"""


# grammar without LR

"""
 g_lr = {
    '🤕': [['🤔']],
    '🤔': [['🤖', "🤔'"]],
    '🤖': [['🤙'], ['🤘'], ['🤚'], ['🤗']],
    '🤙': [['🤛',  '🤜',  '🤝']],
    '🤛': [['🤞'], ['🤟']],
    '🤘': [['🤠',  '🤥',  '🤤',  '🤣',  '🤦',  '🤖',  '🤡',  '🤢',  '🤦',  '🤖',  '🤡']],
    '🤚': [['🤧',  '🤥',  '🤤',  '🤣',  '🤦',  '🤖',  '🤡']],
    '🤗': [['🤜',  '🤨',  '🤤',  '🤝']],
    '🤤': [['🤕0'], ['🤕0',  '🤩',  '🤕0']],
    '🤕0': [['🤕1', "🤕0'"], ['🤕3',  '🤕1', "🤕0'"]],
    '🤕1': [['🤕2', "🤕1'"]],
    '🤕2': [['🤜'], ['🤰'], ['🤥',  '🤤',  '🤣']],
    '🤕3': [['🤭']],
    "🤔'": [[ '🤖', "🤔'"], ['𝛆']],
    "🤕0'": [[ '🤭',  '🤕1', "🤕0'"], ['𝛆']],
    "🤕1'": [[ '🤮',  '🤕2', "🤕1'"], ['𝛆']]
    }


 """

g_lr = {
    'METHOD_BODY': [['STATEMENT_LIST']],
    'STATEMENT_LIST': [['STATEMENT', "STATEMENT_LIST'"]],
    'STATEMENT': [['DECLARATION'], ['IF'], ['WHILE'], ['ASSIGNMENT']],
    'DECLARATION': [['PRIMITIVE_TYPE',  "'id'",  "';'"]],
    'PRIMITIVE_TYPE': [["'int'"], ["'float'"]],
    'IF': [["'if'",  "'('",  'EXPRESSION',  "')'",  "'{'",  'STATEMENT',  "'}'",  "'else'",  "'{'",  'STATEMENT',  "'}'"]],
    'WHILE': [["'while'",  "'('",  'EXPRESSION',  "')'",  "'{'",  'STATEMENT',  "'}'"]],
    'ASSIGNMENT': [["'id'",  "'assign'",  'EXPRESSION',  "';'"]],
    'EXPRESSION': [['METHOD_BODY0'], ['METHOD_BODY0',  "'relop'",  'METHOD_BODY0']],
    'METHOD_BODY0': [['METHOD_BODY1', "METHOD_BODY0'"], ['METHOD_BODY3',  'METHOD_BODY1', "METHOD_BODY0'"]],
    'METHOD_BODY1': [['METHOD_BODY2', "METHOD_BODY1'"]],
    'METHOD_BODY2': [["'id'"], ["'num'"], ["'('",  'EXPRESSION',  "')'"]],
    'METHOD_BODY3': [["'addop'"]],
    "STATEMENT_LIST'": [[ 'STATEMENT', "STATEMENT_LIST'"], ['𝛆']],
    "METHOD_BODY0'": [[ "'addop'",  'METHOD_BODY1', "METHOD_BODY0'"], ['𝛆']],
    "METHOD_BODY1'": [[ "'mulop'",  'METHOD_BODY2', "METHOD_BODY1'"], ['𝛆']]
    }

# eliminating left factoring
g_lf = left_factoring.eliminate_lf(g_lr)
print('f.'*20)
print(g_lf)

