# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app/log/config.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from xray_api.proto.common.log import log_pb2 as common_dot_log_dot_log__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x61pp/log/config.proto\x12\x0cxray.app.log\x1a\x14\x63ommon/log/log.proto\"\xe4\x01\n\x06\x43onfig\x12-\n\x0e\x65rror_log_type\x18\x01 \x01(\x0e\x32\x15.xray.app.log.LogType\x12\x32\n\x0f\x65rror_log_level\x18\x02 \x01(\x0e\x32\x19.xray.common.log.Severity\x12\x16\n\x0e\x65rror_log_path\x18\x03 \x01(\t\x12.\n\x0f\x61\x63\x63\x65ss_log_type\x18\x04 \x01(\x0e\x32\x15.xray.app.log.LogType\x12\x17\n\x0f\x61\x63\x63\x65ss_log_path\x18\x05 \x01(\t\x12\x16\n\x0e\x65nable_dns_log\x18\x06 \x01(\x08*5\n\x07LogType\x12\x08\n\x04None\x10\x00\x12\x0b\n\x07\x43onsole\x10\x01\x12\x08\n\x04\x46ile\x10\x02\x12\t\n\x05\x45vent\x10\x03\x42\x46\n\x10\x63om.xray.app.logP\x01Z!github.com/xtls/xray-core/app/log\xaa\x02\x0cXray.App.Logb\x06proto3')

_LOGTYPE = DESCRIPTOR.enum_types_by_name['LogType']
LogType = enum_type_wrapper.EnumTypeWrapper(_LOGTYPE)
globals()['None'] = 0
Console = 1
File = 2
Event = 3


_CONFIG = DESCRIPTOR.message_types_by_name['Config']
Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'app.log.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.app.log.Config)
  })
_sym_db.RegisterMessage(Config)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\020com.xray.app.logP\001Z!github.com/xtls/xray-core/app/log\252\002\014Xray.App.Log'
  _LOGTYPE._serialized_start=291
  _LOGTYPE._serialized_end=344
  _CONFIG._serialized_start=61
  _CONFIG._serialized_end=289
# @@protoc_insertion_point(module_scope)
