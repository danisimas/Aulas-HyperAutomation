from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('form_produto.html')

# Rota para salvar os dados do produto
@app.route('/salvar', methods=['POST'])
def salvar_produto():
    nome = request.form['nome']
    preco = request.form['preco']
    quantidade = request.form['quantidade']
    
    # Salvar em um arquivo
    with open('produtos.txt', 'a') as f:
        f.write(f"Nome: {nome}, Preço: {preco}, Quantidade: {quantidade}\n")
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
