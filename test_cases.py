import pytest
from first_follow import get_first, get_firsts, get_follow, get_rhs, find_first, parse_production, find_first_sole, get_follows
from first_follow import parse_find_first

ANSI_RESET = "\u001B[0m"
ANSI_RED = "\u001B[31m"
ANSI_GREEN = "\u001B[32m"
ANSI_YELLOW = "\u001B[33m"
ANSI_BLUE = "\u001B[34m"
ANSI_PURPLE = "\u001B[35m"
#ANSI_YELLOW = "\u001B[36m"



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



def test_get_first():
    
    # case 1
    case = f"{ANSI_YELLOW}get first case 1{ANSI_RESET}"
    gram = {
    'A' : [['B','X','b','c'] , ['d','e','f'] , ['g','h','i'] , ['𝛆']],
    'X' : [['q']],
    'B' : [['s'],['𝛆']]
    }

    non_terminal_list = ['A','X','B']
    correct_value = {'A': {'d', 's', 'g', 'q', '𝛆'}, 'X': {'q'}, 'B': {'𝛆', 's'}}
    actual_value = get_firsts(gram, non_terminal_list)
    assert_it(correct_value, actual_value, case)


    # case 2
    case = f"{ANSI_YELLOW}get first case 2{ANSI_RESET}"
    
    gram = {
    'S': [['A','B','C','D']],
    'A': [['a'], ['𝛆']],
    'B': [['C','D'], ['b']],
    'C': [['c'],['𝛆']],
    'D': [['A','a'], ['d'],['𝛆']]
    }
    
    non_terminal_list = ['S','A','B','C','D']
    correct_value = {'S': {'a', 'c', '𝛆', 'b', 'd'}, 'A': {'a', '𝛆'}, 'B': {'a', 'c', '𝛆', 'b', 'd'}, 'C': {'c', '𝛆'}, 'D': {'a', '𝛆', 'd'}}
    actual_value = get_firsts(gram, non_terminal_list)
    assert_it(correct_value, actual_value, case)

    # case 3 ex_2
    case = f"{ANSI_YELLOW}get first case 3{ANSI_RESET}"
    gram = {
    'S': [['A']],
    'A': [['a','B',"A'"]],
    "A'": [['d',"A'"],['𝛆']],
    'B': [['b']],
    "A'": [['d',"A'"],['𝛆']],
    'C': [['g']]
    } 
    
    non_terminal_list = ["S", "A" , "A'", "B", "C"]
    correct_value = {'S': {'a'}, 'A': {'a'}, "A'": {'d', '𝛆'}, 'B': {'b'}, 'C': {'g'}}
    actual_value = get_firsts(gram, non_terminal_list)
    assert_it(correct_value, actual_value, case)

    # case 4 ex3 gatevid
    case = f"{ANSI_YELLOW}get first case 4{ANSI_RESET}"
    gram = {
    'S': [['(','L',')'],['a']],
    'L': [['S',"L'"]],
    "L'": [[',','S'],['𝛆']]
    }

    non_terminal_list = {"S", "L", "L'"}
    correct_value = {'S': {'(','a'}, 'L': {'(','a'}, "L'": {',', '𝛆'}}
    actual_value = get_firsts(gram, non_terminal_list)
    assert_it(correct_value, actual_value, case)


    case = f"{ANSI_YELLOW}get first case 5{ANSI_RESET}"
    gram = {
    'S': [['A', 'a','A','b'],['B', 'b','B','a']],
    'A': [['𝛆']],
    'B': [['𝛆']]
    }

    non_terminal_list = {'S', 'A', 'B'}
    correct_value ={'S': {'a', 'b'}, 'A': {'𝛆'}, 'B': {'𝛆'}}
    actual_value = get_firsts(gram, non_terminal_list)
    assert_it(correct_value, actual_value, case)



