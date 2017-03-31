from os import walk
from glob import glob
import os

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
            new_filename = filename.translate(None,"0123456789")
            print('rename %s -> %s \n' % (path+'/'+filename, path+'/'+new_filename))
            os.rename(path+'/'+filename, path+'/'+new_filename)


home_directory = os.path.expanduser('~')
mypath = home_directory + '/PycharmProjects/PythonPractice/Photos'

print(get_file_names(mypath))
rename_files(mypath)
print(get_file_names(mypath))