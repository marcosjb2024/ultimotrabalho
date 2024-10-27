from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite requisições de outros domínios

# Lista de doces importados
doces_importados = [
    {"id": 1, "nome": "Chocolate Suíço", "preco": 15.00},
    {"id": 2, "nome": "Gomas de Ursinho Alemãs", "preco": 12.50},
    {"id": 3, "nome": "Bala de Coco Brasileira", "preco": 8.00},
    {"id": 4, "nome": "Biscoito de Baunilha Francês", "preco": 20.00},
    {"id": 5, "nome": "Caramelos de Menta Canadenses", "preco": 10.00},
]

@app.route('/doces', methods=['GET'])
def get_doces():
    return jsonify(doces_importados)

if __name__ == '__main__':
    app.run(debug=True)

