#!/usr/bin/env python
import pika
import sys

if __name__ == "__main__":
    exchange = "direct_logs"
    severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
    message = ' '.join(sys.argv[2:]) or "Hello World!"

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange=exchange, exchange_type='direct')

    channel.basic_publish(exchange=exchange, routing_key=severity, body=message)
    print(" [x] Sent %r:%r" % (severity, message))
    connection.close()