def test_rhs():
    # case 1
    case = f"{ANSI_YELLOW}get rhs case 1{ANSI_RESET}"
    gram = {
    'A' : [['B','X','b','c'] , ['X','e','f'] , ['g','h','i'], ['d','X','e','f'], ['𝛆']],
    'X' : [['q']],
    'B' : ['s','𝛆']
    }
    
    correct_value = {}
    actual_value = get_rhs(gram , 'A')
    assert_it(correct_value, actual_value, case)

    # case 2
    case = f"{ANSI_YELLOW}get rhs case 2{ANSI_RESET}"
    correct_value = {'A' : [['b','c'], ['e', 'f']]}
    actual_value = get_rhs(gram , 'X')
    assert_it(correct_value, actual_value, case)

    # case 3
    case = f"{ANSI_YELLOW}get rhs case 3{ANSI_RESET}"
    correct_value = {'A' : [['X','b','c']]}
    actual_value = get_rhs(gram , 'B')
    assert_it(correct_value, actual_value, case)

    gram = {
    'S': [['A']],
    'A': [['a','B',"A'"]],
    "A'": [['d',"A'"],['𝛆']],
    'B': [['b']],
    'C': [['g'],['D','g']],
    'D': [['A','c','d'], ['B'], ['c','A']]

    }

    # case 4
    case = f"{ANSI_YELLOW}get rhs case 4{ANSI_RESET}"
    correct_value = {'S' : [[]], 'D': [['c' , 'd'], []]}
    actual_value = get_rhs(gram , 'A')

    print(len(actual_value["S"]))
    assert_it(correct_value, actual_value, case)

def test_find_first_sole():
    gram = {
    'S': [['A']],
    'A': [['a','B',"A'"]],
    "A'": [['d',"A'"],['𝛆']],
    'B': [['b']],
    'C': [['g'],['D','g']],
    'D': [['A','c','d'], ['B'], ['c','A']]

    }

    case = f"{ANSI_YELLOW}find first case 1{ANSI_RESET}"
    #find follow for A
    non_terminal_list = ['S', "A", "A'", "B", "C", "d"]
    non_terminal_production = {'S' : [['𝛆']], 'D': [['c' , 'd'], ['𝛆']]}
    first, follow = find_first_sole(gram,'A', non_terminal_production, non_terminal_list)
    actual_value = parse_find_first(first, follow) 
    correct_value = [{'c'}, {'S','D'}]
    assert_it(correct_value, actual_value, case)

    case = f"{ANSI_YELLOW}find first case 2{ANSI_RESET}"
    #find follow for A
    non_terminal_production = parse_production(get_rhs(gram, 'D')) 
    first, follow = find_first_sole(gram,'D', non_terminal_production, non_terminal_list) 
    actual_value = parse_find_first(first, follow)
    correct_value = [{'g'}, set()]
    assert_it(correct_value, actual_value, case)

    gram = {
    'A' : [['B','X','b','c'] , ['d','e','f'] , ['g','h','i'] , ['𝛆']],
    'X' : [['q']],
    'B' : [['X', 's'],['𝛆']]
    }

    non_terminal_list = ['A','X','B']

    case = f"{ANSI_YELLOW}find first case 3{ANSI_RESET}"
    #find follow for A
    
    non_terminal_production = parse_production(get_rhs(gram, 'X'))
    first, follow = find_first_sole(gram,'X', non_terminal_production, non_terminal_list)
    actual_value = parse_find_first(first, follow)
    correct_value = [{'b', 's'}, set() ]
    assert_it(correct_value, actual_value, case)

    gram = {
    
    'S' : [['a','B','D','h']],
    'B' : [['c', 'C']],
    'C' : [['b','C'],['𝛆']],
    'D' : [['E','F']],
    'E' : [['g'],['𝛆']],
    'F' : [['f'],['𝛆']]
    }

    case = f"{ANSI_YELLOW}find first case 4{ANSI_RESET}"
    #find follow for A
    non_terminal_list = {'S','B','C','D','E','F'}    
    non_terminal_production = parse_production(get_rhs(gram, 'B')) 
    first, follow = find_first_sole(gram,'B', non_terminal_production, non_terminal_list)
    actual_value = parse_find_first(first, follow)
    correct_value = [{'g','f','h'}, set() ]
    assert_it(correct_value, actual_value, case)



