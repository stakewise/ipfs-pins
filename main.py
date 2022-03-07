import json
import os

import ipfshttpclient
import requests

IPFS_PIN_ENDPOINT = "/dns/ipfs.infura.io/tcp/5001/https"
IPFS_PINATA_PIN_ENDPOINT = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
IPFS_PINATA_API_KEY = os.getenv("PINATA_API_KEY")
IPFS_PINATA_SECRET_KEY = os.getenv("PINATA_SECRET_KEY")

def add_ipfs_prefix(ipfs_id: str) -> str:
    if ipfs_id.startswith("ipfs://"):
        ipfs_id = ipfs_id[len("ipfs://") :]

    if not ipfs_id.startswith("/ipfs/"):
        ipfs_id = "/ipfs/" + ipfs_id

    return 

def upload_data_to_ipfs():
    """Submits files to the IPFS and pins the file."""

    files = [f for f in os.listdir("data") if os.path.isfile(os.path.join("data", f))]

    infura_ids = []
    try:
        with ipfshttpclient.connect(IPFS_PIN_ENDPOINT) as client:
            for file in files:
                with open('data/'+file) as json_file:
                    data = json.load(json_file)
                    ipfs_id = client.add_json(data)
                    client.pin.add(ipfs_id)
                    infura_ids.append(file + ": /ipfs/" + ipfs_id)
    except Exception as e:
            print(e)
            print(f"Failed to submit deposit data to {IPFS_PIN_ENDPOINT}")

    if not infura_ids:
        raise Exception("Failed to submit deposit data to IPFS")

    print("Infura IDs: " + infura_ids)

    pinata_ids = []
    if IPFS_PINATA_API_KEY and IPFS_PINATA_SECRET_KEY:
        headers = {
            "pinata_api_key": IPFS_PINATA_API_KEY,
            "pinata_secret_api_key": IPFS_PINATA_SECRET_KEY,
            "Content-Type": "application/json",
        }
        try:
             for file in files:
                with open('data/'+file) as json_file:
                    data = json.load(json_file)
                    response = requests.post(
                        headers=headers,
                        url=IPFS_PINATA_PIN_ENDPOINT,
                        data=json.dumps({"pinataContent": data}, sort_keys=True),
                    )
                    response.raise_for_status()
                    ipfs_id = response.json()["IpfsHash"]
                    pinata_ids.append(file + ": /ipfs/" + ipfs_id)
        except Exception as e:  # noqa: E722
            print(e)
            print("Failed to submit deposit data to Pinata")

    if not pinata_ids:
        raise Exception("Failed to submit deposit data to IPFS")

    print("Pinata IDs: " + pinata_ids)

upload_data_to_ipfs()