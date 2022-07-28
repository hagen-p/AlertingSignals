import os
from signal import Signals
import yaml
import time
import random
import Signals.splunk as metrics


with open("config.yaml", "r") as ymlfile:
    cfg = yaml.safe_load(ymlfile)

def start_Signal(signaltype):
    if signaltype=="OD":
        start_OD_Signal()
    elif signaltype=="RO":
        start_RO_Signal()
    elif signaltype=="HA":
        start_HA_Signal()
    else:
        print('Invalid Signal Received!.!.!.! Exiting !!!!')
        exit()

def start_RO_Signal():
    random.seed()
    ROseed   = 150
    ROGrowth = 0
    print("Starting Resource Running Out Detection Signals ...")
    while True:
        try:
            f=open ("Alerts/RO.alert","r")
            #org_path=os.path.realpath(f.name)
            #dest_path = os.path.join(os.path.dirname(os.path.realpath(f.name)),'RO.old.alert')
            ROcheck = True
            print(ROGrowth)
            ROGrowth=ROGrowth + 1
            if ROGrowth==1:
               print("Starting to Increase load")   
        except FileNotFoundError:
            ROcheck = False
            
        metrics.write_network_data_to_splunk(
                "LBA-1", 2500 + random.randrange(ROseed)) 
        metrics.write_network_data_to_splunk(
                "LBA-2", 2530 + random.randrange(ROseed) + ROGrowth)
        metrics.write_network_data_to_splunk(
                "LBA-3", 2560 + random.randrange(ROseed))
        metrics.write_network_data_to_splunk(
                "LBA-4", 2590 + random.randrange(ROseed))          
        
        time.sleep(10) # wait 10 second
       
def start_OD_Signal():
    random.seed()
    ODseed = 15
    ODMinute = 0
    ODcheck = False 
    print("Starting Outlier Detection Signals ...")
    while True:
        try:
            f=open ("Alerts/OD.alert","r")
            org_path=os.path.realpath(f.name)
            dest_path = os.path.join(os.path.dirname(os.path.realpath(f.name)),'OD.old.alert')
            deviation = 40
            
        except FileNotFoundError:
            ODcheck = False
            deviation = 80
           #setHigh = False    
        
            metrics.write_outlier_data_to_splunk(
                "Linux-1",80 + random.randrange(ODseed), 1024 )
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
                "Linux-9",deviation + random.randrange(ODseed), 454 )
            metrics.write_outlier_data_to_splunk(
                "Linux-0",80 + random.randrange(ODseed), 728 )    
        
        time.sleep(10) # wait 10 second
       

def start_HA_Signal():
    random.seed()
    HAseed   = 150
    HAGrowth = 1
    print("Starting Historical Anomaly Detection Signals ...")
    while True:
        try:
            f=open ("Alerts/HA.alert","r")
            #org_path=os.path.realpath(f.name)
            #dest_path = os.path.join(os.path.dirname(os.path.realpath(f.name)),'HA.old.alert')
            HAcheck = True
            print(HAGrowth)
            HAGrowth=HAGrowth + 1
            if HAGrowth==1:
               print(" Not yet implemented - Starting to deviate from normal load")   
        except FileNotFoundError:
            HAcheck = False

        time.sleep(10) # wait 10 second
           
         