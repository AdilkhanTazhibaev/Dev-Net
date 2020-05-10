from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls import url
from django.views.static import serve

urlpatterns = [
    path(
        '',
        include('pages.urls', namespace='pages')
    ),
    path(
        'dev/accounts/',
        include('accounts.urls', namespace='accounts')
    ),
    path(
        'dev/posts/',
        include('posts.urls', namespace='posts')
    ),
    path(
        'dev/posts/',
        include('likes.urls', namespace='likes')
    ),
    path(
        'dev/posts/',
        include('unlikes.urls', namespace='unlikes')
    ),
    path(
        'dev/posts/',
        include('comments.urls', namespace='comments')
    ),
    path(
        'dev/profiles/',
        include('profiles.urls', namespace='profiles')
    ),
    path('admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),

    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]


if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
