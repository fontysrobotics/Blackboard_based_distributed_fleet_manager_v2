// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from message_pkg:msg/BBbackup.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "message_pkg/msg/detail/b_bbackup__rosidl_typesupport_introspection_c.h"
#include "message_pkg/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "message_pkg/msg/detail/b_bbackup__functions.h"
#include "message_pkg/msg/detail/b_bbackup__struct.h"


// Include directives for member types
// Member `bbadress`
// Member `buadress`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void BBbackup__rosidl_typesupport_introspection_c__BBbackup_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  message_pkg__msg__BBbackup__init(message_memory);
}

void BBbackup__rosidl_typesupport_introspection_c__BBbackup_fini_function(void * message_memory)
{
  message_pkg__msg__BBbackup__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember BBbackup__rosidl_typesupport_introspection_c__BBbackup_message_member_array[2] = {
  {
    "bbadress",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(message_pkg__msg__BBbackup, bbadress),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "buadress",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(message_pkg__msg__BBbackup, buadress),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers BBbackup__rosidl_typesupport_introspection_c__BBbackup_message_members = {
  "message_pkg__msg",  // message namespace
  "BBbackup",  // message name
  2,  // number of fields
  sizeof(message_pkg__msg__BBbackup),
  BBbackup__rosidl_typesupport_introspection_c__BBbackup_message_member_array,  // message members
  BBbackup__rosidl_typesupport_introspection_c__BBbackup_init_function,  // function to initialize message memory (memory has to be allocated)
  BBbackup__rosidl_typesupport_introspection_c__BBbackup_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t BBbackup__rosidl_typesupport_introspection_c__BBbackup_message_type_support_handle = {
  0,
  &BBbackup__rosidl_typesupport_introspection_c__BBbackup_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_message_pkg
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, message_pkg, msg, BBbackup)() {
  if (!BBbackup__rosidl_typesupport_introspection_c__BBbackup_message_type_support_handle.typesupport_identifier) {
    BBbackup__rosidl_typesupport_introspection_c__BBbackup_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &BBbackup__rosidl_typesupport_introspection_c__BBbackup_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
