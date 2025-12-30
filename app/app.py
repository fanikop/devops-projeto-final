import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    user = os.getenv('APP_USER', 'Visitante')
    secret_code = os.getenv('APP_SECRET', 'Sem Segredo')
    
    return f"Olá {user}! O segredo é: {secret_code} - Versão: v1"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)