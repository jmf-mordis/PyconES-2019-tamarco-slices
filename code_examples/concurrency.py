import asyncio
import time

from tamarco.core.microservice import (Microservice, 
    MicroserviceContext, task, task_timer, thread)


class ConcurrencyExampleMicroservice(Microservice):

    @task
    async def task_example(self):
        while True:
            self.logger.info("task example, beep")
            await asyncio.sleep(1)

    @task_timer(interval=1000, autostart=True)
    async def task_timer_example(self):
        self.logger.info("task timer example, beeep")
    
    @thread
    def thread_example(self):
        while True:
            self.logger.info("thread example, beeep")
            time.sleep(1)


def main():
    ms = ConcurrencyExampleMicroservice()
    ms.run()


if __name__ == "__main__":
    main()
