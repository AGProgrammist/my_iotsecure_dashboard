import requests

#Тухайн төхөөрөмжөөс ирсэн анхааруулга мэдэгдлийг харах
r4 = requests.get("https://iotsecure.xyz:1880/getNotif/device_code/D2005170001/notid/1/last/5", verify=False)
r_dictionary= r4.json()
print(r_dictionary[0])

#Тухайн төхөөрөмжөөс мэдэгдэл илгээх
r1 = requests.get("https://iotsecure.xyz:1880/sendNotif/devCode/D2005170001/notid/1/msg/1", verify=False)
r1_dict = r1.json()
print(r1_dict["success"])

# ТУХАЙН ТӨХӨӨРӨМЖИД КОМАНД ӨГӨХ
#https://iotsecure.xyz:1880/sendCommand/code/D2005170001/command/siOn
# ХАМГИЙН СҮҮЛИЙН КОМАНДЫГ АВАХ
#https://iotsecure.xyz:1880/getcommand/code/D2005170001
# КОММАНД БИЕЛҮҮЛЭХ
#r = requests.post("https://iotsecure.xyz:1880/doCommand/code/D2005170001/isenable/0", verify=False)
