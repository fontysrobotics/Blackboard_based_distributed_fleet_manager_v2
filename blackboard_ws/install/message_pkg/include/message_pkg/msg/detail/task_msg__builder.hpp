// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from message_pkg:msg/TaskMsg.idl
// generated code does not contain a copyright notice

#ifndef MESSAGE_PKG__MSG__DETAIL__TASK_MSG__BUILDER_HPP_
#define MESSAGE_PKG__MSG__DETAIL__TASK_MSG__BUILDER_HPP_

#include "message_pkg/msg/detail/task_msg__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace message_pkg
{

namespace msg
{

namespace builder
{

class Init_TaskMsg_pose
{
public:
  explicit Init_TaskMsg_pose(::message_pkg::msg::TaskMsg & msg)
  : msg_(msg)
  {}
  ::message_pkg::msg::TaskMsg pose(::message_pkg::msg::TaskMsg::_pose_type arg)
  {
    msg_.pose = std::move(arg);
    return std::move(msg_);
  }

private:
  ::message_pkg::msg::TaskMsg msg_;
};

class Init_TaskMsg_robotid
{
public:
  explicit Init_TaskMsg_robotid(::message_pkg::msg::TaskMsg & msg)
  : msg_(msg)
  {}
  Init_TaskMsg_pose robotid(::message_pkg::msg::TaskMsg::_robotid_type arg)
  {
    msg_.robotid = std::move(arg);
    return Init_TaskMsg_pose(msg_);
  }

private:
  ::message_pkg::msg::TaskMsg msg_;
};

class Init_TaskMsg_energycost
{
public:
  explicit Init_TaskMsg_energycost(::message_pkg::msg::TaskMsg & msg)
  : msg_(msg)
  {}
  Init_TaskMsg_robotid energycost(::message_pkg::msg::TaskMsg::_energycost_type arg)
  {
    msg_.energycost = std::move(arg);
    return Init_TaskMsg_robotid(msg_);
  }

private:
  ::message_pkg::msg::TaskMsg msg_;
};

class Init_TaskMsg_cost
{
public:
  explicit Init_TaskMsg_cost(::message_pkg::msg::TaskMsg & msg)
  : msg_(msg)
  {}
  Init_TaskMsg_energycost cost(::message_pkg::msg::TaskMsg::_cost_type arg)
  {
    msg_.cost = std::move(arg);
    return Init_TaskMsg_energycost(msg_);
  }

private:
  ::message_pkg::msg::TaskMsg msg_;
};

class Init_TaskMsg_taskstate
{
public:
  explicit Init_TaskMsg_taskstate(::message_pkg::msg::TaskMsg & msg)
  : msg_(msg)
  {}
  Init_TaskMsg_cost taskstate(::message_pkg::msg::TaskMsg::_taskstate_type arg)
  {
    msg_.taskstate = std::move(arg);
    return Init_TaskMsg_cost(msg_);
  }

private:
  ::message_pkg::msg::TaskMsg msg_;
};

class Init_TaskMsg_payload
{
public:
  explicit Init_TaskMsg_payload(::message_pkg::msg::TaskMsg & msg)
  : msg_(msg)
  {}
  Init_TaskMsg_taskstate payload(::message_pkg::msg::TaskMsg::_payload_type arg)
  {
    msg_.payload = std::move(arg);
    return Init_TaskMsg_taskstate(msg_);
  }

private:
  ::message_pkg::msg::TaskMsg msg_;
};

class Init_TaskMsg_tasktype
{
public:
  explicit Init_TaskMsg_tasktype(::message_pkg::msg::TaskMsg & msg)
  : msg_(msg)
  {}
  Init_TaskMsg_payload tasktype(::message_pkg::msg::TaskMsg::_tasktype_type arg)
  {
    msg_.tasktype = std::move(arg);
    return Init_TaskMsg_payload(msg_);
  }

private:
  ::message_pkg::msg::TaskMsg msg_;
};

class Init_TaskMsg_priority
{
public:
  explicit Init_TaskMsg_priority(::message_pkg::msg::TaskMsg & msg)
  : msg_(msg)
  {}
  Init_TaskMsg_tasktype priority(::message_pkg::msg::TaskMsg::_priority_type arg)
  {
    msg_.priority = std::move(arg);
    return Init_TaskMsg_tasktype(msg_);
  }

private:
  ::message_pkg::msg::TaskMsg msg_;
};

class Init_TaskMsg_taskid
{
public:
  Init_TaskMsg_taskid()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TaskMsg_priority taskid(::message_pkg::msg::TaskMsg::_taskid_type arg)
  {
    msg_.taskid = std::move(arg);
    return Init_TaskMsg_priority(msg_);
  }

private:
  ::message_pkg::msg::TaskMsg msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::message_pkg::msg::TaskMsg>()
{
  return message_pkg::msg::builder::Init_TaskMsg_taskid();
}

}  // namespace message_pkg

#endif  // MESSAGE_PKG__MSG__DETAIL__TASK_MSG__BUILDER_HPP_
