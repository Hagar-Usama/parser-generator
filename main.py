from modules.first_follow import get_non_terminal_list, get_terminal_list, build_parsing_table, parse_input, get_dict_items
from modules.color_print import print_blue, print_green, print_red, print_yellow
from modules.aux_func import get_current_directory, read_file, write_file, write_in_file, get_arg
from modules.parser_genrator import read_input_list, split_rules, get_start_symbol
from modules.parser_genrator import map_rule, trim_rules, grammar_dict,print_dictionary,show_parser_table



def main():

    ## set default file for args
    CFG_file =  get_arg(1, "inputs/CFG.txt")
    tokens_file =  get_arg(2, "inputs/tokens.txt")


    # my welcome
    print("Hello from the parser 🤗")

    # get current directory
    cd = get_current_directory()
    cfg = get_current_directory()

    input_path = cfg + '/' +  tokens_file
    input_list = read_input_list(input_path)

    # building path
    cfg +=   '/' +  CFG_file

    #print_blue(cfg)
    # read grammar input
    file_content = read_file(cfg)
    
    # spliting rules
    rules_list = split_rules(file_content)

    
    # get start symbol
    start_symbol = get_start_symbol(rules_list[0])

    # trim spaces in rule_list
    trim_list = trim_rules(rules_list)
   

    # parsing table LHS ans RHS
    for i in trim_list:
        m = map_rule(i)     
        grammar_dict.update(m)
    
    # print our grammar
    print_dictionary(grammar_dict)

    print("*."*20)

    # get terminal list
    terminal_list = get_terminal_list(grammar_dict)
    # get non-terminal list
    non_terminal_list = get_non_terminal_list(grammar_dict)
    # get input list (read from file)
    """ 
    input_list = ["'int'", "'id'","';'",
                  "'id'", "'assign'", "'num'", "';'",
                  "'if'", "'('", "'id'", "'relop'", "'num'", "')'",
                  "'{'", "'id'", "'assign'", "'num'", "'}'"]

    """  
    input_list = read_input_list(input_path)
    # build parsing table
    parsing_table = build_parsing_table(grammar_dict, non_terminal_list, start_symbol)
    # parse the input and show steps
    #todos, inputs, action = parse_input(parsing_table,input_list.copy(), start_symbol, non_terminal_list, terminal_list)
    package_list = parse_input(parsing_table,input_list.copy(), start_symbol, non_terminal_list, terminal_list)
    
    if not isinstance(package_list,bool):
        # tabulate the steps
        show_parser_table(input_list, package_list[0], package_list[1], package_list[2])
        #show_parser_table(input_list, todos, inputs, action)
        print(package_list[2])
    else:
        print_red("[Visualizing] Syntax Error, cannot tabulate")

    
    output_path = cd + '/' + 'outputs' + '/' + 'actions.txt'
    write_file(output_path, package_list[2]) 
            
    ######################
    # one more example
    #####################

    ## uncomment to reveal 
    """
    parsing_table = {
            'E': {'n': {'E': [['T', 'R']]}, '(': {'E': [['T', 'R']]} },
            'R': {'+': {'R': [['+', 'E']]}, '*': {'R': [['𝛆']]}, ')': {'R': [['𝛆']]}, '$': {'R': [['𝛆']]} },
            'T': {'n': {'T': [['F', 'S']]}, '(': {'T': [['F', 'S']]} },
            'S': {'+': {'S': [['𝛆']]}, ')': {'S': [['𝛆']]}, '$': {'S': [['𝛆']]}, '*': {'S': [['*','T']]}  },
            'F': {'n': {'F': [['n']]}, '(': {'F': [['(','E',')']]}},
    }
    
    non_terminal_list = {"E","R","T","S","F"}
    terminal_list = {'n','+','*','(', ')','$'}
    input_list = list("n+n*n")   
    headers = ["Todo", "Input", "Action"]

    todos, inputs, action = parse_input(parsing_table,input_list.copy(), 'E', non_terminal_list, terminal_list)
    show_parser_table(input_list, todos, inputs, action)
    """
  
if __name__ == '__main__':
    main()
