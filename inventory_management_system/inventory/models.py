from django.core.cache import cache
from django.db import models
from django.utils.translation import gettext_lazy as _

from inventory_management_system.users.models import User


class Inventory(models.Model):
    name = models.CharField(_("Name"), max_length=50, unique=True)
    description = models.TextField(_("Description"))
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_inventory",
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.delete("inventory_list")

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        cache.delete("inventory_list")
