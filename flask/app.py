from flask import Flask, render_template, request

app= Flask(__name__)
app= Flask(__name__, template_folder="theme")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method=="POST":
        kd=request.form["kode"]#atribut nama form
        #ini harus sama dengan form yang di HTML
        nm=request.form["nama"]
        harga=float(request.form["harga"])
        return render_template("handling.html", nama=nm, kode=kd, harga=harga)
    return render_template ("form.html")

if __name__=="__main__":
    app.run(debug=True)