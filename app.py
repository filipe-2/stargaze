from app import app

if __name__ == '__main__': # Executar a aplicação Flask
    app.run(host='127.0.0.1', debug=True, port=5000)