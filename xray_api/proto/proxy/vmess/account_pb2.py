# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proxy/vmess/account.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from xray_api.proto.common.protocol import headers_pb2 as common_dot_protocol_dot_headers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19proxy/vmess/account.proto\x12\x10xray.proxy.vmess\x1a\x1d\x63ommon/protocol/headers.proto\"m\n\x07\x41\x63\x63ount\x12\n\n\x02id\x18\x01 \x01(\t\x12?\n\x11security_settings\x18\x03 \x01(\x0b\x32$.xray.common.protocol.SecurityConfig\x12\x15\n\rtests_enabled\x18\x04 \x01(\tBR\n\x14\x63om.xray.proxy.vmessP\x01Z%github.com/xtls/xray-core/proxy/vmess\xaa\x02\x10Xray.Proxy.Vmessb\x06proto3')



_ACCOUNT = DESCRIPTOR.message_types_by_name['Account']
Account = _reflection.GeneratedProtocolMessageType('Account', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNT,
  '__module__' : 'proxy.vmess.account_pb2'
  # @@protoc_insertion_point(class_scope:xray.proxy.vmess.Account)
  })
_sym_db.RegisterMessage(Account)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024com.xray.proxy.vmessP\001Z%github.com/xtls/xray-core/proxy/vmess\252\002\020Xray.Proxy.Vmess'
  _ACCOUNT._serialized_start=78
  _ACCOUNT._serialized_end=187
# @@protoc_insertion_point(module_scope)
