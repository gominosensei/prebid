from django.conf.urls import patterns, url

from prebid import views

urlpatterns = patterns('',
	# ex /
    url(r'^$', views.ItemList.as_view()),
	# ex /5/
    url(r'^(?P<item_id>\d+)/$', views.item, name='item'),
	# ex /item/5/bid
	#url(r'^(?P<item_id>\d+)/bid/$', views.bid, name='bid'),
	# ex /foo/5
	#url(r'^foo/(?P<item_id>\d+)/$', views.foo, name='foo'),
	)

