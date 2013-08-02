"""
%% functions.py %%

This file is defines some important functions that are then called views.py file.  
"""
from result_generator.report.header import *
import re

from django.db.models import Q


def dates(start_date, end_date):
	import datetime
	from django import forms
	if start_date > datetime.date.today() or end_date > datetime.date.today():
		raise forms.ValidationError("The date cannot be in the future!")
	elif end_date < start_date :
		raise forms.ValidationError("The start_date is greater than end_date!")
	else:
		pass


def normalize_query(query_string,
	findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'(\s{2,})').sub):
    ''' Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:
        
        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']
    
    '''
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)] 

def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.
    
    '''
    query = None # Query to search for every search term        
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query


