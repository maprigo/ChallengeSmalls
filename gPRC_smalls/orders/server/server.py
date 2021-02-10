from concurrent import futures
import time
import logging

import grpc

import orders_pb2_grpc as orders_service
import orders_types_pb2 as orders_messages

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class OrdersService(orders_service.OrdersServicer):

    def CreateOrder(self, request, context):
        metadata = dict(context.invocation_metadata())
        logging.info(metadata)
        order = orders_messages.Order(name=request.name, quantity=1)
        return orders_messages.CreateOrderResult(order=order)

    def GetOrders(self, request, context):
        for order in request.order:
            order = orders_messages.Order(
                name=order.name, quantity=order.quantity
            )
            yield orders_messages.GetOrdersResult(order=order)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    orders_service.add_OrdersServicer_to_server(OrdersService(), server)
    server.add_insecure_port('127.0.0.1:50051')
    logging.info("Server Start")
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
