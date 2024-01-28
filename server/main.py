from flask import Flask ,  request , jsonify

app = Flask(__name__)

@app.route("/" , methods=['GET' , 'POST'])

def home_page():
    if request.method == 'POST':
        # print(request.get_json())
        return jsonify("terimummyrandi"), 200
    
    return "maachuda" , 200


if __name__ == "__main__":
    app.run(debug=True)