# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: log_collector_config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='log_collector_config.proto',
  package='tensorflow.serving',
  syntax='proto3',
  serialized_pb=_b('\n\x1alog_collector_config.proto\x12\x12tensorflow.serving\";\n\x12LogCollectorConfig\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x17\n\x0f\x66ilename_prefix\x18\x02 \x01(\tB\x03\xf8\x01\x01\x62\x06proto3')
)




_LOGCOLLECTORCONFIG = _descriptor.Descriptor(
  name='LogCollectorConfig',
  full_name='tensorflow.serving.LogCollectorConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='tensorflow.serving.LogCollectorConfig.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filename_prefix', full_name='tensorflow.serving.LogCollectorConfig.filename_prefix', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=50,
  serialized_end=109,
)

DESCRIPTOR.message_types_by_name['LogCollectorConfig'] = _LOGCOLLECTORCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LogCollectorConfig = _reflection.GeneratedProtocolMessageType('LogCollectorConfig', (_message.Message,), dict(
  DESCRIPTOR = _LOGCOLLECTORCONFIG,
  __module__ = 'log_collector_config_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.serving.LogCollectorConfig)
  ))
_sym_db.RegisterMessage(LogCollectorConfig)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\370\001\001'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
