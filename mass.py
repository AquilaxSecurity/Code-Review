from flask import Flask, request, jsonify

app = Flask(__name__)

users = {
   "1": {"id": 1, "name": "Alice", "email": "alice@example.com", "is_admin": False},
    "2": {"id": 2,"name": "Bob", "email": "bob@example.com", "is_admin": False},
}

@app. route("/update_user", methods=["POST"])
def update_user():
   data = request. json
   user_id = data. get("id" )

   user = users. get(user_id)
   if not user:
        return jsonify({"error": "User not found"}), 404

user. update(data)

return jsonify({"message": "User updated successfully", "user": user})
