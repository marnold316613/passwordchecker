import requests
import hashlib

def request_api_data(query_char):
  url= 'https://api.pwnedpasswords.com/range/' + query_char
  res = requests.get(url)
  if res.status_code!=200:
    raise RuntimeError(f'Error communicating with API {res.status_code}')
  return res

def pwned_api_check(password):
  return (hashlib.sha1(password.encode('utf-8')).hexdigest().upper())


print(pwned_api_check('123'))
# request_api_data('123')
