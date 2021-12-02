// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from message_pkg:msg/TaskStateMsg.idl
// generated code does not contain a copyright notice

#ifndef MESSAGE_PKG__MSG__DETAIL__TASK_STATE_MSG__BUILDER_HPP_
#define MESSAGE_PKG__MSG__DETAIL__TASK_STATE_MSG__BUILDER_HPP_

#include "message_pkg/msg/detail/task_state_msg__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace message_pkg
{

namespace msg
{

namespace builder
{

class Init_TaskStateMsg_taskstate
{
public:
  explicit Init_TaskStateMsg_taskstate(::message_pkg::msg::TaskStateMsg & msg)
  : msg_(msg)
  {}
  ::message_pkg::msg::TaskStateMsg taskstate(::message_pkg::msg::TaskStateMsg::_taskstate_type arg)
  {
    msg_.taskstate = std::move(arg);
    return std::move(msg_);
  }

private:
  ::message_pkg::msg::TaskStateMsg msg_;
};

class Init_TaskStateMsg_taskid
{
public:
  Init_TaskStateMsg_taskid()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TaskStateMsg_taskstate taskid(::message_pkg::msg::TaskStateMsg::_taskid_type arg)
  {
    msg_.taskid = std::move(arg);
    return Init_TaskStateMsg_taskstate(msg_);
  }

private:
  ::message_pkg::msg::TaskStateMsg msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::message_pkg::msg::TaskStateMsg>()
{
  return message_pkg::msg::builder::Init_TaskStateMsg_taskid();
}

}  // namespace message_pkg

#endif  // MESSAGE_PKG__MSG__DETAIL__TASK_STATE_MSG__BUILDER_HPP_
