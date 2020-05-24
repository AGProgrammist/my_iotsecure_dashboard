import requests
myparams = {'uid':'aagiihan@gmail.com'}
r = requests.get('https://www.iotsecure.xyz:1880/get/user/aagiihan@gmail.com', verify=False)

r_dic = r.json()

print(r_dic[0]['password'])

# r2 = requests.get("https://www.iotsecure.xyz:1880/sms/message/Танайд_хэн_нэгэн_байна!", verify=False)
# print(r2)

# pload = {'username':'olivia','password':'123'}
# r = requests.post('https://httpbin.org/post',data = pload)
# r_dictionary= r.json()
# print(r_dictionary['form'])

r3 = requests.get("https://iotsecure.xyz:1880/get/notif", verify=False)
print(r3)

r4 = requests.get("https://iotsecure.xyz:1880/device_code/D2005170001/notid/1/last/5", verify=False)
r_dictionary= r4.json()
print(r_dictionary[0])
