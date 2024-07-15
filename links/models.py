from django.db import models


class Link(models.Model):
    original_url = models.URLField(verbose_name='Original URL')
    shortened_link = models.CharField(verbose_name='Shortened URL', max_length=7, unique=True, blank=True)
    
    # Override default insert method to ignore shortened_url field as it is being generated on the DB
    def _do_insert(self, manager, using, fields, update_pk, raw):
        return super(Link, self)._do_insert(
            manager, using,
            [f for f in fields if f.attname not in ['shortened_link']],
            update_pk, raw)

    def __str__(self) -> str:
        return f'{self.shortened_link} -> {self.original_url}'

class Click(models.Model):
    source_ip = models.GenericIPAddressField()
    time = models.TimeField(auto_now=True)
    link = models.ForeignKey(Link, on_delete=models.CASCADE)
    