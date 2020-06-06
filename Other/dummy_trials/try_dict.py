#t1 = {'x': "e → te'" }
#t2 = {'y': "e → te'" }
t3 = {'(': "e → te'" }

#E1 = {'e' : {t1,t2,t3}}
E1 = {}
l1 = ['x', 'y', '(']
l2 = ["e → te'", "e → te'", "e → te'"]
c = dict(zip(l1,l2))
#d = dict(zip('E',c))
d = {}
d['E'] = c
print(type(d))
print(c)
print(d['E']['x'])
print(d['E'])
print("*"*20)


nested_dict = { 'dictA': {'key_1': 'value_1' , 'e1':'val1'},
                'dictB': {'key_2': 'value_2'}}
print(type(nested_dict['dictA']))
print(type(t3))