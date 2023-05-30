from flask import Flask, render_template
app= Flask(__name__,template_folder="template")

@app.route("/")
def index():
    nm="Ervin Khoirus Syifa' Uddin"
    no="5220411102"
    pr="Teknik informatika"
    k="Inf-B"
    tgs=90
    kuis=70
    uts=75
    uas=80
    na=tgs*0.2+kuis*0.2+uts*0.3+uas*0.3
    return render_template("index.html", name=nm, nim=no, ps=pr, kls=k, nil=na)

if __name__=="__main__":
    app.run(debug=True)