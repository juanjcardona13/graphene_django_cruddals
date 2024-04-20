import uuid
from datetime import timedelta
from decimal import Decimal

from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models


# region For Test Fields
class ModelA(models.Model):
    binary_field_required = models.BinaryField(editable=True)
    binary_field_not_editable = models.BinaryField()  # editable=False is default
    binary_field_nullable = models.BinaryField(null=True, blank=True, editable=True)
    binary_field_with_default = models.BinaryField(default=b"\x08", editable=True)
    binary_field_with_description = models.BinaryField(
        help_text="binary_field_with_description", editable=True
    )

    boolean_field_required = models.BooleanField()
    boolean_field_not_editable = models.BooleanField(editable=False)
    boolean_field_nullable = models.BooleanField(null=True, blank=True)
    boolean_field_with_default = models.BooleanField(default=True)
    boolean_field_with_description = models.BooleanField(
        help_text="boolean_field_with_description"
    )

    char_field_required = models.CharField(max_length=100)
    char_field_not_editable = models.CharField(max_length=100, editable=False)
    char_field_nullable = models.CharField(max_length=100, null=True, blank=True)
    char_field_with_default = models.CharField(
        max_length=100, default="char_field_with_default"
    )
    char_field_with_description = models.CharField(
        max_length=100, help_text="char_field_with_description"
    )

    choice_field_required = models.CharField(
        max_length=100, choices=[("a", "A"), ("b", "B")]
    )
    choice_field_not_editable = models.CharField(
        max_length=100, choices=[("a", "A"), ("b", "B")], editable=False
    )
    choice_field_nullable = models.CharField(
        max_length=100, choices=[("a", "A"), ("b", "B")], null=True, blank=True
    )
    choice_field_with_default = models.CharField(
        max_length=100, choices=[("a", "A"), ("b", "B")], default="a"
    )
    choice_field_with_description = models.CharField(
        max_length=100,
        choices=[("a", "A"), ("b", "B")],
        help_text="choice_field_with_description",
    )

    date_field_required = models.DateField()
    date_field_not_editable = models.DateField(editable=False)
    date_field_nullable = models.DateField(null=True, blank=True)
    date_field_with_default = models.DateField(auto_now_add=True)
    date_field_with_description = models.DateField(
        help_text="date_field_with_description"
    )

    date_time_field_required = models.DateTimeField()
    date_time_field_not_editable = models.DateTimeField(editable=False)
    date_time_field_nullable = models.DateTimeField(null=True, blank=True)
    date_time_field_with_default = models.DateTimeField(auto_now_add=True)
    date_time_field_with_description = models.DateTimeField(
        help_text="date_time_field_with_description"
    )

    time_field_required = models.TimeField()
    time_field_not_editable = models.TimeField(editable=False)
    time_field_nullable = models.TimeField(null=True, blank=True)
    time_field_with_default = models.TimeField(auto_now_add=True)
    time_field_with_description = models.TimeField(
        help_text="time_field_with_description"
    )

    decimal_field_required = models.DecimalField(max_digits=10, decimal_places=2)
    decimal_field_not_editable = models.DecimalField(
        max_digits=10, decimal_places=2, editable=False
    )
    decimal_field_nullable = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    decimal_field_with_default = models.DecimalField(
        max_digits=10, decimal_places=2, default=Decimal(0.0)
    )
    decimal_field_with_description = models.DecimalField(
        max_digits=10, decimal_places=2, help_text="decimal_field_with_description"
    )

    duration_field_required = models.DurationField()
    duration_field_not_editable = models.DurationField(editable=False)
    duration_field_nullable = models.DurationField(null=True, blank=True)
    duration_field_with_default = models.DurationField(default=timedelta)
    duration_field_with_description = models.DurationField(
        help_text="duration_field_with_description"
    )

    email_field_required = models.EmailField()
    email_field_not_editable = models.EmailField(editable=False)
    email_field_nullable = models.EmailField(null=True, blank=True)
    email_field_with_default = models.EmailField(default="emailField@withDefault.com")
    email_field_with_description = models.EmailField(
        help_text="email_field_with_description"
    )

    float_field_required = models.FloatField()
    float_field_not_editable = models.FloatField(editable=False)
    float_field_nullable = models.FloatField(null=True, blank=True)
    float_field_with_default = models.FloatField(default=0.0)
    float_field_with_description = models.FloatField(
        help_text="float_field_with_description"
    )

    integer_field_required = models.IntegerField()
    integer_field_not_editable = models.IntegerField(editable=False)
    integer_field_nullable = models.IntegerField(null=True, blank=True)
    integer_field_with_default = models.IntegerField(default=0)
    integer_field_with_description = models.IntegerField(
        help_text="integer_field_with_description"
    )

    small_integer_field_required = models.SmallIntegerField()
    small_integer_field_not_editable = models.SmallIntegerField(editable=False)
    small_integer_field_nullable = models.SmallIntegerField(null=True, blank=True)
    small_integer_field_with_default = models.SmallIntegerField(default=0)
    small_integer_field_with_description = models.SmallIntegerField(
        help_text="small_integer_field_with_description"
    )

    positive_integer_field_required = models.PositiveIntegerField()
    positive_integer_field_not_editable = models.PositiveIntegerField(editable=False)
    positive_integer_field_nullable = models.PositiveIntegerField(null=True, blank=True)
    positive_integer_field_with_default = models.PositiveIntegerField(default=0)
    positive_integer_field_with_description = models.PositiveIntegerField(
        help_text="positive_integer_field_with_description"
    )

    slug_field_required = models.SlugField()
    slug_field_not_editable = models.SlugField(editable=False)
    slug_field_nullable = models.SlugField(null=True, blank=True)
    slug_field_with_default = models.SlugField(default="slug_field_with_default")
    slug_field_with_description = models.SlugField(
        help_text="slug_field_with_description"
    )

    text_field_required = models.TextField()
    text_field_not_editable = models.TextField(editable=False)
    text_field_nullable = models.TextField(null=True, blank=True)
    text_field_with_default = models.TextField(default="text_field_with_default")
    text_field_with_description = models.TextField(
        help_text="text_field_with_description"
    )

    url_field_required = models.URLField()
    url_field_not_editable = models.URLField(editable=False)
    url_field_nullable = models.URLField(null=True, blank=True)
    url_field_with_default = models.URLField(
        default="https://url_field_with_default.com"
    )
    url_field_with_description = models.URLField(help_text="url_field_with_description")

    uuid_field_required = models.UUIDField()
    uuid_field_not_editable = models.UUIDField(editable=False)
    uuid_field_nullable = models.UUIDField(null=True, blank=True)
    uuid_field_with_default = models.UUIDField(default=uuid.uuid1)
    uuid_field_with_description = models.UUIDField(
        help_text="uuid_field_with_description"
    )

    foreign_key_field_required = models.ForeignKey(
        "ModelA",
        on_delete=models.CASCADE,
        related_name="foreign_key_related",
    )
    foreign_key_field_nullable = models.ForeignKey(
        "ModelA",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="foreign_key_nullable_related",
    )
    foreign_key_field_with_description = models.ForeignKey(
        "ModelA",
        on_delete=models.CASCADE,
        related_name="foreign_key_with_description_related",
        help_text="foreign_key_field_with_description",
    )
    foreign_key_field_without_related_name = models.ForeignKey(
        "ModelA", on_delete=models.CASCADE, related_name="+"
    )

    one_to_one_field_required = models.OneToOneField(
        "ModelA",
        on_delete=models.CASCADE,
        related_name="one_to_one_related",
    )
    one_to_one_field_nullable = models.OneToOneField(
        "ModelA",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="one_to_one_nullable_related",
    )
    one_to_one_field_with_description = models.OneToOneField(
        "ModelA",
        on_delete=models.CASCADE,
        related_name="one_to_one_with_description_related",
        help_text="one_to_one_field_with_description",
    )
    one_to_one_field_without_related_name = models.OneToOneField(
        "ModelA", on_delete=models.CASCADE, related_name="+"
    )

    many_to_many_field_required = models.ManyToManyField(
        "ModelA", related_name="many_to_many_related"
    )
    many_to_many_field_nullable = models.ManyToManyField(
        "ModelA", blank=True, related_name="many_to_many_nullable_related"
    )
    many_to_many_field_with_description = models.ManyToManyField(
        "ModelA",
        related_name="many_to_many_with_description_related",
        help_text="many_to_many_field_with_description",
    )
    many_to_many_field_without_related_name = models.ManyToManyField(
        "ModelA", related_name="+"
    )

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        help_text="The content type",
        null=True,
        blank=True,
    )  # TODO: limit_choices_to={'model__in': ('nameModel')},
    object_id = models.PositiveIntegerField(
        help_text="The object id", null=True, blank=True
    )

    generic_foreign_key_field = GenericForeignKey("content_type", "object_id")
    generic_relation_field = GenericRelation(
        "ModelA", related_query_name="generic_relation_related"
    )

    # positive_big_integer_field_required = models.PositiveBigIntegerField()
    # positive_big_integer_field_unique = models.PositiveBigIntegerField(unique=True)
    # positive_small_integer_field_required = models.PositiveSmallIntegerField()
    # positive_small_integer_field_unique = models.PositiveSmallIntegerField(unique=True)


