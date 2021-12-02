// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from message_pkg:msg/TaskCost.idl
// generated code does not contain a copyright notice
#include "message_pkg/msg/detail/task_cost__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "message_pkg/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "message_pkg/msg/detail/task_cost__struct.h"
#include "message_pkg/msg/detail/task_cost__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif


// forward declare type support functions


using _TaskCost__ros_msg_type = message_pkg__msg__TaskCost;

static bool _TaskCost__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _TaskCost__ros_msg_type * ros_message = static_cast<const _TaskCost__ros_msg_type *>(untyped_ros_message);
  // Field name: taskid
  {
    cdr << ros_message->taskid;
  }

  // Field name: taskcost
  {
    cdr << ros_message->taskcost;
  }

  // Field name: robotid
  {
    cdr << ros_message->robotid;
  }

  // Field name: energycost
  {
    cdr << ros_message->energycost;
  }

  return true;
}

static bool _TaskCost__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _TaskCost__ros_msg_type * ros_message = static_cast<_TaskCost__ros_msg_type *>(untyped_ros_message);
  // Field name: taskid
  {
    cdr >> ros_message->taskid;
  }

  // Field name: taskcost
  {
    cdr >> ros_message->taskcost;
  }

  // Field name: robotid
  {
    cdr >> ros_message->robotid;
  }

  // Field name: energycost
  {
    cdr >> ros_message->energycost;
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_message_pkg
size_t get_serialized_size_message_pkg__msg__TaskCost(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _TaskCost__ros_msg_type * ros_message = static_cast<const _TaskCost__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name taskid
  {
    size_t item_size = sizeof(ros_message->taskid);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name taskcost
  {
    size_t item_size = sizeof(ros_message->taskcost);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name robotid
  {
    size_t item_size = sizeof(ros_message->robotid);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name energycost
  {
    size_t item_size = sizeof(ros_message->energycost);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _TaskCost__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_message_pkg__msg__TaskCost(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_message_pkg
size_t max_serialized_size_message_pkg__msg__TaskCost(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: taskid
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint16_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint16_t));
  }
  // member: taskcost
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: robotid
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint16_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint16_t));
  }
  // member: energycost
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  return current_alignment - initial_alignment;
}

static size_t _TaskCost__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_message_pkg__msg__TaskCost(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_TaskCost = {
  "message_pkg::msg",
  "TaskCost",
  _TaskCost__cdr_serialize,
  _TaskCost__cdr_deserialize,
  _TaskCost__get_serialized_size,
  _TaskCost__max_serialized_size
};

static rosidl_message_type_support_t _TaskCost__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_TaskCost,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, message_pkg, msg, TaskCost)() {
  return &_TaskCost__type_support;
}

#if defined(__cplusplus)
}
#endif
