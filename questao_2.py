import random
import yaml
from yaml.loader import SafeLoader


with open(
  'format.yml', encoding='utf-8'
) as file:
  yaml_data = yaml.load(file, Loader=SafeLoader)

  
  cpf = dict(yaml_data['cpf'].items())
  name = dict(yaml_data['name'].items())
  value = dict(yaml_data['value'].items())

persons_informations = [{
  "name": "Maria Neusa de Aparecida",
  "cpf": "97905796671",
  "state": "Sao Paulo",
  "value": "1234"
}, {
  "name": "Ricardo Fontes",
  "cpf": "44010762900",
  "state": "Rio Grande do Sul",
  "value": "567"
}]


result: str = ''

for person in persons_informations:
  for person_key, person_value in person.items():

    
    if person_key == 'cpf':

      if len(person_value) == cpf['length']:
        result += person_value

      elif len(person_value) < cpf['length']:
        delta_cpf_length: int = abs(len(person_value) - cpf['length'])
        space_quantity: str = ''.join(
          random.choice(' ') for i in range(delta_cpf_length)
        )
        result += space_quantity + person_value if cpf[
          'align'] == 'left' else person_value + space_quantity

      else:
        result += person_value[:cpf['length']]

   
    if person_key == 'name':

      if len(person_value) == name['length']:
        result += person_value

      elif len(person_value) < name['length']:
        delta_name_length: int = abs(len(person_value) - name['length'])
        space_quantity: str = ''.join(
          random.choice(' ') for i in range(delta_name_length)
        )
        result += space_quantity + person_value if name[
          'length'] == 'left' else person_value + space_quantity

      else:
        result += person_value[:name['length']]


    if person_key == 'value':

      if len(person_value) == value['length']:
        result += person_value

      elif len(person_value) < value['length']:
        delta_value_length: int = abs(len(person_value) - value['length'])
        zero_quantity: str = ''.join(
          random.choice('0') for i in range(delta_value_length)
        )
        result += zero_quantity + person_value if value[
          'length'] == 'left' else person_value + zero_quantity

      else:
        result += person_value[:value['length']]

print(result)
