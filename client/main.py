import json
import logging

import requests

API_BASE = "http://localhost:3000"

EMPTY_BYTES32 = "0x000000000000000000000000000000000000000000000000000000000000000"

logging.basicConfig(level=logging.DEBUG)


def main():
    with open("orders.json") as f:
        orders = json.load(f)

    order_keys = set([order["hash"] for order in orders])

    data = dict(
        contractAddr="0xd223B72593403fC4Ca22d501c198fd9927E4C67E",
        orders={
            order["hash"]: [
                order["tokenGet"],
                order["amountGet"],
                order["tokenGive"],
                order["amountGive"],
                order["expires"],
                order["nonce"],
                order["user"],
                order.get("v") or 0,
                order.get("r") or EMPTY_BYTES32,
                order.get("s") or EMPTY_BYTES32,
            ]
            for order in orders
        })

    r = requests.post(API_BASE, json=data)
    response = r.json()

    print(response)
    print("Update block timestamped", response["blockNumber"])
    print("Sent", len(order_keys), "orders, got back",
          len(response["orders"].keys()), "orders")


if __name__ == "__main__":
    main()
