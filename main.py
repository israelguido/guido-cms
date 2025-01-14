from app import create_app

app = create_app()
app.config["SECRET_KEY"] = "guido-cms-secret"
app.config["DEBUG"] = False

@app.after_request
def remove_server_header(response):
    response.headers['Server'] = "Guido Server"
    if 'X-Powered-By' in response.headers:
        del response.headers['X-Powered-By']
    return response

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)
