h = '192.168.1.2'
g = '1.2.3.4'
k = '0123456789'


#using Index to find the value
print(h[1])


#using Index but two value first one the starting index value and after the colon is the Ending value but not included int the output
print(h[0:3])

#same as the upper one but more python way of doing it 
print(h[:3])

#print all the indexes
print(h[::])


#Negative number is started from the behind or fron right to left as you can see.
print(h[-1])

#usage of Positive and negtive value together. slicing
print(h[2:-2])

# wrong formation because we can start from the behind to front. slicing
print(h[-2:2])

#both negative numbers Slicing. prints till the mentioned ending Index value but not including that value
print(h[-5:-1])

#lets work with the third element of this get item method that is couting values.
print(k)


#Starting from index value 0 and ending at 4 but not including it and showing every second value. for Even values
print(k[0:4:2])

#work with negative value.
print(k[1:-1:2])

#for Odd values
print(k[1::2])

#for all Even Numbers
print(k[::2])

#try with positive and negtive
print(k[1:-3:2])

#Reversal of the String. +1 means we are going from right to left. but when we put -1 in the step count it goes from behind to front.
print(k[::-1])

#try with English string.
kl = "my name is simranjit singh"
print(kl[::-1])