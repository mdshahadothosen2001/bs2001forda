from django.db import models


class SpecializationModel(models.Model):
    ordering_id = models.PositiveSmallIntegerField(unique=True, null=True, blank=True)
    name = models.CharField(max_length=100, unique=True)
    picture = models.URLField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Specialization"
        verbose_name_plural = "Specializations"
        db_table = "specialization"
