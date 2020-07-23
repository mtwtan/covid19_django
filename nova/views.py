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

df_nova = pd.DataFrame(list(DmvMovingAverage.objects.using('data').all().values()))
df_nova['date'] = pd.to_datetime(df_nova['date'])
df_index = df_nova.index
num_rows = len(df_index)
max_index = num_rows - 1

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

def plt_nova_view(request):

  fig, ax = plt.subplots()
  ax.set_title('Confirmed Cases')
  ax.plot('date', 'numconfirmed', data=df_nova.loc[df_nova['county'] == 'Fairfax'], label="Fairfax")
  ax.plot('date', 'numconfirmed', data=df_nova.loc[df_nova['county'] == 'Arlington'], label="Arlington")
  ax.plot('date', 'numconfirmed', data=df_nova.loc[df_nova['county'] == 'District of Columbia'], label="District of Columbia")
  ax.plot('date', 'numconfirmed', data=df_nova.loc[df_nova['county'] == 'Montgomery'], label="Montgomery")

  ax.xaxis.set_major_locator(months)
  ax.xaxis.set_major_formatter(month_fmt)
  ax.xaxis.set_minor_locator(days)

#  # round to nearest months
  datemin = np.datetime64(df_nova['date'][0], 'D')
#  datemax = np.datetime64(df_fairfax['date'][-1], 'D') + np.timedelta64(15, 'D')
  datemax = np.datetime64(df_nova['date'][max_index], 'D')  
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

def plt_nova_movingavg_view(request):
#  df_nova = pd.DataFrame(list(DmvMovingAverage.objects.using('data').all().values()))
#  df_nova['date'] = pd.to_datetime(df_nova['date'])
#  df_index = df_nova.index
#  num_rows = len(df_index)
#  max_index = num_rows - 1

  fig, ax = plt.subplots()
  ax.set_title('7 days Moving Average')
  ax.plot('date', 'movingaverage', data=df_nova.loc[df_nova['county'] == 'Fairfax'], label="Fairfax")
  ax.plot('date', 'movingaverage', data=df_nova.loc[df_nova['county'] == 'Arlington'], label="Arlington")
  ax.plot('date', 'movingaverage', data=df_nova.loc[df_nova['county'] == 'District of Columbia'], label="District of Columbia")
  ax.plot('date', 'movingaverage', data=df_nova.loc[df_nova['county'] == 'Montgomery'], label="Montgomery")

  ax.xaxis.set_major_locator(months)
  ax.xaxis.set_major_formatter(month_fmt)
  ax.xaxis.set_minor_locator(days)

#  # round to nearest months
  datemin = np.datetime64(df_nova['date'][0], 'D')
#  datemax = np.datetime64(df_fairfax['date'][-1], 'D') + np.timedelta64(15, 'D')
  datemax = np.datetime64(df_nova['date'][max_index], 'D')
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

def plt_nova_casechange_view(request):
#  df_nova = pd.DataFrame(list(DmvMovingAverage.objects.using('data').all().values()))
#  df_nova['date'] = pd.to_datetime(df_nova['date'])
#  df_index = df_nova.index
#  num_rows = len(df_index)
#  max_index = num_rows - 1

  fig, ax = plt.subplots()
  ax.set_title('Case Change')
  ax.plot('date', 'change', data=df_nova.loc[df_nova['county'] == 'Fairfax'], label="Fairfax")
  ax.plot('date', 'change', data=df_nova.loc[df_nova['county'] == 'Arlington'], label="Arlington")
  ax.plot('date', 'change', data=df_nova.loc[df_nova['county'] == 'District of Columbia'], label="District of Columbia")
  ax.plot('date', 'change', data=df_nova.loc[df_nova['county'] == 'Montgomery'], label="Montgomery")

  ax.xaxis.set_major_locator(months)
  ax.xaxis.set_major_formatter(month_fmt)
  ax.xaxis.set_minor_locator(days)

#  # round to nearest months
  datemin = np.datetime64(df_nova['date'][0], 'D')
#  datemax = np.datetime64(df_fairfax['date'][-1], 'D') + np.timedelta64(15, 'D')
  datemax = np.datetime64(df_nova['date'][max_index], 'D')
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
  df_fairfax = pd.DataFrame(list(DmvMovingAverage.objects.using('data').all().order_by('county','date').values()))
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
  return render(request, "nova.html", args )
