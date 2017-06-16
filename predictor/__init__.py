import abc

from flask import Flask, request, jsonify
from flask_cors import CORS


class Predictor:
    def __init__(self, name, host, port, route, allow_origin=True):
        self.app = Flask(__name__)
        self.host = host
        self.port = port
        self.route = route

        if allow_origin:
            self.cors = CORS(self.app, resources={r"/*": {"origins": "*"}})

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
        s_route = "/{}/<q>".format(root_name)

        @self.app.route(s_route, methods=["POST", "GET"])
        def function_route(q):
            if request.method == 'POST':
                return jsonify(self.predict(request.get_json()))
            if request.method == 'GET':
                # q = "=".join(itertools.chain.from_iterable([[k, v] for k, v in request.args.to_dict().items()])) + "&" + q
                # dict_query = {elt[0]: elt[1] for elt in [elt.split("=") for elt in q.split("&")] if len(elt) > 1}
                return jsonify(self.predict(request.args.to_dict()))
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
        raise NotImplementedError("You need to override predict method")


if __name__ == "__main__":
    pred = Predictor("test", "localhost", 1234, "test")
    pred.predict = lambda x: x
    pred.launch()
