from tamarco.codecs.json import JsonCodec
from tamarco.core.microservice import Microservice
from tamarco.resources.io.http.resource import HTTPServerResource
from tamarco_amqp.output import AMQPOutput
from tamarco_amqp.resource import AMQPResource
from sanic.response import text


class StringApi(Microservice):
    name = "string_api"

    amqp = AMQPResource(
        outputs=[AMQPOutput(queue='upper_operator', codec=JsonCodec)]
        )
    string_api_http_server = HTTPServerResource()


microservice = StringApi()

@microservice.string_api_http_server.app.route("/upper", methods={'POST'})
async def upper_endpoint(request):
    upper_operator_output = microservice.amqp.outputs.get('upper_operator')
    response = await upper_operator_output.request(request.body)
    return text(response)

microservice.run()
