# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/log/log.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x63ommon/log/log.proto\x12\x0fxray.common.log*D\n\x08Severity\x12\x0b\n\x07Unknown\x10\x00\x12\t\n\x05\x45rror\x10\x01\x12\x0b\n\x07Warning\x10\x02\x12\x08\n\x04Info\x10\x03\x12\t\n\x05\x44\x65\x62ug\x10\x04\x42O\n\x13\x63om.xray.common.logP\x01Z$github.com/xtls/xray-core/common/log\xaa\x02\x0fXray.Common.Logb\x06proto3')

_SEVERITY = DESCRIPTOR.enum_types_by_name['Severity']
Severity = enum_type_wrapper.EnumTypeWrapper(_SEVERITY)
Unknown = 0
Error = 1
Warning = 2
Info = 3
Debug = 4


if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023com.xray.common.logP\001Z$github.com/xtls/xray-core/common/log\252\002\017Xray.Common.Log'
  _SEVERITY._serialized_start=41
  _SEVERITY._serialized_end=109
# @@protoc_insertion_point(module_scope)
