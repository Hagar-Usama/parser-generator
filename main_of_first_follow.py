# main of first follow

def main():
   
   
    grammar = {
    
    'S' : [['a','B','D','h']],
    'B' : [['c', 'C']],
    'C' : [['b','C'],['𝛆']],
    'D' : [['E','F']],
    'E' : [['g'],['𝛆']],
    'F' : [['f'],['𝛆']]

   }

   #print("Hey hey!")
   #non_terminal_list_22 = {'S','A', 'B','C','D', 'E', 'F'}
   #build_parsing_table(grammar, non_terminal_list_22, 'S')
   #get_non_terminal_list(grammar)
   #t = get_terminal_list(grammar)

    """ 
    grammar = {

    'METHOD_BODY': [['STATEMENT_LIST']],
    'STATEMENT_LIST': [['STATEMENT', ' ', 'STATEMENT_LIST_2']],
    'STATEMENT_LIST_2': [['STATEMENT', ' ', 'STATEMENT_LIST_2'], ['𝛆']],
    'STATEMENT': [['DECLARATION'], ['IF'], ['WHILE'], ['ASSIGNMENT']],
    'DECLARATION': [['PRIMITIVE_TYPE', ' ', "'id'", ' ', "';'"]],
    'PRIMITIVE_TYPE': [["'int'"], ["'float'"]],
    'IF': [["'if'", ' ', "'('", ' ', 'EXPRESSION', ' ', "')'", ' ', "'{'", ' ', 'STATEMENT', ' ', "'}'", ' ', "'else'", ' ', "'{'", ' ', 'STATEMENT', ' ', "'}'"]],
    'WHILE': [["'while'", ' ', "'('", ' ', 'EXPRESSION', ' ', "')'", ' ', "'{'", ' ', 'STATEMENT', ' ', "'}'"]],
    'ASSIGNMENT': [["'id'", ' ', "'assign'", ' ', 'EXPRESSION', ' ', "';'"]],
    'EXPRESSION': [['SIMPLE_EXPRESSION', ' ', 'EXPRESSION_2']],
    'EXPRESSION_2': [["'relop'", ' ', 'SIMPLE_EXPRESSION'], ['𝛆']],
    'SIMPLE_EXPRESSION': [['TERM', ' ', 'SIMPLE_EXPRESSION_2'], ['SIGN', ' ', 'TERM', ' ', 'SIMPLE_EXPRESSION_2']],
    'SIMPLE_EXPRESSION_2': [["'addop'", ' ', 'TERM', ' ', 'SIMPLE_EXPRESSION_2'], ['𝛆']],
    'TERM': [['FACTOR', ' ', 'TERM_2']],
    'TERM_2': [["'mulop'", ' ', 'FACTOR', ' ', 'TERM_2'], ['𝛆']],
    'FACTOR': [["'id'"], ["'num'"], ["'('", ' ', 'EXPRESSION', ' ', "')'"]],
    'SIGN': [["'addop'"]]
        
    }
    """

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


    grammar_sim = {
    'METHOD_BODY': [['STATEMENT_LIST']],
    'STATEMENT_LIST': [['STATEMENT', "STATEMENT_LIST'"]],
    'STATEMENT': [['DECLARATION'], ['IF'], ['WHILE'], ['ASSIGNMENT']],
    'DECLARATION': [['PRIMITIVE_TYPE', "'id'", "';'"]],
    'PRIMITIVE_TYPE': [["'int'"], ["'float'"]],
    'IF': [["'if'", "'('", 'EXPRESSION', "')'", "'{'", 'STATEMENT', "'}'", "'else'", "'{'", 'STATEMENT', "'}'"]],
    'WHILE': [["'while'", "'('", 'EXPRESSION', "')'", "'{'", 'STATEMENT', "'}'"]],
    'ASSIGNMENT': [["'id'", "'assign'", 'EXPRESSION', "';'"]],
    'EXPRESSION': [['METHOD_BODY0', "EXPRESSION'"]],
    'METHOD_BODY0': [['METHOD_BODY1', "METHOD_BODY0'"], ['METHOD_BODY3', 'METHOD_BODY1', "METHOD_BODY0'"]],
    'METHOD_BODY1': [['METHOD_BODY2', "METHOD_BODY1'"]],
    'METHOD_BODY2': [["'id'"], ["'num'"], ["'('", 'EXPRESSION', "')'"]],
    'METHOD_BODY3': [["'addop'"]],
    "STATEMENT_LIST'": [['STATEMENT', "STATEMENT_LIST'"], ['𝛆']],
    "METHOD_BODY0'": [["'addop'", 'METHOD_BODY1', "METHOD_BODY0'"], ['𝛆']],
    "METHOD_BODY1'": [["'mulop'", 'METHOD_BODY2', "METHOD_BODY1'"], ['𝛆']],
    "EXPRESSION'": [['𝛆'], ["'relop'", 'METHOD_BODY0']]
    }
    terminal_list = get_terminal_list(grammar)
    non_terminal_list = get_non_terminal_list(grammar)
    start_symbol = 'METHOD_BODY'
    table = build_parsing_table(grammar, non_terminal_list,start_symbol)


    """ 
    input_list = ["'int'", " ", "'id'", " ","';'",
                  " ","'id'"," ", "'assign'", " ", "'num'", " ", "';'",
                  " ", "'if'", " ", "'('", " ", "'id'", " ", "'relop'", " ", "'num'", " ", "')'",
                  " ", "'{'", " ", "'id'", " ", "'assign'", " ", "'num'"," ", "'}'"] 
    """
    """
    input_list = ["'if'", "'('", "'id'", "'relop'", "'num'", "')'",
                  "'{'", "'id'", "'assign'", "'num'", "'}'"]
    """

    
    input_list = ["'int'", "'id'","';'",
                  "'id'", "'assign'", "'num'", "';'",
                  "'if'", "'('", "'id'", "'relop'", "'num'", "')'",
                  "'{'", "'id'", "'assign'", "'num'", "'}'"]


            

    parse_input(table, input_list, start_symbol,non_terminal_list,terminal_list)


   


