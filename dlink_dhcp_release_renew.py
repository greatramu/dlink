import requests, json, hmac

# replace the values of below variables with your router's user and password
user = 'Admin'
password = 'xyz'

url_auth = 'http://192.168.0.1/authentication.cgi'
url_cfg = 'http://192.168.0.1/getcfg.php'
url_service = 'http://192.168.0.1/service.cgi'

# get the uid and challenge key from server
r = requests.get(url_auth)
data = json.loads(str(r.content))

# create the digest key by encoding using HMAC library
mix = user + data['challenge']
h = hmac.new(password, mix)
digest = str.upper(h.hexdigest())

# payload object to send the user and digest key for authentication
payload = {'id': user, 'password': digest}  

# cookie for storing authentication info. 
# This will be useful when performing further operations without authentication
cookies = dict(uid=data['uid'])

# authenticating
r = requests.post(url_auth , data=payload, cookies = cookies)

# check the status
stat = json.loads(str(r.content))

if stat['status'] == 'ok':
    print 'Authentication success'

    # release
    payload = {'EVENT': 'WAN-1.DHCP.RELEASE'}
    r = requests.post(url_service, data=payload, cookies = cookies)
    print r.content
    
    # renew
    payload = {'EVENT': 'WAN-1.DHCP.RENEW'}
    r = requests.post(url_service, data=payload, cookies = cookies)
    print r.content

else:
    print 'Authentication failed'

