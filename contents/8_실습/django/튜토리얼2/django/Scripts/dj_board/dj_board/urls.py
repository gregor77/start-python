from django.conf.urls import patterns, include, url
from sample_board import views 

  urlpatterns = patterns('',
      # Examples:
      # url(r'^$', 'dj_board.views.home', name='home'),
      # url(r'^dj_board/', include('dj_board.foo.urls')),

      # Uncomment the admin/doc line below to enable admin documentation:
      # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

      # Uncomment the next line to enable the admin:
      # url(r'^admin/', include(admin.site.urls)),
      url(r'/$', views.home), 
  )
