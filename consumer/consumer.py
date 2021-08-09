#!/usr/bin/env python
import threading
import pika
import ast
import time


class ConsumeManager:
    def __init__(self, queue_name):
        # Initial setting for RabbitMQ
        pika_params = pika.ConnectionParameters(
            host='rabbitmq',
            connection_attempts=10,
            heartbeat=0
            )

        # Creating connection
        self.pika_conn = pika.BlockingConnection(pika_params)
        self.channel = self.pika_conn.channel()
        self.channel.queue_declare(
            queue=queue_name,
            auto_delete=False,
            durable=True
        )


class Consumer(ConsumeManager):
    def __init__(self, queue_name):
        ConsumeManager.__init__(self, queue_name)
        self.queue_name = queue_name
        self.channel.basic_qos(prefetch_count=1)

    def execute(self):
        try:
            self.channel.basic_consume(
                queue=self.queue_name,
                on_message_callback=self.callback,
                auto_ack=True
            )
            self.channel.start_consuming()
        except Exception as e:
            print(e)

    def callback(self, ch, method, properties, body):
        try:
            body = body.decode("UTF-8")
            body = ast.literal_eval(body)
            print(f'queue_name: {self.queue_name}, body: {body}')
            # time.sleep(3)
            """
            start ML task here.
            """

            # test
            # raise Exception('raise Exception')

        except Exception as e:
            print(e)


THREADS = 10

if __name__ == '__main__':

    threads = []
    for thread in range(THREADS):
        print(f"\n[CREATE]: threading of task1-{thread}.")
        receiver = Consumer(queue_name='task1')
        t1 = threading.Thread(target=receiver.execute)
        t1.daemon = True
        threads.append(t1)
        t1.start()

        print(f"\n[CREATE]: threading of task2-{thread}.")
        receiver = Consumer(queue_name='task2')
        t2 = threading.Thread(target=receiver.execute)
        t2.daemon = True
        threads.append(t2)
        t2.start()

    for t in threads:
        t.join()

