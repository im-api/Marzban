# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transport/internet/websocket/config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)transport/internet/websocket/config.proto\x12!xray.transport.internet.websocket\"\xc5\x01\n\x06\x43onfig\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x45\n\x06header\x18\x03 \x03(\x0b\x32\x35.xray.transport.internet.websocket.Config.HeaderEntry\x12\x1d\n\x15\x61\x63\x63\x65pt_proxy_protocol\x18\x04 \x01(\x08\x12\n\n\x02\x65\x64\x18\x05 \x01(\r\x1a-\n\x0bHeaderEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x85\x01\n%com.xray.transport.internet.websocketP\x01Z6github.com/xtls/xray-core/transport/internet/websocket\xaa\x02!Xray.Transport.Internet.Websocketb\x06proto3')



_CONFIG = DESCRIPTOR.message_types_by_name['Config']
_CONFIG_HEADERENTRY = _CONFIG.nested_types_by_name['HeaderEntry']
Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {

  'HeaderEntry' : _reflection.GeneratedProtocolMessageType('HeaderEntry', (_message.Message,), {
    'DESCRIPTOR' : _CONFIG_HEADERENTRY,
    '__module__' : 'transport.internet.websocket.config_pb2'
    # @@protoc_insertion_point(class_scope:xray.transport.internet.websocket.Config.HeaderEntry)
    })
  ,
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'transport.internet.websocket.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.transport.internet.websocket.Config)
  })
_sym_db.RegisterMessage(Config)
_sym_db.RegisterMessage(Config.HeaderEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%com.xray.transport.internet.websocketP\001Z6github.com/xtls/xray-core/transport/internet/websocket\252\002!Xray.Transport.Internet.Websocket'
  _CONFIG_HEADERENTRY._options = None
  _CONFIG_HEADERENTRY._serialized_options = b'8\001'
  _CONFIG._serialized_start=81
  _CONFIG._serialized_end=278
  _CONFIG_HEADERENTRY._serialized_start=233
  _CONFIG_HEADERENTRY._serialized_end=278
# @@protoc_insertion_point(module_scope)