if __name__ == '__main__':
    main()





""" 

def main():
   
   
    grammar = {
    
    'S' : [['a','B','D','h']],
    'B' : [['c', 'C']],
    'C' : [['b','C'],['𝛆']],
    'D' : [['E','F']],
    'E' : [['g'],['𝛆']],
    'F' : [['f'],['𝛆']]

   }

   #print("Hey hey!")
   #non_terminal_list_22 = {'S','A', 'B','C','D', 'E', 'F'}
   #build_parsing_table(grammar, non_terminal_list_22, 'S')
   #get_non_terminal_list(grammar)
   #t = get_terminal_list(grammar)

    """ 
    """
    grammar = {

    'METHOD_BODY': [['STATEMENT_LIST']],
    'STATEMENT_LIST': [['STATEMENT', ' ', 'STATEMENT_LIST_2']],
    'STATEMENT_LIST_2': [['STATEMENT', ' ', 'STATEMENT_LIST_2'], ['𝛆']],
    'STATEMENT': [['DECLARATION'], ['IF'], ['WHILE'], ['ASSIGNMENT']],
    'DECLARATION': [['PRIMITIVE_TYPE', ' ', "'id'", ' ', "';'"]],
    'PRIMITIVE_TYPE': [["'int'"], ["'float'"]],
    'IF': [["'if'", ' ', "'('", ' ', 'EXPRESSION', ' ', "')'", ' ', "'{'", ' ', 'STATEMENT', ' ', "'}'", ' ', "'else'", ' ', "'{'", ' ', 'STATEMENT', ' ', "'}'"]],
    'WHILE': [["'while'", ' ', "'('", ' ', 'EXPRESSION', ' ', "')'", ' ', "'{'", ' ', 'STATEMENT', ' ', "'}'"]],
    'ASSIGNMENT': [["'id'", ' ', "'assign'", ' ', 'EXPRESSION', ' ', "';'"]],
    'EXPRESSION': [['SIMPLE_EXPRESSION', ' ', 'EXPRESSION_2']],
    'EXPRESSION_2': [["'relop'", ' ', 'SIMPLE_EXPRESSION'], ['𝛆']],
    'SIMPLE_EXPRESSION': [['TERM', ' ', 'SIMPLE_EXPRESSION_2'], ['SIGN', ' ', 'TERM', ' ', 'SIMPLE_EXPRESSION_2']],
    'SIMPLE_EXPRESSION_2': [["'addop'", ' ', 'TERM', ' ', 'SIMPLE_EXPRESSION_2'], ['𝛆']],
    'TERM': [['FACTOR', ' ', 'TERM_2']],
    'TERM_2': [["'mulop'", ' ', 'FACTOR', ' ', 'TERM_2'], ['𝛆']],
    'FACTOR': [["'id'"], ["'num'"], ["'('", ' ', 'EXPRESSION', ' ', "')'"]],
    'SIGN': [["'addop'"]]
        
    }
    """
    """

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


    grammar_sim = {
    'METHOD_BODY': [['STATEMENT_LIST']],
    'STATEMENT_LIST': [['STATEMENT', "STATEMENT_LIST'"]],
    'STATEMENT': [['DECLARATION'], ['IF'], ['WHILE'], ['ASSIGNMENT']],
    'DECLARATION': [['PRIMITIVE_TYPE', "'id'", "';'"]],
    'PRIMITIVE_TYPE': [["'int'"], ["'float'"]],
    'IF': [["'if'", "'('", 'EXPRESSION', "')'", "'{'", 'STATEMENT', "'}'", "'else'", "'{'", 'STATEMENT', "'}'"]],
    'WHILE': [["'while'", "'('", 'EXPRESSION', "')'", "'{'", 'STATEMENT', "'}'"]],
    'ASSIGNMENT': [["'id'", "'assign'", 'EXPRESSION', "';'"]],
    'EXPRESSION': [['METHOD_BODY0', "EXPRESSION'"]],
    'METHOD_BODY0': [['METHOD_BODY1', "METHOD_BODY0'"], ['METHOD_BODY3', 'METHOD_BODY1', "METHOD_BODY0'"]],
    'METHOD_BODY1': [['METHOD_BODY2', "METHOD_BODY1'"]],
    'METHOD_BODY2': [["'id'"], ["'num'"], ["'('", 'EXPRESSION', "')'"]],
    'METHOD_BODY3': [["'addop'"]],
    "STATEMENT_LIST'": [['STATEMENT', "STATEMENT_LIST'"], ['𝛆']],
    "METHOD_BODY0'": [["'addop'", 'METHOD_BODY1', "METHOD_BODY0'"], ['𝛆']],
    "METHOD_BODY1'": [["'mulop'", 'METHOD_BODY2', "METHOD_BODY1'"], ['𝛆']],
    "EXPRESSION'": [['𝛆'], ["'relop'", 'METHOD_BODY0']]
    }
    terminal_list = get_terminal_list(grammar)
    non_terminal_list = get_non_terminal_list(grammar)
    start_symbol = 'METHOD_BODY'
    table = build_parsing_table(grammar, non_terminal_list,start_symbol)


    """ 
    input_list = ["'int'", " ", "'id'", " ","';'",
                  " ","'id'"," ", "'assign'", " ", "'num'", " ", "';'",
                  " ", "'if'", " ", "'('", " ", "'id'", " ", "'relop'", " ", "'num'", " ", "')'",
                  " ", "'{'", " ", "'id'", " ", "'assign'", " ", "'num'"," ", "'}'"] 
    """
    """
    input_list = ["'if'", "'('", "'id'", "'relop'", "'num'", "')'",
                  "'{'", "'id'", "'assign'", "'num'", "'}'"]
    """

    
    input_list = ["'int'", "'id'","';'",
                  "'id'", "'assign'", "'num'", "';'",
                  "'if'", "'('", "'id'", "'relop'", "'num'", "')'",
                  "'{'", "'id'", "'assign'", "'num'", "'}'"]


            

    parse_input(table, input_list, start_symbol,non_terminal_list,terminal_list)


   


if __name__ == '__main__':
    main()

 """