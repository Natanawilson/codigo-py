from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular_media', methods=['POST'])
def calcular_media():
    quantidade_compras = int(request.form['quantidadeCompras'])

    total_media = 0
    total_acoes = 0

    for i in range(1, quantidade_compras + 1):
        qtd_acao = float(request.form[f'quantidade{i}'])
        preco_acao = float(request.form[f'preco{i}'])
        total_media += qtd_acao * preco_acao
        total_acoes += qtd_acao

    media_ponderada = total_media / total_acoes

    return render_template('resultado.html', media=media_ponderada)

if __name__ == '__main__':
    app.run(debug=True)