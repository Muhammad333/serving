# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: logging_config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import log_collector_config_pb2 as log__collector__config__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='logging_config.proto',
  package='tensorflow.serving',
  syntax='proto3',
  serialized_pb=_b('\n\x14logging_config.proto\x12\x12tensorflow.serving\x1a\x1alog_collector_config.proto\"\'\n\x0eSamplingConfig\x12\x15\n\rsampling_rate\x18\x01 \x01(\x01\"\x92\x01\n\rLoggingConfig\x12\x44\n\x14log_collector_config\x18\x01 \x01(\x0b\x32&.tensorflow.serving.LogCollectorConfig\x12;\n\x0fsampling_config\x18\x02 \x01(\x0b\x32\".tensorflow.serving.SamplingConfigB\x03\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[log__collector__config__pb2.DESCRIPTOR,])




_SAMPLINGCONFIG = _descriptor.Descriptor(
  name='SamplingConfig',
  full_name='tensorflow.serving.SamplingConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sampling_rate', full_name='tensorflow.serving.SamplingConfig.sampling_rate', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=72,
  serialized_end=111,
)


_LOGGINGCONFIG = _descriptor.Descriptor(
  name='LoggingConfig',
  full_name='tensorflow.serving.LoggingConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='log_collector_config', full_name='tensorflow.serving.LoggingConfig.log_collector_config', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sampling_config', full_name='tensorflow.serving.LoggingConfig.sampling_config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=114,
  serialized_end=260,
)

_LOGGINGCONFIG.fields_by_name['log_collector_config'].message_type = log__collector__config__pb2._LOGCOLLECTORCONFIG
_LOGGINGCONFIG.fields_by_name['sampling_config'].message_type = _SAMPLINGCONFIG
DESCRIPTOR.message_types_by_name['SamplingConfig'] = _SAMPLINGCONFIG
DESCRIPTOR.message_types_by_name['LoggingConfig'] = _LOGGINGCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SamplingConfig = _reflection.GeneratedProtocolMessageType('SamplingConfig', (_message.Message,), dict(
  DESCRIPTOR = _SAMPLINGCONFIG,
  __module__ = 'logging_config_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.serving.SamplingConfig)
  ))
_sym_db.RegisterMessage(SamplingConfig)

LoggingConfig = _reflection.GeneratedProtocolMessageType('LoggingConfig', (_message.Message,), dict(
  DESCRIPTOR = _LOGGINGCONFIG,
  __module__ = 'logging_config_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.serving.LoggingConfig)
  ))
_sym_db.RegisterMessage(LoggingConfig)


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
