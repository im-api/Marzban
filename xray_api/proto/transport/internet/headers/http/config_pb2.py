# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transport/internet/headers/http/config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,transport/internet/headers/http/config.proto\x12$xray.transport.internet.headers.http\"%\n\x06Header\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x03(\t\"\x18\n\x07Version\x12\r\n\x05value\x18\x01 \x01(\t\"\x17\n\x06Method\x12\r\n\x05value\x18\x01 \x01(\t\"\xd8\x01\n\rRequestConfig\x12>\n\x07version\x18\x01 \x01(\x0b\x32-.xray.transport.internet.headers.http.Version\x12<\n\x06method\x18\x02 \x01(\x0b\x32,.xray.transport.internet.headers.http.Method\x12\x0b\n\x03uri\x18\x03 \x03(\t\x12<\n\x06header\x18\x04 \x03(\x0b\x32,.xray.transport.internet.headers.http.Header\"&\n\x06Status\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x0e\n\x06reason\x18\x02 \x01(\t\"\xcc\x01\n\x0eResponseConfig\x12>\n\x07version\x18\x01 \x01(\x0b\x32-.xray.transport.internet.headers.http.Version\x12<\n\x06status\x18\x02 \x01(\x0b\x32,.xray.transport.internet.headers.http.Status\x12<\n\x06header\x18\x03 \x03(\x0b\x32,.xray.transport.internet.headers.http.Header\"\x96\x01\n\x06\x43onfig\x12\x44\n\x07request\x18\x01 \x01(\x0b\x32\x33.xray.transport.internet.headers.http.RequestConfig\x12\x46\n\x08response\x18\x02 \x01(\x0b\x32\x34.xray.transport.internet.headers.http.ResponseConfigB\x8e\x01\n(com.xray.transport.internet.headers.httpP\x01Z9github.com/xtls/xray-core/transport/internet/headers/http\xaa\x02$Xray.Transport.Internet.Headers.Httpb\x06proto3')



_HEADER = DESCRIPTOR.message_types_by_name['Header']
_VERSION = DESCRIPTOR.message_types_by_name['Version']
_METHOD = DESCRIPTOR.message_types_by_name['Method']
_REQUESTCONFIG = DESCRIPTOR.message_types_by_name['RequestConfig']
_STATUS = DESCRIPTOR.message_types_by_name['Status']
_RESPONSECONFIG = DESCRIPTOR.message_types_by_name['ResponseConfig']
_CONFIG = DESCRIPTOR.message_types_by_name['Config']
Header = _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), {
  'DESCRIPTOR' : _HEADER,
  '__module__' : 'transport.internet.headers.http.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.transport.internet.headers.http.Header)
  })
_sym_db.RegisterMessage(Header)

Version = _reflection.GeneratedProtocolMessageType('Version', (_message.Message,), {
  'DESCRIPTOR' : _VERSION,
  '__module__' : 'transport.internet.headers.http.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.transport.internet.headers.http.Version)
  })
_sym_db.RegisterMessage(Version)

Method = _reflection.GeneratedProtocolMessageType('Method', (_message.Message,), {
  'DESCRIPTOR' : _METHOD,
  '__module__' : 'transport.internet.headers.http.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.transport.internet.headers.http.Method)
  })
_sym_db.RegisterMessage(Method)

RequestConfig = _reflection.GeneratedProtocolMessageType('RequestConfig', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTCONFIG,
  '__module__' : 'transport.internet.headers.http.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.transport.internet.headers.http.RequestConfig)
  })
_sym_db.RegisterMessage(RequestConfig)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {
  'DESCRIPTOR' : _STATUS,
  '__module__' : 'transport.internet.headers.http.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.transport.internet.headers.http.Status)
  })
_sym_db.RegisterMessage(Status)

ResponseConfig = _reflection.GeneratedProtocolMessageType('ResponseConfig', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSECONFIG,
  '__module__' : 'transport.internet.headers.http.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.transport.internet.headers.http.ResponseConfig)
  })
_sym_db.RegisterMessage(ResponseConfig)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'transport.internet.headers.http.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.transport.internet.headers.http.Config)
  })
_sym_db.RegisterMessage(Config)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n(com.xray.transport.internet.headers.httpP\001Z9github.com/xtls/xray-core/transport/internet/headers/http\252\002$Xray.Transport.Internet.Headers.Http'
  _HEADER._serialized_start=86
  _HEADER._serialized_end=123
  _VERSION._serialized_start=125
  _VERSION._serialized_end=149
  _METHOD._serialized_start=151
  _METHOD._serialized_end=174
  _REQUESTCONFIG._serialized_start=177
  _REQUESTCONFIG._serialized_end=393
  _STATUS._serialized_start=395
  _STATUS._serialized_end=433
  _RESPONSECONFIG._serialized_start=436
  _RESPONSECONFIG._serialized_end=640
  _CONFIG._serialized_start=643
  _CONFIG._serialized_end=793
# @@protoc_insertion_point(module_scope)
