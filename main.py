from app import create_app

app = create_app()
app.config["SECRET_KEY"] = "guido-cms-secret"
app.config["DEBUG"] = True

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
