#!/usr/bin/env python
import sys
import pika

if __name__ == "__main__":

    queue = input("Queue (android):") or "android"
    if queue not in ["android", "ios"]:
        raise Exception("Queue must be android or ios")

    message = input("Message:")
    if not message:
        raise Exception("Message is required")

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue=queue, durable=True)

    channel.basic_publish(
        exchange='',
        routing_key=queue,
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=2,  # make message persistent
        )
    )
    print(" [x] Sent %s" % (message, ))

    connection.close()
