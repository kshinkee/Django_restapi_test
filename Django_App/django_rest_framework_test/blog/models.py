from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=32)
    mail = models.EmailField()

    def __repr__(self):
        # Display the primary key and the name.
        # ex) 2: Saskia
        return "{}: {}".format(self.pk, self.name)

    # Apply the same functions of __repr__ to __str__
    __str__ = __repr__


# Entry models
class Entry(models.Model):
    STATUS_DRAFT = "draft"
    STATUS_PUBLIC = "public"
    STATUS_SET = (
        (STATUS_DRAFT, "下書き"),
        (STATUS_PUBLIC, "公開中"),
    )
    title = models.CharField(max_length=128)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_SET, default=STATUS_DRAFT, max_length=8)
    # format
    author = models.ForeignKey(User, related_name='entries', on_delete=models.CASCADE,)
    # ForeignObject, related_query_name, db_constraint




