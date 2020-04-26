import os

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

unique_id = 65
G_identifiers = {}

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
    print_yellow(entire_str)

    statement_list = entire_str.split(" ")
    #print_green(statement_list)
    statement_set = set(statement_list)
    print_blue(statement_set)

    return statement_set

  

def assign_unique_value(statement_set):
    '''
    assign unique values for the identifier
    for simplicty in code
    
    '''
    global unique_id
    for i in statement_set:
        if i not in G_identifiers:
            
            if unique_id == 91:
                unique_id = 97
        

            G_identifiers[i] = chr(unique_id)
            unique_id += 1

            

def print_g_id():
    for i in G_identifiers:
        print_green(f'{i} --> {G_identifiers[i]}')
    


def read_file(filepath):
    # Open a file: file
    file = open(filepath,mode='r')
 
    # read all lines at once
    all_of_it = file.read()
 
    # close the file
    file.close()

    return all_of_it


def main():
    grammar_dict = {}
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
        print_yellow(m)
    
    for i in grammar_dict:
        set_s = simplify_rule(i,grammar_dict[i])
        assign_unique_value(set_s)
    
    
    print_g_id()
    #simplify_rule(m[0], )
    xx = "ggg"
    xx = xx.replace(xx,chr(65))
    print_red(xx)
"""     trim_list = trim_rules(rules_list)
    for rule in trim_list:
        print_red(rule)
    
    g = partition_rule(trim_list[1])
    divide_RHS(g[1])
 """



if __name__ == '__main__':
    main()
