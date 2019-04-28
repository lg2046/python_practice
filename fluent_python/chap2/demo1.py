from collections import namedtuple
from datetime import datetime

symbols = '$¢£¥€¤'
chars = [ord(symbol) for symbol in symbols]

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = {color: size for color in colors for size in sizes}

print(tshirts)

symbols = tuple(ord(symbol) for symbol in symbols)
print(symbols)

City = namedtuple('City', ['name', 'country'])
city = City('chengdu', 'sichuan')
print(city)
print(city.name)
print(city.country)
print(city._fields)
print(city._asdict())
print(city._make(('wuhan', 'hubei')))
print(city._make(['changsha', 'hunan']))

for k, v in city._asdict().items():
    print(f'{k}:{v}')

a = datetime.now()
print(f'{a:%Y-%m-%d %H:%m:%S}')

print(isinstance({'a': 1}, dict))
