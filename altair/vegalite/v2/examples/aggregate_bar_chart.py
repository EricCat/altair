"""
Horizontal Aggregate Bar Chart
------------------------------
This example is a bar chart showing the distribution of US population
by age in the year 2000.
"""
# category: bar charts
import altair as alt
from vega_datasets import data

source = data.population.url

alt.Chart(source).mark_bar().encode(
    x=alt.X('sum(people):Q', axis=alt.Axis(title='population')),
    y='age:O'
).properties(
    height=300,
    width=300
).transform_filter(
    alt.datum.year == 2000
)
