from django.conf.urls import patterns, url

from prebid import views

urlpatterns = patterns('',
	# List all the items up for auction
	# ex /
    url(r'^$', views.ItemList.as_view()),
    # Show details of a single item and bid on it
	# ex /5/
    url(r'^(?P<item_id>\d+)/$', views.item, name='item'),
    # Show all current bids
    # ex /bids
    #url(r'^bids/$', views.bids, name='bids'),
    # Show all current bids on a specific item
    # ex /bids?item=5
    #url(r'^bids?item=(?P<item_id>\d+)/$', views.bids, name='bid_details'),    
	)

