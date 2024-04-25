from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Apointments as Event
from django.urls import reverse

class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

	# formats a day as a td
	# filter events by day
	def formatday(self, day, events):
		events_per_day = events.filter(start_time__day=day)
  
		d = ''
		for event in events_per_day:
			d += f'<li> {event.get_html_url} </li>' 
   
		requests_per_day = events.filter(start_time__day__gte=day,start_time__day__lte=day).order_by('start_time').distinct()
		#print(requests_per_day)
		#d = ''
		#for request in requests_per_day:
		#	d += f'<li> {request.get_html_url_day} </li>'

		if day != 0:
			
			return f"<td><span class='date'>{Event.get_html_url_day(Event,day, self.month,self.year)}</span><ul><ol>{d}</ol></ul></td>"
		return '<td></td>'

	# formats a week as a tr 
	def formatweek(self, theweek, events):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, events)
		return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, withyear=True):
		events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month)
		
		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, events)}\n'
		return cal

class Day(HTMLCalendar):
	def __init__(self, day =None, year=None, month=None, date = None):
		self.day = day
		self.year = year
		self.month = month
		self.date = date
		super(Day, self).__init__() 
  
	def formatday(self):
     
		events_per_day = Event.objects.filter(start_time__day=self.day, start_time__month=self.month, start_time__year=self.year)
  
		d = ''
		numb_event = 1
		for event in events_per_day:
			d += f'<li> {event.get_html_url} </li>' 
   

		if self.day != 0:
			
			return f"<td><span class='date'>{self.day} {self.date.strftime('%B')} {self.year}</span><ul><ol>{d}</ol></ul></td>"
		return '<td></td>'
