from tamarco.codecs.json import JsonCodec
from tamarco.core.microservice import Microservice
from tamarco_amqp.input import AMQPRequestInput
from tamarco_amqp.resource import AMQPResource


class StringOperator(Microservice):
    name = "string_operator"
    amqp = AMQPResource()

    @AMQPRequestInput(resource=amqp, queue='upper_operator', codec=JsonCodec)
    async def upper_handler(self, message, response_handler):
        self.logger.debug(f'Consumed message from upper_operator queue: {message}')
        response = message.upper()
        self.logger.info(f'Upper operation done, sending response: {response}')
        await response_handler.send_response(response)

    @AMQPRequestInput(resource=amqp, queue='lower_operator', codec=JsonCodec)
    async def lower_handler(self, message, response_handler):
        self.logger.debug(f'Consumed message from lower_operator queue: {message}')
        response = message.lower()
        self.logger.info(f'Lower operation done, sending response: {response}')
        await response_handler.send_response(response)


microservice = StringOperator()
microservice.run()
