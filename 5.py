import os


# Create dir
create_dir1 = os.path.join('Dict_for_5')
if not os.path.exists(create_dir1):
    os.mkdir(create_dir1)
else:
    print('Dict {} already exist'.format(create_dir1))

new_dict_name = input('Podaj nową nazwę folderu: ')

# Rename dir
os.rename('Dict_for_5', new_dict_name)
