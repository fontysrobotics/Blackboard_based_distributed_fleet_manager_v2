// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from message_pkg:msg/TaskCost.idl
// generated code does not contain a copyright notice

#ifndef MESSAGE_PKG__MSG__DETAIL__TASK_COST__BUILDER_HPP_
#define MESSAGE_PKG__MSG__DETAIL__TASK_COST__BUILDER_HPP_

#include "message_pkg/msg/detail/task_cost__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace message_pkg
{

namespace msg
{

namespace builder
{

class Init_TaskCost_energycost
{
public:
  explicit Init_TaskCost_energycost(::message_pkg::msg::TaskCost & msg)
  : msg_(msg)
  {}
  ::message_pkg::msg::TaskCost energycost(::message_pkg::msg::TaskCost::_energycost_type arg)
  {
    msg_.energycost = std::move(arg);
    return std::move(msg_);
  }

private:
  ::message_pkg::msg::TaskCost msg_;
};

class Init_TaskCost_robotid
{
public:
  explicit Init_TaskCost_robotid(::message_pkg::msg::TaskCost & msg)
  : msg_(msg)
  {}
  Init_TaskCost_energycost robotid(::message_pkg::msg::TaskCost::_robotid_type arg)
  {
    msg_.robotid = std::move(arg);
    return Init_TaskCost_energycost(msg_);
  }

private:
  ::message_pkg::msg::TaskCost msg_;
};

class Init_TaskCost_taskcost
{
public:
  explicit Init_TaskCost_taskcost(::message_pkg::msg::TaskCost & msg)
  : msg_(msg)
  {}
  Init_TaskCost_robotid taskcost(::message_pkg::msg::TaskCost::_taskcost_type arg)
  {
    msg_.taskcost = std::move(arg);
    return Init_TaskCost_robotid(msg_);
  }

private:
  ::message_pkg::msg::TaskCost msg_;
};

class Init_TaskCost_taskid
{
public:
  Init_TaskCost_taskid()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TaskCost_taskcost taskid(::message_pkg::msg::TaskCost::_taskid_type arg)
  {
    msg_.taskid = std::move(arg);
    return Init_TaskCost_taskcost(msg_);
  }

private:
  ::message_pkg::msg::TaskCost msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::message_pkg::msg::TaskCost>()
{
  return message_pkg::msg::builder::Init_TaskCost_taskid();
}

}  // namespace message_pkg

#endif  // MESSAGE_PKG__MSG__DETAIL__TASK_COST__BUILDER_HPP_
