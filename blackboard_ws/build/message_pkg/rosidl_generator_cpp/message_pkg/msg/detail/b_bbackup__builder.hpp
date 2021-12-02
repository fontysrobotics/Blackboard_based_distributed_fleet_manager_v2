// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from message_pkg:msg/BBbackup.idl
// generated code does not contain a copyright notice

#ifndef MESSAGE_PKG__MSG__DETAIL__B_BBACKUP__BUILDER_HPP_
#define MESSAGE_PKG__MSG__DETAIL__B_BBACKUP__BUILDER_HPP_

#include "message_pkg/msg/detail/b_bbackup__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace message_pkg
{

namespace msg
{

namespace builder
{

class Init_BBbackup_buadress
{
public:
  explicit Init_BBbackup_buadress(::message_pkg::msg::BBbackup & msg)
  : msg_(msg)
  {}
  ::message_pkg::msg::BBbackup buadress(::message_pkg::msg::BBbackup::_buadress_type arg)
  {
    msg_.buadress = std::move(arg);
    return std::move(msg_);
  }

private:
  ::message_pkg::msg::BBbackup msg_;
};

class Init_BBbackup_bbadress
{
public:
  Init_BBbackup_bbadress()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_BBbackup_buadress bbadress(::message_pkg::msg::BBbackup::_bbadress_type arg)
  {
    msg_.bbadress = std::move(arg);
    return Init_BBbackup_buadress(msg_);
  }

private:
  ::message_pkg::msg::BBbackup msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::message_pkg::msg::BBbackup>()
{
  return message_pkg::msg::builder::Init_BBbackup_bbadress();
}

}  // namespace message_pkg

#endif  // MESSAGE_PKG__MSG__DETAIL__B_BBACKUP__BUILDER_HPP_
