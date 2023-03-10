# Generated by Django 2.2.16 on 2023-02-16 13:40

import api.validators
import django.contrib.auth.models
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0011_update_proxy_permissions"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "password",
                    models.CharField(max_length=128, verbose_name="password"),
                ),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        verbose_name="date joined",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "???????????????????????? ?? ?????????? ???????????? ?????? ????????????????????!"
                        },
                        max_length=150,
                        unique=True,
                        validators=[api.validators.username_validator],
                        verbose_name="?????? ????????????????????????",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254,
                        unique=True,
                        verbose_name="?????????????????????? ??????????",
                    ),
                ),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("admin", "??????????????????????????"),
                            ("moderator", "??????????????????"),
                            ("user", "????????????????????????"),
                        ],
                        default="user",
                        max_length=9,
                        verbose_name="????????",
                    ),
                ),
                (
                    "bio",
                    models.TextField(blank=True, verbose_name="??????????????????"),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="??????"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="??????????????"
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "????????????????????????",
                "verbose_name_plural": "????????????????????????",
                "ordering": ("username",),
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddConstraint(
            model_name="user",
            constraint=models.CheckConstraint(
                check=models.Q(_negated=True, username="me"),
                name="name_not_me",
            ),
        ),
    ]
