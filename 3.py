import fnmatch
import os


def check_doc():
    for file in new_dir:
        if fnmatch.fnmatch(file, '*.doc'):
            print(file)


new_dir = os.listdir('Document')

check_doc()
