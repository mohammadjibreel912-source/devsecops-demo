from flask import Flask, request, jsonify
import jwt
import datetime

app = Flask(__name__)

# ملاحظة أمنية: وضع المفاتيح السرية داخل الكود يعتبر خرق أمني سينكشف في فحص DevSecOps
SECRET_KEY = "my_super_secret_hardcoded_key_123"

# قاعدة بيانات مؤقتة في الذاكرة
users_db = {
    "admin": "password123"
}

@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "healthy", "message": "DevSecOps Demo API is running!"})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users_db and users_db[username] == password:
        # إنشاء Token للمستخدم
        token = jwt.encode({
            'user': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, SECRET_KEY, algorithm="HS256")
        
        return jsonify({"token": token}), 200

    return jsonify({"message": "Invalid credentials!"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)