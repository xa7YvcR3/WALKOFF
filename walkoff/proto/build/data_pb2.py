# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: data.proto

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
  name='data.proto',
  package='core',
  serialized_pb=_b('\n\ndata.proto\x12\x04\x63ore\"\x83\x03\n\x07Message\x12 \n\x04type\x18\x01 \x01(\x0e\x32\x12.core.Message.Type\x12\x12\n\nevent_name\x18\x02 \x01(\t\x12/\n\x0fworkflow_packet\x18\x03 \x01(\x0b\x32\x14.core.WorkflowPacketH\x00\x12+\n\raction_packet\x18\x04 \x01(\x0b\x32\x12.core.ActionPacketH\x00\x12-\n\x0egeneral_packet\x18\x05 \x01(\x0b\x32\x13.core.GeneralPacketH\x00\x12+\n\x0emessage_packet\x18\x06 \x01(\x0b\x32\x11.core.UserMessageH\x00\"~\n\x04Type\x12\x12\n\x0eWORKFLOWPACKET\x10\x01\x12\x16\n\x12WORKFLOWPACKETDATA\x10\x02\x12\x10\n\x0c\x41\x43TIONPACKET\x10\x03\x12\x14\n\x10\x41\x43TIONPACKETDATA\x10\x04\x12\x11\n\rGENERALPACKET\x10\x05\x12\x0f\n\x0bUSERMESSAGE\x10\x06\x42\x08\n\x06packet\"\xab\x01\n\x0eWorkflowPacket\x12\x33\n\x06sender\x18\x01 \x01(\x0b\x32#.core.WorkflowPacket.WorkflowSender\x12\x17\n\x0f\x61\x64\x64itional_data\x18\x02 \x01(\t\x1aK\n\x0eWorkflowSender\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03uid\x18\x02 \x01(\t\x12\x1e\n\x16workflow_execution_uid\x18\x03 \x01(\t\"\x80\x03\n\x0c\x41\x63tionPacket\x12/\n\x06sender\x18\x01 \x01(\x0b\x32\x1f.core.ActionPacket.ActionSender\x12\x17\n\x0f\x61\x64\x64itional_data\x18\x02 \x01(\t\x1aS\n\x0e\x41\x63tionArgument\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x11\n\treference\x18\x03 \x01(\t\x12\x11\n\tselection\x18\x04 \x01(\t\x1a\xd0\x01\n\x0c\x41\x63tionSender\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03uid\x18\x02 \x01(\t\x12\x15\n\rexecution_uid\x18\x03 \x01(\t\x12\x10\n\x08\x61pp_name\x18\x04 \x01(\t\x12\x13\n\x0b\x61\x63tion_name\x18\x05 \x01(\t\x12\x34\n\targuments\x18\x06 \x03(\x0b\x32!.core.ActionPacket.ActionArgument\x12\x1e\n\x16workflow_execution_uid\x18\x07 \x01(\t\x12\x11\n\tdevice_id\x18\x08 \x01(\x05\"\x92\x01\n\rGeneralPacket\x12\x31\n\x06sender\x18\x01 \x01(\x0b\x32!.core.GeneralPacket.GeneralSender\x1aN\n\rGeneralSender\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x10\n\x08\x61pp_name\x18\x02 \x01(\t\x12\x1e\n\x16workflow_execution_uid\x18\x03 \x01(\t\"\xe0\x01\n\x13\x43ommunicationPacket\x12,\n\x04type\x18\x01 \x01(\x0e\x32\x1e.core.CommunicationPacket.Type\x12\x1e\n\x16workflow_execution_uid\x18\x02 \x01(\t\x12\x0f\n\x07\x64\x61ta_in\x18\x03 \x01(\t\x12\x34\n\targuments\x18\x04 \x03(\x0b\x32!.core.ActionPacket.ActionArgument\"4\n\x04Type\x12\t\n\x05PAUSE\x10\x01\x12\n\n\x06RESUME\x10\x02\x12\x0b\n\x07TRIGGER\x10\x03\x12\x08\n\x04\x45XIT\x10\x04\"\x94\x01\n\x0bUserMessage\x12/\n\x06sender\x18\x01 \x01(\x0b\x32\x1f.core.ActionPacket.ActionSender\x12\x0f\n\x07subject\x18\x02 \x01(\t\x12\x0c\n\x04\x62ody\x18\x03 \x01(\t\x12\x17\n\x0frequires_reauth\x18\x04 \x01(\x08\x12\r\n\x05users\x18\x05 \x03(\x05\x12\r\n\x05roles\x18\x06 \x03(\x05')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_MESSAGE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='core.Message.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='WORKFLOWPACKET', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WORKFLOWPACKETDATA', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTIONPACKET', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTIONPACKETDATA', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GENERALPACKET', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USERMESSAGE', index=5, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=272,
  serialized_end=398,
)
_sym_db.RegisterEnumDescriptor(_MESSAGE_TYPE)

