// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from message_pkg:msg/BBbackup.idl
// generated code does not contain a copyright notice

#ifndef MESSAGE_PKG__MSG__DETAIL__B_BBACKUP__STRUCT_H_
#define MESSAGE_PKG__MSG__DETAIL__B_BBACKUP__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'bbadress'
// Member 'buadress'
#include "rosidl_runtime_c/string.h"

// Struct defined in msg/BBbackup in the package message_pkg.
typedef struct message_pkg__msg__BBbackup
{
  rosidl_runtime_c__String bbadress;
  rosidl_runtime_c__String buadress;
} message_pkg__msg__BBbackup;

// Struct for a sequence of message_pkg__msg__BBbackup.
typedef struct message_pkg__msg__BBbackup__Sequence
{
  message_pkg__msg__BBbackup * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} message_pkg__msg__BBbackup__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MESSAGE_PKG__MSG__DETAIL__B_BBACKUP__STRUCT_H_
