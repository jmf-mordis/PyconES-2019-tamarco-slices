from tamarco.core.microservice import Microservice


class MyAdmin(Microservice):

    async def pre_start(self):
        await super().pre_start()
        self.default_user = await self.settings.get(
            '/system/microservices/my_admin/default_user')
        self.default_password = await self.settings.get(
            '/system/microservices/my_admin/default_password')
        self.session_expiration_days = await self.settings.get(
            '/system/microservices/my_admin/session_expiration_days')
