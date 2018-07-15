# Copyright (c) 2018, The TurtleCoin Developers
# 
# Please see the included LICENSE file for more information.

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TurtleToTurtle.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import TurtleCoin_pb2 as TurtleCoin__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='TurtleToTurtle.proto',
  package='TurtleToTurtle',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x14TurtleToTurtle.proto\x12\x0eTurtleToTurtle\x1a\x10TurtleCoin.proto\"\x9d\x02\n\x0bT2TDatagram\x12\x14\n\x0cp2pNetworkId\x18\x01 \x01(\r\x12\x0f\n\x07version\x18\x02 \x01(\r\x12\x0e\n\x06peerId\x18\x03 \x01(\t\x12<\n\x10t2tCandidateList\x18\x04 \x01(\x0b\x32 .TurtleToTurtle.T2TCandidateListH\x00\x12J\n\x17t2tCandidateListRequest\x18\x05 \x01(\x0b\x32\'.TurtleToTurtle.T2TCandidateListRequestH\x00\x12>\n\x11\x62lockChainPayload\x18\x06 \x01(\x0b\x32!.TurtleToTurtle.BlockChainPayloadH\x00\x42\r\n\x0b\x64\x61taPayload\"C\n\x10T2TCandidateList\x12/\n\tcandidate\x18\x01 \x03(\x0b\x32\x1c.TurtleToTurtle.T2TCandidate\"/\n\x17T2TCandidateListRequest\x12\x14\n\x0c\x62lockChainId\x18\x01 \x03(\r\"\xab\x01\n\x0cT2TCandidate\x12\x0e\n\x06peerId\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\r\x12\x13\n\x0bipV4Address\x18\x03 \x01(\r\x12\x13\n\x0bipV6Address\x18\x04 \x01(\t\x12\x0c\n\x04port\x18\x05 \x01(\r\x12\x0b\n\x03ttl\x18\x06 \x01(\r\x12\x35\n\ncapability\x18\x07 \x01(\x0b\x32!.TurtleToTurtle.T2TNodeCapability\";\n\x11T2TNodeCapability\x12\x10\n\x08\x61rchival\x18\x01 \x01(\x08\x12\x14\n\x0c\x62lockChainId\x18\x02 \x03(\r\"\x99\x01\n\x11\x42lockChainPayload\x12\x37\n\x05\x62lock\x18\x01 \x01(\x0b\x32&.TurtleToTurtle.TurtleCoin.TurtleBlockH\x00\x12\x43\n\x0btransaction\x18\x02 \x01(\x0b\x32,.TurtleToTurtle.TurtleCoin.TurtleTransactionH\x00\x42\x06\n\x04\x64\x61tab\x06proto3')
  ,
  dependencies=[TurtleCoin__pb2.DESCRIPTOR,])




_T2TDATAGRAM = _descriptor.Descriptor(
  name='T2TDatagram',
  full_name='TurtleToTurtle.T2TDatagram',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='p2pNetworkId', full_name='TurtleToTurtle.T2TDatagram.p2pNetworkId', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='TurtleToTurtle.T2TDatagram.version', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='peerId', full_name='TurtleToTurtle.T2TDatagram.peerId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='t2tCandidateList', full_name='TurtleToTurtle.T2TDatagram.t2tCandidateList', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='t2tCandidateListRequest', full_name='TurtleToTurtle.T2TDatagram.t2tCandidateListRequest', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blockChainPayload', full_name='TurtleToTurtle.T2TDatagram.blockChainPayload', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='dataPayload', full_name='TurtleToTurtle.T2TDatagram.dataPayload',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=59,
  serialized_end=344,
)


_T2TCANDIDATELIST = _descriptor.Descriptor(
  name='T2TCandidateList',
  full_name='TurtleToTurtle.T2TCandidateList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='candidate', full_name='TurtleToTurtle.T2TCandidateList.candidate', index=0,
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
  serialized_start=346,
  serialized_end=413,
)