def test_find_first():

    gram = {
    'S': [['A']],
    'A': [['a','B',"A'"]],
    "A'": [['d',"A'"],['𝛆']],
    'B': [['b']],
    'C': [['g'],['D','g']],
    'D': [['A','c','d'], ['B'], ['c','A']]

    }

    case = f"{ANSI_YELLOW}find first case 1{ANSI_RESET}"
    #find follow for A
    non_terminal_list = ['S', "A", "A'", "B", "C", "d"]
    non_terminal_production = {'S' : [['𝛆']], 'D': [['c' , 'd'], ['𝛆']]}
    actual_value = find_first(gram, non_terminal_production, non_terminal_list)
    correct_value = None
    assert_it(correct_value, actual_value, case)

    pass

def test_get_follow():
    gram = {
    
    'S' : [['a','B','D','h']],
    'B' : [['c', 'C']],
    'C' : [['b','C'],['𝛆']],
    'D' : [['E','F']],
    'E' : [['g'],['𝛆']],
    'F' : [['f'],['𝛆']]
    }

    case = f"{ANSI_YELLOW}get follow case 1{ANSI_RESET}"
    #find follow for A
    non_terminal_list = {'S','B','C','D','E','F'} 
    non_terminal = 'S'   
    first_set = get_firsts(gram, non_terminal_list)
    start_symbol = 'S'


    actual_value = get_follow(gram, non_terminal, first_set, start_symbol, non_terminal_list)
    correct_value = {'$'}
    assert_it(correct_value, actual_value, case)

    case = f"{ANSI_YELLOW}get follow case 2{ANSI_RESET}"
    non_terminal = 'B' 
    actual_value = get_follow(gram, non_terminal, first_set, start_symbol, non_terminal_list)
    correct_value = {'g','f','h'}
    assert_it(correct_value, actual_value, case)

    case = f"{ANSI_YELLOW}get follow case 3{ANSI_RESET}"
    non_terminal = 'C' 
    actual_value = get_follow(gram, non_terminal, first_set, start_symbol, non_terminal_list)
    correct_value = {'g','f','h'}
    assert_it(correct_value, actual_value, case)

    case = f"{ANSI_YELLOW}get follow case 4{ANSI_RESET}"
    non_terminal = 'D' 
    actual_value = get_follow(gram, non_terminal, first_set, start_symbol, non_terminal_list)
    correct_value = {'h'}
    assert_it(correct_value, actual_value, case)

    case = f"{ANSI_YELLOW}get follow case 5{ANSI_RESET}"
    non_terminal = 'E' 
    actual_value = get_follow(gram, non_terminal, first_set, start_symbol, non_terminal_list)
    correct_value = {'f','h'}
    assert_it(correct_value, actual_value, case)

    case = f"{ANSI_YELLOW}get follow case 5{ANSI_RESET}"
    non_terminal = 'F' 
    actual_value = get_follow(gram, non_terminal, first_set, start_symbol, non_terminal_list)
    correct_value = {'h'}
    assert_it(correct_value, actual_value, case)

    
    gram = {
    'S': [['A']],
    'A': [['a','B',"A'"]],
    "A'": [['d',"A'"],['𝛆']],
    'B': [['b']],
    'C': [['g'],['D','g']],
    'D': [['A','c','d'], ['B'], ['c','A']]
    }

    ase = f"{ANSI_YELLOW}get follow case 5{ANSI_RESET}"
    #find follow for A
    non_terminal_list = {'S','A', "A'", 'B','C','D'} 
    non_terminal = 'S'   
    first_set = get_firsts(gram, non_terminal_list)
    start_symbol = 'S'


    actual_value = get_follow(gram, non_terminal, first_set, start_symbol, non_terminal_list)
    correct_value = {'$'}
    assert_it(correct_value, actual_value, case)

