from flask import Flask,render_template

app = Flask(__name__) #creating flask app name

@app.route('/resume_2')
def home():
    return render_template("index.html")

@app.route('/resume_1')
def resume_1():
    return render_template("resume_1.html")

@app.route('/')
def resume_2():
    return render_template("resume_2.html")


@app.route('/fiche_client/<int:api_key>')
def sha256_hash(input_string):
    # Fonction de hachage SHA-256
    sha256 = hashlib.sha256()
    sha256.update(input_string.encode('utf-8'))
    return sha256.hexdigest()

def check_sum_256(array, api_value, key_to_check):
    # Calcul de la somme
    array_sum = array[0] + api_value

    # Hachage de la somme avec SHA-256
    hashed_sum = sha256_hash(str(array_sum))

    # Vérification avec la clé spécifique
    if hashed_sum == key_to_check:
        return True
    else:
        return False
    
    
def Readfiche(api_key):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients')
    data = cursor.fetchall()
    
    conn.close()
    
    # Rendre le template HTML et transmettre les données
    return render_template('read_data.html', data=data)



@app.route('/resume_template')
def resume_template():
    return render_template("resume_template.html")

if(__name__ == "__main__"):
    app.run()
