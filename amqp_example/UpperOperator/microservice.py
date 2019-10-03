import asyncio

from tamarco.codecs.json import JsonCodec
from tamarco.core.microservice import Microservice
from tamarco_amqp.input import AMQPRequestInput
from tamarco_amqp.output import AMQPOutput
from tamarco_amqp.resource import AMQPResource


class UpperOperator(Microservice):
    name = "UpperOperator"
    amqp = AMQPResource()

    @AMQPRequestInput(resource=amqp, queue='upper_operator', codec=JsonCodec)
    async def upper_handler(self, message, response_handler):
        self.logger.debug(f'Consumed message from upper_operator queue: {message}')
        response = message.upper()
        await response_handler.send_response(response)

microservice = UpperOperator()
microservice.run()
