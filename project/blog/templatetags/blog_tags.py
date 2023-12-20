from django import template
from django.db.models import Count, Max
from markdown import markdown
from django.utils.safestring import mark_safe
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


@register.simple_tag()
def most_popular_posts(count=5):
    # Not a good way to specify popular posts but it's enough for now.
    return Post.published.annotate(comments_count=Count("comments")).order_by(
        "-comments_count"
    )[:count]


@register.simple_tag()
def longest_post():
    return Post.published.order_by("reading_time").last()


@register.simple_tag()
def shortest_post():
    return Post.published.order_by("reading_time").first()


@register.inclusion_tag("partials/latest_posts.html")
def latest_posts(count=5):
    posts =  Post.published.all()[:count]
    context = {"posts":posts}
    return context


@register.filter(name="markdown")
def to_markdown(text):
    return mark_safe(markdown(text))
