import requests

if __name__ == '__main__':
    url = 'http://api.github.com/user'
    session = requests.session()
    session.auth = ('Engellundez', 'Quesolulu23')
    
    response = session.get(url)
    if response.ok:
        print(response.text)
    else:
        print(response.text)