// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from message_pkg:msg/BBsynch.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "message_pkg/msg/detail/b_bsynch__rosidl_typesupport_introspection_c.h"
#include "message_pkg/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "message_pkg/msg/detail/b_bsynch__functions.h"
#include "message_pkg/msg/detail/b_bsynch__struct.h"


// Include directives for member types
// Member `tasks`
#include "message_pkg/msg/task_msg.h"
// Member `tasks`
#include "message_pkg/msg/detail/task_msg__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void BBsynch__rosidl_typesupport_introspection_c__BBsynch_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  message_pkg__msg__BBsynch__init(message_memory);
}

void BBsynch__rosidl_typesupport_introspection_c__BBsynch_fini_function(void * message_memory)
{
  message_pkg__msg__BBsynch__fini(message_memory);
}

size_t BBsynch__rosidl_typesupport_introspection_c__size_function__TaskMsg__tasks(
  const void * untyped_member)
{
  const message_pkg__msg__TaskMsg__Sequence * member =
    (const message_pkg__msg__TaskMsg__Sequence *)(untyped_member);
  return member->size;
}

const void * BBsynch__rosidl_typesupport_introspection_c__get_const_function__TaskMsg__tasks(
  const void * untyped_member, size_t index)
{
  const message_pkg__msg__TaskMsg__Sequence * member =
    (const message_pkg__msg__TaskMsg__Sequence *)(untyped_member);
  return &member->data[index];
}

void * BBsynch__rosidl_typesupport_introspection_c__get_function__TaskMsg__tasks(
  void * untyped_member, size_t index)
{
  message_pkg__msg__TaskMsg__Sequence * member =
    (message_pkg__msg__TaskMsg__Sequence *)(untyped_member);
  return &member->data[index];
}

bool BBsynch__rosidl_typesupport_introspection_c__resize_function__TaskMsg__tasks(
  void * untyped_member, size_t size)
{
  message_pkg__msg__TaskMsg__Sequence * member =
    (message_pkg__msg__TaskMsg__Sequence *)(untyped_member);
  message_pkg__msg__TaskMsg__Sequence__fini(member);
  return message_pkg__msg__TaskMsg__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember BBsynch__rosidl_typesupport_introspection_c__BBsynch_message_member_array[1] = {
  {
    "tasks",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(message_pkg__msg__BBsynch, tasks),  // bytes offset in struct
    NULL,  // default value
    BBsynch__rosidl_typesupport_introspection_c__size_function__TaskMsg__tasks,  // size() function pointer
    BBsynch__rosidl_typesupport_introspection_c__get_const_function__TaskMsg__tasks,  // get_const(index) function pointer
    BBsynch__rosidl_typesupport_introspection_c__get_function__TaskMsg__tasks,  // get(index) function pointer
    BBsynch__rosidl_typesupport_introspection_c__resize_function__TaskMsg__tasks  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers BBsynch__rosidl_typesupport_introspection_c__BBsynch_message_members = {
  "message_pkg__msg",  // message namespace
  "BBsynch",  // message name
  1,  // number of fields
  sizeof(message_pkg__msg__BBsynch),
  BBsynch__rosidl_typesupport_introspection_c__BBsynch_message_member_array,  // message members
  BBsynch__rosidl_typesupport_introspection_c__BBsynch_init_function,  // function to initialize message memory (memory has to be allocated)
  BBsynch__rosidl_typesupport_introspection_c__BBsynch_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t BBsynch__rosidl_typesupport_introspection_c__BBsynch_message_type_support_handle = {
  0,
  &BBsynch__rosidl_typesupport_introspection_c__BBsynch_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_message_pkg
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, message_pkg, msg, BBsynch)() {
  BBsynch__rosidl_typesupport_introspection_c__BBsynch_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, message_pkg, msg, TaskMsg)();
  if (!BBsynch__rosidl_typesupport_introspection_c__BBsynch_message_type_support_handle.typesupport_identifier) {
    BBsynch__rosidl_typesupport_introspection_c__BBsynch_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &BBsynch__rosidl_typesupport_introspection_c__BBsynch_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
