// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from message_pkg:msg/BBsynch.idl
// generated code does not contain a copyright notice

#ifndef MESSAGE_PKG__MSG__DETAIL__B_BSYNCH__TRAITS_HPP_
#define MESSAGE_PKG__MSG__DETAIL__B_BSYNCH__TRAITS_HPP_

#include "message_pkg/msg/detail/b_bsynch__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<message_pkg::msg::BBsynch>()
{
  return "message_pkg::msg::BBsynch";
}

template<>
inline const char * name<message_pkg::msg::BBsynch>()
{
  return "message_pkg/msg/BBsynch";
}

template<>
struct has_fixed_size<message_pkg::msg::BBsynch>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<message_pkg::msg::BBsynch>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<message_pkg::msg::BBsynch>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // MESSAGE_PKG__MSG__DETAIL__B_BSYNCH__TRAITS_HPP_
