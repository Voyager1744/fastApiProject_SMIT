from tortoise import Model, fields
from tortoise.contrib.pydantic import pydantic_model_creator


class Insurance(Model):
    cargo_type = fields.CharField(max_length=255)
    declared_value = fields.DecimalField(max_digits=10, decimal_places=2)
