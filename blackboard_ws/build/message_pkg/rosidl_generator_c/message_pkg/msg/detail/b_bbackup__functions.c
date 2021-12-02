// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from message_pkg:msg/BBbackup.idl
// generated code does not contain a copyright notice
#include "message_pkg/msg/detail/b_bbackup__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `bbadress`
// Member `buadress`
#include "rosidl_runtime_c/string_functions.h"

bool
message_pkg__msg__BBbackup__init(message_pkg__msg__BBbackup * msg)
{
  if (!msg) {
    return false;
  }
  // bbadress
  if (!rosidl_runtime_c__String__init(&msg->bbadress)) {
    message_pkg__msg__BBbackup__fini(msg);
    return false;
  }
  // buadress
  if (!rosidl_runtime_c__String__init(&msg->buadress)) {
    message_pkg__msg__BBbackup__fini(msg);
    return false;
  }
  return true;
}

void
message_pkg__msg__BBbackup__fini(message_pkg__msg__BBbackup * msg)
{
  if (!msg) {
    return;
  }
  // bbadress
  rosidl_runtime_c__String__fini(&msg->bbadress);
  // buadress
  rosidl_runtime_c__String__fini(&msg->buadress);
}

message_pkg__msg__BBbackup *
message_pkg__msg__BBbackup__create()
{
  message_pkg__msg__BBbackup * msg = (message_pkg__msg__BBbackup *)malloc(sizeof(message_pkg__msg__BBbackup));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(message_pkg__msg__BBbackup));
  bool success = message_pkg__msg__BBbackup__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
message_pkg__msg__BBbackup__destroy(message_pkg__msg__BBbackup * msg)
{
  if (msg) {
    message_pkg__msg__BBbackup__fini(msg);
  }
  free(msg);
}


bool
message_pkg__msg__BBbackup__Sequence__init(message_pkg__msg__BBbackup__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  message_pkg__msg__BBbackup * data = NULL;
  if (size) {
    data = (message_pkg__msg__BBbackup *)calloc(size, sizeof(message_pkg__msg__BBbackup));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = message_pkg__msg__BBbackup__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        message_pkg__msg__BBbackup__fini(&data[i - 1]);
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
message_pkg__msg__BBbackup__Sequence__fini(message_pkg__msg__BBbackup__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      message_pkg__msg__BBbackup__fini(&array->data[i]);
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

message_pkg__msg__BBbackup__Sequence *
message_pkg__msg__BBbackup__Sequence__create(size_t size)
{
  message_pkg__msg__BBbackup__Sequence * array = (message_pkg__msg__BBbackup__Sequence *)malloc(sizeof(message_pkg__msg__BBbackup__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = message_pkg__msg__BBbackup__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
message_pkg__msg__BBbackup__Sequence__destroy(message_pkg__msg__BBbackup__Sequence * array)
{
  if (array) {
    message_pkg__msg__BBbackup__Sequence__fini(array);
  }
  free(array);
}
