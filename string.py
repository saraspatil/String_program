# find length of the string in 3 ways:
#1 len():
d = 'hello my name is saras'
print(len(d))

======================
#2 for loop:
d = 'hello my name is saras'
c = 0
for i in d:
    c += 1
print(c)
=============================================
#3 while loop:
#def findLen(str):
str = 'hello my name is saras'
c = 0
while str[c:]:
    c += 1
#return c

print(c)
# find length of the string in 3 ways:
#1 len():
d = 'hello my name is saras'
print(len(d))

#2 for loop:
d = 'hello my name is saras'
c = 0
for i in d:
    c += 1
print(c)


#3 while loop:
#def findLen(str):
str = 'hello my name is saras'
c = 0
while str[c:]:
    c += 1
#return c

print(c)
====================================================
#WAP to print even length word in a string:

for i in str.split():
    #print(len(i))
    if len(i)%2==0:
        print(i)

str = 'my name is saras and i lived in pune'
print([i for i in str.split() if len(i)%2==1])
===================================================
# get uppercase of halfstring
str = 'pune'
print(str[0:len(str)//2]+str[len(str)//2:].upper())
========================================================

# WAP to check whether the string contains numeric and alphabets at least one:
f1 = False
f2 = False
str = 'patil1'
for i in str:
    if i.isalpha():
        f1 = True
    if i.isdigit():
        f2 = True
print(f1 and f2)
==========================================================
# WAP to accept the string if it contains all the vowels if not then print not accepted: 
str = 'perIotUuik'
v = 'AEIOU'
s = set(str.upper()).intersection(set(v))

if len(s) == len(v):
    print('accepted given string')
else:
    print('noy accepted')
    # WAP to remove all duplicates in a given string:
str1 = 'saraspatilpatil'
s = set(str1)
print(sorted(s)) #for ascending order
==================================================

# WAP to get least frequent character in string:
str1 = 'geekforgeek'
s = {}
for i in str1:
    if i in s:
        s[i] += 1
    else:
        s[i] = 1
res = min(s, key= s.get)
print(res)
=================================================================
s = 'geeksfor$geeks'
chr = '[!@#$%^&*()_<>?/\|{}~:]'
z = set(s)
x = set(chr)
print(z)
print(x)
for i in x:
    if s.find(i) == -1:
        print('accepted')
else :
    print('not accepted')
===============================================================
# WAP to check whether the special character is present or not:

import re
s = 'geeksfor/geeks'
chr = re.compile('[!@#$%^&*()_<>?/\|{}~:]')
if chr.search(s) == None:
    print('accepted')
else:
    print('not accepted')

from collections import Counter
s = Counter('geeksforgeeks')
a = input('enter the string: ')
res = s[str(a)]
print(a, 'present', str(res),'times')

# number of vowels present in given string:


from collections import Counter

s = Counter('geeksforgeeks')
v = 'aeiou'
a = ''.join(v)
print(s)
count = 0
for i in a:
    if i in s:
        count += s[i]
print(count,'times')
# 2 method to find vowels in given string:
def v_count():
    count = 0
    v = set('aeiou')
    for i in s:
        if i in v:
            count += 1
    print(count,'times')
s = 'geeksforgeeks'
v_count()
=============================================================
# odd occurrences of given string

from collections import Counter
s = Counter('geeksforgeeks')
for i in s:
    if s[i] % 2 == 1:
        print(i, 'is the odd occurrence',s[i])

=================================================================================================
# WAP to check if entered chr is present or not and if present then how any occurrences are there:
from collections import Counter

# method 1:

str1 = 'geeksforgeeks'
s = Counter('geeksforgeeks')
print('original string is:', str1)
a = input('enter the word to search: ')

for j in a:
    if j in s:
        print(j, 'present', s[j], 'times')
    else:
        print(j, 'is not present')
        #method 2
from collections import Counter

str1 = 'geeksforgeeks'
a = input('enter the chracter: ')
res = {i:j for i,j in dict(Counter(str1)).items() if i in a }
print(res)

s = 'geeks1234555forgeeks'
d = '123456789'
count = 0
for i in s:
    for j in d:
        if j in i:
            count +=1

print(count)
===================================================================
s = 'amaama'
if s[0:((len(s)//2))]== s[len(s)//2:]:
    print('string is symmetrical')
if s[0:((len(s) // 2))] == s[(len(s)-1) // 2::-1]:
    print('string is palindrome')
else:
    print('not symmetric as well palindrome')
======================================================================
# check if string is binary or not
s = set('101100h')
se = {'0', '1'}
if s == se or s == {'0'} or s == {'1'}:
    print('binary')
else:
    print('not binary')

=================================================================

# uncommon words from two string
method 1:

a  = 'geeks for geeks'
b = 'learning from geeks for geeks'
x = set(a.split())
y = set(b.split())
print(x.symmetric_difference(y))
========================================
#method2
def uncommon(a, b):
    un_comm = [i for i in ''.join(b).split() if i not in ''.join(a).split()]
    print(un_comm)
a = 'geeks for geeks'
b = 'learning from geeks for geeks'
uncommon(a,b)

a = str(input('enter the string: '))
x = a.replace(',','/')
y = x.replace('.',',')
z = y.replace('/','.')
print(z)

# permutation of a given string:
from itertools import permutations
def perm(s):

    z = permutations(s)
    for i in z:
        print(''.join(i))
s = 'abc'
perm(s)

# using recursion reverse the string:
str = 'geeks for geeks'
str = list(str)
l = []
===============================================
for i in range(len(str)):
    l.append(str[i])

for i in range(len(str)):
    str[i] = l.pop() # condition
print(''.join(str))
===============================================
# WAP to get addition of list of two element after reverse and concatenation:

s1 = [2,4,3]
s2 = [5,6,4]
x1=[]
x2=[]
x5 = []
x3 = ''
x4 = ''
for i in range(len(s1)):
    x1.append(s1.pop())

for j in range(len(s2)):
    x2.append(s2.pop())

for a in range(len(x1)):
    x3 += str(x1[a])
print(x3)
for b in range(len(x2)):
    x4 += str(x2[b])
print(x4)
z = int(x3)+int(x4)
print(z)
z1 = str(z)
for q in range(len(z1)):
    x5.append(int(z1[q]))
print(x5[::-1])
======================================
#input : n =[7,2,11,15] and target = t
#output : [0,1]
def IndCheck(n,t):
    for i in range(len(n)):
        for j in range(i+1,(len(n))):
            if n[i]+n[j] == t:
                return [i,j]
print(IndCheck([7,2,11,15],9))
============================================
# Python program to find the character position of Kth word from a list of strings
#Input : test_list = [“geekforgeeks”, “is”, “best”, “for”, “geeks”], K = 21
#Output : 0
#Explanation : 21st index occurs in “geeks” and point to “g” which is 0th element of word.

s = ['geekforgeeks', 'is', 'best', 'for', 'geeks']
k =22
a = 0
x = ''
for j in s:
    x += j
print(''.join(x))
x = x[k:k+1]
print('kth letter is -',x)
for i in range(len(s)):
     a += len(s[i])
     if a>k:
         y = s[i]
         break
print('kth index occure in - ',y)
print('which is,',y.index(x),'th element of word')
===========================================================
#Input : test_list = [(4, 5, 5, 4), (5, 4, 3)], K = 5, N = 2
#Output : [(4, 5, 5, 4)]

l = [(4, 5, 5, 4), (5, 4, 3)]
k = 5
n = 2

for i in l:
    if k in i:
        if  i.count(k) == n:
            print([i])

    else:
        print(l.clear())
==============================================================
#Remove punctuation from string

s = 'abc!dh#nf$'
for i in s:
    if i.isalpha() == True:
        print(i, end='')
        
 ==========================================================

# WAP to get string after the right and left shift operation:

s = 'geeksforgeeks'
r = 7
l = 10
t = (r-l) % len(s)
print(t)
res = s[t:len(s)]+s[:t]
print(res)

s = 'gfg, is, (best, for), geeks'
temp = ''
res = []
check = 0
for i in s:
    if i == '(':
        check += 1
    elif i == ')':
        check -= 1
    if i == ', ' and check == 0:
        if temp.strip():
            res.append(temp)
        temp = ''
    else:
        temp += i
if temp.strip():
    res.append(temp)
print(res)
==========================================================
# add string in list without comma:

s = 'gfg, is, (best, for), geeks'
a = [' '.join(s.split())]
print(a)
========================================================
# check range of number and print number which is divisible by 3:

s = (1, 10, 3)
res = [i for i in range(s[0],s[1]) if i%3==0]
print(res)
def leftOperator(s):


==========================================================
# as we see below if list of first elements shifted right by 1 and the number in second list same then 
print 'True' otherwise 'False':
# rightOperator([1, 2, 3, 4, 5], [0, 1, 2, 3, 4])

s = ([1, 2, 3, 4, 5], [5, 5, 2, 3, 4])
#print(len(s))
l = 1
t =l%len(s)
a = s[0]
b = s[1]
res = b[t:len(a)]
if res == (a[:(len(a)-1)]):
    print('True')
else:
    print('false')
=========================================================================
# implement this: (["Adam", "Sarah", "Malcolm"]) ➞ "AMS"

s = ['Adam', 'Sarah', 'Malcolm']
res = sorted(i[0] for i in s)
print(''.join(res))
==========================================================
#check isogram:

s =("AlgorismM s")
ss = set(s.lower())

if len(s) == len(ss):
    print('isogram')
elif ' ' in ss:
    print('not valid')
else:
    print('not isogram')
===========================================================
# WAP to check the string string is in sorted formate and if yes the print 'true' else 'false' 
also if string contains two words then it is not valid:
s = 'abc'
res = sorted(s)
print(type(res))
if s == '':
    print('entered some character')
elif list(s) == res:
    print('true')
else:
    print('false')
================================================================================

## 1. Program to print duplicates from a list of integers

s = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
list(set([i for i in s if s.count(i)!=1]))

=============================================================================
## 2. Replace index elements with elements in Other List

a = ['Gfg', 'is', 'best']
b = [0, 1, 2, 1, 0, 0, 0, 2, 1, 1, 2, 0]

a1 = {a.index(i):i for i in a}
res = [a1[j] for j in b] 
res
========================================================================
## 3. Split String on vowels


l = 'GFGaBst'
v = ['a','e','i','o','u','A','E','I','O','U']


[l.split(i) for i in v if l.find(i)!= -1]

============================================================================
## 4. Convert binary to string using Python

c = 10001111100101110010111010111110011


==========================================================================

## 5. Remove K length Duplicates from String

k = 3
d = 'geeksforfreeksfo'

m = set()
res = []
for i in range(0,len(d)-k):
    #slicing k lenght sub string
    sub = d[i:i+k]
    if sub not in m:
        m.add(sub)
        res.append(sub)
res = ''.join([res[i] for i in range(0,len(res),k)])
res
        
============================================================================
## 8. remove all the duplicates from string

s = 'geeksforgeeks'

#1 method:
''.join(set(s))

#2 method:
from collections import Counter

''.join(Counter(s).keys())

#3 method:

l = []
for i in s:
    if i in l:
        pass
    else:
        l.append(i)
''.join(l)

#4 method:

''.join({i for i in s})

#5 method
''.join({i[1] for i in enumerate(s)})

#6 method
from collections import OrderedDict
''.join(OrderedDict.fromkeys(s).keys())

=========================================================================
## 9. least frequent character in a string

#1 method 

[i for i in Counter(s).items() if i[1]==min(Counter(s).values())][0][0]

d = {}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
d

# to get min least frequent character:
for i in d.items():
    if i[1] == min(d.values()):
        print('least frequent chracter in given string is:',i[0])
        break

# important key function:
min(d, key=d.get)

# 3 using counter method
min(d,key=Counter(s).get)

===============================================================================
## 10. check if a string is binaary or not

s = '11001111'

#1 method
if set(s)=={'0','1'}:
    print('str is binary')
else:
    print('not binary')

#2 list comprehension
l =[i for i in s if i != '0' and i!='1']
print(l)
if l == []:
    print('bin str')
else:
    print('not bin str')

#3 method for loop:
x = []
for i in s:
    if i == '0' or i == '1':
        x.append(i)
if len(x)==len(s):
    print('bin str')
else:
    print('not bin str')
=========================================================================
    
## 11. find all close match of input string from a list

p = ['ape','apple','peanch','puppy']
ip = 'appel'

#1 method
cm = [] 
for i in p:
    if len(i)<=3:
        if i[:2]==ip[:2] :
            cm.append(i)
    elif len(i)>3:
        if i[:3]==ip[:3] :
            cm.append(i)
print(cm)
            

#2 method:
from difflib import get_close_matches


get_close_matches(ip,p)

str1 = 'pratik santosh salaskar'
str2 = 'Pratik Santosh Salaskar '

==================================================================================
## 12. check two string maches each other with percentage

from difflib import SequenceMatcher

# create an object
sq=SequenceMatcher(a=str1,b=str2)

sq.ratio()*100

==================================================================================
## 13. find uncommon word from two string

str1 = 'my name is pratik'
str2 = 'ur name is salaskar'

#1 method using set:
set(str1.split()).symmetric_difference(set(str2.split()))

#2 method using list comprehension:
[i for i in str1.split() if i not in str2.split()]+[j for j in str2.split() if j not in str1.split()]


#3 method using for loop:
res = []
for i in str1.split():
    if i not in str2.split():
        res.append(i)
for j in str2.split():
    if j not in str1.split():
        res.append(j)
print(res)
=============================================================================
## 14. permutation of given string using in built function

s = 'ABC'

from itertools import permutations

#1 method:
p = permutations(s)
for i in list(p):
    print(''.join(i))

    ==================================================================================
## 15. substring presence in string list

str1 = ['pratik','santosh','salskar']

str2 = ['p','z','r']

#1 method:
c = []
for i in str1:
    if len(set(str2).intersection({j for j in i}))>=1:
        c.append('True')
    else:
        c.append('False')

#2 method
[True if len(set(str2).intersection({j for j in i}))>=1 else False for i in str1]

========================================================================================
# 16. all substring frequency in string

t = 'ababa'

#1 method
d={}
for i in range(1,len(t)+1):
   d[t[:i]] = t.count(t[:i])
for j in range(2,len(t)+1):
    d[t[1:j]]=t.count(t[:j])
d

=========================================================================================
## 17. maximum consecutive sunstring occurance:

s = 'geeks for geeksgeeks are three geeksgeeksgeeks'

ss = 'geeks\w+'


import re

res=re.findall(ss,s)

max(res)

print('frequency of occ.:',len(max(res))//len('geeks'))

============================================================================================
## 18. maximum occuring substring from list

s = 'gfgakjgisgfgksfnjabestfwefnigfglkefjngfgisksfnj'

ss = ['gfg','is','best']

l = []

for j in range(len(ss)):
    for i in range(len(s)):
        if ss[j]==s[i:(len(ss[j])+i)]:
            l.append(ss[j])
d = {i:l.count(i) for i in l}
[i for i in d.items() if i[1]==max(d.values())][0][0]

l1=[]
for i in Counter(l).items():
    l1.append(i[1])

max(l1)
