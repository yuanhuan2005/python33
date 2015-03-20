#!/usr/bin/python3

# type
a, b = 1, 2.32
c = True
d = 4+3j
print(type(a), type(b), type(c), type(d))

# calc
print("")
print(4 + 3)
print(4 - 3)
print(3 + 2.34)
print(3 * 4)
print(7 / 7)
print(7 / 3) # get float
print(7 // 3) # get  int
print(13 % 5) # get remainder
print(2 ** 5) # factorial

# string
print("")
s = "hello world"
print(s, type(s), len(s))
print('C:\some\name')
print(r'C:\some\name')
print('str'+'ing', 'my'*3)
word = 'Python'
print(word[0], word[5])
print(word[-1], word[-6])
word = 'ilovepython'
print(word[1:5])
print(word[:])
print(word[5:])
print(word[-10:-6])
# word[0] = 'm' # will error


# list
print("")
a = ['him', 25, 100, 'her']
print(a)
a = [1, 2, 3, 4, 5]
a += [6, 7, 8]
print(a)
a = [1, 2, 3, 4, 5, 6]
a[0] = 9
a[2:5] = [13, 14, 15]
print(a)
a[2:5] = []
print(a)

# tuple
print("")
a = (1991, 2014, 'physics', 'math')
print(a, type(a), len(a))
tup = (1, 2, 3, 4, 5, 6)
print(tup[0], tup[1:5])
tup1 = ()
tup2 = (20,)
print(len(tup1))
print(len(tup2))
tup1, tup2 = (1, 2, 3), (4, 5, 6)
print(tup1+tup2)

# set
print("")
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)
print('Rose' in student)
a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)
a = set()
print(len(a))

# dictionaries
print("")
dic = {}
print(dic)
print(len(dic))
tel = {'Jack':1557, 'Tom':1320, 'Rose':1886}
print(tel)
print(tel['Jack'])
del tel['Rose']
print(tel)
tel['Mary'] = 4127
print(tel)
list(tel.keys())
sorted(tel.keys())
print("Tom" in tel)
print("Mary" not in tel)
d = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(d)
d = {x: x**2 for x in (2, 4, 6)}
print(d)
d = dict(sape=4139, guido=4127, jack=4098)
print(d)
print("Keys:", d.keys())
print("Values:", d.values())
d.clear()
print(d)

