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
    #dirpath = os.getcwd()
    #print("current directory is : " + dirpath)
    #foldername = os.path.basename(dirpath)
    #print("Directory name is : " + foldername)
    #scriptpath = os.path.realpath(__file__)
    #scriptpath = os.path.abspath(__file__)
    current_path = os.path.dirname(os.path.abspath(__file__))
    return current_path
    print("Script path is : " + scriptpath)


def split_rules(rules_str):
    rules_str = rules_str.split('#')
    rules_list = []
    for rule in rules_str:
        if rule != '':
            rules_list.append(rule)
            #print('*.*'+ rule + '*.*')
    return rules_list

def trim_rules(rules_list):
    trim_list = []
    for rule in rules_list:
        trim_list.append(rule.strip())
   
    return trim_list

def map_rule(rule_statment):
    rule_dict = {}




def read_file(filepath):
    # Open a file: file
    file = open(filepath,mode='r')
 
    # read all lines at once
    all_of_it = file.read()
 
    # close the file
    file.close()

    return all_of_it


def main():
    print("Hello from the parser 🤗")
    cfg = get_current_directory()
    print_yellow(cfg)
    cfg +=  "/CFG.txt"
    print_blue(cfg)
    file_content = read_file(cfg)
    rules_list = split_rules(file_content)
    
    """ print_green(rules_list[0])
    rules_list[0].strip()
    print_red(rules_list[0])
 """
    trim_list = trim_rules(rules_list)
    for rule in trim_list:
        print_red(rule)
    
    



if __name__ == '__main__':
    main()
