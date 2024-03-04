from flask import Flask, request, render_template, redirect, url_for
from models import Person, db

##Configuration de l'application Flask
app = Flask(__name__) #Crée une instance de l'application Flask
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///people.db" #Configure l'application pour utiliser SQLite comme base de données, avec le fichier people.db

##Initialisation de la base de données
db.init_app(app)

with app.app_context():
    db.create_all() #Crée toutes les tables nécessaires dans la base de données (selon les modèles définis, comme Person)


@app.route("/") #Définit la route pour l'URL racine ("/")
def index(): #La fonction qui est exécutée quand on accède à cette route
    people = Person.query.all() #Récupère toutes les entrées de personnes de la base de données
    return render_template("index.html", people=people) #Renvoie le template HTML avec la liste des personnes


@app.route("/add", methods=["GET", "POST"]) #Définit la route pour ajouter une personne, acceptant les méthodes GET et POST
def add_person():
    if request.method == "POST":
        name = request.form["name"] #Récupère le nom de la personne à partir du formulaire
        new_person = Person(name=name) #Crée une nouvelle instance de Person
        db.session.add(new_person) #ajoute la nouvelle personne à la base de données
        db.session.commit() #sauvegarde
        return redirect(url_for("index")) #Redirige vers la page d'accueil après l'ajout
    return render_template("person_form.html") #Si la méthode n'est pas POST, affiche le formulaire d'ajout


if __name__ == "__main__": #Exécute l'application en mode debug si le script est exécuté directement
    app.run(debug=True)
