h = '1.2.3.4'
#print(h)
# output: 1.2.3.4
#It splits the string object with the help of the parameter. and converts it into a list from that we can use it for future use such as indexing or slicing.

k = h.split(".") 
#print(k)
#output: ['1', '2', '3', '4']


#This is a method. in method variable is prepended.
h.split(".")

#This is a Function in which the variable is getting passed to work.
#print(h)


# dir() : to see what is in our current directory.
# dir(str): it will show all the methods that are available to String Class. Type(str) this shows that this a type of class. As opposed to type(h) it will show that it’s a instance or object of String Class. We can also use dir(h) to see what’s methods are available to this instance or object because it inherited those methods from the parent class in this case from String class.

#getting and Item using Index. its 0 based system. 
l = h.__getitem__(2) #longer method
e = h[2] #shorter or most usable way of using Index.
#print(l)
#print(e)



#To get help 
#help(str.split)


kl = '   192.168   .   1 .   1      '
print(kl)

#Remove heading and Trailing space
lk = kl.strip()
print(lk)