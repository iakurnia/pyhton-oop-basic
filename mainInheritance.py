from inheritance.hewan import Hewan
from inheritance.manusia import Manusia

print('---'*10)
print('Program Pyhton OOP Basic Inheritance')
print('---'*10)

o1=Manusia('Berakal')
print(o1.info())
print(f'Manusia : {o1.data()}')

o1=Hewan('Tidak Berakal')
print(o1.info())
print(f'Manusia : {o1.data()}')