# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/protocol/user.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from xray_api.proto.common.serial import typed_message_pb2 as common_dot_serial_dot_typed__message__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x63ommon/protocol/user.proto\x12\x14xray.common.protocol\x1a!common/serial/typed_message.proto\"W\n\x04User\x12\r\n\x05level\x18\x01 \x01(\r\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x31\n\x07\x61\x63\x63ount\x18\x03 \x01(\x0b\x32 .xray.common.serial.TypedMessageB^\n\x18\x63om.xray.common.protocolP\x01Z)github.com/xtls/xray-core/common/protocol\xaa\x02\x14Xray.Common.Protocolb\x06proto3')



_USER = DESCRIPTOR.message_types_by_name['User']
User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'common.protocol.user_pb2'
  # @@protoc_insertion_point(class_scope:xray.common.protocol.User)
  })
_sym_db.RegisterMessage(User)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030com.xray.common.protocolP\001Z)github.com/xtls/xray-core/common/protocol\252\002\024Xray.Common.Protocol'
  _USER._serialized_start=87
  _USER._serialized_end=174
# @@protoc_insertion_point(module_scope)
