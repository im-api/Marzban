# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app/stats/config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x61pp/stats/config.proto\x12\x0exray.app.stats\"\x08\n\x06\x43onfig\"N\n\rChannelConfig\x12\x10\n\x08\x42locking\x18\x01 \x01(\x08\x12\x17\n\x0fSubscriberLimit\x18\x02 \x01(\x05\x12\x12\n\nBufferSize\x18\x03 \x01(\x05\x42L\n\x12\x63om.xray.app.statsP\x01Z#github.com/xtls/xray-core/app/stats\xaa\x02\x0eXray.App.Statsb\x06proto3')



_CONFIG = DESCRIPTOR.message_types_by_name['Config']
_CHANNELCONFIG = DESCRIPTOR.message_types_by_name['ChannelConfig']
Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'app.stats.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.app.stats.Config)
  })
_sym_db.RegisterMessage(Config)

ChannelConfig = _reflection.GeneratedProtocolMessageType('ChannelConfig', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELCONFIG,
  '__module__' : 'app.stats.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.app.stats.ChannelConfig)
  })
_sym_db.RegisterMessage(ChannelConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\022com.xray.app.statsP\001Z#github.com/xtls/xray-core/app/stats\252\002\016Xray.App.Stats'
  _CONFIG._serialized_start=42
  _CONFIG._serialized_end=50
  _CHANNELCONFIG._serialized_start=52
  _CHANNELCONFIG._serialized_end=130
# @@protoc_insertion_point(module_scope)
