from django.utils.translation import gettext as _
from django.conf import settings
from django.db import models




class Post(models.Model):
    content = models.CharField(_('content'), max_length=140)
    creation_date = models.DateTimeField(
        _('creation_date'),
        auto_now_add=True
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('user'),
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')

    def __str__(self):
        return "{:5}(...)".format(self.content)