_COMMUNICATIONPACKET_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='core.CommunicationPacket.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PAUSE', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESUME', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRIGGER', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXIT', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1293,
  serialized_end=1345,
)
_sym_db.RegisterEnumDescriptor(_COMMUNICATIONPACKET_TYPE)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='core.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='core.Message.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='event_name', full_name='core.Message.event_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='workflow_packet', full_name='core.Message.workflow_packet', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='action_packet', full_name='core.Message.action_packet', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='general_packet', full_name='core.Message.general_packet', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message_packet', full_name='core.Message.message_packet', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MESSAGE_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='packet', full_name='core.Message.packet',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=21,
  serialized_end=408,
)


_WORKFLOWPACKET_WORKFLOWSENDER = _descriptor.Descriptor(
  name='WorkflowSender',
  full_name='core.WorkflowPacket.WorkflowSender',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='core.WorkflowPacket.WorkflowSender.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uid', full_name='core.WorkflowPacket.WorkflowSender.uid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='workflow_execution_uid', full_name='core.WorkflowPacket.WorkflowSender.workflow_execution_uid', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=507,
  serialized_end=582,
)

_WORKFLOWPACKET = _descriptor.Descriptor(
  name='WorkflowPacket',
  full_name='core.WorkflowPacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sender', full_name='core.WorkflowPacket.sender', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='additional_data', full_name='core.WorkflowPacket.additional_data', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_WORKFLOWPACKET_WORKFLOWSENDER, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=411,
  serialized_end=582,
)


_ACTIONPACKET_ACTIONARGUMENT = _descriptor.Descriptor(
  name='ActionArgument',
  full_name='core.ActionPacket.ActionArgument',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='core.ActionPacket.ActionArgument.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='core.ActionPacket.ActionArgument.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reference', full_name='core.ActionPacket.ActionArgument.reference', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='selection', full_name='core.ActionPacket.ActionArgument.selection', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=675,
  serialized_end=758,
)

_ACTIONPACKET_ACTIONSENDER = _descriptor.Descriptor(
  name='ActionSender',
  full_name='core.ActionPacket.ActionSender',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='core.ActionPacket.ActionSender.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uid', full_name='core.ActionPacket.ActionSender.uid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='execution_uid', full_name='core.ActionPacket.ActionSender.execution_uid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='app_name', full_name='core.ActionPacket.ActionSender.app_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='action_name', full_name='core.ActionPacket.ActionSender.action_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='arguments', full_name='core.ActionPacket.ActionSender.arguments', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='workflow_execution_uid', full_name='core.ActionPacket.ActionSender.workflow_execution_uid', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_id', full_name='core.ActionPacket.ActionSender.device_id', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=761,
  serialized_end=969,
)

_ACTIONPACKET = _descriptor.Descriptor(
  name='ActionPacket',
  full_name='core.ActionPacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sender', full_name='core.ActionPacket.sender', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='additional_data', full_name='core.ActionPacket.additional_data', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ACTIONPACKET_ACTIONARGUMENT, _ACTIONPACKET_ACTIONSENDER, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=585,
  serialized_end=969,
)


_GENERALPACKET_GENERALSENDER = _descriptor.Descriptor(
  name='GeneralSender',
  full_name='core.GeneralPacket.GeneralSender',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='core.GeneralPacket.GeneralSender.uid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='app_name', full_name='core.GeneralPacket.GeneralSender.app_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='workflow_execution_uid', full_name='core.GeneralPacket.GeneralSender.workflow_execution_uid', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1040,
  serialized_end=1118,
)

