// Generated by gencpp from file zed_interfaces/set_led_status.msg
// DO NOT EDIT!


#ifndef ZED_INTERFACES_MESSAGE_SET_LED_STATUS_H
#define ZED_INTERFACES_MESSAGE_SET_LED_STATUS_H

#include <ros/service_traits.h>


#include <zed_interfaces/set_led_statusRequest.h>
#include <zed_interfaces/set_led_statusResponse.h>


namespace zed_interfaces
{

struct set_led_status
{

typedef set_led_statusRequest Request;
typedef set_led_statusResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct set_led_status
} // namespace zed_interfaces


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::zed_interfaces::set_led_status > {
  static const char* value()
  {
    return "bd86bfb1e9db5dfcf2eea2f02bf12142";
  }

  static const char* value(const ::zed_interfaces::set_led_status&) { return value(); }
};

template<>
struct DataType< ::zed_interfaces::set_led_status > {
  static const char* value()
  {
    return "zed_interfaces/set_led_status";
  }

  static const char* value(const ::zed_interfaces::set_led_status&) { return value(); }
};


// service_traits::MD5Sum< ::zed_interfaces::set_led_statusRequest> should match 
// service_traits::MD5Sum< ::zed_interfaces::set_led_status > 
template<>
struct MD5Sum< ::zed_interfaces::set_led_statusRequest>
{
  static const char* value()
  {
    return MD5Sum< ::zed_interfaces::set_led_status >::value();
  }
  static const char* value(const ::zed_interfaces::set_led_statusRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::zed_interfaces::set_led_statusRequest> should match 
// service_traits::DataType< ::zed_interfaces::set_led_status > 
template<>
struct DataType< ::zed_interfaces::set_led_statusRequest>
{
  static const char* value()
  {
    return DataType< ::zed_interfaces::set_led_status >::value();
  }
  static const char* value(const ::zed_interfaces::set_led_statusRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::zed_interfaces::set_led_statusResponse> should match 
// service_traits::MD5Sum< ::zed_interfaces::set_led_status > 
template<>
struct MD5Sum< ::zed_interfaces::set_led_statusResponse>
{
  static const char* value()
  {
    return MD5Sum< ::zed_interfaces::set_led_status >::value();
  }
  static const char* value(const ::zed_interfaces::set_led_statusResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::zed_interfaces::set_led_statusResponse> should match 
// service_traits::DataType< ::zed_interfaces::set_led_status > 
template<>
struct DataType< ::zed_interfaces::set_led_statusResponse>
{
  static const char* value()
  {
    return DataType< ::zed_interfaces::set_led_status >::value();
  }
  static const char* value(const ::zed_interfaces::set_led_statusResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // ZED_INTERFACES_MESSAGE_SET_LED_STATUS_H
