# predictors_api
Basic Architecture to release sklearn models

## Installation

```
pip install git+https://github.com/rcourivaud/predictors_api.git
```

## Usage 

```
class MyPredictor(Predictor):
    self.port = 5000
    self.host = "localhost"
    self.route = "mypredictor"
    super().__init__(name=name, host=self.host, port=self.port, route=self.route) 
```

You need to override predict method. This method take in parameters data which is the json send by post method on route API. 

```
def predict(self, data):
    #do some stuff 
    return result
```

This method need to return JSON serializable object like Python list of dictionnary

## Run
```
if __name__ == "__main__":
    mpred = MyPredictor()
    mpred.launch()
```

The predictor start to listen on precised host and port. You just need to send POST with your JSON data body.
