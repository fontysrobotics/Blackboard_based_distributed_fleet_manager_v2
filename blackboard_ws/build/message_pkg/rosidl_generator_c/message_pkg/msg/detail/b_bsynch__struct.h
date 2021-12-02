// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from message_pkg:msg/BBsynch.idl
// generated code does not contain a copyright notice

#ifndef MESSAGE_PKG__MSG__DETAIL__B_BSYNCH__STRUCT_H_
#define MESSAGE_PKG__MSG__DETAIL__B_BSYNCH__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'tasks'
#include "message_pkg/msg/detail/task_msg__struct.h"

// Struct defined in msg/BBsynch in the package message_pkg.
typedef struct message_pkg__msg__BBsynch
{
  message_pkg__msg__TaskMsg__Sequence tasks;
} message_pkg__msg__BBsynch;

// Struct for a sequence of message_pkg__msg__BBsynch.
typedef struct message_pkg__msg__BBsynch__Sequence
{
  message_pkg__msg__BBsynch * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} message_pkg__msg__BBsynch__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MESSAGE_PKG__MSG__DETAIL__B_BSYNCH__STRUCT_H_
