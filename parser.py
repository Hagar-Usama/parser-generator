import os

# https://bluesock.org/~willkg/dev/ansi.html
ANSI_RESET = "\u001B[0m"
ANSI_RED = "\u001B[31m"
ANSI_GREEN = "\u001B[32m"
ANSI_YELLOW = "\u001B[33m"
ANSI_BLUE = "\u001B[34m"



def print_yellow(msg):
    print(f"{ANSI_YELLOW}{msg}{ANSI_RESET}")


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
    
    rule_dict = {}
    part1 = partition_rule(rule_statment)
    part2 = divide_RHS(part1[1])
    rule_dict[part1[0]] = part2

    return rule_dict


def partition_rule(rule_statment):
    parts = rule_statment.split('=', 1)
    parts_temp = []
    for i in parts:
        parts_temp.append(i.strip()) 

    return parts_temp
    
def divide_RHS(rule_statment):
    parts = rule_statment.split('|')
    parts_temp = []
    for i in parts:
        parts_temp.append(i.strip())
        #print_green(i)

    return parts_temp



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
    
    #for i in grammar_dict:
    #    print_blue(i.value()
    
    
"""     trim_list = trim_rules(rules_list)
    for rule in trim_list:
        print_red(rule)
    
    g = partition_rule(trim_list[1])
    divide_RHS(g[1])
 """



if __name__ == '__main__':
    main()
