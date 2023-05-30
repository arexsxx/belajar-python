from flask import Flask
from models import persegipanjang
app= Flask(__name__)

@app.route('/')
def index():
    obj_p=persegipanjang()
    obj_p.panjang=10.0
    obj_p.lebar=8.0

    return'''
        <h2>Bangun Datar: Persegi Panjang<h2/>
        Luas persegi panjang=%.3f</br>
        keliling persegi panjang=%.3f
    '''%(obj_p.luas(),obj_p.keliling())

if __name__=='__main__':
    app.run(debug=True)    


 
