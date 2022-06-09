from hewanair import hewan_air
from hewandarat import hewan_darat

sapi = hewan_darat('sapi',4,False)
kambing = hewan_darat('Kambing',4,False)
merpati = hewan_darat('Burung Merpati',2,True)
cupang = hewan_air('Ikan Cupang','Air Tawar')
hiu = hewan_air('Ikan Hiu','Air Laut')
paus = hewan_air('Ikan Paus','Air Laut')

print(sapi.__dict__)
sapi.bernafas()
sapi.makan()
print('\n')

print(kambing.__dict__)
kambing.bernafas()
kambing.makan()
print('\n')

print(merpati.__dict__)
merpati.bernafas()
merpati.makan()
print('\n')

print(cupang.__dict__)
cupang.bernafas()
cupang.makan()
print('\n')

print(hiu.__dict__)
hiu.bernafas()
hiu.makan()
print('\n')
print(paus.__dict__)
paus.bernafas()
paus.makan()
print('\n')
