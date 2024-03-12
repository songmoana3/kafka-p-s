import time
import pandas as pd
from kafka import KafkaProducer


def publish_to_topic():
    
    try:
        # start = time.time()
        producer = KafkaProducer(
        bootstrap_servers="localhost:29092" # broker server와 연결
    )
        df = pd.read_csv("~/Downloads/test2.csv", index_col=0)
        data = df.to_json()
        
        # count = 0
        while True:
            [producer.send(topic=f"test-topic{i}", value=data.encode('utf-8')) for i in range(100)]
            # count += 1
            # print(count)
            time.sleep(0.01)
            
        # print(f"Elapsed time : {time.time() - start}s")

    except Exception as e:
        print(e)
        raise Exception
        
        
if __name__=="__main__":
    publish_to_topic()
