#IBM Watson IOT platfotm
#Pip install wiotp-sdk
import wiotp.sdk.device
import time
import random
import requests
import json

# For Cloud Device conectivity
myConfig={
    "identity":{
        "orgId": "346x5j",
        "typeId":"abc",
        "deviceId":"123"
        },
        "auth":{
            "token":"qwertyuiop"
        }
}

def myCommandCallback(cmd):
    
    print("Message received from IBM loT Platform:%s"%cmd.data['command'])
    m=cmd.data['command']
client=wiotp.sdk.device.DeviceClient(config=myConfig,logHandlers=None)
client.connect()
while True:
    
    temp=random.randint(-20,50) # Random Temperature data
    
    #flamesensor=random.randint(0,100)
    
    gas=random.randint(0,500)   # Random Gas-sensor data
    
    myData={'temp':temp,'gas':gas}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data successfully:%", myData)
    client.commandCallback = myCommandCallback
    
    time.sleep(1) # time delay for 1 second
    
    if (temp > 38):
        print("Alarm is ON due to High Temperature",temp)
    else:
        print("Normal Temperature")
        
    if (gas > 400):
        print("Alarm is ON due to High Air pollution",gas)
    else:
        print("Normal Atmospheric gas")
        
    print() # dummy print for adding space between lines in output
    
    time.sleep(3) # time delay for 3 seconds
client.disconnect()
