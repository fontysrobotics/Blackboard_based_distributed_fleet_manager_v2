// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from message_pkg:msg/BBsync.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "message_pkg/msg/detail/b_bsync__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace message_pkg
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void BBsync_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) message_pkg::msg::BBsync(_init);
}

void BBsync_fini_function(void * message_memory)
{
  auto typed_message = static_cast<message_pkg::msg::BBsync *>(message_memory);
  typed_message->~BBsync();
}

size_t size_function__BBsync__tasks(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<message_pkg::msg::TaskMsg> *>(untyped_member);
  return member->size();
}

const void * get_const_function__BBsync__tasks(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<message_pkg::msg::TaskMsg> *>(untyped_member);
  return &member[index];
}

void * get_function__BBsync__tasks(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<message_pkg::msg::TaskMsg> *>(untyped_member);
  return &member[index];
}

void resize_function__BBsync__tasks(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<message_pkg::msg::TaskMsg> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember BBsync_message_member_array[1] = {
  {
    "tasks",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<message_pkg::msg::TaskMsg>(),  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(message_pkg::msg::BBsync, tasks),  // bytes offset in struct
    nullptr,  // default value
    size_function__BBsync__tasks,  // size() function pointer
    get_const_function__BBsync__tasks,  // get_const(index) function pointer
    get_function__BBsync__tasks,  // get(index) function pointer
    resize_function__BBsync__tasks  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers BBsync_message_members = {
  "message_pkg::msg",  // message namespace
  "BBsync",  // message name
  1,  // number of fields
  sizeof(message_pkg::msg::BBsync),
  BBsync_message_member_array,  // message members
  BBsync_init_function,  // function to initialize message memory (memory has to be allocated)
  BBsync_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t BBsync_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &BBsync_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace message_pkg


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<message_pkg::msg::BBsync>()
{
  return &::message_pkg::msg::rosidl_typesupport_introspection_cpp::BBsync_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, message_pkg, msg, BBsync)() {
  return &::message_pkg::msg::rosidl_typesupport_introspection_cpp::BBsync_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
