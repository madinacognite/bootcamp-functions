# def handle(data, client):
#     print(f"Hello from {__name__}!")
#     print("I got the following data:")
#     print(data)
#     print("Will now return data")
#     return data

import os
from common.csv_extractor_simple import extractor

def handle(secrets):
   print("running csv extractor")
   os.environ["COGNITE_CLIENT_SECRET"] = secrets.get("client-secret")
   extractor.main()
   print("running csv extractor done")

