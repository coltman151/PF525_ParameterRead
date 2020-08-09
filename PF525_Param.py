from pycomm3 import CIPDriver, CommonService, Pack
from os import system, name
import ParamDict

def read_525_param():
    
    with CIPDriver(drivePath) as drive:
        parm = drive.generic_message(
            service=CommonService.get_attribute_single,  #b'\x0E'
            class_code=b'\x93',
            instance=intParam,
            attribute=b'\x09',
            connected=False,
            unconnected_send=True,
            route_path=True,
            data_format=[(dataFormatString, 'INT'), ],
            name="PF525"
            )
            
        return(parm)

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


clear()
print("PF525 Parameter Read. Q to quit.")
#drivePath = input("Enter the drive path ({PLC IP}/bp/{Ethernet Adapter Slot}/enet/{Drive IP})")
drivePath = "10.64.138.13/bp/2/enet/192.168.1.30"
while True:    
    readParam = input("Enter the parameter number to be read: ")
    if readParam == "q" or readParam == "Q":
        break
    else:
        intParam = int(readParam)
        paramList = ParamDict.ParamDict[readParam]
        instanceString = paramList[1]
        dataFormatString = paramList[0]
        returnedParam = read_525_param()
        returnedDict = returnedParam[1]
        returnedDesc = str(list(returnedParam[1]))
        for key, value in returnedDict.items():
            print(key)
            print(value)