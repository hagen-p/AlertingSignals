import os
from signal import Signals
import yaml
import time
import random
import Signals.splunk as metrics


with open("config.yaml", "r") as ymlfile:
    cfg = yaml.safe_load(ymlfile)

def start_Signal(signaltype):
    random.seed()
    ODseed = 15
    ODMinute = 0
    ODcheck = False 
    print(f"Starting signalType {signaltype} ...")
    while True:
        try:
            f=open ("Alerts/OD.alert","r")
            org_path=os.path.realpath(f.name)
            dest_path = os.path.join(os.path.dirname(os.path.realpath(f.name)),'OD.old.alert')
            ODcheck = True
        except FileNotFoundError:
            ODcheck = False

        if  ODcheck == False:
            metrics.write_outlier_data_to_splunk(
                "Linux-1",80 + random.randrange(ODseed)  , 1024 )
            metrics.write_outlier_data_to_splunk(
                "Linux-2",80 + random.randrange(ODseed), 2024 )
            metrics.write_outlier_data_to_splunk(
                "Linux-3",80 + random.randrange(ODseed), 1144 )
            metrics.write_outlier_data_to_splunk(
                "Linux-4",80 + random.randrange(ODseed), 1824 )
            metrics.write_outlier_data_to_splunk(
                "Linux-5",80 + random.randrange(ODseed), 1424 )
            metrics.write_outlier_data_to_splunk(
                "Linux-6",80 + random.randrange(ODseed), 1224 )
            metrics.write_outlier_data_to_splunk(
                "Linux-7",80 + random.randrange(ODseed), 3024 )
            metrics.write_outlier_data_to_splunk(
                "Linux-8",80 + random.randrange(ODseed), 1324 )
            metrics.write_outlier_data_to_splunk(
                "Linux-9",80 + random.randrange(ODseed), 454 )
            metrics.write_outlier_data_to_splunk(
                "Linux-0",80 + random.randrange(ODseed), 728 )
            #setHigh = False    
        elif ODcheck ==  True: 
            print (60-ODMinute)       
            metrics.write_outlier_data_to_splunk(
                "Linux-1",80 + random.randrange(ODseed)  , 1024 )
            metrics.write_outlier_data_to_splunk(
                "Linux-2",80 + random.randrange(ODseed), 2024 )
            metrics.write_outlier_data_to_splunk(
                "Linux-3",80 + random.randrange(ODseed), 1144 )
            metrics.write_outlier_data_to_splunk(
                "Linux-4",80 + random.randrange(ODseed), 1824 )
            metrics.write_outlier_data_to_splunk(
                "Linux-5",80 + random.randrange(ODseed), 1424 )
            metrics.write_outlier_data_to_splunk(
                "Linux-6",80 + random.randrange(ODseed), 1224 )
            metrics.write_outlier_data_to_splunk(
                "Linux-7",80 + random.randrange(ODseed), 3024 )
            metrics.write_outlier_data_to_splunk(
                "Linux-8",80 + random.randrange(ODseed), 1324 )
            metrics.write_outlier_data_to_splunk(
                "Linux-9",40 + random.randrange(ODseed), 454 )
            metrics.write_outlier_data_to_splunk(
                "Linux-0",80 + random.randrange(ODseed), 728 )
            ODMinute = ODMinute + 10 # Add 10 seconds to counter
            if ODMinute >= 60: # more then a minute has gone by    
                os.rename(org_path, dest_path) #renaming the alert file to stop the Outlier
                ODMinute = 0 #reset
        else:
            print ("OD_ALERT needs to be set to True of False")
        
        time.sleep(10) # wait 10 second
       