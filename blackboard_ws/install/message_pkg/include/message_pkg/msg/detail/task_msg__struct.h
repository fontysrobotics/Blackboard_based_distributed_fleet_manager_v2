// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from message_pkg:msg/TaskMsg.idl
// generated code does not contain a copyright notice

#ifndef MESSAGE_PKG__MSG__DETAIL__TASK_MSG__STRUCT_H_
#define MESSAGE_PKG__MSG__DETAIL__TASK_MSG__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'pose'
#include "geometry_msgs/msg/detail/pose__struct.h"

// Struct defined in msg/TaskMsg in the package message_pkg.
typedef struct message_pkg__msg__TaskMsg
{
  int16_t taskid;
  int16_t priority;
  int16_t tasktype;
  int16_t payload;
  int16_t taskstate;
  float cost;
  float energycost;
  int16_t robotid;
  geometry_msgs__msg__Pose__Sequence pose;
} message_pkg__msg__TaskMsg;

// Struct for a sequence of message_pkg__msg__TaskMsg.
typedef struct message_pkg__msg__TaskMsg__Sequence
{
  message_pkg__msg__TaskMsg * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} message_pkg__msg__TaskMsg__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MESSAGE_PKG__MSG__DETAIL__TASK_MSG__STRUCT_H_
