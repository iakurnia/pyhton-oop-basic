from geomeri.persegiPanjang import PersegiPanjang
from geomeri.segitiga import Segitiga

print('---'*10)
print('Program Pyhton OOP Basic')
print('---'*10)

o1=PersegiPanjang(10, 5)
print(o1.info())
print(f'Luasnya : {o1.luas()}')

o2=Segitiga(10,5)
print(o2.info())
print(f'Luasnya : {o2.luas()}')