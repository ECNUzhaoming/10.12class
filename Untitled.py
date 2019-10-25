
# coding: utf-8

# In[1]:

count={}
for ch in "hello world":
    if count.get(ch)==None:
        count[ch]=1
    else:
        count[ch]=count[ch]+1
print(count)


# In[2]:

count={}
for ch in "hello world":
    count.setdefault(ch,0)#对于每一个CH设置缺省值为0
    count[ch]+=1
print(count)


# In[5]:

text='''ocalization of Specifi c Functions to Different Parts of the Brain. If dif-
ferent functions are localized in different spinal roots, then perhaps dif-
ferent functions are also localized in different parts of the brain. In 1811,
Bell proposed that the origin of the motor fi bers is the cerebellum and the
destination of the sensory fi bers is the cerebrum.
How would you test this proposal? One way is to use the same approach
that Bell and Magendie employed to identify the functions of the spinal
roots: to destroy these parts of the brain and test for sensory and motor
defi cits. This approach, in which parts of the brain are systematically
destroyed to determine their function, is called the experimental ablation
method. In 1823, the esteemed French physiologist Marie-Jean-Pierre
Flourens used this method in a variety of animals (particularly birds) to
show that the cerebellum does indeed play a role in the coordination of
movement. He also concluded that the cerebrum is involved in sensation
and perception, as Bell and Galen before him had suggested. Unlike his
predecessors, however, Flourens provided solid experimental support for
his conclusions.
What about all those bumps on the brain’s surface? Do they perform
different functions as well? The idea that they do was irresistible to a
young Austrian medical student named Franz Joseph Gall. Believing
that bumps on the surface of the skull refl ect bumps on the surface of
the brain, Gall proposed in 1809 that the propensity for certain personal-
ity traits, such as generosity, secretiveness, and destructiveness, could
be related to the dimensions of the head (Figure 1.10). To support his
claim, Gall and his followers collected and carefully measured the skulls
of hundreds of people representing an extensive range of personality
types, from the very gifted to the criminally insane. This new “science”
of correlating the structure of the head with personality traits was called
phrenology. Although the claims of the phrenologists were never taken
seriously by the mainstream scientifi c community, they did capt
'''
words=text.split(' ')
print(words)


# In[22]:

sep='\n\t\'\",.()-'
for ch in sep:
    text=text.replace(ch,' ')
words=text.lower().split(' ')
try:
    while True:words.remove('')
except:
    pass
    
count={}
for word in words:
    count.setdefault(word,0)
    count[word]+=1
print(count)


# In[18]:

words_by_count=dict()
for word in count.keys():
    words_by_count.setdefault(count[word],[])
    words_by_count[count[word]].append(word)
print(words_by_count[5])


# In[21]:

sorted(words_by_count.keys())


# In[25]:

for item in sorted(words_by_count.keys(),reverse=True):
    print("Count {}:".format(item),end="")
    for word in words_by_count[item]:
        print(word,end=' ')
    print('\n')


# In[31]:

new_count=[]
occurences=sorted(words_by_count.keys())
for occurence in occurences:
    new_count.append(len(words_by_count[occurence]))
print(sorted(words_by_count.keys()))
print(new_count)


# In[46]:

import matplotlib.pyplot as plt
plt.plot(occurences,new_count)


# In[47]:

x,y,*r=1,2,3,4,5
print(x,y,r)


# In[48]:

x,*m,y=1,2,3,4,5
print(x,y,m)


# In[49]:

x,*m,y="hello,world"
print(x,y,m)


# In[50]:

x=y=3
print(x,y)


# In[51]:

x=y=[1,2]
x[0]=0
print(x,y)


# In[52]:

x is y


# In[53]:

x=[1,2]
y=[1,2]
x is y


# In[54]:

x==y


# In[55]:

x[0]=0


# In[56]:

print(x,y)


# In[57]:

x=(1,2)
y=(1,2)
x is y


# In[60]:

a=[1,2]
b=a
print(a is b)
a=a+[3]
print(a)
a is b


# In[61]:

a=[1,2]
b=a
print(a is b)
a+=[3]
print(a)
a is b


# In[62]:

if a>b:
    print(a)


# In[63]:

True+1


# In[64]:

bool(0)


# In[65]:

bool(-1
    )


# In[66]:

#0," ",[],()
bool(())


# In[67]:

name=input("your name please:")
if name:
    print("hello,"+name)
else:
    print("you forget your name?")


# In[69]:

def abs(a):
    return a if a>=0 else -a
print(abs(-3),abs(3),abs(0))


# In[70]:

a=[1,2,3]
1 in a


# In[79]:

chr(128584)


# In[82]:

chr(128583)


# In[83]:

chr(128582)


# In[84]:

i=0
while i<5:
    print("*"*10)
    i+=1


# In[ ]:



