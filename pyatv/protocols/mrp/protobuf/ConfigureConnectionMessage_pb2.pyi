"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.extension_dict
import google.protobuf.message
import pyatv.protocols.mrp.protobuf.ProtocolMessage_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class ConfigureConnectionMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    GROUPID_FIELD_NUMBER: builtins.int
    groupID: typing.Text
    def __init__(self,
        *,
        groupID: typing.Optional[typing.Text] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["groupID",b"groupID"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["groupID",b"groupID"]) -> None: ...
global___ConfigureConnectionMessage = ConfigureConnectionMessage

CONFIGURECONNECTIONMESSAGE_FIELD_NUMBER: builtins.int
configureConnectionMessage: google.protobuf.internal.extension_dict._ExtensionFieldDescriptor[pyatv.protocols.mrp.protobuf.ProtocolMessage_pb2.ProtocolMessage, global___ConfigureConnectionMessage]
