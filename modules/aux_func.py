import os
import sys

def get_current_directory(): 
    path = os.getcwd() 
    return path
   

def write_file(path_file, output_list):

    os.makedirs(os.path.dirname(path_file), exist_ok=True)
    with open(path_file, 'w') as filehandle:
        #filehandle.write(str(output_list))
        for listitem in output_list:
           filehandle.write('%s\n' % listitem)


def read_file(filepath):
    # Open a file: file
    file = open(filepath,mode='r')
 
    # read all lines at once
    all_of_it = file.read()
 
    # close the file
    file.close()

    #all_of_it.replace("\\L",'𝛆')

    return all_of_it

def write_in_file(filepath , content , mod='w'):
    # Open a file: file
    file = open(filepath,mode=mod)
 
    # read all lines at once
    all_of_it = file.write(content)
 
    # close the file
    file.close()


def get_arg(param_index, default=None):
    """
        Gets a command line argument by index (note: index starts from 1)
        If the argument is not supplies, it tries to use a default value.

        If a default value isn't supplied, an error message is printed
        and terminates the program.
    """
    try:
        return sys.argv[param_index]
    except IndexError as e:
        if default:
            return default
        else:
            print(e)
            print(
                f"[FATAL] The comand-line argument #[{param_index}] is missing")
            exit(-1)    # Program execution failed.



