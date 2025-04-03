from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
 return """
<h1>¡Hola! Soy Andrés</h1>
<p>Estudio en: UVM</p>
<p>Me gusta: videojuegos</p>
<p><em>"no se trata de porque peleo, si no por quien"</em></p> """
if __name__ == '__main__':  
    app.run(debug=True)