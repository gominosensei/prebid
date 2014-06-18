from django import forms

class BidForm(forms.Form):
	#item = models.ForeignKey(Item)
	bidderName = models.CharField(max_length = 255, blank=False)	
	bidderEmail = models.CharField(max_length = 255, blank=True, default='')	
	bidderPhone = models.CharField(max_length = 40, blank=True, default='')	
	amount = models.DecimalField(max_digits=5, decimal_places=2)
	#timestamp = models.DateTimeField(auto_now=True)
