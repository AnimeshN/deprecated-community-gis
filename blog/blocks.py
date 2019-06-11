from wagtail.core import blocks

class RichtextBlock(blocks.RichTextBlock):
    """Richtext with all the features."""

    class Meta:  # noqa
        template = "streams/post_page.html"
        icon = "doc-full"
        label = "Full RichText"


class SimpleRichtextBlock(blocks.RichTextBlock):
    """Richtext without (limited) all the features."""
    def __init__(
       self, required=True, help_text=None, editor="default", features=None, **kwargs
    ):  # noqa
       super().__init__(**kwargs)
       self.features = ["bold", "italic", "link"]

    class Meta:  # noqa
       template = "blog/post_page.html"
       icon = "edit"
       label = "simplerichtext"