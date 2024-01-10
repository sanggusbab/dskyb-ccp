from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route('/api/send-string', methods=['POST'])
def send_string():
    try:
        data = request.get_json()
        input_text = data.get('text', '')

        # 문자열을 대문자로 변환
        response = input_text.upper()

        return jsonify({'response': 'Order sent and processed'})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)

