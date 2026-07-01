#Loops in python:-
#(1)While loops:-
i = 5
while i >= 1:
    print(i)
    i -= 1

#print number from 1 to 100:-
a = 1
while a <= 100 :
    print(a)
    a += 1
print("loop is ended")

#print number from 100 to 1:-
b = 100
while b >=1 :
    print(b)
    b -= 1
print("loop is ended") 

#print the multiplication table of a number n:-
n = int(input("enter the value :"))
c = 1
while c <= 10 :
    print(n*c)
    c += 1
print("loop is ended") 

#print the element of the following list using a loop:-
tup1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx1 = 0
while idx1 < len(tup1) :
    print(tup1[idx1])
    idx1 += 1
print("loop is ended") 

#search for a number x in this tuple using loop:-
tup2 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
e = 25
idx2 = 0
while idx2 < len(tup2) :
    if(tup2[idx2]  == e):
        print("found at index", idx2)
        break
    else:
        print("finding..")    
    idx2 += 1