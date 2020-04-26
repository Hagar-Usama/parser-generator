import os
import sys


my_path = current_path = os.path.dirname(os.path.abspath(__file__))
my_path = my_path[:-16]
sys.path.insert(1, my_path)
import left_recursion
import left_factoring


# https://bluesock.org/~willkg/dev/ansi.html
ANSI_RESET = "\u001B[0m"
ANSI_RED = "\u001B[31m"
ANSI_GREEN = "\u001B[32m"
ANSI_YELLOW = "\u001B[33m"
ANSI_BLUE = "\u001B[34m"
ANSI_PURPLE = "\u001B[35m"
""" ANSI_Light_Blue       "\e[1;34m"
ANSI_Light_Green      "\e[1;32m"
ANSI_Light_Cyan       "\e[1;36m"
ANSI_Light_Red        "\e[1;31m"
ANSI_Light_Purple     "\e[1;35m" """

# it shall be 65 
unique_id = 129300
G_identifiers = {}
grammar_dict = {}
grammar_dict_sym = {}



def print_yellow(msg):
    print(f"{ANSI_YELLOW}{msg}{ANSI_RESET}")

def print_purple(msg):
    print(f"{ANSI_PURPLE}{msg}{ANSI_RESET}")

def print_blue(msg):
    print(f"{ANSI_BLUE}{msg}{ANSI_RESET}")


def print_red(msg):
    print(f"{ANSI_RED}{msg}{ANSI_RESET}")


def print_green(msg):
    print(f"{ANSI_GREEN}{msg}{ANSI_RESET}")



def get_current_directory(): 
    current_path = os.path.dirname(os.path.abspath(__file__))
    return current_path
    print("Script path is : " + scriptpath)

def read_file(filepath):
    # Open a file: file
    file = open(filepath,mode='r')
 
    # read all lines at once
    all_of_it = file.read()
 
    # close the file
    file.close()

    return all_of_it

def write_in_file(filepath , content , mod='w'):
    # Open a file: file
    file = open(filepath,mode=mod)
 
    # read all lines at once
    all_of_it = file.write(content)
 
    # close the file
    file.close()


def split_rules(rules_str):
    '''
    returns a list of rules
    '''
    rules_str = rules_str.split('#')
    rules_list = []
    for rule in rules_str:
        if rule != '':
            rules_list.append(rule)
    return rules_list


def trim_rules(rules_list):
    '''
    trims the list of rules
    
    '''
    trim_list = []
    for rule in rules_list:
        trim_list.append(rule.strip())
   
    return trim_list

def map_rule(rule_statment):
    '''
    converts rule into map LHS & RHS
    '''
    
    rule_dict = {}
    part1 = partition_rule(rule_statment)
    part2 = divide_RHS(part1[1])
    rule_dict[part1[0]] = part2

    return rule_dict


def partition_rule(rule_statment):
    '''
    partition rule LHS and RHS
    '''
    parts = rule_statment.split('=', 1)
    parts_temp = []
    for i in parts:
        parts_temp.append(i.strip()) 

    return parts_temp
    
def divide_RHS(rule_statment):
    '''
    divides the RHS if contains more than one option
    '''
    parts = rule_statment.split('|')
    parts_temp = []
    for i in parts:
        parts_temp.append(i.strip())
        #print_green(i)

    return parts_temp

def  simplify_rule(LHS, RHS):
    ''' 
    replaces identifiers with one char 
    for simplicity 

    updates the identifier set

    '''
    unique_char = 65
    set_all = {}
    RHS_list = []
    RHS_str = ''

    for i in RHS: 
        RHS_str += i
        RHS_str += " "

    entire_str = str(LHS) + " " + RHS_str   
        
    #print_purple(RHS_str)
    entire_str = entire_str.strip()
    #print_yellow(entire_str)

    statement_list = entire_str.split(" ")
    #print_green(statement_list)
    statement_set = set(statement_list)
    #print_blue(statement_set)

    return statement_set

  

def assign_unique_value(statement_set):
    '''
    assign unique values for the identifier
    for simplicty in code
    
    '''
    global unique_id

    keys = G_identifiers.keys()
    keys_list = sort_keys(keys)

    for i in statement_set:
        if i not in keys:
            
            if unique_id == 91:
                unique_id = 97
            elif unique_id == 120518:
                #reserved for epsilon
                unique_id +=1
        

            G_identifiers[i] = chr(unique_id)
            unique_id += 1


def subs_grammar():

    new_dict = {}
    for i in grammar_dict:
        RHS_list = subs_list(grammar_dict[i])
        
        new_dict[G_identifiers[i]] = RHS_list

    #print_dictionary(new_dict)
    
    return new_dict

         
def subs_list(statement_list):
    new_list = []
    for i in statement_list:
        if  i in G_identifiers:
            #print_blue("found")
            new_list.append(G_identifiers[i])
        else:
            #print_red("not found")
            new_list.append(subs_loop(i))
           # print_yellow(i)
     
    return new_list               

def sort_keys(keys):
    key_list = []
    # sort keys by length to avoid error
    for k in sorted(keys, key=lambda k: len(k), reverse=True):
        key_list.append(k)
    return key_list


def subs_loop(statement_list):
    
    keys = G_identifiers.keys()
    key_list = sort_keys(keys)
    
    statement_str = statement_list
    
    for i in key_list:
        statement_str = statement_str.replace(i, G_identifiers[i])
    
    return statement_str
    
def print_dictionary(dict_map):
    
    for i in dict_map:
        print_blue(f'{i} ⟶ {dict_map[i]}')
        

def print_g_id():
    path = get_current_directory()
    path+='/identifiers.txt'
    write_in_file(path,"", 'w+')
        
    for i in G_identifiers:
        print_green(f'{i} ⟶  {G_identifiers[i]}\n')
        write_in_file(path,f'{i} ⟶ {G_identifiers[i]}\n', 'a+')

    




def main():
    
    print("Hello from the parser 🤗")
    cfg = get_current_directory()
    print_yellow(cfg)
    cfg +=  "/CFG.txt"
    print_blue(cfg)
    file_content = read_file(cfg)
    rules_list = split_rules(file_content)
    trim_list = trim_rules(rules_list)

    for i in trim_list:
        m = map_rule(i)
        grammar_dict.update(m)
        #print_yellow(m)
    
    for i in grammar_dict:
        set_s = simplify_rule(i,grammar_dict[i])
        assign_unique_value(set_s)
    
    
    print_g_id()
    # get dictionary in symbols (one symbol for each identifier)
    grammar_dict_sym =  subs_grammar()
    print("-0-0-"*20)

    print_dictionary(grammar_dict_sym)
    
    #simplify_rule(m[0], )

    print(ord('🤗'))
    print(chr(129303))
    print(grammar_dict_sym)

    print("*.*.*"*15)
    # eliminating left recursion
    e_grammar = left_recursion.eliminate_lr(grammar_dict_sym)
    for i in e_grammar:
        print(f'{i}->{e_grammar[i]}')

    # eliminating left factoring
    el_grammar = left_factoring.eliminate_lf(e_grammar)

    for i in e_grammar:
        print_yellow(f'{i}->{el_grammar[i]}')
    
    i = 129300
    for j in range(1,70):
        print(chr(i))
        i += 1

    print_blue(ord('𝛆'))
    xx = "ggg"
    print_purple(ord('🤿'))
    print_blue(ord('🤻'))
    """ for i in range(100,200):
        xx = xx.replace(xx,chr(i))
        print_red(xx)🤻🤿
 """

if __name__ == '__main__':
    main()
