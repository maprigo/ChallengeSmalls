# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: orders.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import orders_types_pb2 as orders__types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='orders.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0corders.proto\x1a\x12orders_types.proto2\x90\x01\n\x06Orders\x12\x44\n\x0b\x43reateOrder\x12\x1a.orders.CreateOrderRequest\x1a\x19.orders.CreateOrderResult\x12@\n\tGetOrders\x12\x18.orders.GetOrdersRequest\x1a\x17.orders.GetOrdersResult0\x01\x62\x06proto3'
  ,
  dependencies=[orders__types__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_ORDERS = _descriptor.ServiceDescriptor(
  name='Orders',
  full_name='Orders',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=37,
  serialized_end=181,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateOrder',
    full_name='Orders.CreateOrder',
    index=0,
    containing_service=None,
    input_type=orders__types__pb2._CREATEORDERREQUEST,
    output_type=orders__types__pb2._CREATEORDERRESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetOrders',
    full_name='Orders.GetOrders',
    index=1,
    containing_service=None,
    input_type=orders__types__pb2._GETORDERSREQUEST,
    output_type=orders__types__pb2._GETORDERSRESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ORDERS)

DESCRIPTOR.services_by_name['Orders'] = _ORDERS

# @@protoc_insertion_point(module_scope)