Python 3.12.5 (v3.12.5:ff3bc82f7c9, Aug  7 2024, 05:32:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> date = {1:'Jakub',2:'Tom',4:'Adam'}
>>> data
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    data
NameError: name 'data' is not defined. Did you mean: 'date'?
>>> date
{1: 'Jakub', 2: 'Tom', 4: 'Adam'}
>>> date[1]
'Jakub'
>>> date[4]
'Adam'
>>> date[3]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    date[3]
KeyError: 3
>>> date[2]
'Tom'
>>> date.get(1)
'Jakub'
>>> date = data
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    date = data
NameError: name 'data' is not defined. Did you mean: 'date'?
>>> data
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    data
NameError: name 'data' is not defined. Did you mean: 'date'?
>>> date
{1: 'Jakub', 2: 'Tom', 4: 'Adam'}
>>> date.get(1,'Not Found')
'Jakub'
>>> date[3]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    date[3]
KeyError: 3
date.get(3,'Not Found')
'Not Found'

keys = ['Jakub','Adam','Mark']
values = ['Python','Java','C#']
data = dict(zip(keys,values))
data
{'Jakub': 'Python', 'Adam': 'Java', 'Mark': 'C#'}


data['Adam']
'Java'

data['Monica']
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    data['Monica']
KeyError: 'Monica'


data['Monica'] = 'JS'
data
{'Jakub': 'Python', 'Adam': 'Java', 'Mark': 'C#', 'Monica': 'JS'}

del data['Adam']
data
{'Jakub': 'Python', 'Mark': 'C#', 'Monica': 'JS'}










prog ={'JS':'Atom', 'CS':'VS','Python':['Pycharm','Sublime'],'Java':{'JSE':'Netbeans','JEE':'Eclipse'}}
prog
{'JS': 'Atom', 'CS': 'VS', 'Python': ['Pycharm', 'Sublime'], 'Java': {'JSE': 'Netbeans', 'JEE': 'Eclipse'}}

prog['Python']
['Pycharm', 'Sublime']

prog['Python'][1]
'Sublime'
prog['Java']
{'JSE': 'Netbeans', 'JEE': 'Eclipse'}
prog['Java'][JEE']
             
SyntaxError: unterminated string literal (detected at line 1)
prog['Java']['JEE']
             
'Eclipse'

prog['Java'][1]
             
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    prog['Java'][1]
KeyError: 1

prog['Java']['JSE']
             
'Netbeans'
