#instagram/models.py
from django.core import validators
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.core.validators import MinLengthValidator

class Post(models.Model) : #원하는 설계에 맞춰 작성하면 된다.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField(
        validators = [MinLengthValidator(10)]
    )
    photo = models.ImageField(blank=True, upload_to = 'instagram/post/%Y/%m/%d') 
    #blank=True를 통해 photo를 옵션 필드로 설정할 수 있다.
    is_public = models.BooleanField(default=False, verbose_name="공개 여부")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    tag_set = models.ManyToManyField('Tag', blank = True)

    def __str__(self) : 
        #return f"My Post object ({self.id})"
        #return "My Post object ({})".format(self.id)
        return self.message

    def get_absolute_url(self) : 
        return reverse('instagram:post_detail', args=[self.pk])

    # def message_length(self) : 
    #     return len(self.message)
    # message_length.short_description = "메세지 글자수"

    class Meta : 
        ordering = ['-id']

class Comment(models.Model) : 
    post = models.ForeignKey(Post, on_delete=models.CASCADE, limit_choices_to={'is_public' : True}) #post_id 필드 생성
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

class Tag(models.Model) : 
    name = models.CharField(max_length=50, unique=True)
    #post_set = models.ManyToManyField(Post)
    def __str__(self) : 
        return self.name