# librería pre-instalada de python
import requests

import json

if __name__ == '__main__':
    # url = 'https://httpbin.org/get'
    url = 'https://httpbin.org/post'
    # args = {'nombre': 'Angel', 'curso': 'Python', 'nivel': 'intermedio'}
    payload = {'nombre': 'Angel', 'curso': 'Python', 'nivel': 'intermedio'}
    # response = requests.get(url, params=args)
    
    response = requests.post(url, json=payload)
    # json post se encarga de serializarlos
    # data entonces nosotros nos encargamos de serializarlos
    
    # get status code from request
    if response.status_code == 200:
        # content Json get a BINARY string
        # content = response.content
        # # generate new file with name google.html, (wb): write binary
        # file = open('google.html', 'wb')
        # file.write(content)
        # file.close()
        
        # print(content.decode('UTF-8'))
        
        # response_json = response.json() # Dic
        # origin = response_json.get('origin')
        # print(origin) 
        
        # response_json = json.loads(response.text)
        # print(response.content)
        # print(response.text)
        # origin = response_json.get('origin')
        print(response.text) 