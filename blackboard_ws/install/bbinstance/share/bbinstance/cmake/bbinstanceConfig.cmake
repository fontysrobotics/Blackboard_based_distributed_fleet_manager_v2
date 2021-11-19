# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_bbinstance_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED bbinstance_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(bbinstance_FOUND FALSE)
  elseif(NOT bbinstance_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(bbinstance_FOUND FALSE)
  endif()
  return()
endif()
set(_bbinstance_CONFIG_INCLUDED TRUE)

# output package information
if(NOT bbinstance_FIND_QUIETLY)
  message(STATUS "Found bbinstance: 0.0.0 (${bbinstance_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'bbinstance' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${bbinstance_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(bbinstance_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${bbinstance_DIR}/${_extra}")
endforeach()
