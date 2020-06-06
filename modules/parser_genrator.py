import os
import sys
from tabulate import tabulate
from modules.first_follow import get_non_terminal_list, get_terminal_list, build_parsing_table, parse_input, get_dict_items
from modules.color_print import print_blue, print_green, print_red, print_yellow
from modules.aux_func import get_current_directory, read_file, write_file, write_in_file

# accent characters is special case, DO NOT use them


# it shall be 65 
unique_id = 129300
G_identifiers = {}
grammar_dict = {}
grammar_dict_sym = {}
start_symbol = ''



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

def map_rule(rule_statment, option=1):
    '''
    converts rule into map LHS & RHS
    '''
    
    rule_dict = {}
    part1 = partition_rule(rule_statment)
    part2 = divide_RHS(part1[1])
    # print_green(f'part2: {part2}')
    if option:
        part2 = separate_by_delim(part2)
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
        print_blue(f'{i}  ⟶  {dict_map[i]}')
        

def print_g_id():
    path = get_current_directory()
    path+='/identifiers.txt'
    write_in_file(path,"", 'w+')
        
    for i in G_identifiers:
        print_green(f'{i} ⟶  {G_identifiers[i]}\n')
        write_in_file(path,f'{i} ⟶ {G_identifiers[i]}\n', 'a+')

    


# function created after first and follows
def separate_by_delim(the_list):
    # for each statement in the list
    y = []
    g = []
    # print(f"the list is: {the_list}")
    for i in the_list:
            #print(f"i in the list {i}")
            x = i.split(' ')
            """ 
            y = []
            for j in x:
                y.append(j)
                y.append(' ')
            y.pop(-1)
            """
            g.append(x)
            #print(f"splited: {y}")

    return g
    
def get_start_symbol(rule):
    symbol = rule.split("=")
    symbol = symbol[0]
    symbol = symbol.strip()
    return symbol

def read_input_list(file_path):
    with open(file_path) as f:
        lines = [line.rstrip() for line in f]
    return lines

def show_parser_table(input_list, todos, inputs, action):

    headers = ["Todo", "Input", "Action"]
    table = zip(todos,inputs,action)
    print_blue("*."*20)
    print_yellow(f"input is : {input_list}")
    print(tabulate(table, headers=headers))



