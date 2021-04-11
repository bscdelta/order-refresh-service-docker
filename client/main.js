const fetch = require("isomorphic-unfetch");

const API_BASE = "http://localhost:3000";
const ORDERS = require("./orders.json");

const ZERO_BYTES32 =
  "0x0000000000000000000000000000000000000000000000000000000000000000";

(async () => {
  const orders = Object.fromEntries(
    ORDERS.map(
      ({
        hash,
        tokenGet,
        amountGet,
        tokenGive,
        amountGive,
        expires,
        nonce,
        user,
        v,
        r,
        s
      }) => [
        hash,
        [
          tokenGet,
          amountGet,
          tokenGive,
          amountGive,
          expires,
          nonce,
          user,
          v || 0,
          r || ZERO_BYTES32,
          s || ZERO_BYTES32
        ]
      ]
    )
  );

  const body = JSON.stringify({
    contractAddr: "0xd223B72593403fC4Ca22d501c198fd9927E4C67E",
    orders
  });

  console.log(body);

  const response = await fetch(API_BASE, {
    method: "POST",
    body
  });
  const jsonResponse = await response.json();

  console.log(jsonResponse);
})();
