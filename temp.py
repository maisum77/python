# test_sender.py
import hmac, hashlib, json, requests

secret = "f3f0a1b2c79b6d349328feadc1ee99834a9b112accc1d2a88d529bcbbfa91320"
payload = {"event": "phone.test23456789", "order_id": 55}
raw = json.dumps(payload, separators=(',', ':')).encode()
sig = "sha256=" + hmac.new(secret.encode(), raw, hashlib.sha256).hexdigest()

r = requests.post(
    "https://unopiatic-jamey-winterishly.ngrok-free.dev/api/webhooks/dxscript/",
    data=raw,
    headers={"X-Signature": sig, "Content-Type": "application/json"}
)
print(r.status_code, r.json())