from copy import Error
import logging, json , requests
from flask import Flask, request, jsonify, Response
from werkzeug.exceptions import HTTPException

#helpers
from Functions.Checks.ValidateOrder import Validate
from Functions.Order import Order

from google.protobuf.json_format import MessageToJson
from client_wrapper import ServiceClient

import orders_pb2_grpc as orders_service
import orders_types_pb2 as orders_messages

app = Flask(__name__)
app.config['orders'] = ServiceClient(orders_service, 'OrdersStub', 'localhost', 50051)

@app.route("/",)
def Miau():
    
    return "Miau!"

@app.route("/order",methods=["post"])
def order():
    #Check method is Post
    if request.method == "POST":
        if request.is_json:
            logging.info("Its a Json")
            data = request.get_json() #get json from body request  
            result=Validate(data).validateOrder()#validate the schema at dict 
            billingDate= Order().bDate #this check the next friday and add 21 days 
            message= f'Data checked, the date is: -> {str(billingDate)}'
            # Validate Data in Order
            if result: # True , data is correct , an then make a response 
                logging.info(message)
                datos=data.update({'billing_date':str(billingDate)})
                print(data)
                # requests.post(url=GRPC_SERVICE, data=data)
                return  jsonify(message=message,response=billingDate, status=200)  , 200
    message = "The structure of data is wrong"
    logging.info(message)
    return jsonify(message=message, status=400)  , 400

#this method return the date 
@app.route("/date",methods=["post"])
def date():
    try :
        result= Order()
        print(result.bDate)
        message= f'the date is: -> {str(result.bDate)}'
        return  jsonify(message=message,response= result.bDate, status=200)  , 200
    except Error as e:
        message= e
        logging.info(message)
        return  jsonify(message=message, status=400)  , 400


#this method Test Server
@app.route('/orderstest',methods=["post"])
def orders_get():
    request = orders_messages.GetOrdersRequest(
        user=[orders_messages.Order(name="alexa", quantity=1),
              orders_messages.Order(name="christie", quantity=1)]
    )
    def get_order():
        response = app.config['orders'].GetOrders(request)
        for resp in response:
            yield MessageToJson(resp)
    return Response(get_order(), content_type='application/json')


#this handle all exception on API  
@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response
        
if __name__ == '__main__':
    app.run(debug=False , port=5000 , host='0.0.0.0')