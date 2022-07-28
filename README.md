# README

Check out this repository and change into the directory `AlertingSignals`
Create a config.yaml in the root directory that contains the following  where:
- xxx is a valid ingest Access token for Splunk observability
- yyy is the value of the realm you are using ie *eu0,us0,us1*


```yaml

ACCESS_TOKEN: xxx
REALM: yyy
```

Set up your env by running the following to install the python dependencies and run the main app 

```bash
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

## OUTLIER DETECTION

To test an Outlier Detection detector, run the OD signal from the main.py app.
and let the app run for at least 10 minutes it will generate  10 time series that have a variation of 10% cpu%
as the demo.alerting.cpu signal (with a dimension of server:Linux-0 to Linux-9)

**How to trigger the condition**:

Rename the OD.old.alert file in the *Alerts* subdirectory to OD.alert (or create it in the *Alerts* directory if it doesn't exist)
The app will then change one single Time Series to be an outlier  and keep it running at a lower number for a minute. (you can see it count back)
Set your outlier detection to have a trigger threshold of 2 and a duration of 80% of 1 minute
the clear threshold is 1.4 again with a duration 80% of one minute

## RESOURCE RUNNING OUT

To test a Resource Running Out detector, run the RO signal from the main.py app.
Let the app run for at least 10 minutes, it will generate 4 time series for network bandwidth with an average 
the demo.alerting.networkbandwith signal (with a dimension of server:LBA-0 to LBA-4)

**How to trigger the condition:**

Rename the RO.old.alert file in the *Alerts* subdirectory to OD.alert or create it in the *Alerts* directory if it doesn't exist)
The app will then start adding  extra load to the LBA-2 time series with a rate of 1 per second (on top of the normal variation of the signal)
Set your Resource  detection to  trigger on Capacity and set that to 10000,  trigger sensitivity to Custom
have a trigger threshold of 1 hour and a duration of 80% of 5 minutes
the clear threshold is 1 hour again with a duration of 80% of 5 minutes

