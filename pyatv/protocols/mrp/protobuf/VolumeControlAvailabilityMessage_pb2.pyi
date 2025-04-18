"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.internal.extension_dict
import google.protobuf.message
import pyatv.protocols.mrp.protobuf.ProtocolMessage_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class VolumeCapabilities(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Enum:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _EnumEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[VolumeCapabilities._Enum.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        Relative: VolumeCapabilities._Enum.ValueType  # 1
        Absolute: VolumeCapabilities._Enum.ValueType  # 2
        Both: VolumeCapabilities._Enum.ValueType  # 3

    class Enum(_Enum, metaclass=_EnumEnumTypeWrapper):
        """This is really a bitmap but protobuf has no type for that, so lets just add a "Both"
        option since only two values exist anyway
        """

    Relative: VolumeCapabilities.Enum.ValueType  # 1
    Absolute: VolumeCapabilities.Enum.ValueType  # 2
    Both: VolumeCapabilities.Enum.ValueType  # 3

    def __init__(
        self,
    ) -> None: ...

global___VolumeCapabilities = VolumeCapabilities

@typing.final
class VolumeControlAvailabilityMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VOLUMECONTROLAVAILABLE_FIELD_NUMBER: builtins.int
    VOLUMECAPABILITIES_FIELD_NUMBER: builtins.int
    volumeControlAvailable: builtins.bool
    volumeCapabilities: global___VolumeCapabilities.Enum.ValueType
    def __init__(
        self,
        *,
        volumeControlAvailable: builtins.bool | None = ...,
        volumeCapabilities: global___VolumeCapabilities.Enum.ValueType | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["volumeCapabilities", b"volumeCapabilities", "volumeControlAvailable", b"volumeControlAvailable"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["volumeCapabilities", b"volumeCapabilities", "volumeControlAvailable", b"volumeControlAvailable"]) -> None: ...

global___VolumeControlAvailabilityMessage = VolumeControlAvailabilityMessage

VOLUMECONTROLAVAILABILITYMESSAGE_FIELD_NUMBER: builtins.int
volumeControlAvailabilityMessage: google.protobuf.internal.extension_dict._ExtensionFieldDescriptor[pyatv.protocols.mrp.protobuf.ProtocolMessage_pb2.ProtocolMessage, global___VolumeControlAvailabilityMessage]