_T2TCANDIDATELISTREQUEST = _descriptor.Descriptor(
  name='T2TCandidateListRequest',
  full_name='TurtleToTurtle.T2TCandidateListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='blockChainId', full_name='TurtleToTurtle.T2TCandidateListRequest.blockChainId', index=0,
      number=1, type=13, cpp_type=3, label=3,
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
  serialized_start=415,
  serialized_end=462,
)


_T2TCANDIDATE = _descriptor.Descriptor(
  name='T2TCandidate',
  full_name='TurtleToTurtle.T2TCandidate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='peerId', full_name='TurtleToTurtle.T2TCandidate.peerId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='TurtleToTurtle.T2TCandidate.version', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ipV4Address', full_name='TurtleToTurtle.T2TCandidate.ipV4Address', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ipV6Address', full_name='TurtleToTurtle.T2TCandidate.ipV6Address', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='TurtleToTurtle.T2TCandidate.port', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ttl', full_name='TurtleToTurtle.T2TCandidate.ttl', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='capability', full_name='TurtleToTurtle.T2TCandidate.capability', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=465,
  serialized_end=636,
)


_T2TNODECAPABILITY = _descriptor.Descriptor(
  name='T2TNodeCapability',
  full_name='TurtleToTurtle.T2TNodeCapability',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='archival', full_name='TurtleToTurtle.T2TNodeCapability.archival', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blockChainId', full_name='TurtleToTurtle.T2TNodeCapability.blockChainId', index=1,
      number=2, type=13, cpp_type=3, label=3,
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
  serialized_start=638,
  serialized_end=697,
)


_BLOCKCHAINPAYLOAD = _descriptor.Descriptor(
  name='BlockChainPayload',
  full_name='TurtleToTurtle.BlockChainPayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='block', full_name='TurtleToTurtle.BlockChainPayload.block', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transaction', full_name='TurtleToTurtle.BlockChainPayload.transaction', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='data', full_name='TurtleToTurtle.BlockChainPayload.data',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=700,
  serialized_end=853,
)

_T2TDATAGRAM.fields_by_name['t2tCandidateList'].message_type = _T2TCANDIDATELIST
_T2TDATAGRAM.fields_by_name['t2tCandidateListRequest'].message_type = _T2TCANDIDATELISTREQUEST
_T2TDATAGRAM.fields_by_name['blockChainPayload'].message_type = _BLOCKCHAINPAYLOAD
_T2TDATAGRAM.oneofs_by_name['dataPayload'].fields.append(
  _T2TDATAGRAM.fields_by_name['t2tCandidateList'])
_T2TDATAGRAM.fields_by_name['t2tCandidateList'].containing_oneof = _T2TDATAGRAM.oneofs_by_name['dataPayload']
_T2TDATAGRAM.oneofs_by_name['dataPayload'].fields.append(
  _T2TDATAGRAM.fields_by_name['t2tCandidateListRequest'])
_T2TDATAGRAM.fields_by_name['t2tCandidateListRequest'].containing_oneof = _T2TDATAGRAM.oneofs_by_name['dataPayload']
_T2TDATAGRAM.oneofs_by_name['dataPayload'].fields.append(
  _T2TDATAGRAM.fields_by_name['blockChainPayload'])
_T2TDATAGRAM.fields_by_name['blockChainPayload'].containing_oneof = _T2TDATAGRAM.oneofs_by_name['dataPayload']
_T2TCANDIDATELIST.fields_by_name['candidate'].message_type = _T2TCANDIDATE
_T2TCANDIDATE.fields_by_name['capability'].message_type = _T2TNODECAPABILITY
_BLOCKCHAINPAYLOAD.fields_by_name['block'].message_type = TurtleCoin__pb2._TURTLEBLOCK
_BLOCKCHAINPAYLOAD.fields_by_name['transaction'].message_type = TurtleCoin__pb2._TURTLETRANSACTION
_BLOCKCHAINPAYLOAD.oneofs_by_name['data'].fields.append(
  _BLOCKCHAINPAYLOAD.fields_by_name['block'])
