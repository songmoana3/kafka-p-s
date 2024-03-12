# Kafka R&D for P/S


## _Structure_
```
.
├── README.md
├── consumer.py
├── docker-compose.yml
├── producer.py
└── producer_async.py
```
## _How to Execute_

1. Start kafka with Docker  
`$docker compose up -d`

2. Start producer  
`$python3 producer.py`
+ If you want to test async kafka, then `$python3 producer_async.py`

3. Start consumer  
`$python3 consumer.py`

