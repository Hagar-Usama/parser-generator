gram = {


    'A' : [['B','X','b','c'] , ['d','e','f'] , ['g','h','i'] , ['𝛆']],
    'X' : [['q']],
    'B' : ['s','𝛆']
}

terminal_list = ['A','X','B']

def is_terminal(A, terminal_list):
    if A in terminal_list:
        return True
    return False

def has_epsilon(my_list):
    if '𝛆' in my_list:
        return True
    return False

def get_first(grammar, terminal, terminal_list):
    first_i = set()

    print(f"first of {terminal}")

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
        1) For a production rule X → ∈,
            First(X) = { ∈ }

        2) For any terminal symbol ‘a’,
            First(a) = { a }
        
    
    '''
    firsts = {}
    for i in grammar:
        first_i = set()
        print(f"first of {i}")
        for j in grammar[i]:
            print(j[0])
            if not is_terminal(j[0], terminal_list):
                first_i.add(j[0])
            """ else:
                for k in j:
                    if is_terminal(k, terminal_list):
                        temp = get_first(k,terminal_list)
                        first_i.add(get_first(k))
                        if not has_epsilon(temp):
                            break """

                        


        print(first_i)
        return first_i




my_first = get_first(gram,'A', terminal_list)
print(my_first)
my_first = get_first(gram,'B', terminal_list)
print(my_first)
my_first = get_first(gram,'X', terminal_list)
print(my_first)




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