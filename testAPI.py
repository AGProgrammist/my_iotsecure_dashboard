import requests
myparams = {'uid':'aagiihan@gmail.com'}
r = requests.get('http://www.iotsecure.xyz:1880/get/user/aagiihan@gmail.com')

r_dic = r.json()

print(r_dic[0]['password'])


# pload = {'username':'olivia','password':'123'}
# r = requests.post('https://httpbin.org/post',data = pload)
# r_dictionary= r.json()
# print(r_dictionary['form'])
