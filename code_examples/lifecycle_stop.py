from tamarco import Microservice


class LifecycleMicroservice(Microservice):

    async def stop(self):
        print("Before stop of the service")
        await super().stop()
        print("After stop of the service")

    async def post_stop(self):
        print("Before post stop of the service")
        await super().post_stop()
        print("After post stop of the service")


def main():
    microservice = LifecycleMicroservice()
    microservice.run()


def __name__ == '__main__':
    main()
