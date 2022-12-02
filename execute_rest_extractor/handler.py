# from common.utilities import sum_integers

import os
from ice_cream_factory_datapoints_extractor import extractor


def handle(secrets, data):
    print("running rest extractor")
    os.environ["COGNITE_CLIENT_SECRET"] = secrets.get("client-secret")
    os.environ["BACKFILL_MIN"] = data.get("backfill_min", "")
    extractor.main()
    print("running rest extractor done")


# def handle(data, client):
#     print("I got the following data:")
#     print(data)

#     if not ("a" in data and "b" in data):
#         raise KeyError("Data should contain both keys: 'a' and 'b'")

#     data["sum"] = sum_integers(data["a"], data["b"])

#     print("Will now return updated data")

#     return data
