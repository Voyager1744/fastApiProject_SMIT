from tortoise import Model, fields


class Insurance(Model):
    """Модель страхования"""

    cargo_type = fields.CharField(max_length=255)
    declared_value = fields.DecimalField(max_digits=10, decimal_places=2)
