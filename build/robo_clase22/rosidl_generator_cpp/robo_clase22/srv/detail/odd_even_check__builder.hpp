// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from robo_clase22:srv/OddEvenCheck.idl
// generated code does not contain a copyright notice

#ifndef ROBO_CLASE22__SRV__DETAIL__ODD_EVEN_CHECK__BUILDER_HPP_
#define ROBO_CLASE22__SRV__DETAIL__ODD_EVEN_CHECK__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "robo_clase22/srv/detail/odd_even_check__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace robo_clase22
{

namespace srv
{

namespace builder
{

class Init_OddEvenCheck_Request_number
{
public:
  Init_OddEvenCheck_Request_number()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::robo_clase22::srv::OddEvenCheck_Request number(::robo_clase22::srv::OddEvenCheck_Request::_number_type arg)
  {
    msg_.number = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robo_clase22::srv::OddEvenCheck_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::robo_clase22::srv::OddEvenCheck_Request>()
{
  return robo_clase22::srv::builder::Init_OddEvenCheck_Request_number();
}

}  // namespace robo_clase22


namespace robo_clase22
{

namespace srv
{

namespace builder
{

class Init_OddEvenCheck_Response_decision
{
public:
  Init_OddEvenCheck_Response_decision()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::robo_clase22::srv::OddEvenCheck_Response decision(::robo_clase22::srv::OddEvenCheck_Response::_decision_type arg)
  {
    msg_.decision = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robo_clase22::srv::OddEvenCheck_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::robo_clase22::srv::OddEvenCheck_Response>()
{
  return robo_clase22::srv::builder::Init_OddEvenCheck_Response_decision();
}

}  // namespace robo_clase22

#endif  // ROBO_CLASE22__SRV__DETAIL__ODD_EVEN_CHECK__BUILDER_HPP_
