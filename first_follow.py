
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

def is_non_terminal(A, non_terminal_list):
    if A in non_terminal_list:
        return True
    return False

def has_epsilon(my_list):
    if '𝛆' in my_list:
        return True
    return False

def get_first(grammar, non_terminal, non_terminal_list):
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

    for j in grammar[non_terminal]:
        #print(j[0])
        if not is_non_terminal(j[0], non_terminal_list):
            first_i.add(j[0])
        else:
            for k in j:
                if is_non_terminal(k, non_terminal_list):
                    temp = get_first(grammar, k, non_terminal_list)
                    first_i.update(temp)
                    if not has_epsilon(temp):
                        break
                    

    return first_i

def get_follow(grammar, non_terminal, first_set, start_symbol):
    '''
        1) for starting symbol place $ in the follow set
        2) if the is a production A → 𝞪B𝝱:
            Follow(B) = First(𝝱)
            if First(𝝱) has 𝝴 :
                Follow(B) = Follow(A)
        3) if the is a production A → 𝞪B:
            Follow(B) = Follow(A)

    '''
    follow_i = set()
    if non_terminal is start_symbol:
        follow_i.add('$')
        print("follow first")

    # step one get the follows based on firsts
    productions = get_rhs(grammar, non_terminal)
    for production in productions:
        find_first()

def find_first(grammar, non_terminal_production, non_terminal_list):
    '''
    
    '''
    first_i = set()
    follow_of_follow = set()

    count = 0
    
    #print(f'terminal production = {terminal_production}')
    for i in non_terminal_production:
        #print(f'terminal production part: {terminal_production[i]}')
        if len(non_terminal_production[i]) == 0:
            print("just get follow")
            break

        #print("enteur find")
        for j in non_terminal_production[i]:
            count += 1
            print(f'j is : {j}')

            # first of non-terminal = get_first
            print(len(non_terminal_production[i]))
            if is_non_terminal(j, non_terminal_list):
                print(f"{j} is non-terminal")

                first_ii = get_first(grammar, j, non_terminal_list)
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
    print("ho")

if __name__ == '__main__':
    main()
