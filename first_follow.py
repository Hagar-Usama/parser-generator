
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
non_terminal_list = ['A','X','B']
non_terminal_list2 = ['S','A','B','C','D']
termial_pr1 = ["S", "A" , "A'", "B", "C"]
termial_pr3 = ["S", "L", "L'"]

G_follow = {}
def is_non_terminal(A, non_terminal_list):
    if A in non_terminal_list:
        return True
    return False

def has_epsilon(my_list):
    if '𝛆' in my_list:
        return True
    return False

def get_first(grammar, non_terminal, non_terminal_list):
    first_i = set()

    # scanning each list in non_terminal
    for j in grammar[non_terminal]:
        #print(j[0])
        if is_non_terminal(j[0], non_terminal_list):
            # scanning each element in list
            for element in j:
                if is_non_terminal(element, non_terminal_list):
                    x = get_first(grammar, element, non_terminal_list)
                    #print(f"first of {element}")
                    first_i.update(x)
                    if not has_epsilon(x):
                        break
                else:
                    first_i.add(element)
                    
        else:
            first_i.add(j[0])
    return first_i


    

def get_first_1(grammar, non_terminal, non_terminal_list):
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

    # scanning each list in non_terminal
    for j in grammar[non_terminal]:
        #print(j[0])

        # if terminal add it directly
        if not is_non_terminal(j[0], non_terminal_list):
            first_i.add(j[0])
            
        else:
            # if a non-terminal,walk through
            for k in j:
                if is_non_terminal(k, non_terminal_list):
                    temp = get_first(grammar, k, non_terminal_list)
                    first_i.update(temp)
                    if not has_epsilon(temp):
                        break
                else:
                    print(k)
                    first_i.add[k]
                    break
                    

    return first_i

def get_follow(grammar, non_terminal, first_set, start_symbol, non_terminal_list):
    '''
        1) for starting symbol place $ in the follow set
        2) if the is a production A → 𝞪B𝝱:
            Follow(B) = First(𝝱)
            if First(𝝱) has 𝝴 :
                Follow(B) = Follow(A)
        3) if the is a production A → 𝞪B:
            Follow(B) = Follow(A)

        find_first_sole → returns firsts and follows NT

    '''
    follow_i = set()
    if non_terminal is start_symbol:
        follow_i.add('$')
        print("follow first")

    # step one get the follows based on firsts
    productions = parse_production(get_rhs(grammar, non_terminal))
    first_follow = find_first_sole(grammar, non_terminal, productions, non_terminal_list)
    follow_i.update(first_follow[0])
    for i in first_follow[1]:
        follow_i.update(get_follow(grammar, i, first_set, start_symbol, non_terminal_list)) 
    return follow_i



def parse_production(production_list):
    new_production_list = {}
    new_list_out = []
    temp = []
    for i in production_list:
        #print(production_list[i])
        new_list = []
        for j in production_list[i]:
            #print(j)
            
            if not j:
                #print("epsilon")
                temp = ['𝛆']
            else:
                temp = j
            new_list.append(temp)
        new_production_list[i] = new_list    
        #new_list_out.append(new_list)
    #print(new_production_list)
    return new_production_list


def find_first_sole(grammar, non_terminal, non_terminal_production, non_terminal_list):
    #non terminal production for one non-terminal
    first = set()
    follow_of_follow = set()
    
    for i in non_terminal_production:
        count = 0
        for j in non_terminal_production[i]:
            count += 1

            #print(f'*{j}*')
            #print(f'len of j : {len(j)}')
            for element in j:
                if is_non_terminal(element,non_terminal_list):
                    first.add(get_first(grammar, non_terminal, non_terminal_list))

                    # if a NT has no epsilon then no need to continue
                    if '𝛆' not in first_t:
                        break
                    # if NT has epsilon and it's the last one in list
                    elif count == len(j):
                        follow_of_follow.add(i)

                else:
                    if element == '𝛆':
                        follow_of_follow.add(i)
                    else:
                        first.add(element) 
                    break

        #print("*.*"*20)
    if '𝛆' in first:
        first.remove('𝛆')
    if '𝛆'in follow_of_follow:
        follow_of_follow.remove('𝛆')

    print(first)
    print(follow_of_follow)
    return [first,follow_of_follow]
    pass 


def find_first(grammar, non_terminal_production, non_terminal_list):
    '''
    
    '''
    first_i = set()
    follow_of_follow = set()

    count = 0

    for i in non_terminal_production:
        #print(i)
        for j in non_terminal_production[i]:
            print(j)
    
    #print(f'terminal production = {terminal_production}')
    """ 
    for i in non_terminal_production:
        print(f'non-terminal production part: {non_terminal_production[i]}')
        if len(non_terminal_production[i]) == 0:
            print("just get follow")
            break

        #print("enteur find")
        # going to each list for a 
        for j in non_terminal_production[i]:
            count += 1
            print(f'j is : {j}')

            for k in j:
                # first of non-terminal = get_first
                print(len(non_terminal_production[i]))
                if is_non_terminal(k, non_terminal_list):
                    print(f"{k} is non-terminal")

                    first_ii = get_first(grammar, k, non_terminal_list)
                    print(f'first : {first_ii}')
                    first_i.update(first_ii)
                    if '𝛆' not in first_ii:
                        print("epsilon not found!!")
                        # if last of the list of firsts  &&  is a non-terminal
                        # add follow of j
                        break
                    
                    # if we are in the last element and this element has 𝛆
                    # then get follow of j 
                    if count == len(non_terminal_production[i]):
                        print(f"followee = {i}")
                        follow_of_follow.add(i)

                else:
                    first_i.add(j)
    first_i.remove('𝛆')
    print(f'i in find first = {count}') 
    """
    return first_i



def get_rhs(grammar, non_terminal):
    rhs_dict = {}
    first = []
    second = []
    # for each rule
    for i in grammar:
        #print(grammar[i])
        # for each list in a rule
        first = []
        for j in grammar[i]:
            #print(f'j is: {j}')
            if non_terminal in j:
                #print("guard")
                indx = j.index(non_terminal)
                #print(indx)
                #print(f"{i} --> *{j[indx+1:]}* ")
                if j[indx+1:] not in first:
                    first.append(j[indx+1:])
        if len(first) != 0:
            rhs_dict[i] = first
        #first.clear()
    return rhs_dict
        
def get_firsts(grammar , non_terminal_list):
    '''
     collects each firsts in a BIG dictionary   
    
    '''
    firsts = {}
    for i in grammar:
        first_i = get_first(grammar, i, non_terminal_list)
        firsts[i] = first_i
    return firsts


def main():
   print("ho ho ho")
   grammar = {
    
    'F' : [['f'],['𝛆']],
    'D' : [['E','F']],
    'E' : [['g'],['𝛆']],
    'C' : [['b','C'],['𝛆']],
    'B' : [['c', 'C']],
    'S' : [['a','B','D','h']]
   }

   non_terminal_list_22 = {'S','A', 'B','C','D', 'E', 'F'}

   non_terminal = 'B'
   first_D = get_first(grammar, 'D', non_terminal_list)
   fist_new = get_first_1(grammar, 'D', non_terminal_list_22)
   print(fist_new)

   print(first_D)

   first_set = get_firsts(grammar,non_terminal_list)
   print(first_set)
   start_symbol = 'S'
   follows = get_follow(grammar, non_terminal, first_set, start_symbol, non_terminal_list_22)
   print(follows)


if __name__ == '__main__':
    main()
