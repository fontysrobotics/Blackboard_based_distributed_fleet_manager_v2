// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from message_pkg:msg/BBsync.idl
// generated code does not contain a copyright notice

#ifndef MESSAGE_PKG__MSG__DETAIL__B_BSYNC__TRAITS_HPP_
#define MESSAGE_PKG__MSG__DETAIL__B_BSYNC__TRAITS_HPP_

#include "message_pkg/msg/detail/b_bsync__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<message_pkg::msg::BBsync>()
{
  return "message_pkg::msg::BBsync";
}

template<>
inline const char * name<message_pkg::msg::BBsync>()
{
  return "message_pkg/msg/BBsync";
}

template<>
struct has_fixed_size<message_pkg::msg::BBsync>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<message_pkg::msg::BBsync>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<message_pkg::msg::BBsync>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // MESSAGE_PKG__MSG__DETAIL__B_BSYNC__TRAITS_HPP_
