from django.conf.urls import patterns, url

urlpatterns = patterns(
    'quoteGetter.views',
    url(r'^$', 'index'),
    url(r'^style.css', 'style'),
    url(r'^channel.html', 'channel'),
    url(r'^index/', 'index'),
    url(r'^more/', 'new_quote'),
    url(r'^search/(?P<search_string>\w+)', 'search_for'),
    url(r'^profane/', 'profanity_filter'),
    url(r'^link/', 'link_filter'),
    url(r'^quote/', 'quote_filter'),
    url(r'^music/', 'music_filter'),
    url(r'^new/', 'new_filter'),
    url(r'^get/(?P<quote_hash>\w+)', 'get_specific_quote')
)
