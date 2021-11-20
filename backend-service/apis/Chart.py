"""
Providing charts based on user statistics.
"""

from flask_restful import Resource
import pandas as pd

import plotly.express as px
import numpy as np

import datetime

class Chart(Resource):

	def get(self, user_id, chart_type=None):
		x = np.linspace(0, 2, 100)
		y = np.sin(x)

		fig = px.line(x=x, y=y)

		fig_div = offline.plot(
			figure_or_data=fig,
			include_plotlyjs=False,
			output_type="div"
		)

		return fig_div
