from flask import Flask, request, make_response, render_template

app = Flask(__name__)

# Pagina di login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Qui puoi validare l'utente e la password come desideri
        # Ad esempio, puoi confrontarli con un database o una lista predefinita

        # Una volta validati, crea un cookie
        resp = make_response("Accesso riuscito")
        resp.set_cookie('username', username)
        return resp

    return render_template('login2.html')

if __name__ == '__main__':
    app.run()
