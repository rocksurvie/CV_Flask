from flask import Flask, render_template, request, redirect
import hashlib
import sqlite3


app = Flask(__name__) #creating flask app name

@app.route('/resume_2')
def home():
    return render_template("index.html")

@app.route('/remplirDon')
def resume_1():
    return render_template("addFi.html")

@app.route('/')
def resume_2():
    return render_template("resume_2.html")


@app.route('/consultation/<int:api_key>')
def sha256_hash(input_string):
    # Fonction de hachage SHA-256
    sha256 = hashlib.sha256()
    sha256.update(input_string.encode('utf-8'))
    return sha256.hexdigest()

def check_sum_256(array, api_value, key_to_check):
    # Calcul de la somme
    array_sum = str(array[0]) + str(api_value)

    # Hachage de la somme avec SHA-256
    hashed_sum = sha256_hash(str(array_sum))

    # Vérification avec la clé spécifique
    if hashed_sum == key_to_check:
        return True
    else:
        return False
    
"""5625719273"""

def Readfiche(api_key):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients')
    data = cursor.fetchall()
    conn.close()
    array_sum = str(data[0]) + "5625719273"
    if check_sum_256(data, sha256_hash(array_sum), api_key): 
        # Rendre le template HTML et transmettre les données
        return render_template('read_data.html', data=data)
    return "api_key !!"


@app.route('/graphique/<int:api_key>')
def afficheGraph(api_key):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients')
    data = cursor.fetchall()
    conn.close()
    array_sum = str(data[0]) + "5625719273"
    if check_sum_256(data, api_key, sha256_hash(array_sum)): 
        # Rendre le template HTML et transmettre les données
        return render_template('graph.html', data=data)
    return "api_key !!"


@app.route('/ajouter_message', methods=['POST'])
def ajouter_client():
    nom = request.form['nom']
    prenom = request.form['prenom']
    messages = request.form['messages']

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO clients (nom, prenom, messages) VALUES (?, ?, ?)", (nom, prenom, messages))

    conn.commit()
    conn.close()

    return redirect('/ajouter_message')




@app.route('/resume_template')
def resume_template():
    return render_template("resume_template.html")

if(__name__ == "__main__"):
    app.run()
