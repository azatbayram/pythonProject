# sort list alphanumerically
mylist = ["orange", "mango", "kiwi", "pineapple", "banana"]
mylist.sort()
print(mylist)

# sort numbers
myNums=[100, 76, 126, 98, 26, 63]
myNums.sort()
print(myNums)

# sort descending
mylist.sort(reverse=True)
myNums.sort(reverse=True)
print(mylist)
print(myNums)

# customize sort function
# Sort the list based on how close the number is to 50:
def myFunc(n):
    return abs(n-50)

myNums.sort(key=myFunc)
print(myNums)

# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)