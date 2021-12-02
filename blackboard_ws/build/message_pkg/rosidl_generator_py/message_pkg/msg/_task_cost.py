# generated from rosidl_generator_py/resource/_idl.py.em
# with input from message_pkg:msg/TaskCost.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_TaskCost(type):
    """Metaclass of message 'TaskCost'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('message_pkg')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'message_pkg.msg.TaskCost')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__task_cost
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__task_cost
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__task_cost
            cls._TYPE_SUPPORT = module.type_support_msg__msg__task_cost
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__task_cost

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class TaskCost(metaclass=Metaclass_TaskCost):
    """Message class 'TaskCost'."""

    __slots__ = [
        '_taskid',
        '_taskcost',
        '_robotid',
        '_energycost',
    ]

    _fields_and_field_types = {
        'taskid': 'int16',
        'taskcost': 'float',
        'robotid': 'int16',
        'energycost': 'float',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('int16'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('int16'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.taskid = kwargs.get('taskid', int())
        self.taskcost = kwargs.get('taskcost', float())
        self.robotid = kwargs.get('robotid', int())
        self.energycost = kwargs.get('energycost', float())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.taskid != other.taskid:
            return False
        if self.taskcost != other.taskcost:
            return False
        if self.robotid != other.robotid:
            return False
        if self.energycost != other.energycost:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def taskid(self):
        """Message field 'taskid'."""
        return self._taskid

    @taskid.setter
    def taskid(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'taskid' field must be of type 'int'"
            assert value >= -32768 and value < 32768, \
                "The 'taskid' field must be an integer in [-32768, 32767]"
        self._taskid = value

    @property
    def taskcost(self):
        """Message field 'taskcost'."""
        return self._taskcost

    @taskcost.setter
    def taskcost(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'taskcost' field must be of type 'float'"
        self._taskcost = value

    @property
    def robotid(self):
        """Message field 'robotid'."""
        return self._robotid

    @robotid.setter
    def robotid(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'robotid' field must be of type 'int'"
            assert value >= -32768 and value < 32768, \
                "The 'robotid' field must be an integer in [-32768, 32767]"
        self._robotid = value

    @property
    def energycost(self):
        """Message field 'energycost'."""
        return self._energycost

    @energycost.setter
    def energycost(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'energycost' field must be of type 'float'"
        self._energycost = value
