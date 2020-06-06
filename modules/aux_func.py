import os

def get_current_directory(): 
    path = os.getcwd() 
    return path
   

def write_file(path_file, output_list):

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

