import requests

if __name__ == '__main__':
    url = 'https://imgs.search.brave.com/_oVuy6v15rqorwj8qzF2QydD1JqNoOrCJ7JEnjaB2jw/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9pbWcu/ZnJlZXBpay5jb20v/Zm90by1ncmF0aXMv/bGluZG8tZ2F0by1l/c3BhY2lvXzIzLTIx/NTA5MzIxODIuanBn/P3NpemU9NjI2JmV4/dD1qcGc'
    
    # Realiza una petición sin descargar el contenido
    response = requests.get(url, stream=True)
    print(response)
    with open('image.jpeg', 'wb') as file:
        # Archivos de gran peso como lo son videos o sets de datos 
        # así se van descargando poco a poco iterando el contenido
        for chunk in response.iter_content():
            file.write(chunk)
    
    response.close()