class ModelB(models.Model):
    foreign_key_field = models.ForeignKey(
        "ModelA", on_delete=models.CASCADE, related_name="foreign_key_B_related"
    )
    one_to_one_field = models.OneToOneField(
        "ModelA", on_delete=models.CASCADE, related_name="one_to_one_B_related"
    )
    many_to_many_field = models.ManyToManyField(
        "ModelA", related_name="many_to_many_B_related"
    )


# endregion


# region For Test Operations
class ModelC(models.Model):
    char_field = models.CharField(max_length=100)
    integer_field = models.IntegerField(default=1, null=True, blank=True)
    boolean_field = models.BooleanField(null=True, blank=True)
    date_time_field = models.DateTimeField(null=True, blank=True)
    json_field = models.JSONField(null=True, blank=True)
    file_field = models.FileField(null=True, blank=True)
    one_to_one_field = models.OneToOneField(
        "ModelD",
        on_delete=models.CASCADE,
        related_name="one_to_one_C_related",
        null=True,
        blank=True,
    )
    many_to_many_field = models.ManyToManyField(
        "ModelD", related_name="many_to_many_C_related", blank=True
    )
    is_active = models.BooleanField(default=True)


class ModelD(models.Model):
    foreign_key_field = models.ForeignKey(
        "ModelC",
        on_delete=models.CASCADE,
        related_name="foreign_key_D_related",
        null=True,
        blank=True,
    )


class ModelE(models.Model):
    foreign_key_field_deep = models.ForeignKey(
        "ModelD",
        on_delete=models.CASCADE,
        related_name="foreign_key_E_related",
        null=True,
        blank=True,
    )


# endregion
