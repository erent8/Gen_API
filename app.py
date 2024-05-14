from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

NCBI_GENE_API_URL = "API_KEY/{organism}/{symbol}"

@app.route('/')
def home():
    return "Gen Bilgi Uygulamasına Hoş Geldiniz!"

@app.route('/gene', methods=['GET'])
def get_gene_info():
    organism = request.args.get('organism', 'human')  # Varsayılan organizma 'human'
    symbol = request.args.get('symbol')
    
    if not symbol:
        return jsonify({"error": "Lütfen bir gen adı veya ID'si girin."}), 400
    
    url = NCBI_GENE_API_URL.format(organism=organism, symbol=symbol)
    response = requests.get(url)
    
    if response.status_code != 200:
        return jsonify({"error": "Gen bilgisi bulunamadı."}), 404
    
    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
