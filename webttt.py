from flask import Flask,render_template,request
class player:
    def __init__(self,name,symbol):
        self.name=name
        self.sym=symbol
app=Flask(__name__,static_folder='static',template_folder='templates')
app.secret_key="viggu2205"
@app.route("/",methods=["POST","GET"])
def infoplayer():
    return render_template("home.html")
@app.route("/play",methods=["POST"])
def play():
    pl1=player(request.form["pl1n"],request.form["pl1s"])
    pl2=player(request.form["pl2n"],request.form["pl2s"])
    return render_template("new.html",plr=[pl1,pl2])
if __name__=="__main__":
    app.run(debug=True)