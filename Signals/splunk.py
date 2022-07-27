import signalfx
import logging
import yaml
import sys

with open("config.yaml", "r") as ymlfile:
    cfg = yaml.safe_load(ymlfile)

sfx = signalfx.SignalFx(
    api_endpoint="https://api." + cfg["REALM"] + ".signalfx.com",
    ingest_endpoint="https://ingest." + cfg["REALM"] + ".signalfx.com",
    stream_endpoint="https://stream." + cfg["REALM"] + ".signalfx.com",
)

ingest = sfx.ingest(cfg["ACCESS_TOKEN"])


def write_outlier_data_to_splunk(server_name, cpu,memory):
    # logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    ingest.send(
        gauges=[
            {
                "metric": "demo.alerting.cpu",
                "value": cpu,
                "dimensions": {"server": server_name},
            },
            {
                "metric": "demo.alerting.memory",
                "value": memory,
                "dimensions": {"server": server_name},
            }
        ]
    )
