file = open('C:\Desktop\C\algo\matrix.txt', 'r')
content = file.readline
a = 0
 
# Iterating through the content
# Of the file
for line in content:
     
    for i in line:
         
        # Checking for the digit in
        # the string
        if i.isdigit() == True:
             
            a += int(i)
 
print("The sum is:", a)