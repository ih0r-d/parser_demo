import requests as req
from pprint import pprint as pr

resp = req.get('https://www.python.org/download/releases/')
print(resp)  # <Response [200]>

resp = req.get('https://www.python.org/download/releases/43')
print(resp)  # <Response [404]>

print(dir(resp))
print(help(resp))
print(resp.content)


print(resp.status_code)  # 404

if resp:
    print('Responce is correct')
else:
    print('bad response')

print(resp.headers) # return all headers

print(resp.text) # return all of page

with open('resp.html', 'w') as file:
    file.write(resp.text)
r = req.get('https://i2.wp.com/itc.ua/wp-content/uploads/2018/09/3-1.jpg?fit=830%2C460&quality=100&strip=all&ssl=1')
with open('logo.png', 'wb') as f:
    f.write(r.content)

payload = {'username': 'test', 'password': 'pass'}
auth = req.post('http://httpbin.org/post', data=payload)
auth_dict = auth.json()
# pr(auth_dict)
pr(auth_dict['form'])

basic_auth = req.get('http://httpbin.org/basic-auth/test/pass', auth=('test', 'pass'))
print(basic_auth.text)

timeout_req = req.get('https://httpbin.org/delay/2',timeout=2)
pr(timeout_req)
# python3 requests_demo.py > page.html
