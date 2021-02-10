import sys

import grpc

import orders_pb2_grpc as orders_service
import orders_types_pb2 as orders_messages


def run():
    channel = grpc.insecure_channel('localhost:50051')
    try:
        grpc.channel_ready_future(channel).result(timeout=10)
    except grpc.FutureTimeoutError:
        sys.exit('Error connecting to server')
    else:
        stub = orders_service.OrdersStub(channel)
        metadata = [('ip', '127.0.0.1')]
        response = stub.DeleteOrder(
            orders_messages.DeleteOrderRequest(name='tom'),
            metadata=metadata,
        )
        if response:
            print("Order created:", response.order.name)
        request = orders_messages.GetOrdersRequest(
            order=[orders_messages.Order(name="alexa", quantity=1),
                  orders_messages.Order(name="christie", quantity=1)]
        )
        response = stub.GetOrders(request)
        for resp in response:
            print(resp)


if __name__ == '__main__':
        run()
