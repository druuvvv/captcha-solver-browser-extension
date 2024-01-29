from flask import Flask ,  request , jsonify
import captchaSolver
app = Flask(__name__)

@app.route("/" , methods=['GET' , 'POST'])

def url():
    if request.method == 'POST':
        print("request recieved")
        returnedValue = captchaSolver.binaryImgToOpenCV(request.get_json())
        print("returnedValue")
        return jsonify("answer"), 200
    
    return "bruh" , 200


if __name__ == "__main__":
    app.run(debug=True)