def test_get_follows():
    gram = {
    
    'S' : [['a','B','D','h']],
    'B' : [['c', 'C']],
    'C' : [['b','C'],['𝛆']],
    'D' : [['E','F']],
    'E' : [['g'],['𝛆']],
    'F' : [['f'],['𝛆']]
    }

    case = f"{ANSI_YELLOW}get follows case 1{ANSI_RESET}"
    #find follow for A
    non_terminal_list = {'S','B','C','D','E','F'}   
    first_set = get_firsts(gram, non_terminal_list)
    start_symbol = 'S'

    actual_value = get_follows(gram, first_set, start_symbol, non_terminal_list)
    correct_value =  {'S': {'$'}, 'F': {'h'}, 'C': {'f', 'h', 'g'}, 'B': {'f', 'h', 'g'}, 'E': {'f', 'h'}, 'D': {'h'}}

    assert_it(correct_value, actual_value, case)


    gram = {
    'S': [['A']],
    'A': [['a','B',"A'"]],
    "A'": [['d',"A'"],['𝛆']],
    'B': [['b']],
    'C': [['g']]
    
    }

    case = f"{ANSI_YELLOW}get follows case 2{ANSI_RESET}"
    non_terminal_list = {'S', 'A', "A'", 'B','C'} 
    first_set = get_firsts(gram, non_terminal_list)
    start_symbol = 'S'  
    actual_value = get_follows(gram, first_set, start_symbol, non_terminal_list)
    correct_value =  {'A': {'$'}, 'C': set(), "A'": {'$'}, 'S': {'$'}, 'B': {'$', 'd'}}
    assert_it(correct_value, actual_value, case)

    gram = {
    'S': [['(','L',')'],['a']],
    'L': [['S',"L'"]],
    "L'": [[',','S'],['𝛆']]
    }

    case = f"{ANSI_YELLOW}get follows case 3{ANSI_RESET}"
    non_terminal_list = {'S', 'L', "L'"} 
    first_set = get_firsts(gram, non_terminal_list)
    start_symbol = 'S'  
    actual_value = get_follows(gram, first_set, start_symbol, non_terminal_list)
    correct_value =  {'L': {')'}, 'S': {'$', ')', ','}, "L'": {')'}}
    assert_it(correct_value, actual_value, case)

    gram = {
    'S': [['A','a','A','b'],['B','b', 'B', 'a']],
    'A': [['𝛆']],
    'B': [['𝛆']]
    }

    case = f"{ANSI_YELLOW}get follows case 4{ANSI_RESET}"
    non_terminal_list = {'S', 'A', 'B'} 
    first_set = get_firsts(gram, non_terminal_list)
    start_symbol = 'S'  
    actual_value = get_follows(gram, first_set, start_symbol, non_terminal_list)
    correct_value =  {'A': {'a', 'b'}, 'S': {'$'}, 'B': {'a','b'}}
    assert_it(correct_value, actual_value, case)

    

    




def test_parse_production():

    case = f"{ANSI_YELLOW}parse production case 1{ANSI_RESET}"
    production_list = {'S' : [[]], 'D': [['c' , 'd'], []]}
    actual_value = parse_production(production_list)
    correct_value = {'S' : [['𝛆']], 'D': [['c' , 'd'], ['𝛆']]}
    assert_it(correct_value, actual_value, case)



def assert_it(correct_value, actual_value, case=""):
        assert correct_value == actual_value,\
        f"{ANSI_RED}[failed] {case}"\
        f" Expected ( {correct_value} )\n got\n ( {actual_value} ){ANSI_RESET}"
        print_green(f"[success] {case}")


def main():
    ###################
    # Run tests
    ###################
    # Sorted by checklist order, feel free to comment/un-comment
    # any of those functions.
    try:
        test_get_first()
        print_blue('*.*.'*15)
        test_rhs()
        print_blue('*.*.'*15)
        test_parse_production()
        print_blue('*.*.'*15)
        test_find_first_sole()
        print_blue('*.*.'*15)
        test_get_follow()
        print_blue('*.*.'*15)
        test_get_follows()

    except AssertionError as e:
        print("Test case failed:\n", str(e))
        exit(-1)


if __name__ == "__main__":
    main()