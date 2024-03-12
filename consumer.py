import json
import pandas as pd
from kafka import KafkaConsumer


class Consumer:

    def connect_kafka_consumer(self):
        try:
            self.consumer = KafkaConsumer(
                "test-topic1",  # topic name 
                bootstrap_servers="localhost:29092",  # kafka broker ip address
                auto_offset_reset="latest",  # get message from the earliest
                enable_auto_commit=True,
                group_id="test_group",  # consumer group identifier
            )
            return self.consumer
        except Exception as e:
            print(e)

    def check_message(self):
        for message in self.consumer:
            # print(message.value)  # check the message
            message = message.value.decode("utf-8")
            mess_json = json.loads(message)
            df = pd.DataFrame.from_dict(mess_json)
            print(df)


if __name__ == "__main__":
    consumer = Consumer()
    consumer.connect_kafka_consumer()
    consumer.check_message()
