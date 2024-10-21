import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

# Sample data creation
np.random.seed(42)
dates = pd.date_range('2023-01-01', periods=100)
values1 = np.random.randn(100).cumsum()  # cumulative data for Line Plot 1
values2 = np.random.randn(100).cumsum()  # cumulative data for Line Plot 2
categories = ['Category A', 'Category B', 'Category C']
bar_values = np.random.randint(20, 100, size=3)

# Creating subplots: 1 row, 2 columns
fig = make_subplots(rows=1, cols=2, 
                    subplot_titles=('Interactive Line Plot', 'Interactive Bar Plot'),
                    specs=[[{"type": "scatter"}, {"type": "bar"}]])

# First subplot - Line Plot 1 with hover data
line_trace1 = go.Scatter(
    x=dates,
    y=values1,
    mode='lines+markers',
    name='Cumulative Data 1',
    hoverinfo='x+y+name',  # Interactive hover with custom info
    line=dict(color='royalblue'),
    marker=dict(size=8, color='darkblue')
)

# Adding first line plot to the first subplot
fig.add_trace(line_trace1, row=1, col=1)

# Second subplot - Line Plot 2 with hover data
line_trace2 = go.Scatter(
    x=dates,
    y=values2,
    mode='lines+markers',
    name='Cumulative Data 2',
    hoverinfo='x+y+name',
    line=dict(color='orange'),
    marker=dict(size=8, color='darkorange')
)

# Adding second line plot to the first subplot
fig.add_trace(line_trace2, row=1, col=1)

# Third subplot - Bar Chart with hover data
bar_trace = go.Bar(
    x=categories,
    y=bar_values,
    name='Bar Chart',
    text=bar_values,  # Display values on hover
    textposition='auto',  # Positioning text above bars
    hoverinfo='x+y+name',
    marker=dict(color=['green', 'blue', 'red'])  # Custom colors for bars
)

# Adding bar plot to the second subplot
fig.add_trace(bar_trace, row=1, col=2)

# Update layout for better interactivity and visualization
fig.update_layout(
    title='Highly Interactive and Visual Dashboard',
    hovermode='x unified',  # Tooltip mode - unified on x-axis
    height=600,  # Adjust dashboard height
    plot_bgcolor='lightgray',  # Background color for the plot
    paper_bgcolor='white',  # Background for the overall figure
    title_font=dict(size=24, family='Arial'),
    showlegend=True,  # Show the legend for the plots
    legend=dict(orientation='h', yanchor='bottom', y=-0.2, xanchor='right', x=1),
)

# Add custom axis titles
fig.update_xaxes(title_text='Date', row=1, col=1)
fig.update_yaxes(title_text='Cumulative Values', row=1, col=1)
fig.update_xaxes(title_text='Categories', row=1, col=2)
fig.update_yaxes(title_text='Values', row=1, col=2)

# Display the final interactive plot
fig.show()
