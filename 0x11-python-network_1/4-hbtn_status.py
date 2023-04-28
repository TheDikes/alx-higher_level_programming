#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status."""
import requests


if __name__ == "__main__":
    response = requests.get("https://intranet.hbtn.io/status")
    json_data = response.json()

    print("Body response:")
    print("\t- type:", type(json_data))
    print("\t- content:", json_data)
