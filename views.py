from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.views.generic import ListView
from django.forms import ModelForm, HiddenInput
from django.core.exceptions import ValidationError

from prebid.models import Item, Bid

class ItemList(ListView):
	model = Item

def currentHighBid(item):
	bid = Bid.objects.filter(item=item).order_by('-amount').first()
	if bid:
		return bid.amount
	return ''	

class BidForm(ModelForm):
	class Meta:
		model = Bid
		fields = ['item', 'amount', 'name', 'email', 'phone']		
		widgets = {
			'item': HiddenInput(),
		}
		
	def clean(self):
		super(BidForm, self).clean() 
		
		# Make sure the current bid is higher than the highest bid on record for this item
		amount = self.cleaned_data.get('amount')
		item = self.cleaned_data.get('item')
		current_bid = currentHighBid(item)
				
		if amount:
			if current_bid:
				if amount < current_bid+1:
					raise ValidationError('The new bid must be at least $1.00 higher than the current high bid')
			else:
				if amount < item.minimumBid:
					raise ValidationError('The initial bid must be at least the minimum bid')
		
		return self.cleaned_data                            

def item(request, item_id):
	item = get_object_or_404(Item, pk=item_id)

	current_bid = currentHighBid(item)
	
	if request.method == 'POST':
		form = BidForm(request.POST)
		if form.is_valid():
			m = form.save()
			return HttpResponse('whoa, it is valid %s', m.pk)
	else:	
		form = BidForm(initial={'item':item}) 

	return render(request, 'prebid/bidform.html', {
		'form': form,
		'item': item,
		'current_bid': current_bid
	})
 