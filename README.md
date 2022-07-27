# README

Check out this repository and change into the directory `AlertingSignals`
Create a config.yaml in the root directory that contains the following  where:
- xxx is a valid ingest Access token for Splunk observability
- yyy is the value of the realm you are using ie *eu0,us0,us1*


```yaml

ACCESS_TOKEN: xxx
REALM: yyy
OD_ALERT: False
```

Set up your env by running the following to install the python dependencies and run the main app 

```bash
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

To test an Outlier Detection, Run the OD signal from the main.py app.

To Trigger the condition let  the app run for at least 10 minutes then change the value of OD_ALERT in the config.yal to True, and keep it set for at least one minute  ( you can set the alert  for 80% of 1 Minute)
