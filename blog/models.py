from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.
class Tag(models.Model):
    caption = models.CharField(max_length=50)
    def __str__(self):
        return "{}".format(self.caption)

class Author(models.Model):
    # name=models.CharField(max_length=10,default="qwe")
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    email_id = models.EmailField(default='abc@email.com')

    def __str__(self):
        return "{} {}".format(self.first_name,self.last_name)




class Post(models.Model):
    title = models.CharField(max_length=100,default="notitle")
    summary = models.CharField(max_length=100,null=True)
    image = models.CharField(max_length=100,null=True)
    date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(db_index=True, unique=True)  # coz we are searching by slug to enhance the search
    content = models.TextField(validators=[MinLengthValidator(5)],default="lorem50")
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='posts')
    # to change the default post_set to posts for fetching all posts by an author from POst model.
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return"{} {}".format(self.slug,self.author)


class Comment(models.Model):
    user_name = models.CharField(max_length=50,default="rashmi")
    user_email = models.CharField(max_length=50,null=True)
    text = models.CharField(max_length=500,null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
