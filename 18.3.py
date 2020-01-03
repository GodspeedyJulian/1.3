def GetTemp (SensorID):
    return 50
def Alarm():
    print("Too hot")
    return
HighTemp=100
LowTemp=10

SensorID=int(input("Input sensor ID"))
while SensorID<1 or SensorID>10:
    SensorID=int(input("Input snesor ID"))
Temp=GetTemp(SensorID)
if Temp > HighTemp:
    Alarm()
    if Temp < LowTemp:
        print("Cold")
    else :
        print("Normal")
