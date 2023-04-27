// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from robo_clase22:srv/OddEvenCheck.idl
// generated code does not contain a copyright notice

#ifndef ROBO_CLASE22__SRV__DETAIL__ODD_EVEN_CHECK__TRAITS_HPP_
#define ROBO_CLASE22__SRV__DETAIL__ODD_EVEN_CHECK__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "robo_clase22/srv/detail/odd_even_check__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace robo_clase22
{

namespace srv
{

inline void to_flow_style_yaml(
  const OddEvenCheck_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: number
  {
    out << "number: ";
    rosidl_generator_traits::value_to_yaml(msg.number, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const OddEvenCheck_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: number
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "number: ";
    rosidl_generator_traits::value_to_yaml(msg.number, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const OddEvenCheck_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace robo_clase22

namespace rosidl_generator_traits
{

[[deprecated("use robo_clase22::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const robo_clase22::srv::OddEvenCheck_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  robo_clase22::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use robo_clase22::srv::to_yaml() instead")]]
inline std::string to_yaml(const robo_clase22::srv::OddEvenCheck_Request & msg)
{
  return robo_clase22::srv::to_yaml(msg);
}

template<>
inline const char * data_type<robo_clase22::srv::OddEvenCheck_Request>()
{
  return "robo_clase22::srv::OddEvenCheck_Request";
}

template<>
inline const char * name<robo_clase22::srv::OddEvenCheck_Request>()
{
  return "robo_clase22/srv/OddEvenCheck_Request";
}

template<>
struct has_fixed_size<robo_clase22::srv::OddEvenCheck_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<robo_clase22::srv::OddEvenCheck_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<robo_clase22::srv::OddEvenCheck_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace robo_clase22
{

namespace srv
{

inline void to_flow_style_yaml(
  const OddEvenCheck_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: decision
  {
    out << "decision: ";
    rosidl_generator_traits::value_to_yaml(msg.decision, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const OddEvenCheck_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: decision
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "decision: ";
    rosidl_generator_traits::value_to_yaml(msg.decision, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const OddEvenCheck_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace robo_clase22

namespace rosidl_generator_traits
{

[[deprecated("use robo_clase22::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const robo_clase22::srv::OddEvenCheck_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  robo_clase22::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use robo_clase22::srv::to_yaml() instead")]]
inline std::string to_yaml(const robo_clase22::srv::OddEvenCheck_Response & msg)
{
  return robo_clase22::srv::to_yaml(msg);
}

template<>
inline const char * data_type<robo_clase22::srv::OddEvenCheck_Response>()
{
  return "robo_clase22::srv::OddEvenCheck_Response";
}

template<>
inline const char * name<robo_clase22::srv::OddEvenCheck_Response>()
{
  return "robo_clase22/srv/OddEvenCheck_Response";
}

template<>
struct has_fixed_size<robo_clase22::srv::OddEvenCheck_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<robo_clase22::srv::OddEvenCheck_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<robo_clase22::srv::OddEvenCheck_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<robo_clase22::srv::OddEvenCheck>()
{
  return "robo_clase22::srv::OddEvenCheck";
}

template<>
inline const char * name<robo_clase22::srv::OddEvenCheck>()
{
  return "robo_clase22/srv/OddEvenCheck";
}

template<>
struct has_fixed_size<robo_clase22::srv::OddEvenCheck>
  : std::integral_constant<
    bool,
    has_fixed_size<robo_clase22::srv::OddEvenCheck_Request>::value &&
    has_fixed_size<robo_clase22::srv::OddEvenCheck_Response>::value
  >
{
};

template<>
struct has_bounded_size<robo_clase22::srv::OddEvenCheck>
  : std::integral_constant<
    bool,
    has_bounded_size<robo_clase22::srv::OddEvenCheck_Request>::value &&
    has_bounded_size<robo_clase22::srv::OddEvenCheck_Response>::value
  >
{
};

template<>
struct is_service<robo_clase22::srv::OddEvenCheck>
  : std::true_type
{
};

template<>
struct is_service_request<robo_clase22::srv::OddEvenCheck_Request>
  : std::true_type
{
};

template<>
struct is_service_response<robo_clase22::srv::OddEvenCheck_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // ROBO_CLASE22__SRV__DETAIL__ODD_EVEN_CHECK__TRAITS_HPP_
