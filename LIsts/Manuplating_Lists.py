#   1.Change List Items

# Changing at specific index
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#["apple","blackcurrent","cherry"]

# Changing a range of values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
#["apple", "blackcurrant", "watermelon", "orange", "kiwi", "mango"]

#  --If you insert more items than you replace, the new items will be 
#    inserted where you specified, and the remaining items will move accordingly
#
#  --If you insert less items than you replace, the new items will be
#    inserted where you specified, and the remaining items will move accordingly

#   2.Adding List Items

# Adding at end of the list "append() method"
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#['apple', 'banana', 'cherry', 'orange']

#To insert a list item at a specified index, use the insert() method.
#The insert() method inserts an item at the specified index
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
#['apple', 'orange', 'banana', 'cherry']

#   3.Extending Lists

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']