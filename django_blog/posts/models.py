from django.db import models
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _

User = get_user_model()

class STATUS_CHOICES(models.TextChoices):
        DRAFT = 'DRAFT', _('DRAFT')
        PUBLISHED = 'PUBLISHED', _('PUBLISHED')


class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(status=STATUS_CHOICES.PUBLISHED)

    def draft(self):
        return self.filter(status=STATUS_CHOICES.DRAFT)

    def search(self, query):
        return self.filter(
            Q(title_icontains=query) |
            Q(content_icontains=query)
        )

class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()

    def draft(self):
        return self.get_queryset().draft()

    def search(self, query):
        return self.get_queryset().search(query)

    def new(self, fields):
        self.model.create(**fields)


# Create your models here.
class Post(models.Model):
    title = models.CharField("Title", max_length=255, blank=False, null=False)
    slug = models.CharField("Slug", max_length=255, unique=True, blank=True, null=True)
    content = models.TextField("Content", max_length=10000, blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    status = models.CharField(max_length=100, choices=STATUS_CHOICES.choices, default=STATUS_CHOICES.DRAFT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = PostManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = ['-created_at']
