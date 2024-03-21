import base64
import re
from datetime import timedelta
from typing import Any
from urllib.parse import urlparse

import graphene
from graphql import GraphQLError, IntValueNode, StringValueNode, ValueNode, print_ast
from graphql.language import ast


class URL(graphene.Scalar):
    """
    A field whose value conforms to the standard URL format as specified in RFC3986: https://www.ietf.org/rfc/rfc3986.txt.
    """

    @staticmethod
    def validate(value: Any):
        if value is None:
            return value

        url = urlparse(str(value))
        if url.scheme and url.netloc:
            return url.geturl()
        else:
            raise GraphQLError(f"Value is not a valid URL: {value}")

    serialize = validate
    parse_value = validate

    @staticmethod
    def parse_url_literal(value_node: ValueNode):
        if not isinstance(value_node, StringValueNode):
            raise GraphQLError(
                f"Can only validate strings as URLs but got a: {value_node.kind}",
                nodes=value_node,
            )

        return URL.validate(value_node.value)


class Upload(graphene.Scalar):
    """Create scalar that ignores normal serialization/deserialization, since
    that will be handled by the multipart request spec"""

    @staticmethod
    def serialize(value):
        return value

    @staticmethod
    def parse_literal(node):
        return node

    @staticmethod
    def parse_value(value):
        return value


SLUG_REGEX = re.compile(r"^[-a-zA-Z0-9_]+\Z")


class Slug(graphene.Scalar):
    """
    Slug is a newspaper term. A slug is a short label for something, containing only letters, numbers, underscores or hyphens. They’re generally used in URLs.
    """

    @staticmethod
    def validate(value: Any, ast: Any = None):
        if not isinstance(value, str):
            raise GraphQLError(f"Value is not string: {value}", nodes=ast)

        if not SLUG_REGEX.match(value):
            raise GraphQLError(f"Value is not a valid slug: {value}", nodes=ast)

        return value

    serialize = validate
    parse_value = validate

    @staticmethod
    def parse_url_literal(value_node: ValueNode):
        if not isinstance(value_node, StringValueNode):
            raise GraphQLError(
                f"Can only validate strings as Slugs but got a: {value_node.kind}",
                nodes=value_node,
            )

        return Slug.validate(value_node.value)


class PositiveInt(graphene.Scalar):
    """
    Integers that will have a value of 0 or more.
    """

    @staticmethod
    def process_value(value: Any, type: str):
        if value is None:
            return value
        try:
            value = int(value)
        except (TypeError, ValueError):
            raise GraphQLError(f"Value is not a valid {type}: {value}")
        if value < 0:
            raise GraphQLError(f"{type} cannot be less than 0")
        return value

    serialize = lambda value: PositiveInt.process_value(value, "PositiveInt")
    parse_value = lambda value: PositiveInt.process_value(value, "PositiveInt")

    @staticmethod
    def parse_int_literal(value_node: ValueNode):
        if not isinstance(value_node, IntValueNode):
            raise GraphQLError(
                f"Can only validate integers as positive integers but got a: {value_node.kind}",
                nodes=value_node,
            )

        return PositiveInt.process_value(value_node.value, "PositiveInt")


class OrderEnum(graphene.Enum):
    ASC = "ASC"
    DESC = "DESC"


class OrderStringEnum(graphene.Enum):
    ASC = "ASC"
    DESC = "DESC"
    IASC = "IASC"
    IDESC = "IDESC"


IPV4_REGEX = re.compile(
    r"^(?:(?:(?:0?0?[0-9]|0?[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}(?:0?0?[0-9]|0?[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(?:\/(?:[0-9]|[1-2][0-9]|3[0-2]))?)$"
)
IPV6_REGEX = re.compile(
    r"^(?:(?:(?:[0-9A-Fa-f]{1,4}:){6}(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|(?:(?:0?0?[0-9]|0?[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}(?:0?0?[0-9]|0?[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))|::(?:[0-9A-Fa-f]{1,4}:){5}(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|(?:(?:0?0?[0-9]|0?[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}(?:0?0?[0-9]|0?[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))|(?:[0-9A-Fa-f]{1,4})?::(?:[0-9A-Fa-f]{1,4}:){4}(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|(?:(?:0?0?[0-9]|0?[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}(?:0?0?[0-9]|0?[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))|(?:(?:[0-9A-Fa-f]{1,4}:){0,1}[0-9A-Fa-f]{1,4})?::(?:[0-9A-Fa-f]{1,4}:){3}(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|(?:(?:0?0?[0-9]|0?[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}(?:0?0?[0-9]|0?[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))|(?:(?:[0-9A-Fa-f]{1,4}:){0,2}[0-9A-Fa-f]{1,4})?::(?:[0-9A-Fa-f]{1,4}:){2}(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|(?:(?:0?0?[0-9]|0?[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}(?:0?0?[0-9]|0?[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))|(?:(?:[0-9A-Fa-f]{1,4}:){0,3}[0-9A-Fa-f]{1,4})?::[0-9A-Fa-f]{1,4}:(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|(?:(?:0?0?[0-9]|0?[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}(?:0?0?[0-9]|0?[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))|(?:(?:[0-9A-Fa-f]{1,4}:){0,4}[0-9A-Fa-f]{1,4})?::(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|(?:(?:0?0?[0-9]|0?[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}(?:0?0?[0-9]|0?[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))|(?:(?:[0-9A-Fa-f]{1,4}:){0,5}[0-9A-Fa-f]{1,4})?::[0-9A-Fa-f]{1,4}|(?:(?:[0-9A-Fa-f]{1,4}:){0,6}[0-9A-Fa-f]{1,4})?::)(?:\/(?:0?0?[0-9]|0?[1-9][0-9]|1[01][0-9]|12[0-8]))?)$"
)


