import socket
import yaml
import time
import Signals.splunk as metrics


with open("config.yaml", "r") as ymlfile:
    cfg = yaml.safe_load(ymlfile)


def start_Signal(signaltype):
    print(f"Starting signalType {signaltype} ...")
 
    # Receive Packages
    setHigh = False
    while True:   
        time.sleep(10)
        if setHigh == True:
            metrics.write_outlier_data_to_splunk(
                "Linux-1",80, 1024 )
            metrics.write_outlier_data_to_splunk(
                "Linux-2",99, 2024 )
            metrics.write_outlier_data_to_splunk(
                "Linux-3",78, 1144 )
            metrics.write_outlier_data_to_splunk(
                "Linux-4",82, 1824 )
            metrics.write_outlier_data_to_splunk(
                "Linux-5",89, 1424 )
            metrics.write_outlier_data_to_splunk(
                "Linux-6",87, 1224 )
            metrics.write_outlier_data_to_splunk(
                "Linux-7",91, 3024 )
            metrics.write_outlier_data_to_splunk(
                "Linux-8",75, 1324 )
            metrics.write_outlier_data_to_splunk(
                "Linux-9",66, 454 )
            metrics.write_outlier_data_to_splunk(
                "Linux-0",69, 728 )
            setHigh = False    
        else:        
            metrics.write_outlier_data_to_splunk(
                "Linux-1", 60, 400)
            metrics.write_outlier_data_to_splunk(
                "Linux-2",55, 1024 )
            metrics.write_outlier_data_to_splunk(
                "Linux-3",78, 644 )
            metrics.write_outlier_data_to_splunk(
                "Linux-5",89, 824 )
            metrics.write_outlier_data_to_splunk(
                "Linux-6",87, 1024 )
            metrics.write_outlier_data_to_splunk(
                "Linux-7",80, 2046 )
            metrics.write_outlier_data_to_splunk(
                "Linux-8",34, 624 )
            metrics.write_outlier_data_to_splunk(
                "Linux-9",44, 354 )
            metrics.write_outlier_data_to_splunk(
                "Linux-0",69, 728 )
            setHigh = True