_GENERALPACKET = _descriptor.Descriptor(
  name='GeneralPacket',
  full_name='core.GeneralPacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sender', full_name='core.GeneralPacket.sender', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_GENERALPACKET_GENERALSENDER, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=972,
  serialized_end=1118,
)


_COMMUNICATIONPACKET = _descriptor.Descriptor(
  name='CommunicationPacket',
  full_name='core.CommunicationPacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='core.CommunicationPacket.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='workflow_execution_uid', full_name='core.CommunicationPacket.workflow_execution_uid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data_in', full_name='core.CommunicationPacket.data_in', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='arguments', full_name='core.CommunicationPacket.arguments', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _COMMUNICATIONPACKET_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1121,
  serialized_end=1345,
)


_USERMESSAGE = _descriptor.Descriptor(
  name='UserMessage',
  full_name='core.UserMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sender', full_name='core.UserMessage.sender', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='subject', full_name='core.UserMessage.subject', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='body', full_name='core.UserMessage.body', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='requires_reauth', full_name='core.UserMessage.requires_reauth', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='users', full_name='core.UserMessage.users', index=4,
      number=5, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='roles', full_name='core.UserMessage.roles', index=5,
      number=6, type=5, cpp_type=1, label=3,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1348,
  serialized_end=1496,
)

_MESSAGE.fields_by_name['type'].enum_type = _MESSAGE_TYPE
_MESSAGE.fields_by_name['workflow_packet'].message_type = _WORKFLOWPACKET
_MESSAGE.fields_by_name['action_packet'].message_type = _ACTIONPACKET
_MESSAGE.fields_by_name['general_packet'].message_type = _GENERALPACKET
_MESSAGE.fields_by_name['message_packet'].message_type = _USERMESSAGE
_MESSAGE_TYPE.containing_type = _MESSAGE
_MESSAGE.oneofs_by_name['packet'].fields.append(
  _MESSAGE.fields_by_name['workflow_packet'])
_MESSAGE.fields_by_name['workflow_packet'].containing_oneof = _MESSAGE.oneofs_by_name['packet']
_MESSAGE.oneofs_by_name['packet'].fields.append(
  _MESSAGE.fields_by_name['action_packet'])
_MESSAGE.fields_by_name['action_packet'].containing_oneof = _MESSAGE.oneofs_by_name['packet']
_MESSAGE.oneofs_by_name['packet'].fields.append(
  _MESSAGE.fields_by_name['general_packet'])
_MESSAGE.fields_by_name['general_packet'].containing_oneof = _MESSAGE.oneofs_by_name['packet']
_MESSAGE.oneofs_by_name['packet'].fields.append(
  _MESSAGE.fields_by_name['message_packet'])
_MESSAGE.fields_by_name['message_packet'].containing_oneof = _MESSAGE.oneofs_by_name['packet']
_WORKFLOWPACKET_WORKFLOWSENDER.containing_type = _WORKFLOWPACKET
_WORKFLOWPACKET.fields_by_name['sender'].message_type = _WORKFLOWPACKET_WORKFLOWSENDER
_ACTIONPACKET_ACTIONARGUMENT.containing_type = _ACTIONPACKET
_ACTIONPACKET_ACTIONSENDER.fields_by_name['arguments'].message_type = _ACTIONPACKET_ACTIONARGUMENT
_ACTIONPACKET_ACTIONSENDER.containing_type = _ACTIONPACKET
_ACTIONPACKET.fields_by_name['sender'].message_type = _ACTIONPACKET_ACTIONSENDER
_GENERALPACKET_GENERALSENDER.containing_type = _GENERALPACKET
_GENERALPACKET.fields_by_name['sender'].message_type = _GENERALPACKET_GENERALSENDER
_COMMUNICATIONPACKET.fields_by_name['type'].enum_type = _COMMUNICATIONPACKET_TYPE
_COMMUNICATIONPACKET.fields_by_name['arguments'].message_type = _ACTIONPACKET_ACTIONARGUMENT
_COMMUNICATIONPACKET_TYPE.containing_type = _COMMUNICATIONPACKET
_USERMESSAGE.fields_by_name['sender'].message_type = _ACTIONPACKET_ACTIONSENDER
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
DESCRIPTOR.message_types_by_name['WorkflowPacket'] = _WORKFLOWPACKET
DESCRIPTOR.message_types_by_name['ActionPacket'] = _ACTIONPACKET
DESCRIPTOR.message_types_by_name['GeneralPacket'] = _GENERALPACKET
DESCRIPTOR.message_types_by_name['CommunicationPacket'] = _COMMUNICATIONPACKET
DESCRIPTOR.message_types_by_name['UserMessage'] = _USERMESSAGE

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGE,
  __module__ = 'data_pb2'
  # @@protoc_insertion_point(class_scope:core.Message)
  ))
