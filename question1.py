#Question 1
import requests

url = 'https://swapi.dev/api/vehicles/'

try:
  data = requests.get(url).json()
except:
  raise Exception('Could not retrieve data from API.')

brands = set(car['manufacturer'].title() for car in data['results'])
answer1 = sorted(list(brands)[:5])
print(answer1)