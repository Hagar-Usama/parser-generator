
# test cases
# https://www.gatevidyalay.com/first-and-follow-compiler-design/

gram = {


    'A' : [['B','X','b','c'] , ['d','e','f'] , ['g','h','i'] , ['𝛆']],
    'X' : [['q']],
    'B' : ['s','𝛆']
}

gram2 = {
    'S': [['A','B','C','D']],
    'A': [['a'], ['𝛆']],
    'B': [['C','D'], ['b']],
    'C': [['c'],['𝛆']],
    'D': [['A','a'], ['d'],['𝛆']]

}

pr1 = {
    'S': [['A']],
    'A': [['a','B',"A'"]],
    "A'": [['d',"A'"],['𝛆']],
    'B': [['b']],
    "A'": [['d',"A'"],['𝛆']],
    'C': [['g']]

}

pr3 = {
    'S': [['(','L',')'],['a']],
    'L': [['S',"L'"]],
    "L'": [[',','S'],['𝛆']],
}
terminal_list = ['A','X','B']
terminal_list2 = ['S','A','B','C','D']
termial_pr1 = ["S", "A" , "A'", "B", "C"]
termial_pr3 = ["S", "L", "L'"]

def is_terminal(A, terminal_list):
    if A in terminal_list:
        return True
    return False

def has_epsilon(my_list):
    if '𝛆' in my_list:
        return True
    return False

def get_first(grammar, terminal, terminal_list):
    '''
    https://www.gatevidyalay.com/first-and-follow-compiler-design/

    rules applied: 

        1) For a production rule X → ∈,
            First(X) = { ∈ }

        2) For any terminal symbol ‘a’,
            First(a) = { a }

        3) For a production rule X → Y1Y2Y3,
            calculate first(Y1):
                If ∈ ∉ First(Y1), then First(X) = First(Y1)
                If ∈ ∈ First(Y1), then First(X) = { First(Y1) – ∈ } ∪ First(Y2Y3)
            else repeat 3) for Y(n+1)

        assumption for recursion:
            left recursion is eliminated

    '''
    first_i = set()

    #print(f"first of {terminal}")

    for j in grammar[terminal]:
        #print(j[0])
        if not is_terminal(j[0], terminal_list):
            first_i.add(j[0])
        else:
            for k in j:
                if is_terminal(k, terminal_list):
                    temp = get_first(grammar, k, terminal_list)
                    first_i.update(temp)
                    if not has_epsilon(temp):
                        break
                    

    return first_i

def get_firsts(grammar , terminal_list):
    '''
     collects each firsts in a BIG dictionary   
    
    '''
    firsts = {}
    for i in grammar:
        first_i = get_first(grammar, i, terminal_list)
        firsts[i] = first_i
    return firsts



first_set = get_firsts(gram2, terminal_list2)
first_set = get_firsts(gram, terminal_list)
first_set = get_firsts(pr1, termial_pr1)
first_set = get_firsts(pr3, termial_pr3)


#first_a = get_first(gram2, 'S',terminal_list2)
print(first_set)
""" 
my_first = get_first(gram,'A', terminal_list)
print(my_first)
my_first = get_first(gram,'B', terminal_list)
print(my_first)
my_first = get_first(gram,'X', terminal_list)
print(my_first)
 """



""" for i in gram:
    print(i, gram[i]) """
""" 
if '𝛆' == '𝛆':
    print("equal")
if "ê" == "ê":
    print("equal accent ")
if '🤕' == '🤕':
    print("equal emoji")
 """