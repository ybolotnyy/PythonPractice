from os import walk
from glob import glob
import os

home_directory = os.path.expanduser('~')
mypath = home_directory + '/PycharmProjects/PythonPractice/Photos'

def get_file_names(path):
    f = []
    for (dirpath, dirnames, filenames) in walk(path):
        f.extend(filenames)
        break
    return f

def rename_files(path):
    filenames = get_file_names(path)
    for filename in filenames:
        if filename.endswith('.jpg'):
            shift = 0
            for i in range(0,2):
                if filename[i].isdigit():
                    shift += 1
                new_filename = filename[shift:]
                print('rename %s -> %s \n' % (path+'/'+filename, path+'/'+new_filename))
                #os.rename(path+'/'+filename, path+'/'+filename[shift:])


print(get_file_names(mypath))
rename_files(mypath)
print(get_file_names(mypath))