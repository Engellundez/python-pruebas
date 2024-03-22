# librería pre-instalada de python
import requests

import json

if __name__ == '__main__':
    # url = 'https://www.google.com.mx/'
    url = 'https://httpbin.org/get'
    args = {'nombre': 'Angel', 'curso': 'Python', 'nivel': 'intermedio'}
    response = requests.get(url, params=args)
    
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
        
        response_json = json.loads(response.text)
        print(response.content)
        print(response.text)
        origin = response_json.get('origin')
        print(origin) 