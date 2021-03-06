import uuid
from django.db import models
from django.urls import reverse
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager

# Create your models here.


def image_path(_, filename):
    extension = filename.split(".")[-1]
    unique_id = uuid.uuid4().hex
    new_file_name = unique_id + "." + extension
    new_file_name = f"{str(_.publish)}/{str(_.author)}/{new_file_name}"
    return "post/" + new_file_name


class PublishedPost(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="published")


class Post(models.Model):
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published"),
    )
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to=image_path, null=True, blank=True)
    slug = models.SlugField(max_length=250, editable=True, null=True, blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="blog_posts",
        default=1,
    )
    body = RichTextField()
    publish = models.DateField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")

    objects = models.Manager()  # The default manager.
    published = PublishedPost()  # Our custom manager.
    tags = TaggableManager()  # For managing tag
    count = models.IntegerField(default=0)

    class Meta:
        ordering = ("-publish",)
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    @staticmethod
    def draft():
        return Post.objects.all().filter(status="draft")

    def get_absolute_url(self):
        return reverse(
            "blogposts:user_post_list",
            kwargs={
                "author": self.author.username,
                "author_id": self.author.id,
            },
        )


class Comment(models.Model):
    email = models.EmailField(max_length=150)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_comments",
        null=True,
        blank=True,
    )
    comment_content = models.TextField(verbose_name="comment")
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comment_post",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return "" + self.email or "" + " " + self.user or ""

    def get_absolute_url(self):
        return reverse(
            "blogposts:detail",
            kwargs={
                "author": self.post.author.username,
                "author_id": self.post.author.id,
                "slug": self.post.slug,
            },
        )