import pika
import json
import time

def callback(ch, method, properties, body):
    data = json.loads(body)
    print(f"📧 Enviando email de boas-vindas para {data['email']}")

while True:
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
        channel = connection.channel()
        channel.queue_declare(queue='email_queue', durable=True)

        channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)

        print('🟢 Aguardando mensagens. Para sair, pressione CTRL+C')
        channel.start_consuming()
        break  # Se sair do start_consuming, interrompe o loop

    except pika.exceptions.AMQPConnectionError:
        print("⚠️ RabbitMQ não disponível ainda. Tentando novamente em 5 segundos...")
        time.sleep(5)
