import logging
import time
from os import getenv

import click
import zmq
from tenacity import retry

logging.basicConfig(
    format="%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)


@click.group()
def cli():
    pass


@cli.command(help="Run Application in Server Mode")
def server() -> None:
    logging.info("Starting Server...")
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    while True:
        message = socket.recv()
        logging.info(f"Recieved Message {message}")
        time.sleep(0.1)
        socket.send(b"World")


@cli.command(help="Run Application in Client Mode")
@retry
def client() -> None:
    logging.info("Starting Client...")
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect(f"tcp://{getenv('SERVER_ADDRESS', '127.0.0.1')}:5555")
    socket.setsockopt(zmq.RCVTIMEO, 1000)
    count = 0

    while True:
        count += 1
        logging.info(f"Sending request: #{count}")
        socket.send(b"Hello")
        message = socket.recv()
        logging.info(f"Recieved Reply: {message}")


if __name__ == "__main__":
    cli()
