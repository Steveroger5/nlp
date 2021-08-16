
from flask import Flask,render_template,request,redirect
import Prediction


app = Flask(__name__)


@app.route('/')
def first_page():
    return render_template("index.html")

@app.route('/submit',methods = ['POST'])
def display():
        path = request.form.get("fname")
        print(path)
        pred = Prediction.get_pred(path)
        return render_template("result.html",result  ={"path":path,"pred":pred})

if __name__ == "__main__":
    app.run(debug=True)