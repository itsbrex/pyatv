# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: pyatv/protocols/mrp/protobuf/ClientUpdatesConfigMessage.proto
# Protobuf Python Version: 6.31.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    31,
    1,
    '',
    'pyatv/protocols/mrp/protobuf/ClientUpdatesConfigMessage.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyatv.protocols.mrp.protobuf import ProtocolMessage_pb2 as pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=pyatv/protocols/mrp/protobuf/ClientUpdatesConfigMessage.proto\x1a\x32pyatv/protocols/mrp/protobuf/ProtocolMessage.proto\"\x9c\x01\n\x1a\x43lientUpdatesConfigMessage\x12\x16\n\x0e\x61rtworkUpdates\x18\x01 \x01(\x08\x12\x19\n\x11nowPlayingUpdates\x18\x02 \x01(\x08\x12\x15\n\rvolumeUpdates\x18\x03 \x01(\x08\x12\x17\n\x0fkeyboardUpdates\x18\x04 \x01(\x08\x12\x1b\n\x13outputDeviceUpdates\x18\x05 \x01(\x08:Q\n\x1a\x63lientUpdatesConfigMessage\x12\x10.ProtocolMessage\x18\x15 \x01(\x0b\x32\x1b.ClientUpdatesConfigMessage')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pyatv.protocols.mrp.protobuf.ClientUpdatesConfigMessage_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CLIENTUPDATESCONFIGMESSAGE']._serialized_start=118
  _globals['_CLIENTUPDATESCONFIGMESSAGE']._serialized_end=274
# @@protoc_insertion_point(module_scope)