class IPv6(graphene.Scalar):
    """
    A field whose value is a IPv6 address: https://en.wikipedia.org/wiki/IPv6.
    """

    @staticmethod
    def validate(value: Any, ast: Any = None):
        if not value:
            return value

        if not isinstance(value, str):
            raise GraphQLError(f"Value is not string: {value}", nodes=ast)

        if not IPV6_REGEX.match(value):
            raise GraphQLError(f"Value is not a valid IPv6 address: {value}", nodes=ast)

        return value

    serialize = validate
    parse_value = validate

    @staticmethod
    def parse_ipv6_literal(value_node: ValueNode):
        if not isinstance(value_node, StringValueNode):
            raise GraphQLError(
                f"Can only validate strings as IP addresses but got a: {print_ast(value_node)}",
                nodes=value_node,
            )

        return IPv6.validate(value_node.value, value_node)


class IPv4(graphene.Scalar):
    """
    A field whose value is a IPv4 address: https://en.wikipedia.org/wiki/IPv4.
    """

    @staticmethod
    def validate(value: Any, ast: Any = None):
        if not value:
            return value

        if not isinstance(value, str):
            raise GraphQLError(f"Value is not string: {value}", nodes=ast)

        if not IPV4_REGEX.match(value):
            raise GraphQLError(f"Value is not a valid IPv4 address: {value}", nodes=ast)

        return value

    serialize = validate
    parse_value = validate

    @staticmethod
    def parse_literal(value_node: ValueNode):
        if not isinstance(value_node, StringValueNode):
            raise GraphQLError(
                f"Can only validate strings as IPv4 addresses but got a: {print_ast(value_node)}",
                nodes=value_node,
            )

        return IPv4.validate(value_node.value, value_node)


class IP(graphene.Scalar):
    """
    A field whose value is either an IPv4 or IPv6 address: https://en.wikipedia.org/wiki/IP_address.
    """

    @staticmethod
    def validate(value: Any, ast: Any = None):
        if not value:
            return value

        if not isinstance(value, str):
            raise GraphQLError(f"Value is not string: {value}", nodes=ast)

        if not IPV4_REGEX.match(value) and not IPV6_REGEX.match(value):
            raise GraphQLError(
                f"Value is not a valid IPv4 or IPv6 address: {value}", nodes=ast
            )

        return value

    serialize = validate
    parse_value = validate

    @staticmethod
    def parse_literal(value_node: ValueNode):
        if not isinstance(value_node, StringValueNode):
            raise GraphQLError(
                f"Can only validate strings as IP addresses but got a: {print_ast(value_node)}",
                nodes=value_node,
            )

        return IP.validate(value_node.value, value_node)


class Binary(graphene.Scalar):
    """
    BinaryArray is used to convert a Django BinaryField to the string form
    """

    @staticmethod
    def binary_to_string(value):
        return base64.b64encode(value).decode("utf-8")

    @staticmethod
    def string_to_binary(value):
        return base64.b64decode(value)

    serialize = binary_to_string
    parse_value = string_to_binary

    @classmethod
    def parse_literal(cls, node):
        if isinstance(node, ast.StringValue):
            return cls.string_to_binary(node.value)


class Email(graphene.Scalar):
    """
    A field whose value conforms to the standard
    internet email address format as specified in
    HTML Spec: https://html.spec.whatwg.org/multipage/input.html#valid-e-mail-address.
    """

    @staticmethod
    def validate(value: Any, ast: Any = None):
        EMAIL_ADDRESS_REGEX = re.compile(
            r"^[a-zA-Z0-9.!#$%&\'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
        )

        if not isinstance(value, str):
            raise GraphQLError(f"Value is not string: {value}", nodes=ast)

        if not EMAIL_ADDRESS_REGEX.match(value):
            raise GraphQLError(
                f"Value is not a valid email address: {value}", nodes=ast
            )

        return value

    serialize = validate
    parse_value = validate

    @staticmethod
    def parse_literal(value_node: ValueNode):
        if not isinstance(value_node, StringValueNode):
            raise GraphQLError(
                f"Can only validate strings as email addresses but got a: {print_ast(value_node)}",
                value_node,
            )

        return Email.validate(value_node.value, value_node)


class Duration(graphene.Scalar):
    """
    Duration fields in Django are stored as timedelta in Python,
    and as a duration in the Database. We will represent them as
    a total number of seconds in GraphQL.
    """

    @staticmethod
    def serialize(dt):
        if isinstance(dt, timedelta):
            return dt.total_seconds()
        else:
            raise Exception(f"Expected a timedelta object, but got {repr(dt)}")

    @staticmethod
    def parse_literal(node):
        if isinstance(node, graphene.IntValue):
            return timedelta(seconds=node.value)
        else:
            raise Exception(f"Cannot represent {node} as timedelta.")

    @staticmethod
    def parse_value(value):
        return timedelta(seconds=value)
