# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: BuildingInfo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='BuildingInfo.proto',
  package='AnimFireChalBuilding',
  syntax='proto3',
  serialized_options=_b('\n\024AnimFireChalBuildingB\021AnimFireChalProto'),
  serialized_pb=_b('\n\x12\x42uildingInfo.proto\x12\x14\x41nimFireChalBuilding\"A\n\x0c\x42uildingInfo\x12\x31\n\tbuildings\x18\x01 \x03(\x0b\x32\x1e.AnimFireChalBuilding.Building\"G\n\x08\x42uilding\x12\x11\n\tfieryness\x18\x01 \x01(\x05\x12\x13\n\x0btemperature\x18\x02 \x01(\x01\x12\x13\n\x0b\x62uilding_id\x18\x03 \x01(\x05\"\x07\n\x05\x45mpty\"\x18\n\x06Reward\x12\x0e\n\x06reward\x18\x01 \x01(\x01\x32\xb7\x01\n\x14\x41nimFireChalBuilding\x12T\n\x0fgetBuildingInfo\x12\x1b.AnimFireChalBuilding.Empty\x1a\".AnimFireChalBuilding.BuildingInfo\"\x00\x12I\n\ngetRewards\x12\x1b.AnimFireChalBuilding.Empty\x1a\x1c.AnimFireChalBuilding.Reward\"\x00\x42)\n\x14\x41nimFireChalBuildingB\x11\x41nimFireChalProtob\x06proto3')
)




_BUILDINGINFO = _descriptor.Descriptor(
  name='BuildingInfo',
  full_name='AnimFireChalBuilding.BuildingInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='buildings', full_name='AnimFireChalBuilding.BuildingInfo.buildings', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=44,
  serialized_end=109,
)


_BUILDING = _descriptor.Descriptor(
  name='Building',
  full_name='AnimFireChalBuilding.Building',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fieryness', full_name='AnimFireChalBuilding.Building.fieryness', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='temperature', full_name='AnimFireChalBuilding.Building.temperature', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='building_id', full_name='AnimFireChalBuilding.Building.building_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=111,
  serialized_end=182,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='AnimFireChalBuilding.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=184,
  serialized_end=191,
)


_REWARD = _descriptor.Descriptor(
  name='Reward',
  full_name='AnimFireChalBuilding.Reward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reward', full_name='AnimFireChalBuilding.Reward.reward', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=193,
  serialized_end=217,
)

_BUILDINGINFO.fields_by_name['buildings'].message_type = _BUILDING
DESCRIPTOR.message_types_by_name['BuildingInfo'] = _BUILDINGINFO
DESCRIPTOR.message_types_by_name['Building'] = _BUILDING
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['Reward'] = _REWARD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BuildingInfo = _reflection.GeneratedProtocolMessageType('BuildingInfo', (_message.Message,), {
  'DESCRIPTOR' : _BUILDINGINFO,
  '__module__' : 'BuildingInfo_pb2'
  # @@protoc_insertion_point(class_scope:AnimFireChalBuilding.BuildingInfo)
  })
_sym_db.RegisterMessage(BuildingInfo)

Building = _reflection.GeneratedProtocolMessageType('Building', (_message.Message,), {
  'DESCRIPTOR' : _BUILDING,
  '__module__' : 'BuildingInfo_pb2'
  # @@protoc_insertion_point(class_scope:AnimFireChalBuilding.Building)
  })
_sym_db.RegisterMessage(Building)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'BuildingInfo_pb2'
  # @@protoc_insertion_point(class_scope:AnimFireChalBuilding.Empty)
  })
_sym_db.RegisterMessage(Empty)

Reward = _reflection.GeneratedProtocolMessageType('Reward', (_message.Message,), {
  'DESCRIPTOR' : _REWARD,
  '__module__' : 'BuildingInfo_pb2'
  # @@protoc_insertion_point(class_scope:AnimFireChalBuilding.Reward)
  })
_sym_db.RegisterMessage(Reward)


DESCRIPTOR._options = None

_ANIMFIRECHALBUILDING = _descriptor.ServiceDescriptor(
  name='AnimFireChalBuilding',
  full_name='AnimFireChalBuilding.AnimFireChalBuilding',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=220,
  serialized_end=403,
  methods=[
  _descriptor.MethodDescriptor(
    name='getBuildingInfo',
    full_name='AnimFireChalBuilding.AnimFireChalBuilding.getBuildingInfo',
    index=0,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_BUILDINGINFO,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='getRewards',
    full_name='AnimFireChalBuilding.AnimFireChalBuilding.getRewards',
    index=1,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_REWARD,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ANIMFIRECHALBUILDING)

DESCRIPTOR.services_by_name['AnimFireChalBuilding'] = _ANIMFIRECHALBUILDING

# @@protoc_insertion_point(module_scope)
