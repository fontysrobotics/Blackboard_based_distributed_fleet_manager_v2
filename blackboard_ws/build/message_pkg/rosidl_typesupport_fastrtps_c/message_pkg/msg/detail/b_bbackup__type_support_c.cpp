// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from message_pkg:msg/BBbackup.idl
// generated code does not contain a copyright notice
#include "message_pkg/msg/detail/b_bbackup__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "message_pkg/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "message_pkg/msg/detail/b_bbackup__struct.h"
#include "message_pkg/msg/detail/b_bbackup__functions.h"
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

#include "rosidl_runtime_c/string.h"  // bbadress, buadress
#include "rosidl_runtime_c/string_functions.h"  // bbadress, buadress

// forward declare type support functions


using _BBbackup__ros_msg_type = message_pkg__msg__BBbackup;

static bool _BBbackup__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _BBbackup__ros_msg_type * ros_message = static_cast<const _BBbackup__ros_msg_type *>(untyped_ros_message);
  // Field name: bbadress
  {
    const rosidl_runtime_c__String * str = &ros_message->bbadress;
    if (str->capacity == 0 || str->capacity <= str->size) {
      fprintf(stderr, "string capacity not greater than size\n");
      return false;
    }
    if (str->data[str->size] != '\0') {
      fprintf(stderr, "string not null-terminated\n");
      return false;
    }
    cdr << str->data;
  }

  // Field name: buadress
  {
    const rosidl_runtime_c__String * str = &ros_message->buadress;
    if (str->capacity == 0 || str->capacity <= str->size) {
      fprintf(stderr, "string capacity not greater than size\n");
      return false;
    }
    if (str->data[str->size] != '\0') {
      fprintf(stderr, "string not null-terminated\n");
      return false;
    }
    cdr << str->data;
  }

  return true;
}

static bool _BBbackup__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _BBbackup__ros_msg_type * ros_message = static_cast<_BBbackup__ros_msg_type *>(untyped_ros_message);
  // Field name: bbadress
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->bbadress.data) {
      rosidl_runtime_c__String__init(&ros_message->bbadress);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->bbadress,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'bbadress'\n");
      return false;
    }
  }

  // Field name: buadress
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->buadress.data) {
      rosidl_runtime_c__String__init(&ros_message->buadress);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->buadress,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'buadress'\n");
      return false;
    }
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_message_pkg
size_t get_serialized_size_message_pkg__msg__BBbackup(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _BBbackup__ros_msg_type * ros_message = static_cast<const _BBbackup__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name bbadress
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->bbadress.size + 1);
  // field.name buadress
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->buadress.size + 1);

  return current_alignment - initial_alignment;
}

static uint32_t _BBbackup__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_message_pkg__msg__BBbackup(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_message_pkg
size_t max_serialized_size_message_pkg__msg__BBbackup(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: bbadress
  {
    size_t array_size = 1;

    full_bounded = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }
  // member: buadress
  {
    size_t array_size = 1;

    full_bounded = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }

  return current_alignment - initial_alignment;
}

static size_t _BBbackup__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_message_pkg__msg__BBbackup(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_BBbackup = {
  "message_pkg::msg",
  "BBbackup",
  _BBbackup__cdr_serialize,
  _BBbackup__cdr_deserialize,
  _BBbackup__get_serialized_size,
  _BBbackup__max_serialized_size
};

static rosidl_message_type_support_t _BBbackup__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_BBbackup,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, message_pkg, msg, BBbackup)() {
  return &_BBbackup__type_support;
}

#if defined(__cplusplus)
}
#endif
