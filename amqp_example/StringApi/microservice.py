from tamarco.codecs.json import JsonCodec
from tamarco.core.microservice import Microservice
from tamarco.resources.io.http.resource import HTTPServerResource
from tamarco_amqp.output import AMQPOutput
from tamarco_amqp.resource import AMQPResource
from sanic.response import text


class StringApi(Microservice):
    name = "string_api"
    amqp = AMQPResource(
        outputs=[
            AMQPOutput(queue='upper_operator', codec=JsonCodec),
            AMQPOutput(queue='lower_operator', codec=JsonCodec)
        ]
    )
    string_api_http_server = HTTPServerResource()

    async def upper_handler(self, request):
        self.logger.info(f"Received request in upper endpoint: {request.body}")
        upper_operator_output = microservice.amqp.outputs.get('upper_operator')
        response = await upper_operator_output.request(request.body)
        self.logger.info(f"Sending response in upper endpoint {response}")
        return text(response)

    async def lower_handler(self, request):
        self.logger.info(f"Received request in lower endpoint: {request.body}")
        lower_operator_output = microservice.amqp.outputs.get('lower_operator')
        response = await lower_operator_output.request(request.body)
        self.logger.info(f"Sending response in lower endpoint {response}")
        return text(response)

    async def start(self):
        self.string_api_http_server.add_endpoint("/upper", self.upper_endpoint)
        self.string_api_http_server.add_endpoint("/lower", self.lower_endpoint)
        await super().start()


microservice = StringApi()
microservice.run()
