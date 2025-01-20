from flask import Flask, request, jsonify

app = Flask(__name__)

users = {
     "1": {"id": 1, "name": "Alice", "email": "alice@example.com"},
      "2": {"id": 2, "name": "Bob","email": "bob@example.com"},
}

@app. route("/profile", methods=["GET"])
def profile():
  user_id = request.args.get("user_id" )
  api_key = request. headers.get "Authorization")
  
  if not api_key or api_key != "VALID_API_KEY" : 
     return jsonify({"error": "Unauthorized"}), 401

user = users. get(user_id)
if not user:
  return jsonify({"error": "User not found"}), 404

return jsonify(user)
