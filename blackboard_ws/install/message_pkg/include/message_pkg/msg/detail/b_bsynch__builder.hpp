// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from message_pkg:msg/BBsynch.idl
// generated code does not contain a copyright notice

#ifndef MESSAGE_PKG__MSG__DETAIL__B_BSYNCH__BUILDER_HPP_
#define MESSAGE_PKG__MSG__DETAIL__B_BSYNCH__BUILDER_HPP_

#include "message_pkg/msg/detail/b_bsynch__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace message_pkg
{

namespace msg
{

namespace builder
{

class Init_BBsynch_tasks
{
public:
  Init_BBsynch_tasks()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::message_pkg::msg::BBsynch tasks(::message_pkg::msg::BBsynch::_tasks_type arg)
  {
    msg_.tasks = std::move(arg);
    return std::move(msg_);
  }

private:
  ::message_pkg::msg::BBsynch msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::message_pkg::msg::BBsynch>()
{
  return message_pkg::msg::builder::Init_BBsynch_tasks();
}

}  // namespace message_pkg

#endif  // MESSAGE_PKG__MSG__DETAIL__B_BSYNCH__BUILDER_HPP_
