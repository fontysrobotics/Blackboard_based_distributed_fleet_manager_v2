// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from message_pkg:msg/TaskStateMsg.idl
// generated code does not contain a copyright notice

#ifndef MESSAGE_PKG__MSG__DETAIL__TASK_STATE_MSG__STRUCT_HPP_
#define MESSAGE_PKG__MSG__DETAIL__TASK_STATE_MSG__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__message_pkg__msg__TaskStateMsg __attribute__((deprecated))
#else
# define DEPRECATED__message_pkg__msg__TaskStateMsg __declspec(deprecated)
#endif

namespace message_pkg
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct TaskStateMsg_
{
  using Type = TaskStateMsg_<ContainerAllocator>;

  explicit TaskStateMsg_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->taskid = 0;
      this->taskstate = 0;
    }
  }

  explicit TaskStateMsg_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->taskid = 0;
      this->taskstate = 0;
    }
  }

  // field types and members
  using _taskid_type =
    int16_t;
  _taskid_type taskid;
  using _taskstate_type =
    int16_t;
  _taskstate_type taskstate;

  // setters for named parameter idiom
  Type & set__taskid(
    const int16_t & _arg)
  {
    this->taskid = _arg;
    return *this;
  }
  Type & set__taskstate(
    const int16_t & _arg)
  {
    this->taskstate = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    message_pkg::msg::TaskStateMsg_<ContainerAllocator> *;
  using ConstRawPtr =
    const message_pkg::msg::TaskStateMsg_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<message_pkg::msg::TaskStateMsg_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<message_pkg::msg::TaskStateMsg_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      message_pkg::msg::TaskStateMsg_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<message_pkg::msg::TaskStateMsg_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      message_pkg::msg::TaskStateMsg_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<message_pkg::msg::TaskStateMsg_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<message_pkg::msg::TaskStateMsg_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<message_pkg::msg::TaskStateMsg_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__message_pkg__msg__TaskStateMsg
    std::shared_ptr<message_pkg::msg::TaskStateMsg_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__message_pkg__msg__TaskStateMsg
    std::shared_ptr<message_pkg::msg::TaskStateMsg_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const TaskStateMsg_ & other) const
  {
    if (this->taskid != other.taskid) {
      return false;
    }
    if (this->taskstate != other.taskstate) {
      return false;
    }
    return true;
  }
  bool operator!=(const TaskStateMsg_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct TaskStateMsg_

// alias to use template instance with default allocator
using TaskStateMsg =
  message_pkg::msg::TaskStateMsg_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace message_pkg

#endif  // MESSAGE_PKG__MSG__DETAIL__TASK_STATE_MSG__STRUCT_HPP_