_BLOCKCHAINPAYLOAD.fields_by_name['block'].containing_oneof = _BLOCKCHAINPAYLOAD.oneofs_by_name['data']
_BLOCKCHAINPAYLOAD.oneofs_by_name['data'].fields.append(
  _BLOCKCHAINPAYLOAD.fields_by_name['transaction'])
_BLOCKCHAINPAYLOAD.fields_by_name['transaction'].containing_oneof = _BLOCKCHAINPAYLOAD.oneofs_by_name['data']
DESCRIPTOR.message_types_by_name['T2TDatagram'] = _T2TDATAGRAM
DESCRIPTOR.message_types_by_name['T2TCandidateList'] = _T2TCANDIDATELIST
DESCRIPTOR.message_types_by_name['T2TCandidateListRequest'] = _T2TCANDIDATELISTREQUEST
DESCRIPTOR.message_types_by_name['T2TCandidate'] = _T2TCANDIDATE
DESCRIPTOR.message_types_by_name['T2TNodeCapability'] = _T2TNODECAPABILITY
DESCRIPTOR.message_types_by_name['BlockChainPayload'] = _BLOCKCHAINPAYLOAD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

T2TDatagram = _reflection.GeneratedProtocolMessageType('T2TDatagram', (_message.Message,), dict(
  DESCRIPTOR = _T2TDATAGRAM,
  __module__ = 'TurtleToTurtle_pb2'
  # @@protoc_insertion_point(class_scope:TurtleToTurtle.T2TDatagram)
  ))
_sym_db.RegisterMessage(T2TDatagram)

T2TCandidateList = _reflection.GeneratedProtocolMessageType('T2TCandidateList', (_message.Message,), dict(
  DESCRIPTOR = _T2TCANDIDATELIST,
  __module__ = 'TurtleToTurtle_pb2'
  # @@protoc_insertion_point(class_scope:TurtleToTurtle.T2TCandidateList)
  ))
_sym_db.RegisterMessage(T2TCandidateList)

T2TCandidateListRequest = _reflection.GeneratedProtocolMessageType('T2TCandidateListRequest', (_message.Message,), dict(
  DESCRIPTOR = _T2TCANDIDATELISTREQUEST,
  __module__ = 'TurtleToTurtle_pb2'
  # @@protoc_insertion_point(class_scope:TurtleToTurtle.T2TCandidateListRequest)
  ))
_sym_db.RegisterMessage(T2TCandidateListRequest)

T2TCandidate = _reflection.GeneratedProtocolMessageType('T2TCandidate', (_message.Message,), dict(
  DESCRIPTOR = _T2TCANDIDATE,
  __module__ = 'TurtleToTurtle_pb2'
  # @@protoc_insertion_point(class_scope:TurtleToTurtle.T2TCandidate)
  ))
_sym_db.RegisterMessage(T2TCandidate)

T2TNodeCapability = _reflection.GeneratedProtocolMessageType('T2TNodeCapability', (_message.Message,), dict(
  DESCRIPTOR = _T2TNODECAPABILITY,
  __module__ = 'TurtleToTurtle_pb2'
  # @@protoc_insertion_point(class_scope:TurtleToTurtle.T2TNodeCapability)
  ))
_sym_db.RegisterMessage(T2TNodeCapability)

BlockChainPayload = _reflection.GeneratedProtocolMessageType('BlockChainPayload', (_message.Message,), dict(
  DESCRIPTOR = _BLOCKCHAINPAYLOAD,
  __module__ = 'TurtleToTurtle_pb2'
  # @@protoc_insertion_point(class_scope:TurtleToTurtle.BlockChainPayload)
  ))
_sym_db.RegisterMessage(BlockChainPayload)


# @@protoc_insertion_point(module_scope)