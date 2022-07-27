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

To test an Outlier Detection, Run the OD signal from the main.py app.

To Trigger the condition let  the app run for at least 10 minutes 
then rename the OD.old.alert file in the *Alerts* subdirectory to OD.alert  (or create it if it doesn't exist)
The app will then change one single to be an outlier  and keep it running at a lower number for a minute. 
(you can see it count back)
Set your outlier detection to have a trigger threshold of 2  and a duration of 80% of 1 minute
the clear threshold is 1.4 again 80% of one minute