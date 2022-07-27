# README

Check out this repository and change into the directory `AlertingSignals`
Create a config.yaml in the root directory that contains the following  where xx is a valid ingest Access token for Splunk observability and yyy is the realm you  are using ie eu0,us0,us1, jp0:

```text

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

