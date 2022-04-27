import os

# Create dicts
create_dir1 = os.path.join('StudentDoc')
if not os.path.exists(create_dir1):
    os.mkdir(create_dir1)
else:
    print('Dict {} already exist'.format(create_dir1))

create_dir2 = os.path.join('StudentObrazy')
if not os.path.exists(create_dir2):
    os.mkdir(create_dir2)
else:
    print('Dict {} already exist'.format(create_dir2))

# Create txt files
file_txt_1 = r'StudentDoc\file_text_1.txt'
if not os.path.exists(file_txt_1):
    with open(file_txt_1, 'w'):
        pass
else:
    print('File {} already exist'.format(file_txt_1))

file_txt_2 = r'StudentDoc\file_text_2.txt'
if not os.path.exists(file_txt_2):
    with open(file_txt_2, 'w'):
        pass
else:
    print('File {} already exist'.format(file_txt_2))

# Create png files
file_png_1 = r'StudentObrazy\file_png_1.png'
if not os.path.exists(file_png_1):
    with open(file_png_1, 'w'):
        pass
else:
    print('File {} already exist'.format(file_png_1))

file_png_2 = r'StudentObrazy\file_png_2.png'
if not os.path.exists(file_png_2):
    with open(file_png_2, 'w'):
        pass
else:
    print('File {} already exist'.format(file_png_2))

# Contents of dicts and size of files
print('Contents of StudentDoc')
print(os.listdir('StudentDoc'))
list_dir_txt = os.listdir('StudentDoc')

size_txt1 = os.path.getsize('StudentDoc/file_text_1.txt')
print('Size of {}: {} b'.format(list_dir_txt[0], size_txt1))
size_txt2 = os.path.getsize('StudentDoc/file_text_2.txt')
print('Size of {}: {} b'.format(list_dir_txt[1], size_txt2))

print('Contents of StudentObrazy')
print(os.listdir('StudentObrazy'))
list_dir_png = os.listdir('StudentObrazy')

size_png1 = os.path.getsize('StudentObrazy/file_png_1.png')
print('Size of {}: {} b'.format(list_dir_png[0], size_png1))
size_png2 = os.path.getsize('StudentObrazy/file_png_2.png')
print('Size of {}: {} b'.format(list_dir_png[1], size_png2))
