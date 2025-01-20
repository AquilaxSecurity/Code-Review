from flask import Flask, request 

app = Flask(__name__)

@app.route("/set-config", methods=["POST"]) 
def set_config():
    config = request. json.get "config") 
    exec (f"settings = {config}") 
    return "Configuration updated successfully!"

if __name__ == "__main__":
   app. run (debug=True)
