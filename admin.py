from django.contrib import admin
from prebid.models import Item, Bid

class ItemAdmin(admin.ModelAdmin):
	list_display = ('title', 'minimumBid',)
	
class BidAdmin(admin.ModelAdmin):
	list_display = ('item', 'amount', 'name', 'timestamp',)
	
admin.site.register(Item, ItemAdmin)
admin.site.register(Bid, BidAdmin)