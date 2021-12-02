// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from message_pkg:msg/TaskStateMsg.idl
// generated code does not contain a copyright notice

#ifndef MESSAGE_PKG__MSG__DETAIL__TASK_STATE_MSG__TRAITS_HPP_
#define MESSAGE_PKG__MSG__DETAIL__TASK_STATE_MSG__TRAITS_HPP_

#include "message_pkg/msg/detail/task_state_msg__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<message_pkg::msg::TaskStateMsg>()
{
  return "message_pkg::msg::TaskStateMsg";
}

template<>
inline const char * name<message_pkg::msg::TaskStateMsg>()
{
  return "message_pkg/msg/TaskStateMsg";
}

template<>
struct has_fixed_size<message_pkg::msg::TaskStateMsg>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<message_pkg::msg::TaskStateMsg>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<message_pkg::msg::TaskStateMsg>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // MESSAGE_PKG__MSG__DETAIL__TASK_STATE_MSG__TRAITS_HPP_
