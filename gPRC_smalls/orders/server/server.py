import asyncio
from concurrent import futures
import time
import logging
from google.protobuf import empty_pb2
from gino import Gino

import grpc

''' I declare the path of the Protos in the execution '''
import orders_pb2_grpc as orders_service
import orders_types_pb2 as orders_messages


_ONE_DAY_IN_SECONDS = 60 * 60 * 24

''' Declare ORM  '''
db = Gino()

''' I create the structure of the table of the orders to demonstrate the interaction with an ORM
I clearly keep order by order and not the full payload, because I had to spend a lot of time understanding gPrc
and it seemed more logical to focus on that '''

class Order(db.Model):
    __tablename__ = 'Orders'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String)
    quantity = db.Column(db.Integer())


''' This is where we declare our service, we are going to have 3 functions which receive two parameters. '''
class OrdersService(orders_service.OrdersServicer):

    def CreateOrder(self, request, context):
        metadata = dict(context.invocation_metadata())
        logging.info(metadata)
        order = orders_messages.Order(name=request.name, quantity=1)
        # orders_messages.Order(name=request.name,quantity=request.quantity)
        new_order = Order.create(name=request.name,quantity=request.quantity)
        # only just by debug 
        print(metadata)
        return orders_messages.CreateOrderResult(order=order)
    
    def DeleteStudent(self,request , context):
        metadata = dict(context.invocation_metadata())
        logging.info(metadata)
        order = orders_messages.Order(name=request.name, quantity=1)
        order_name = request.name
        Order.delete.where(Order.name == order_name).gino.status()
        context.send_message(empty_pb2.Empty())
        return orders_messages.DeleteOrderResult(order=order)
        

    def GetOrders(self, request, context):
        for order in request.order:
            order = orders_messages.Order(
                name=order.name, quantity=order.quantity
            )
            yield orders_messages.GetOrdersResult(order=order)

''' I do it asynchronously, in order to wait for the connection to the DB '''
async def serve():
    ''' this I can be put on env variables '''
    await db.set_bind('postgresql://postgres:1234@localhost/main')
    await db.gino.create_all()
    ''' The grpc.Server function creates a server. We call it above with the only required argument,
    a futures.ThreadPoolExecutor with the maximum number of workers set to 10. 
    hen we call the add_UsersServicer_to_server function to register UsersService with the server. '''
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    orders_service.add_OrdersServicer_to_server(OrdersService(), server)
    ''' function is used since we are not setting SSL/TLS for our client/server  '''
    server.add_insecure_port('127.0.0.1:50051')
    logging.info("Server Start")
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    asyncio.run(serve())
