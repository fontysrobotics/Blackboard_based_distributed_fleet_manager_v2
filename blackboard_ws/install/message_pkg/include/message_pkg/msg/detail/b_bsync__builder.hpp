// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from message_pkg:msg/BBsync.idl
// generated code does not contain a copyright notice

#ifndef MESSAGE_PKG__MSG__DETAIL__B_BSYNC__BUILDER_HPP_
#define MESSAGE_PKG__MSG__DETAIL__B_BSYNC__BUILDER_HPP_

#include "message_pkg/msg/detail/b_bsync__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace message_pkg
{

namespace msg
{

namespace builder
{

class Init_BBsync_tasks
{
public:
  Init_BBsync_tasks()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::message_pkg::msg::BBsync tasks(::message_pkg::msg::BBsync::_tasks_type arg)
  {
    msg_.tasks = std::move(arg);
    return std::move(msg_);
  }

private:
  ::message_pkg::msg::BBsync msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::message_pkg::msg::BBsync>()
{
  return message_pkg::msg::builder::Init_BBsync_tasks();
}

}  // namespace message_pkg

#endif  // MESSAGE_PKG__MSG__DETAIL__B_BSYNC__BUILDER_HPP_
