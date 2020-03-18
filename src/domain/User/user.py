from dataclasses import dataclass

from marshmallow import Schema, fields
import marshmallow_dataclass


@dataclass
class User:
    """
    username: str length <= 16
    """

    username: str


UserSchema = marshmallow_dataclass.class_schema(User)
