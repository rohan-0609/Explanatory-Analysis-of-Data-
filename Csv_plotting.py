import pandas as pd
import plotly.express as px

df = pd.read_csv('COVID-19_DataSet.csv')
fig = px.line(df, x = 'Month', y='COVID patients', title='COVID patients in Months(2020)')
fig1 = px.line(df, x = 'COVID patients', y='Recoveries', title='Recovery Data (2020')
fig2 = px.line(df, x = 'Deaths', y='Year', title="Deaths in 2020")
fig3 = px.line(df, x = 'Deaths', y = 'Recoveries', title="Death and Recoveries in 2020")
fig4 = px.line(df, x = 'COVID patients', y='Deaths', title = "COVID patients and deaths")
fig1.show()
fig2.show()
fig3.show()
fig4.show()
