
# Creates a new directory
import os
for i in range(0, 100):
    os.mkdir(f"Day{i+1}")


# Returns the path of the current working directory as a string
import os
print(os.getcwd())


# Lists contents of the current directory
import os
print(os.listdir('.'))  


# Deletes an empty directory
import os
os.rmdir('empty_folder')


# Permanently deletes a specified file from the file system
import os
os.remove('old_log.txt')