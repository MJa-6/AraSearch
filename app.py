from flask import Flask, render_template, url_for, request, jsonify
from adv_ara_sem_search import query_model

app = Flask(__name__, static_folder='static')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search')
def get_result () :
    keyword=request.args.get('word')
    return jsonify(query_model(keyword))


if __name__=="__main__":
    app.run(debug=True)