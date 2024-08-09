# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proxy/socks/config.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from xray_api.proto.common.net import address_pb2 as common_dot_net_dot_address__pb2
from xray_api.proto.common.protocol import server_spec_pb2 as common_dot_protocol_dot_server__spec__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18proxy/socks/config.proto\x12\x10xray.proxy.socks\x1a\x18\x63ommon/net/address.proto\x1a!common/protocol/server_spec.proto\"-\n\x07\x41\x63\x63ount\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"\x9a\x02\n\x0cServerConfig\x12-\n\tauth_type\x18\x01 \x01(\x0e\x32\x1a.xray.proxy.socks.AuthType\x12>\n\x08\x61\x63\x63ounts\x18\x02 \x03(\x0b\x32,.xray.proxy.socks.ServerConfig.AccountsEntry\x12,\n\x07\x61\x64\x64ress\x18\x03 \x01(\x0b\x32\x1b.xray.common.net.IPOrDomain\x12\x13\n\x0budp_enabled\x18\x04 \x01(\x08\x12\x13\n\x07timeout\x18\x05 \x01(\rB\x02\x18\x01\x12\x12\n\nuser_level\x18\x06 \x01(\r\x1a/\n\rAccountsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"p\n\x0c\x43lientConfig\x12\x34\n\x06server\x18\x01 \x03(\x0b\x32$.xray.common.protocol.ServerEndpoint\x12*\n\x07version\x18\x02 \x01(\x0e\x32\x19.xray.proxy.socks.Version*%\n\x08\x41uthType\x12\x0b\n\x07NO_AUTH\x10\x00\x12\x0c\n\x08PASSWORD\x10\x01*.\n\x07Version\x12\n\n\x06SOCKS5\x10\x00\x12\n\n\x06SOCKS4\x10\x01\x12\x0b\n\x07SOCKS4A\x10\x02\x42R\n\x14\x63om.xray.proxy.socksP\x01Z%github.com/xtls/xray-core/proxy/socks\xaa\x02\x10Xray.Proxy.Socksb\x06proto3')

_AUTHTYPE = DESCRIPTOR.enum_types_by_name['AuthType']
AuthType = enum_type_wrapper.EnumTypeWrapper(_AUTHTYPE)
_VERSION = DESCRIPTOR.enum_types_by_name['Version']
Version = enum_type_wrapper.EnumTypeWrapper(_VERSION)
NO_AUTH = 0
PASSWORD = 1
SOCKS5 = 0
SOCKS4 = 1
SOCKS4A = 2


_ACCOUNT = DESCRIPTOR.message_types_by_name['Account']
_SERVERCONFIG = DESCRIPTOR.message_types_by_name['ServerConfig']
_SERVERCONFIG_ACCOUNTSENTRY = _SERVERCONFIG.nested_types_by_name['AccountsEntry']
_CLIENTCONFIG = DESCRIPTOR.message_types_by_name['ClientConfig']
Account = _reflection.GeneratedProtocolMessageType('Account', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNT,
  '__module__' : 'proxy.socks.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.proxy.socks.Account)
  })
_sym_db.RegisterMessage(Account)

ServerConfig = _reflection.GeneratedProtocolMessageType('ServerConfig', (_message.Message,), {

  'AccountsEntry' : _reflection.GeneratedProtocolMessageType('AccountsEntry', (_message.Message,), {
    'DESCRIPTOR' : _SERVERCONFIG_ACCOUNTSENTRY,
    '__module__' : 'proxy.socks.config_pb2'
    # @@protoc_insertion_point(class_scope:xray.proxy.socks.ServerConfig.AccountsEntry)
    })
  ,
  'DESCRIPTOR' : _SERVERCONFIG,
  '__module__' : 'proxy.socks.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.proxy.socks.ServerConfig)
  })
_sym_db.RegisterMessage(ServerConfig)
_sym_db.RegisterMessage(ServerConfig.AccountsEntry)

ClientConfig = _reflection.GeneratedProtocolMessageType('ClientConfig', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTCONFIG,
  '__module__' : 'proxy.socks.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.proxy.socks.ClientConfig)
  })
_sym_db.RegisterMessage(ClientConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024com.xray.proxy.socksP\001Z%github.com/xtls/xray-core/proxy/socks\252\002\020Xray.Proxy.Socks'
  _SERVERCONFIG_ACCOUNTSENTRY._options = None
  _SERVERCONFIG_ACCOUNTSENTRY._serialized_options = b'8\001'
  _SERVERCONFIG.fields_by_name['timeout']._options = None
  _SERVERCONFIG.fields_by_name['timeout']._serialized_options = b'\030\001'
  _AUTHTYPE._serialized_start=553
  _AUTHTYPE._serialized_end=590
  _VERSION._serialized_start=592
  _VERSION._serialized_end=638
  _ACCOUNT._serialized_start=107
  _ACCOUNT._serialized_end=152
  _SERVERCONFIG._serialized_start=155
  _SERVERCONFIG._serialized_end=437
  _SERVERCONFIG_ACCOUNTSENTRY._serialized_start=390
  _SERVERCONFIG_ACCOUNTSENTRY._serialized_end=437
  _CLIENTCONFIG._serialized_start=439
  _CLIENTCONFIG._serialized_end=551
# @@protoc_insertion_point(module_scope)
