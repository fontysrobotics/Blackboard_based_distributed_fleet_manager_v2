// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from message_pkg:msg/TaskMsg.idl
// generated code does not contain a copyright notice
#include "message_pkg/msg/detail/task_msg__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `pose`
#include "geometry_msgs/msg/detail/pose__functions.h"

bool
message_pkg__msg__TaskMsg__init(message_pkg__msg__TaskMsg * msg)
{
  if (!msg) {
    return false;
  }
  // taskid
  // priority
  // tasktype
  // payload
  // taskstate
  // cost
  // energycost
  // robotid
  // pose
  if (!geometry_msgs__msg__Pose__Sequence__init(&msg->pose, 0)) {
    message_pkg__msg__TaskMsg__fini(msg);
    return false;
  }
  return true;
}

void
message_pkg__msg__TaskMsg__fini(message_pkg__msg__TaskMsg * msg)
{
  if (!msg) {
    return;
  }
  // taskid
  // priority
  // tasktype
  // payload
  // taskstate
  // cost
  // energycost
  // robotid
  // pose
  geometry_msgs__msg__Pose__Sequence__fini(&msg->pose);
}

message_pkg__msg__TaskMsg *
message_pkg__msg__TaskMsg__create()
{
  message_pkg__msg__TaskMsg * msg = (message_pkg__msg__TaskMsg *)malloc(sizeof(message_pkg__msg__TaskMsg));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(message_pkg__msg__TaskMsg));
  bool success = message_pkg__msg__TaskMsg__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
message_pkg__msg__TaskMsg__destroy(message_pkg__msg__TaskMsg * msg)
{
  if (msg) {
    message_pkg__msg__TaskMsg__fini(msg);
  }
  free(msg);
}


bool
message_pkg__msg__TaskMsg__Sequence__init(message_pkg__msg__TaskMsg__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  message_pkg__msg__TaskMsg * data = NULL;
  if (size) {
    data = (message_pkg__msg__TaskMsg *)calloc(size, sizeof(message_pkg__msg__TaskMsg));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = message_pkg__msg__TaskMsg__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        message_pkg__msg__TaskMsg__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
message_pkg__msg__TaskMsg__Sequence__fini(message_pkg__msg__TaskMsg__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      message_pkg__msg__TaskMsg__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

message_pkg__msg__TaskMsg__Sequence *
message_pkg__msg__TaskMsg__Sequence__create(size_t size)
{
  message_pkg__msg__TaskMsg__Sequence * array = (message_pkg__msg__TaskMsg__Sequence *)malloc(sizeof(message_pkg__msg__TaskMsg__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = message_pkg__msg__TaskMsg__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
message_pkg__msg__TaskMsg__Sequence__destroy(message_pkg__msg__TaskMsg__Sequence * array)
{
  if (array) {
    message_pkg__msg__TaskMsg__Sequence__fini(array);
  }
  free(array);
}
