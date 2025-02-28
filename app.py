from flask import Flask,jsonify, request, redirect, url_for, render_template, render_template_string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        
        option = request.form.get("option")
        
    
        if option == "はい":
            return redirect(url_for("result"))
        elif option == "いいえ":
            return redirect(url_for("result2"))
        else:
            return redirect(url_for("featuring"))
  

    my_list = [
        ["1", "HlGFzHE3W50.jpg", "https://www.youtube.com/watch?v=HlGFzHE3W50"],
        ["2", "lhvGiY0Qjt8.jpg", "https://www.youtube.com/watch?v=lhvGiY0Qjt8"],
        ["3", "YB0rrc5B2LM.jpg", "https://www.youtube.com/watch?v=YB0rrc5B2LM"],
        ["4", "WjbJReewZC4.jpg", "https://www.youtube.com/watch?v=WjbJReewZC4"],
        ["5", "Q1hg5xjs5yY.jpg", "https://www.youtube.com/watch?v=Q1hg5xjs5yY"],
        ["6", "vprWhBtb298.jpg", "https://www.youtube.com/watch?v=vprWhBtb298"],
        ["7", "NOHArqrTk40.jpg", "https://www.youtube.com/watch?v=NOHArqrTk40"],
        ["8", "gqAcBxaowEw.jpg", "https://www.youtube.com/watch?v=gqAcBxaowEw"],
        ["9", "pasdesbourres.jpg", "https://www.youtube.com/watch?v=1hdHc1hJAWU"]
    ]
    return render_template("indexa.html", movies=my_list)

@app.route("/index2")
def index2():
    return render_template('index2.html')

@app.route('/index3')
def index3():
    return render_template('index3.html')

@app.route('/index4')
def index4():
    return render_template('index4.html')

@app.route('/history17')
def history17():
    return render_template('history17.html')

@app.route('/history19c')
def history19c():
    return render_template('history19c.html')

@app.route('/historymodern')
def historymodern():
    return render_template('historymodern.html')

@app.route("/index0")
def index0():
    return render_template('index0.html')

@app.route("/indexmove")
def indexmove():
    return render_template('indexmove.html')

@app.route("/sandsand")
def sandsand():
    return render_template('sandsand.html')

@app.route("/variation")
def variation():
    return render_template('variation.html')


@app.route("/result")
def result():
    return render_template("result.html")

@app.route("/result2")
def result2():
    return render_template("result2.html")

@app.route("/result3")
def result3():
    return render_template("result3.html")

@app.route("/aurora")
def aurora():
    return render_template('aurora.html')

@app.route("/Cinderella")
def Cinderella():
    return render_template('Cinderella.html')

@app.route("/blackswan")
def blackswan():
    return render_template('blackswan.html')

@app.route("/Kaizoku")
def Kaizoku():
    return render_template('Kaizoku.html')

@app.route("/gayane")
def gayane():
    return render_template('gayane.html')

@app.route("/Paris")
def Paris():
    return render_template('Paris.html')

@app.route("/pasdedeux")
def pasdedeux():
    return render_template('pasdedeux.html')
    
@app.route("/romeo")
def romeo():
    return render_template('romeo.html')

@app.route("/talisman")
def talisman():
    return render_template('talisman.html')

@app.route("/featuring")
def featuring():
    return render_template('featuring.html')

