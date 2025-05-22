from flask import Flask, request, jsonify
import pika
from db import SessionLocal, User, init_db

app = Flask(__name__)
init_db()

def send_to_queue(message: str):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="rabbitmq")
    )
    channel = connection.channel()
    channel.queue_declare(queue="email_queue", durable=True)
    channel.basic_publish(
        exchange='',
        routing_key='email_queue',
        body=message,
        properties=pika.BasicProperties(delivery_mode=2)  # torna a mensagem persistente
    )
    connection.close()

@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    if not name or not email:
        return jsonify({"error": "Name and email are required"}), 400

    session = SessionLocal()
    # Verifica se usuário já existe
    user = session.query(User).filter(User.email == email).first()
    if user:
        session.close()
        return jsonify({"error": "Email already registered"}), 400

    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    session.close()

    # Envia mensagem para fila (pode ser json simples)
    import json
    message = json.dumps({"name": name, "email": email})
    send_to_queue(message)

    return jsonify({"message": f"User {name} registered and queued for email."}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
