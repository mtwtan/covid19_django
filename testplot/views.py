from django.shortcuts import render
from django.http import HttpResponse
#from django.views.generic.base import View
from django.template import Context, Template
from django.template.response import TemplateResponse

# Create your views here.
from io import BytesIO
import base64
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

from testplot.models import Testcovid, DmvMovingAverage
import pandas as pd
import numpy as np
import matplotlib.dates as mdates
import matplotlib.cbook as cbook

years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month
days = mdates.DayLocator(interval=5) # every day
month_fmt = mdates.DateFormatter('%m-%y')
day_fmt = mdates.DateFormatter('%d')

def test_view(request):
  # Create a new Matplotlib figure
  fig, ax = plt.subplots()
  ax.plot([1, 2, 3, 4], [3,6,9,12])
  ax.set_title('Matplotlib Chart in Django')

  plt.tight_layout()

  # Create a byte buffer for saving image
  fig_buffer = BytesIO()
  plt.savefig(fig_buffer, format='png', dpi=150)

  # Save the figure as a HttpPesponse
  response = HttpResponse(content_type='image/png')
  response.write(fig_buffer.getvalue())

#  image_base64 = base64.b64encode(fig_buffer.getvalue()).decode('utf-8').replace('\n','')

  fig_buffer.close()

  return response

def plt_fairfax_view(request):
  df_fairfax = pd.DataFrame(list(DmvMovingAverage.objects.using('data').filter(county__exact='Fairfax').values()))
  df_fairfax['date'] = pd.to_datetime(df_fairfax['date'])
  df_index = df_fairfax.index
  num_rows = len(df_index)
  max_index = num_rows - 1

  fig, ax = plt.subplots()
  ax.set_title('Fairfax cases')
  ax.plot('date', 'numconfirmed', data=df_fairfax, label="Fairfax - Confirmed Cases")

  ax.xaxis.set_major_locator(months)
  ax.xaxis.set_major_formatter(month_fmt)
  ax.xaxis.set_minor_locator(days)

#  # round to nearest months
  datemin = np.datetime64(df_fairfax['date'][0], 'D')
#  datemax = np.datetime64(df_fairfax['date'][-1], 'D') + np.timedelta64(15, 'D')
  datemax = np.datetime64(df_fairfax['date'][max_index], 'D')  
  ax.set_xlim(datemin, datemax)

  plt.tight_layout()
  plt.text
  plt.legend()
  fig_buffer = BytesIO()
  plt.savefig(fig_buffer, format='png', dpi=150)

  # Save the figure as a HttpPesponse
  response = HttpResponse(content_type='image/png')
  response.write(fig_buffer.getvalue())

#  image_base64 = base64.b64encode(fig_buffer.getvalue()).decode('utf-8').replace('\n','')

  fig_buffer.close()

  return response

def plt_fairfax_movingavg_view(request):
  df_fairfax = pd.DataFrame(list(DmvMovingAverage.objects.using('data').filter(county__exact='Fairfax').values()))
  df_fairfax['date'] = pd.to_datetime(df_fairfax['date'])
  df_index = df_fairfax.index
  num_rows = len(df_index)
  max_index = num_rows - 1

  fig, ax = plt.subplots()
  ax.set_title('Fairfax cases')
  ax.plot('date', 'movingaverage', data=df_fairfax, label="Fairfax - 7 day Moving Average")

  ax.xaxis.set_major_locator(months)
  ax.xaxis.set_major_formatter(month_fmt)
  ax.xaxis.set_minor_locator(days)

#  # round to nearest months
  datemin = np.datetime64(df_fairfax['date'][0], 'D')
#  datemax = np.datetime64(df_fairfax['date'][-1], 'D') + np.timedelta64(15, 'D')
  datemax = np.datetime64(df_fairfax['date'][max_index], 'D')
  ax.set_xlim(datemin, datemax)

  plt.tight_layout()
  plt.text
  plt.legend()
  fig_buffer = BytesIO()
  plt.savefig(fig_buffer, format='png', dpi=150)

  # Save the figure as a HttpPesponse
  response = HttpResponse(content_type='image/png')
  response.write(fig_buffer.getvalue())

#  image_base64 = base64.b64encode(fig_buffer.getvalue()).decode('utf-8').replace('\n','')

  fig_buffer.close()

  return response

def tbl_fairfax_view():
  df_fairfax = pd.DataFrame(list(DmvMovingAverage.objects.using('data').filter(county__exact='Fairfax').values()))
  df_html = df_fairfax.to_html()
  return df_html

def df_covid19():
  df = pd.DataFrame(list(Testcovid.objects.using('data').all().values()))
  df_html = df.to_html()
  return df_html

def index(request):
  df = tbl_fairfax_view()
  args = {}
  args['df'] = df
  return render(request, "testplot.html", args )

