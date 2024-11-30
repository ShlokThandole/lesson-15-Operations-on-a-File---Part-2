new_file = open('empty.txt', 'x')
new_file.close()

import os
print("checking if the file aldready exist or not..............")
if os.path.exists("new_file.txt"):
    os.remove("new_file.txt")
else:
    print("the file does not exist")

my_file = open("empty.txt", "w")
my_file.write('HI I AM THE EMPEROR!!!!!!!!!!!')
my_file.close()

os.remove('codingal.txt')

os.rmdir('Folder')