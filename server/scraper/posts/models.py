from django.db import models


class LihkgSon(models.Model):
    lihkgson_id = models.IntegerField(primary_key=True, null=False)
    nickname = models.CharField(max_length=255, null=False)

    class Meta:
        ordering = ['lihkgson_id']
        verbose_name = "連登仔"
        verbose_name_plural = verbose_name


class Post(models.Model):
    imported = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(null=False)
    post_id = models.IntegerField(primary_key=True, null=False)
    author = models.ForeignKey(LihkgSon, related_name='user_posts', on_delete=models.CASCADE)
    topic = models.CharField(max_length=255, null=False)

    class Meta:
        ordering = ['-created']
        verbose_name = "文章"
        verbose_name_plural = verbose_name


class Comment(models.Model):
    created = models.DateTimeField(null=False)
    comment_id = models.CharField(primary_key=True, max_length=255, null=False)
    author = models.ForeignKey(LihkgSon, related_name='user_comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='post_comments', on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-created']
        verbose_name = "回覆"
        verbose_name_plural = verbose_name