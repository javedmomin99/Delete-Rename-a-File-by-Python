import os

old_name = "old_name.txt"
renamed_by_python = "renamed_by_python.txt"

f = open(old_name, "r")
data = f.read()

f = open(renamed_by_python, "w")
data = f.write(data)
f.close()

os.remove(old_name)
# Now, When you run the file again, it will throw an error since we have deleted old_name.txt file, so if you want to run the program, please create a new file named as "old_name.txt" and delete the existing file named "renamed_by_python.txt" & then run the code again to get the desired output. 
