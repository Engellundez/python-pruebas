# librería pre-instalada de python
import requests
import json

if __name__ == '__main__':
    # url = 'https://httpbin.org/put'
    url = 'https://httpbin.org/delete'
    payload = {'nombre': 'Angel', 'curso': 'Python', 'nivel': 'intermedio'}
    headers = {'Conten-Type': 'application/json', 'access-token': '12345'}
    
    response = requests.put(url, json=payload, headers=headers)
    response = requests.delete(url, json=payload, headers=headers)
    print(response.url)
    if response.status_code == 200:
        headers_response = response.headers # Dic
        server = headers_response.get('Server')
        print(server) 
        print(headers_response) 