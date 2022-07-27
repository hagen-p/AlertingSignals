 
import socket
import yaml
import time
import Signals.splunk as metrics


with open("config.yaml", "r") as ymlfile:
    cfg = yaml.safe_load(ymlfile)
    metrics.write_outlier_data_to_splunk(
                "Linux-4",82, 924 )