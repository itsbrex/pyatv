# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyatv/mrp/protobuf/NotificationMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyatv.mrp.protobuf import ProtocolMessage_pb2 as pyatv_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyatv/mrp/protobuf/NotificationMessage.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n,pyatv/mrp/protobuf/NotificationMessage.proto\x1a(pyatv/mrp/protobuf/ProtocolMessage.proto\"=\n\x13NotificationMessage\x12\x14\n\x0cnotification\x18\x01 \x03(\t\x12\x10\n\x08userInfo\x18\x02 \x03(\x0c:C\n\x13notificationMessage\x12\x10.ProtocolMessage\x18\x10 \x01(\x0b\x32\x14.NotificationMessage')
  ,
  dependencies=[pyatv_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.DESCRIPTOR,])


NOTIFICATIONMESSAGE_FIELD_NUMBER = 16
notificationMessage = _descriptor.FieldDescriptor(
  name='notificationMessage', full_name='notificationMessage', index=0,
  number=16, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)


_NOTIFICATIONMESSAGE = _descriptor.Descriptor(
  name='NotificationMessage',
  full_name='NotificationMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='notification', full_name='NotificationMessage.notification', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='userInfo', full_name='NotificationMessage.userInfo', index=1,
      number=2, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=90,
  serialized_end=151,
)

DESCRIPTOR.message_types_by_name['NotificationMessage'] = _NOTIFICATIONMESSAGE
DESCRIPTOR.extensions_by_name['notificationMessage'] = notificationMessage
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NotificationMessage = _reflection.GeneratedProtocolMessageType('NotificationMessage', (_message.Message,), dict(
  DESCRIPTOR = _NOTIFICATIONMESSAGE,
  __module__ = 'pyatv.mrp.protobuf.NotificationMessage_pb2'
  # @@protoc_insertion_point(class_scope:NotificationMessage)
  ))
_sym_db.RegisterMessage(NotificationMessage)

notificationMessage.message_type = _NOTIFICATIONMESSAGE
pyatv_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.ProtocolMessage.RegisterExtension(notificationMessage)

# @@protoc_insertion_point(module_scope)
