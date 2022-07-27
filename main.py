from Signals import server

if __name__ == "__main__":
    alertsCondition =  ["od"] #,"ro","ha"]
    signalType = str(input("signalType:  (OD [Not yet implemented RO, HA)")).strip().lower()
    if server.indexExists(alertsCondition,signalType)
        server.start_signal(signalType)
    else
        print ( singalTypes allowed are :")
        print ("                            OD - Outlier Detection")
        print ("                            RO - Resource Running Out")
        print ("                            HA - Historical Anomaly")

        




