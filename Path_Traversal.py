import os 
from flask import Flask, request, jsonify 

app = Flask(__name__) 

@app. route("/read-file", methods= [ "GET" ] ) 
def read_file():
     filename = request.args. get( "filename" ) 
     with open (f" /var/www/uploads/{filename}", "r") as file:
         content = file. read ()
     return jsonify({"content": content}) 

if __name__ == "__main__":
    app.run(debug=True)
