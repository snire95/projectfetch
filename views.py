from flask import Flask
from flask import render_template
from flask import request, jsonify, make_response

 
app = Flask(__name__)
@app.route("/guestbook")
def guestbook():
    return render_template("public/guestbook.html")

@app.route("/guestbook/create-entry", methods=["POST"])
def create_entry():

    req = request.get_json()

    print(req)

    res = make_response(jsonify("eitan the king"), 200)

    return res    

if __name__ == "__main__":
    app.run() 


