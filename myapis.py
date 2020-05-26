import requests

# #Тухайн төхөөрөмжөөс ирсэн анхааруулга мэдэгдлийг харах
# r4 = requests.get("https://iotsecure.xyz:1880/getNotif/device_code/D2005170001/notid/1/last/5", verify=False)
# r_dictionary= r4.json()
# print(r_dictionary[0])

#Тухайн төхөөрөмжөөс мэдэгдэл илгээх
r1 = requests.get("http://iotsecure.xyz:1880/sendNotif/devCode/D2005170001/notid/1/msg/1")
r1_dict = r1.json()
print(r1_dict["success"])

# ТУХАЙН ТӨХӨӨРӨМЖИД КОМАНД ӨГӨХ
#https://iotsecure.xyz:1880/sendCommand/code/D2005170001/command/siOn

# ХАМГИЙН СҮҮЛИЙН КОМАНДЫГ АВАХ
#https://iotsecure.xyz:1880/getcommand/code/D2005170001

# КОМАНДЫГ БИЕЛҮҮЛСЭН БОЛ ТӨХӨӨРӨМЖ БА КОММАНД ХҮСНЭГТИЙН ИДЭВХТЭЙ БАГАНЫГ 0 БОЛГОХ
# КОММАНД БИЕЛҮҮЛЭХ
#r = requests.post("https://iotsecure.xyz:1880/doCommand/code/D2005170001/isenable/0", verify=False)

# MODE/ГОРИМ ӨӨРЧЛӨХ
#https://iotsecure.xyz:1880/changeMode/devCode/D2005170001/modeCode/md01

# ТӨХӨӨРӨМЖИЙН ХАМГИЙН СҮҮЛИЙН ГОРИМЫГ АВАХ
#https://iotsecure.xyz:1880/getMode/devCode/:code
