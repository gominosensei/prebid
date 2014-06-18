from django.db import models
from django.utils import timezone
from django.utils.encoding import smart_text
from django.core.validators import EMPTY_VALUES
from django.core.exceptions import ValidationError
from django import forms

import re
phone_digits_re = re.compile(r'^(?:1-?)?(\d{3})[-\.]?(\d{3})[-\.]?(\d{4})$')

class Item(models.Model):
	title = models.CharField(max_length = 255, blank=False)	
	photo = models.ImageField(upload_to='auction_items', null=True)
	description = models.TextField(blank=True, default='')	
	minimumBid = models.DecimalField(max_digits=5, decimal_places=2, null=True)
	
	def __str__(self):
		return self.title

class USPhoneNumberField(forms.CharField):
	# Copied from django.contrib.localflavor
	"""
	A form field that validates input as a U.S. phone number.
	"""
	default_error_messages = {
		'invalid': ('Phone numbers must be in XXX-XXX-XXXX format.',)
	}

	def clean(self, value):
		super(USPhoneNumberField, self).clean(value)
		if value in EMPTY_VALUES:
			return ''
		value = re.sub('(\(|\)|\s+)', '', smart_text(value))
		m = phone_digits_re.search(value)
		if m:
			return '%s-%s-%s' % (m.group(1), m.group(2), m.group(3))
		raise ValidationError(self.error_messages['invalid'])

class PhoneNumberField(models.CharField):
	# Copied from django.contrib.localflavor
	from south.modelsinspector import add_introspection_rules
	"""
	A :class:`~django.db.models.CharField` that checks that the value
	is a valid U.S.A.-style phone number (in the format ``XXX-XXX-XXXX``).
	"""
	description = ("Phone number")
	add_introspection_rules([], ["^prebid\.models\.PhoneNumberField"])

	def __init__(self, *args, **kwargs):
		kwargs['max_length'] = 20
		super(PhoneNumberField, self).__init__(*args, **kwargs)

	def formfield(self, **kwargs):
		#from localflavor.us.forms import USPhoneNumberField
		defaults = {'form_class': USPhoneNumberField}
		defaults.update(kwargs)
		return super(PhoneNumberField, self).formfield(**defaults)

class Bid(models.Model):
	item = models.ForeignKey(Item)
	amount = models.DecimalField(max_digits=5, decimal_places=2)

	name = models.CharField(max_length = 255, blank=False)	
	email = models.EmailField(blank=True, default='')	
	phone = PhoneNumberField(blank=True, default='')	

	timestamp = models.DateTimeField(auto_now=True)
	
	def clean(self):
		if not self.phone and not self.email:
			raise ValidationError('We need to know either your phone number or email address so we can contact you if you win.')