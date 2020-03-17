s='Python is great!'
s="Python is great!"
s='''Python is great!'''
s="""Python is great!"""
print(s)

sentence='Python is the \
most popular programming\
language in these days.'
print(sentence)

a="say 'hello' to mom"
b='''say 'hello' to mom'''
c="""say 'hello' to mom"""
d="""say "hello" to mom"""
print (d)

#letter to Alice
print('''Dear Alice,

How are you?
I am busy to study programming this vacation.

Say hello to your parents.

Sincerely,
Bob''')

greeting='hello world'
print(greeting[7])
print(greeting[0])
#greeting[0]='H'

lang='python programming'
lang[:]
lang[::]
lang[3:10]
lang[:5]
lang[10:]
lang[5:-8]
lang[10:5]
lang[-10:-13]
lang[2:10:3]
lang[:10:3]
lang[10::2]
lang[12:3:-2]

a='hello'
b='world'
c=a+b
print(c)
d=a+''+b
print(d)

score=95
x='I got'+str(score)+'in the exam.'
print(x)

subject='programming'
len(subject)
'r' in subject
'gram' in subject
'abcd' not in subject

name='steve jobs'
name.upper()

school='SOGANG University'
school.lower()

a='hello';b='WORLD'
a.islower()
b.isupper()

y='steve jobs made toy story'
y.capitalize()
y.title()

x='I Am Learning Programming'
x.istitle()
y='I am learning Programming'
y.istitle()

state='mississippi'
state.count('s')
state.count('ssi')
state.count('s',5)
state.count('s',1,5)
state.find('s')
state.find('i',5)

friends=['alice', 'bob', 'cindy']
dash='-'
dash.join(friends)
'''
lists='alice bob cindy david'
lists.split()
date='2016/12/25'
date.split('/')
'''
