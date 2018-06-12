from flask import Flask, jsonify
from flask import make_response
import requests

app = Flask(__name__)

url = 'https://api.github.com/users/originaloregano'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)


# payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://api.github.com/events')

print(r.status_code)
print(r.url)
r.headers['content-type']

print(r.json())

# >>> r = requests.post('http://httpbin.org/post', data = {'key':'value'})
# >>> payload = {'key1': 'value1', 'key2': 'value2'}
#
# >>> r = requests.post("http://httpbin.org/post", data=payload)
# >>> print(r.text)
>>> url = 'https://api.github.com/some/endpoint'
>>> payload = {'some': 'data'}

>>> r = requests.post(url, json=payload)
# >>> r = requests.put('http://httpbin.org/put', data = {'key':'value'})
# >>> r = requests.delete('http://httpbin.org/delete')
# >>> r = requests.head('http://httpbin.org/get')
# >>> r = requests.options('http://httpbin.org/get')
@app.route('/')
def index():
    return "Hello Worlds"


if __name__ == "__main__":
    app.run(debug=True)
