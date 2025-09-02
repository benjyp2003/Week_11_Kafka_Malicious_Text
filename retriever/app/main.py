from manager import Manager
from kafka_producer import Producer
import time
import sys


def wait_for_kafka():
    """Wait for Kafka to be ready before starting the application"""
    max_retries = 30
    retry_count = 0
    
    while retry_count < max_retries:
        try:
            print(f"Attempt {retry_count + 1}/{max_retries}: Trying to connect to Kafka...")
            producer = Producer()
            print("Successfully connected to Kafka!")
            return producer
        except Exception as e:
            print(f"Failed to connect to Kafka: {e}")
            retry_count += 1
            if retry_count < max_retries:
                print(f"Retrying in 5 seconds...")
                time.sleep(5)
            else:
                print("Max retries reached. Exiting...")
                sys.exit(1)


if __name__ == "__main__":
    print("Starting retriever service...")
    producer = wait_for_kafka()
    manager = Manager(producer)
    print("Starting message publishing...")
    manager.publish_messages()