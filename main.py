import pandas as pd
import requests
import json

base = pd.read_csv('base_basketball_orderByDateDecres_pt1_2_2.csv',low_memory=False)

ids = base['id'].to_list()
  


TOKEN = '135809-0OL1dKtAJJPTWN'


iter = 0
history = list()


while iter < len(ids):
# while iter < 100:

  valores_id = ids[iter:iter+10]
  string_valores_id = ",".join(map(str, valores_id))

  
  link = f'https://api.b365api.com/v1/event/view?token={TOKEN}&event_id={string_valores_id}'
  


  response = requests.get(link)
  status = response.status_code
  info = response.json()

  results = info["results"]
  

  if ('results' not in info or results == []):
      print(f'Id com problema: {ids} Results Vazio - :{results}')
      
  

  history.append({'results': results})
  file_path = f"json-view/baskteball_view_{ids[iter]}.json"
  


  with open(file_path, 'w') as outfile:
      print(f"Salvando arquivo em: {file_path}")
      json.dump(history, outfile)

  outfile.close()
  history = list()
  iter = iter + 10 
  


