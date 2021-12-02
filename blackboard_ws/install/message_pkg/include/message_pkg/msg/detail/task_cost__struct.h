// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from message_pkg:msg/TaskCost.idl
// generated code does not contain a copyright notice

#ifndef MESSAGE_PKG__MSG__DETAIL__TASK_COST__STRUCT_H_
#define MESSAGE_PKG__MSG__DETAIL__TASK_COST__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/TaskCost in the package message_pkg.
typedef struct message_pkg__msg__TaskCost
{
  int16_t taskid;
  float taskcost;
  int16_t robotid;
  float energycost;
} message_pkg__msg__TaskCost;

// Struct for a sequence of message_pkg__msg__TaskCost.
typedef struct message_pkg__msg__TaskCost__Sequence
{
  message_pkg__msg__TaskCost * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} message_pkg__msg__TaskCost__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MESSAGE_PKG__MSG__DETAIL__TASK_COST__STRUCT_H_
