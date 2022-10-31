for x in "banana":
  print(x)


a = "Hello, World!"
print(len(a))


txt = "The best things in life are free!"
print("free" in txt)

#########################################################################
###Next, will pull bac to local repository and add more Python Codes ####
#########################################################################

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")


txt = "The best thing in life is free"
##print('"Expensive"  not in txt')
if "Expensive"  not in txt:
    print('  "Expensive" is not in txt    ')


b = "Hello, World!"
print(b[2:5])
print(b[:5])
b = "Hello, World!"
print(b[-6:-2])


a = 200
b = 33




if b >a:
    print('b is bigger than a')
else:
    print(" b is smaller than a")


##bool(123)

print(bool(0))

#############

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
print(bool(("","2","3")))
print(bool(["","2","3"]))
print(bool({"","2","3"}))


## Save my current work, and push it to the github repository.



### This is copied from other folder, and will be cloned to VSC00 local repository


### Tomorrow I will switch to Gitea instead of github

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:])

#Negative indexing means starting from the end of the list.

#This example returns the items from index -4 (included) to index -1 (excluded)

#Remember that the last item has the index -1,

#Python list index the last index of the range does not include itself (exclude)
