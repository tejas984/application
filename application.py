from flask import Flask, render_template

#app object created for flask named app
app=Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "Welcome to world of AI"

@app.route("/")
def hello():
    return "<h1 style='color:red'>This is second route</h1>"
    #return render_template("index.html")
@app.route("/login")
def login():
     #return "<h1 style='color:red'>This is second route</h1>"
     return render_template("index.html")
#print("****",__name__)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)