from django.shortcuts import render, redirect
from django.views import View
from .forms import DefaultForm
from kafka import KafkaProducer
import time
import random
from pykafka import KafkaClient
#from .kafkaclient import KafkaClient




class DefaultView(View):
    def __init__(self):
        super(DefaultView, self)
    
    def get_kafka_client(self):
        return KafkaClient(hosts="kafka:29092")

        #if hasattr(self.get_kafka_client, 'instance'):
        #    return get_kafka_client.instance
        #else:
        #    inst = get_kafka_client = KafkaClient()
        #    return inst

    def get(self, request):
        default_form = DefaultForm()
        context = {
            "form": default_form,
        }
        return render(request, "sqs/default.html", context)

    def post(self, request):
        import json
        # give broker IP from docker
        client = self.get_kafka_client()
        topic = client.topics["test"]

        default_form = DefaultForm(request.POST)

        if default_form.is_valid():
            default = default_form.save()
            message = '{} {}'.format(default.first_number, default.second_number)
            print("post action")
            with topic.get_producer() as producer:
                print("got producer")
                for i in range(4):
                    print("sending data")
                    msg={'id': i, 'first_number': default.first_number, 'second_number':default.second_number}
                    proto = json.dumps(msg)
                    msg=str.encode(proto)
                    producer.produce(msg)

            return redirect('default')

        