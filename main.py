from Signals import server

if __name__ == "__main__":
    signalType = input("signalType:  (OD [Not yet implemented RO, HA)")
    if signalType == "OD": #or signalType == "RO" or signalType == "HA":
        server.start_Signal(signalType)
    else:
        print ( "signalTypes allowed are :")
        print ("                            OD - Outlier Detection")
        print ("                            RO - Resource Running Out")
        print ("                            HA - Historical Anomaly")

        




