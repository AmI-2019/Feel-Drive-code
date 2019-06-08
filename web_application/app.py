from flask import Flask, redirect, url_for, render_template, request, session, jsonify

import db_interaction

app = Flask(__name__)
app.secret_key="feel&drivesecret"
api_endopoint="/api/v1"

@app.route('/')
def home_redirect():
    return redirect(url_for("home"))

@app.route('/home',methods=['GET'])
def home():
    user_id = session.get("user_id", "")
    authenticated = False
    if user_id != "":
        authenticated = True
    return render_template("login.html", status = authenticated)

@app.route("/login", methods=['POST'])
def login():
    username = request.form["username"]
    password = request.form["password"]
    result=db_interaction.check_user_password(username,password)
    if result is not None:
        session["user_id"]=result
        return render_template("system.html", user=username)
    else:
        return redirect(url_for("login_error"))


@app.route("/registration_page")
def registration_page():
    return render_template("registration.html")

@app.route('/registration', methods=['POST'])
def registration():
    username = request.form["username"]
    password = request.form["password"]

    if username == "" or password == "":
        return redirect(url_for("registration_error",status=True))

    result=db_interaction.check_user(username)

    if result is None:
        db_interaction.add_user(username,password)
        session["user_id"] = result
        return redirect(url_for("registration_succeed"))
    else:
        return redirect(url_for("registration_error",status = False))


@app.route("/logout")
def logout():
    del session["user_id"]
    return redirect(url_for("home"))


@app.route("/registration_error")
def registration_error():
    return render_template("registration_error.html")


@app.route("/login_error")
def login_error():
    return render_template("login_error.html")


@app.route("/registration_succeed")
def registration_succeed():
    return render_template("registration_succeed.html")


@app.route(api_endopoint+'/login', methods=['GET'])
def REST_user_check():
    payload=request.json
    password=payload['password']
    username=payload['username']
    result=db_interaction.check_user_password(username,password)
    if result is None:
        return jsonify("404")
    else:
        return jsonify("200")

@app.route(api_endopoint+'/add_relation', methods=['POST'])
def REST_add_relation():
    payload=request.json
    username=payload['username']
    song=payload['song']
    liked=payload['liked']
    feeling=payload['feeling']
    db_interaction.add_relation(username, song, liked, feeling)
    return jsonify('200')


@app.route(api_endopoint+'/liked_songs', methods=['GET'])
def REST_get_liked_songs():
    payload=request.json
    feeling=payload['feeling']
    username=payload['username']
    result=db_interaction.get_liked_songs_by_feeling(username,feeling)
    return jsonify(result)


@app.route(api_endopoint+'/songs', methods=['GET'])
def REST_get_songs():
    payload=request.json
    feeling=payload['feeling']
    result=db_interaction.get_songs_by_feeling(feeling)
    return jsonify(result)


@app.route(api_endopoint+'/is_song_liked', methods=['GET'])
def REST_song_liked():
    payload=request.json
    song=payload['song']
    username=payload['username']
    result=db_interaction.check_user_song_relation(song,username)
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0')