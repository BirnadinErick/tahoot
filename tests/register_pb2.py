# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: register.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eregister.proto\"#\n\x0fRegisterRequest\x12\x10\n\x08username\x18\x01 \x01(\t\"2\n\rAnswerRequest\x12\r\n\x05qu_id\x18\x01 \x01(\r\x12\x12\n\nanswer_idx\x18\x02 \x01(\rb\x06proto3')



_REGISTERREQUEST = DESCRIPTOR.message_types_by_name['RegisterRequest']
_ANSWERREQUEST = DESCRIPTOR.message_types_by_name['AnswerRequest']
RegisterRequest = _reflection.GeneratedProtocolMessageType('RegisterRequest', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERREQUEST,
  '__module__' : 'register_pb2'
  # @@protoc_insertion_point(class_scope:RegisterRequest)
  })
_sym_db.RegisterMessage(RegisterRequest)

AnswerRequest = _reflection.GeneratedProtocolMessageType('AnswerRequest', (_message.Message,), {
  'DESCRIPTOR' : _ANSWERREQUEST,
  '__module__' : 'register_pb2'
  # @@protoc_insertion_point(class_scope:AnswerRequest)
  })
_sym_db.RegisterMessage(AnswerRequest)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REGISTERREQUEST._serialized_start=18
  _REGISTERREQUEST._serialized_end=53
  _ANSWERREQUEST._serialized_start=55
  _ANSWERREQUEST._serialized_end=105
# @@protoc_insertion_point(module_scope)
