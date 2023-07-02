from pykafka import KafkaClient

class KafkaClient(object):
    instance = None
    client = None
    topic = None
    def __new__(cls):
        if cls.instance is not None:
            return cls.instance
        else:
            inst = cls.instance = super(KafkaClient, cls).__new__()
            return inst
    def __init__(self):
        self.client = KafkaClient(hosts="kafka:29092")
        self.topic = client.topics["test"]
        super(KafkaClient, self)
