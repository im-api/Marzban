# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/net/network.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x63ommon/net/network.proto\x12\x0fxray.common.net\"8\n\x0bNetworkList\x12)\n\x07network\x18\x01 \x03(\x0e\x32\x18.xray.common.net.Network*B\n\x07Network\x12\x0b\n\x07Unknown\x10\x00\x12\x0e\n\x06RawTCP\x10\x01\x1a\x02\x08\x01\x12\x07\n\x03TCP\x10\x02\x12\x07\n\x03UDP\x10\x03\x12\x08\n\x04UNIX\x10\x04\x42O\n\x13\x63om.xray.common.netP\x01Z$github.com/xtls/xray-core/common/net\xaa\x02\x0fXray.Common.Netb\x06proto3')

_NETWORK = DESCRIPTOR.enum_types_by_name['Network']
Network = enum_type_wrapper.EnumTypeWrapper(_NETWORK)
Unknown = 0
RawTCP = 1
TCP = 2
UDP = 3
UNIX = 4


_NETWORKLIST = DESCRIPTOR.message_types_by_name['NetworkList']
NetworkList = _reflection.GeneratedProtocolMessageType('NetworkList', (_message.Message,), {
  'DESCRIPTOR' : _NETWORKLIST,
  '__module__' : 'common.net.network_pb2'
  # @@protoc_insertion_point(class_scope:xray.common.net.NetworkList)
  })
_sym_db.RegisterMessage(NetworkList)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023com.xray.common.netP\001Z$github.com/xtls/xray-core/common/net\252\002\017Xray.Common.Net'
  _NETWORK.values_by_name["RawTCP"]._options = None
  _NETWORK.values_by_name["RawTCP"]._serialized_options = b'\010\001'
  _NETWORK._serialized_start=103
  _NETWORK._serialized_end=169
  _NETWORKLIST._serialized_start=45
  _NETWORKLIST._serialized_end=101
# @@protoc_insertion_point(module_scope)
