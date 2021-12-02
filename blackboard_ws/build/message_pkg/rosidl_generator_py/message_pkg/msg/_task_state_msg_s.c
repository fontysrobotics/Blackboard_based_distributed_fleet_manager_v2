// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from message_pkg:msg/TaskStateMsg.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "message_pkg/msg/detail/task_state_msg__struct.h"
#include "message_pkg/msg/detail/task_state_msg__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool message_pkg__msg__task_state_msg__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[45];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("message_pkg.msg._task_state_msg.TaskStateMsg", full_classname_dest, 44) == 0);
  }
  message_pkg__msg__TaskStateMsg * ros_message = _ros_message;
  {  // taskid
    PyObject * field = PyObject_GetAttrString(_pymsg, "taskid");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->taskid = (int16_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // taskstate
    PyObject * field = PyObject_GetAttrString(_pymsg, "taskstate");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->taskstate = (int16_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * message_pkg__msg__task_state_msg__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of TaskStateMsg */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("message_pkg.msg._task_state_msg");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "TaskStateMsg");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  message_pkg__msg__TaskStateMsg * ros_message = (message_pkg__msg__TaskStateMsg *)raw_ros_message;
  {  // taskid
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->taskid);
    {
      int rc = PyObject_SetAttrString(_pymessage, "taskid", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // taskstate
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->taskstate);
    {
      int rc = PyObject_SetAttrString(_pymessage, "taskstate", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}