"""hellowebapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

# added chapter 11
from collection.backends import MyRegistrationView #Added Chapter 11

# added chapter 10
from django.contrib.auth.views import (
   password_reset,
   password_reset_done,
   password_reset_confirm,
   password_reset_complete
)
from django.conf.urls import url, include #include added chapter 10
from django.contrib import admin
from django.views.generic import (TemplateView,
    RedirectView,
) #imports Django's TemplateView.  Chapter 4.  Redirect view added Chapter 12.
from collection import views #Import views, chapter 4

urlpatterns = [
    url(r'^$', views.index, name='home'), #url, includes regex, calls views.index, is named 'home'.  Chapter 4
    url(r'^about/$', #url for about.html.  Chapter 5
    TemplateView.as_view(template_name='about.html'),
    name='about'),
    url(r'^contact/$', #url for contact.html.  Chapter 5
        TemplateView.as_view(template_name='contact.html'),
        name='contact'),
    url(r'^projects/$', RedirectView.as_view(pattern_name='browse', permanent=True)), #Redirect, added Chapter 12
    url(r'^projects/(?P<slug>[-\w]+)/$', views.project_detail,
        name='project_detail'), #url for project pages.  Changed thing to project.  Chapter 8
    url(r'^projects/(?P<slug>[-\w]+)/edit/$', #url to edit projects.  Changed thing to project.  Chapter 8.
        views.edit_project,
        name='edit_project'),
        #Added Chapter 10
    url(r'^accounts/password/reset/$', #Added Chapter 10
        password_reset,
        {'template_name':
        'registration/password_reset_form.html'},
        name="password_reset"),
    url(r'^accounts/password/reset/done/$', #Added Chapter 10
        password_reset_done,
        {'template_name':
        'registration/password_reset_done.html'},
        name="password_reset_done"),
    url(r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', #Added Chapter 10
        password_reset_confirm,
        {'template_name':
        'registration/password_reset_confirm.html'},
        name="password_reset_confirm"),
    url(r'^accounts/password/done/$', #Added Chapter 10
        password_reset_complete,
        {'template_name':
        'registration/password_reset_complete.html'},
        name="password_reset_complete"),
    url(r'^browse/$', RedirectView.as_view(pattern_name='browse', permanent=True)), #Redirect from browse.  Added Chapter 12
# our new browse flow Added Chapter 12
    url(r'^browse/name/$',#Browse list. Added Chapter 12
        views.browse_by_name, name='browse'),
    url(r'^browse/name/(?P<initial>[-\w]+)/$', #Browse by first letter Added Chapter 12
        views.browse_by_name, name='browse_by_name'),
    url(r'^accounts/register/$', #Password Reset Urls Added Chapter 11
        MyRegistrationView.as_view(),
        name='registration_register'),
    url(r'^accounts/create_project/$', views.create_project, #added chapter 11
        name='registration_create_project'),
    url(r'^accounts/', include('registration.backends.simple.urls')), #added chapter 10.
    url(r'^admin/', admin.site.urls),
]
