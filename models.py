from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() #Crée une instance de SQLAlchemy. Cette instance sera utilisée pour interagir avec la base de données


class Person(db.Model): #Définit une nouvelle classe Person qui hérite de db.Model, faisant de Person un modèle de base de données dans SQLAlchemy.
    id = db.Column(db.Integer, primary_key=True) # Définit une colonne id qui est de type entier (Integer) et est également la clé primaire de la table. Chaque instance de Person aura un identifiant unique.
    name = db.Column(db.String(50), nullable=False) #Définit une colonne name qui est de type chaîne de caractères (String) avec une longueur maximale de 50 caractères. nullable=False indique que cette colonne ne peut pas être vide (c'est-à-dire que chaque Person doit avoir un nom).

    def __repr__(self): #méthode spéciale utilisée pour définir comment une instance de la classe Person est représentée sous forme de chaîne de caractères.
        return f"<Person {self.name}>" #utile pour le débogage et pour afficher des informations sur les objets Person dans les logs ou dans une console interactive.