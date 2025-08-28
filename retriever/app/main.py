from manager import Manager
from kafka_producer import Producer


if __name__ == "__main__":
    producer = Producer()
    manager = Manager(producer)
    manager.publish_messages()