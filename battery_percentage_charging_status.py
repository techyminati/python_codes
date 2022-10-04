#Find battery percentage and charging status in windows and linux using Python
#First install required package
#pip install scipy
import psutil
batteryinformation  = psutil.sensors_battery()
print("The Battery percentage of the sytem  = ",batteryinformation.percent)
if batteryinformation.power_plugged == True :
    print("The battery of the system is Charging!!!")
elif batteryinformation.power_plugged == False:
    print("The battery of the system is NOT Charging")
