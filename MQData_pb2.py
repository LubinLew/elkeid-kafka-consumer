# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: MQData.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='MQData.proto',
  package='hids_pb',
  syntax='proto3',
  serialized_options=b'Z\007hids_pb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0cMQData.proto\x12\x07hids_pb\"\xad\x02\n\x06MQData\x12\x11\n\tdata_type\x18\x01 \x01(\x05\x12\x11\n\ttimestamp\x18\x02 \x01(\x03\x12\x1b\n\x04\x62ody\x18\x03 \x01(\x0b\x32\r.hids_pb.Item\x12\x10\n\x08\x61gent_id\x18\x04 \x01(\t\x12\x14\n\x0cin_ipv4_list\x18\x05 \x01(\t\x12\x14\n\x0c\x65x_ipv4_list\x18\x06 \x01(\t\x12\x14\n\x0cin_ipv6_list\x18\x07 \x01(\t\x12\x14\n\x0c\x65x_ipv6_list\x18\x08 \x01(\t\x12\x10\n\x08hostname\x18\t \x01(\t\x12\x0f\n\x07version\x18\n \x01(\t\x12\x0f\n\x07product\x18\x0b \x01(\t\x12\x10\n\x08time_pkg\x18\x0c \x01(\x03\x12\x10\n\x08psm_name\x18\r \x01(\t\x12\x10\n\x08psm_path\x18\x0e \x01(\t\x12\x0c\n\x04tags\x18\x0f \x01(\t\"`\n\x04Item\x12)\n\x06\x66ields\x18\x01 \x03(\x0b\x32\x19.hids_pb.Item.FieldsEntry\x1a-\n\x0b\x46ieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\tZ\x07hids_pbb\x06proto3'
)




_MQDATA = _descriptor.Descriptor(
  name='MQData',
  full_name='hids_pb.MQData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data_type', full_name='hids_pb.MQData.data_type', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='hids_pb.MQData.timestamp', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='body', full_name='hids_pb.MQData.body', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='agent_id', full_name='hids_pb.MQData.agent_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='in_ipv4_list', full_name='hids_pb.MQData.in_ipv4_list', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ex_ipv4_list', full_name='hids_pb.MQData.ex_ipv4_list', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='in_ipv6_list', full_name='hids_pb.MQData.in_ipv6_list', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ex_ipv6_list', full_name='hids_pb.MQData.ex_ipv6_list', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hostname', full_name='hids_pb.MQData.hostname', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='hids_pb.MQData.version', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='product', full_name='hids_pb.MQData.product', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time_pkg', full_name='hids_pb.MQData.time_pkg', index=11,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='psm_name', full_name='hids_pb.MQData.psm_name', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='psm_path', full_name='hids_pb.MQData.psm_path', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tags', full_name='hids_pb.MQData.tags', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=26,
  serialized_end=327,
)


_ITEM_FIELDSENTRY = _descriptor.Descriptor(
  name='FieldsEntry',
  full_name='hids_pb.Item.FieldsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='hids_pb.Item.FieldsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='hids_pb.Item.FieldsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=380,
  serialized_end=425,
)

_ITEM = _descriptor.Descriptor(
  name='Item',
  full_name='hids_pb.Item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fields', full_name='hids_pb.Item.fields', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_ITEM_FIELDSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=329,
  serialized_end=425,
)

_MQDATA.fields_by_name['body'].message_type = _ITEM
_ITEM_FIELDSENTRY.containing_type = _ITEM
_ITEM.fields_by_name['fields'].message_type = _ITEM_FIELDSENTRY
DESCRIPTOR.message_types_by_name['MQData'] = _MQDATA
DESCRIPTOR.message_types_by_name['Item'] = _ITEM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MQData = _reflection.GeneratedProtocolMessageType('MQData', (_message.Message,), {
  'DESCRIPTOR' : _MQDATA,
  '__module__' : 'MQData_pb2'
  # @@protoc_insertion_point(class_scope:hids_pb.MQData)
  })
_sym_db.RegisterMessage(MQData)

Item = _reflection.GeneratedProtocolMessageType('Item', (_message.Message,), {

  'FieldsEntry' : _reflection.GeneratedProtocolMessageType('FieldsEntry', (_message.Message,), {
    'DESCRIPTOR' : _ITEM_FIELDSENTRY,
    '__module__' : 'MQData_pb2'
    # @@protoc_insertion_point(class_scope:hids_pb.Item.FieldsEntry)
    })
  ,
  'DESCRIPTOR' : _ITEM,
  '__module__' : 'MQData_pb2'
  # @@protoc_insertion_point(class_scope:hids_pb.Item)
  })
_sym_db.RegisterMessage(Item)
_sym_db.RegisterMessage(Item.FieldsEntry)


DESCRIPTOR._options = None
_ITEM_FIELDSENTRY._options = None
# @@protoc_insertion_point(module_scope)
