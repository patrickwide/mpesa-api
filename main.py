from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template("index.html")

@app.route('/about', methods=['POST', 'GET'])
def about():
    return render_template("about.html")



if __name__ == "__main__":
    app.run(debug=True, port=4000)