_sym_db.RegisterMessage(Message)

WorkflowPacket = _reflection.GeneratedProtocolMessageType('WorkflowPacket', (_message.Message,), dict(

  WorkflowSender = _reflection.GeneratedProtocolMessageType('WorkflowSender', (_message.Message,), dict(
    DESCRIPTOR = _WORKFLOWPACKET_WORKFLOWSENDER,
    __module__ = 'data_pb2'
    # @@protoc_insertion_point(class_scope:core.WorkflowPacket.WorkflowSender)
    ))
  ,
  DESCRIPTOR = _WORKFLOWPACKET,
  __module__ = 'data_pb2'
  # @@protoc_insertion_point(class_scope:core.WorkflowPacket)
  ))
_sym_db.RegisterMessage(WorkflowPacket)
_sym_db.RegisterMessage(WorkflowPacket.WorkflowSender)

ActionPacket = _reflection.GeneratedProtocolMessageType('ActionPacket', (_message.Message,), dict(

  ActionArgument = _reflection.GeneratedProtocolMessageType('ActionArgument', (_message.Message,), dict(
    DESCRIPTOR = _ACTIONPACKET_ACTIONARGUMENT,
    __module__ = 'data_pb2'
    # @@protoc_insertion_point(class_scope:core.ActionPacket.ActionArgument)
    ))
  ,

  ActionSender = _reflection.GeneratedProtocolMessageType('ActionSender', (_message.Message,), dict(
    DESCRIPTOR = _ACTIONPACKET_ACTIONSENDER,
    __module__ = 'data_pb2'
    # @@protoc_insertion_point(class_scope:core.ActionPacket.ActionSender)
    ))
  ,
  DESCRIPTOR = _ACTIONPACKET,
  __module__ = 'data_pb2'
  # @@protoc_insertion_point(class_scope:core.ActionPacket)
  ))
_sym_db.RegisterMessage(ActionPacket)
_sym_db.RegisterMessage(ActionPacket.ActionArgument)
_sym_db.RegisterMessage(ActionPacket.ActionSender)

GeneralPacket = _reflection.GeneratedProtocolMessageType('GeneralPacket', (_message.Message,), dict(

  GeneralSender = _reflection.GeneratedProtocolMessageType('GeneralSender', (_message.Message,), dict(
    DESCRIPTOR = _GENERALPACKET_GENERALSENDER,
    __module__ = 'data_pb2'
    # @@protoc_insertion_point(class_scope:core.GeneralPacket.GeneralSender)
    ))
  ,
  DESCRIPTOR = _GENERALPACKET,
  __module__ = 'data_pb2'
  # @@protoc_insertion_point(class_scope:core.GeneralPacket)
  ))
_sym_db.RegisterMessage(GeneralPacket)
_sym_db.RegisterMessage(GeneralPacket.GeneralSender)

CommunicationPacket = _reflection.GeneratedProtocolMessageType('CommunicationPacket', (_message.Message,), dict(
  DESCRIPTOR = _COMMUNICATIONPACKET,
  __module__ = 'data_pb2'
  # @@protoc_insertion_point(class_scope:core.CommunicationPacket)
  ))
_sym_db.RegisterMessage(CommunicationPacket)

UserMessage = _reflection.GeneratedProtocolMessageType('UserMessage', (_message.Message,), dict(
  DESCRIPTOR = _USERMESSAGE,
  __module__ = 'data_pb2'
  # @@protoc_insertion_point(class_scope:core.UserMessage)
  ))
_sym_db.RegisterMessage(UserMessage)


# @@protoc_insertion_point(module_scope)
