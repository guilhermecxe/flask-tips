from flask import Flask, render_template, jsonify, request, flash
from forms import Form

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'

# A lista de itens retornados será estática
items = [
        {'id': 1, 'text': 'laranja'},
        {'id': 2, 'text': 'banana'},
        {'id': 3, 'text': 'maça'},
        {'id': 4, 'text': 'melância'},
        {'id': 5, 'text': 'uva'},
    ]

@app.route('/', methods=['GET', 'POST'])
def index():
    form = Form()
    if form.validate_on_submit():
        id = int(form.select.data)
        item = [item for item in items if item['id'] == id][0]
        flash(f"The selected option was {item['text']} with id: {id}")
    return render_template('index.html', form=form)

# Essa é a rota para onde a requisição assíncrona é enviada
@app.route('/search')
def search():
    query = request.args.get('q') # na verdade, não faço nada com a query obtida
    return jsonify(items)

if __name__ == '__main__':
    app.run(debug=True)