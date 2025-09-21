from flask import Flask, request, jsonify
import requests
import os
import logging

app = Flask(name)

API_KEY = "P6NW6D1"
OWNER = "Zionix (@zioniiix), Encore(@frappeash)"

Logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("demo_api")

def error_response(message, code=502, extra=None):
"""Show contact info only when really needed."""
payload = {"error": message, "owner": OWNER}
if extra:
payload.update(extra)
return jsonify(payload), code

@app.route("/demo")
def demo():
term = request.args.get("term")
if not term:
return jsonify({"error": "Term missing", "owner": OWNER}), 400

url = f"http://osintx.info/API/krobetahack.php?key={API_KEY}&type=mobile&term={term}"
try:
resp = requests.get(url, timeout=10)
except requests.RequestException as e:
logger.exception("Upstream request failed")
return error_response("Upstream request failed", code=502, extra={"details": str(e)})

try:
remote_json = resp.json()
except ValueError:
logger.exception("Invalid JSON from upstream")
return error_response("Invalid JSON from upstream", code=502)

status_code = resp.status_code if isinstance(resp.status_code, int) else 502
if isinstance(remote_json, dict):
remote_json.setdefault("owner", OWNER)
return jsonify(remote_json), status_code

Wrap list or other JSON types

return jsonify({"data": remote_json, "owner": OWNER}), status_code

if name == "main":
host = os.getenv("FLASK_HOST", "0.0.0.0")
port = int(os.getenv("FLASK_PORT", 5000))
app.run(host=host, port=port)

