from tamarco import Microservice


class LifecycleMicroservice(Microservice):

    async def pre_start(self):
        print("Before pre_start of the service")
        await super().pre_start()
        print("After pre_start of the service")

    async def start(self):
        print("Before start of the service")
        await super().start()
        print("After start of the service")

    async def post_start(self):
        print("Before post_start of the service")
        await super().post_start()
        print("After post_start of the service")


def main():
    microservice = LifecycleMicroservice(Microservice)
    microservice.run()


def __name__ == '__main__':
    main()
