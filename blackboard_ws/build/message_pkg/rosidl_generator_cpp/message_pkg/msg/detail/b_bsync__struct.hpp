// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from message_pkg:msg/BBsync.idl
// generated code does not contain a copyright notice

#ifndef MESSAGE_PKG__MSG__DETAIL__B_BSYNC__STRUCT_HPP_
#define MESSAGE_PKG__MSG__DETAIL__B_BSYNC__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


// Include directives for member types
// Member 'tasks'
#include "message_pkg/msg/detail/task_msg__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__message_pkg__msg__BBsync __attribute__((deprecated))
#else
# define DEPRECATED__message_pkg__msg__BBsync __declspec(deprecated)
#endif

namespace message_pkg
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct BBsync_
{
  using Type = BBsync_<ContainerAllocator>;

  explicit BBsync_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
  }

  explicit BBsync_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
    (void)_alloc;
  }

  // field types and members
  using _tasks_type =
    std::vector<message_pkg::msg::TaskMsg_<ContainerAllocator>, typename ContainerAllocator::template rebind<message_pkg::msg::TaskMsg_<ContainerAllocator>>::other>;
  _tasks_type tasks;

  // setters for named parameter idiom
  Type & set__tasks(
    const std::vector<message_pkg::msg::TaskMsg_<ContainerAllocator>, typename ContainerAllocator::template rebind<message_pkg::msg::TaskMsg_<ContainerAllocator>>::other> & _arg)
  {
    this->tasks = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    message_pkg::msg::BBsync_<ContainerAllocator> *;
  using ConstRawPtr =
    const message_pkg::msg::BBsync_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<message_pkg::msg::BBsync_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<message_pkg::msg::BBsync_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      message_pkg::msg::BBsync_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<message_pkg::msg::BBsync_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      message_pkg::msg::BBsync_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<message_pkg::msg::BBsync_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<message_pkg::msg::BBsync_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<message_pkg::msg::BBsync_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__message_pkg__msg__BBsync
    std::shared_ptr<message_pkg::msg::BBsync_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__message_pkg__msg__BBsync
    std::shared_ptr<message_pkg::msg::BBsync_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const BBsync_ & other) const
  {
    if (this->tasks != other.tasks) {
      return false;
    }
    return true;
  }
  bool operator!=(const BBsync_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct BBsync_

// alias to use template instance with default allocator
using BBsync =
  message_pkg::msg::BBsync_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace message_pkg

#endif  // MESSAGE_PKG__MSG__DETAIL__B_BSYNC__STRUCT_HPP_
