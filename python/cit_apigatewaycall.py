import requests

API_HOST = 'https://cif-prv-api-dstg.amorepacific.com'
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



idx=0
a = []
b = []
while(idx < 1000):
	resp = req('/cif/getptextcmthinq/v1.00', '', 'POST','{"incsNo":"200000296"}')
	#print("response status:\n%d" % resp.status_code)
	#print("response headers:\n%s" % resp.headers)
	#print("response body:\n%s" % resp.text)
	a.append(resp.headers)
	a.append(resp.status_code)
	a.append(resp.text)
	b.append(a)
	idx = idx + 1
			
f = open("apicall.csv", 'w')
for api in b:
	ln=""
	#print(sgs)
	idx = 0
	for iu in api:
		if(idx > 0):
			ln=ln+","
			#print(sg)
		ln = ln + str(iu)
		idx = idx + 1
	#print(ln)
	f.write(ln+"\n")
f.close()
print("end")		
