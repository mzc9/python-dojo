#set midpoint
midpoint = 5

# make 2 empty lists
lower = []; upper = [] #to terminate a line to put two statements on a single line

#split the numbers into the lists based on conditional logic
for i in range(10):
    if (i < midpoint):
        lower.append(i)
    else:
        upper.append(i)

print("Lower values are: ", lower)
print("Upper values are: ", upper)

#to continue expressions on the next line can use \ marker
# but preferable not to use it
x = 1 + 2+\
5+6
print(x)
