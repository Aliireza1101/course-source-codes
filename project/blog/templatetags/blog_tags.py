from django import template
from ..models import Post, Comment


register = template.Library()

@register.simple_tag()
def total_posts():
    return Post.published.count()


@register.simple_tag()
def total_comments():
    return Comment.actives.count()


@register.simple_tag()
def last_post_publish():
    return Post.published.last().publish_date


@register.inclusion_tag("partials/latest_posts.html")
def latest_posts(count=5):
    posts =  Post.published.all()[:count]
    context = {"posts":posts}
    return context