// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from message_pkg:msg/TaskCost.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "message_pkg/msg/detail/task_cost__rosidl_typesupport_introspection_c.h"
#include "message_pkg/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "message_pkg/msg/detail/task_cost__functions.h"
#include "message_pkg/msg/detail/task_cost__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void TaskCost__rosidl_typesupport_introspection_c__TaskCost_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  message_pkg__msg__TaskCost__init(message_memory);
}

void TaskCost__rosidl_typesupport_introspection_c__TaskCost_fini_function(void * message_memory)
{
  message_pkg__msg__TaskCost__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember TaskCost__rosidl_typesupport_introspection_c__TaskCost_message_member_array[4] = {
  {
    "taskid",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT16,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(message_pkg__msg__TaskCost, taskid),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "taskcost",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(message_pkg__msg__TaskCost, taskcost),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "robotid",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT16,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(message_pkg__msg__TaskCost, robotid),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "energycost",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(message_pkg__msg__TaskCost, energycost),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers TaskCost__rosidl_typesupport_introspection_c__TaskCost_message_members = {
  "message_pkg__msg",  // message namespace
  "TaskCost",  // message name
  4,  // number of fields
  sizeof(message_pkg__msg__TaskCost),
  TaskCost__rosidl_typesupport_introspection_c__TaskCost_message_member_array,  // message members
  TaskCost__rosidl_typesupport_introspection_c__TaskCost_init_function,  // function to initialize message memory (memory has to be allocated)
  TaskCost__rosidl_typesupport_introspection_c__TaskCost_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t TaskCost__rosidl_typesupport_introspection_c__TaskCost_message_type_support_handle = {
  0,
  &TaskCost__rosidl_typesupport_introspection_c__TaskCost_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_message_pkg
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, message_pkg, msg, TaskCost)() {
  if (!TaskCost__rosidl_typesupport_introspection_c__TaskCost_message_type_support_handle.typesupport_identifier) {
    TaskCost__rosidl_typesupport_introspection_c__TaskCost_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &TaskCost__rosidl_typesupport_introspection_c__TaskCost_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
