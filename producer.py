#!/usr/bin/env python
import pika
import sys

if __name__ == "__main__":
    exchange = "logs"
    message = ' '.join(sys.argv[1:]) or "info: Hello World!"

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange=exchange, exchange_type='fanout')

    channel.basic_publish(exchange=exchange, routing_key='', body=message)
    print(" [x] Sent %r" % message)
    connection.close()
