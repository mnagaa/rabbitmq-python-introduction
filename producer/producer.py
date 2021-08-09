
import pika
import json


class Task:
    def __init__(self, queue_name):
        self.producer = Producer(queue_name)  # queue_name

    def send(self, params):
        message_json = json.dumps(params)
        self.producer.send_message(message=message_json)


class ProduceManager:
    def __init__(self, queue_name):
        pika_params = pika.ConnectionParameters(
            # host='localhost',
            host='rabbitmq',
            connection_attempts=10,
            heartbeat=0)
        self.pika_conn = pika.BlockingConnection(pika_params)
        self.channel = self.pika_conn.channel()


class Producer(ProduceManager):
    def __init__(self, queue_name):
        ProduceManager.__init__(self, queue_name)
        self.queue_name = queue_name

    def send_message(self, message):
        queue_name = self.queue_name
        self.channel.basic_publish(
            exchange='',
            routing_key=queue_name,
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=2,  # make message persistent
            )
        )

    def close_connection(self):
        self.pika_conn.close()


if __name__ == '__main__':

    # Create Queues
    task1 = Task(queue_name='task1')
    task2 = Task(queue_name='task2')

    # Sending messages
    iteration = 10_000
    for i in range(iteration):
        task1.send({'message': i})
        task2.send({'message': i})
