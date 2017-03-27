import abc

from flask import Flask, request, jsonify


class Predictor:
    def __init__(self, name, host, port, route):
        self.app = Flask(__name__)
        self.host = host
        self.port = port
        self.route = route

        @self.app.route('/')
        def welcome():
            route_link = "http://" + self.host + ":" + str(self.port) + "/" + self.route

            return "<h1> This is " + name + " API </h1>\n<p> Route define : " \
                                            "<a href={}>here</a> </p>".format(route_link)

        self.define_root(self.route)

    def define_root(self, root_name):
        """
        Define route where the predictors can be called

        :param root_name: String name of the route
        :return:
        """
        s_route = "/{}".format(root_name)

        @self.app.route(s_route, methods=["POST"])
        def function_route():
            if request.method == 'POST':
                return jsonify(self.predict(request.get_json()))
            return request.method

    def launch(self):
        self.app.run(self.host, port=self.port)

    @abc.abstractmethod
    def predict(self, data):
        """
        This is the method called when the predictor API is required by the client
        :param data: JSON like python dictonnary used to create dataframe to predict
        :return:
        """
        return "Need to be impletemented"


if __name__ == "__main__":
    pred = Predictor("test", "localhost", 1234, "test")
    pred.launch()
