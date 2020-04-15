from crypto.managers import TwitterManager, GoogleManager



class RouteFactory:
    def get_route(self, input_data: dict, crypto_currency_name: str):
        if crypto_currency_name == "BTC":
            return GoogleManager()
        else:
            raise ValueError(crypto_currency_name)


route_factory = RouteFactory()
