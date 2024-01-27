from django import template
from django.db.models import Count, Max
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User

from markdown import markdown
from better_profanity import profanity

from ..models import Post, Comment


register = template.Library()

# Create your custome tags/filters here.
@register.simple_tag() # Return number of posts
def total_posts():
    return Post.published.count()


@register.simple_tag() # Return number of comments
def total_comments():
    return Comment.actives.count()


@register.simple_tag()
def last_post_publish(): # Return publish date of the last post
    return Post.published.last().publish_date


@register.simple_tag()
def most_popular_posts(count=5): # Return list of must popular posts
    # Not a good way to specify popular posts but it's enough for now.
    return Post.published.annotate(comments_count=Count("comments")).order_by(
        "-comments_count"
    )[:count]


@register.simple_tag() # Return longest post
def longest_post():
    return Post.published.order_by("reading_time").last()


@register.simple_tag() # Return shortest post
def shortest_post():
    return Post.published.order_by("reading_time").first()


@register.simple_tag()
def most_active_users(count:int=2): # Return list of most active users
    return User.objects.annotate(post_count=Count("posts")).order_by("-post_count")[:count]


@register.inclusion_tag("partials/latest_posts.html")
def latest_posts(count=5): # Return a list of most recent posts
    posts =  Post.published.all()[:count]
    context = {"l_posts":posts}
    return context


@register.filter(name="markdown")
def to_markdown(text): # Filter, change markdown to html
    return mark_safe(markdown(text))


@register.filter()
def censor(text:str, censor_char:str="*"): # Filter, censor all of the profanity words
    return profanity.censor(text, censor_char)
