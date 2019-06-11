from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField , StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.models import Image, AbstractImage, AbstractRendition
from wagtail.images.edit_handlers import ImageChooserPanel

from django.contrib.auth.models import User
import datetime




from . import blocks
# Create your models here.

class BlogPage(Page):
    description = models.CharField(max_length=255, blank=True,)

    content_panels = Page.content_panels + [
        FieldPanel('description', classname="full")
    ]

class PostPage(Page):
    content = StreamField(
        [
            ("simple_richtext", blocks.SimpleRichtextBlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel("content"),
    ]


class CustomImage(AbstractImage):
    # Add any extra fields to image here

    # eg. To add a caption field:
    caption = models.CharField(max_length=255, blank=True)

    admin_form_fields = Image.admin_form_fields + (
        # Then add the field names here to make them appear in the form:
        'caption',
    )


class PostPages(Page):
    author = models.ForeignKey(User,on_delete=models.PROTECT)
    body = RichTextField(blank=True,features=['h2', 'h3', 'bold', 'italic', 'link', 'hr', 'link','document-link'])
    # image = models.ForeignKey(CustomImage, on_delete=models.CASCADE, related_name='renditions',null=True)
    post_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    created = models.DateTimeField(default=datetime.datetime.now,null=True, blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('author'),
        FieldPanel('body', classname="full"),
        ImageChooserPanel('post_image'),

        # FieldPanel('image'),

    ]
