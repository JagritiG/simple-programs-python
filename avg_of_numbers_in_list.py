# The following program calculates the average of numbers in a given List.

n = int(input("Enter the number of elements to be inserted: "))
new_list = []
for i in range(0, n):
    element = int(input("Enter element: "))
    new_list.append(element)
average = sum(new_list)/n
print("Average of elements in the given list: {0}".format(average))
