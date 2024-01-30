from flask import Flask, request, jsonify

app = Flask(__name__)
data = []


@app.route('/api/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        req_data = request.json
        data.append(req_data)
        return jsonify(status="Success")


@app.route('/api/download/<int:index>', methods=['GET'])
def download(index):
    if request.method == 'GET':
        return jsonify(data[index])


if __name__ == '__main__':
    app.run(debug=True, port=5000)
