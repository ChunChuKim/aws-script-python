import requests

API_HOST = 'http://APNE2-DSPDSTG-NLB-API-825f7fea1cd14f03.elb.ap-northeast-2.amazonaws.com'
headers = {'Authorization': 'Bearer [YOUR_ACCESS_TOKEN]'}

def req(path, query, method, data={}):
    url = API_HOST + path
    print('HTTP Method: %s' % method)
    print('Request URL: %s' % url)
    print('Headers: %s' % headers)
    print('QueryString: %s' % query)

    if method == 'GET':
        return requests.get(url, headers=headers)
    else:
        return requests.post(url, headers=headers, data=data)



resp = req('/cip/cit/custmgnt/ptmgnt/svc/ptinq/getptextcmthinq/v1.00', '', 'POST','{"incsNo":"200000296"}')
print("response status:\n%d" % resp.status_code)
print("response headers:\n%s" % resp.headers)
print("response body:\n%s" % resp.text)
			
