#!/usr/bin/env python
import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go

# Streams
stream_ids = tls.get_credentials_file()['stream_ids']

stream_iq = go.Stream(
    token=stream_ids[0],
    maxpoints=3000
)

stream_i = go.Stream(
    token=stream_ids[1],
    maxpoints=3000
)

stream_q = go.Stream(
    token=stream_ids[2],
    maxpoints=3000
)

# Traces
trace_iq = go.Scatter(
    x =[],
    y=[],
    mode='lines+markers',
    stream=stream_iq
)

trace_i = go.Scatter(
    x =[],
    y=[],
    mode='lines+markers',
    stream=stream_i
)

trace_q = go.Scatter(
    x =[],
    y=[],
    mode='lines+markers',
    stream=stream_q
)

# Layout
fig = tls.make_subplots(rows=2, cols=1)
fig.append_trace(trace_i, 1, 1)
fig.append_trace(trace_q, 1, 1)
fig.append_trace(trace_iq, 2, 1)

fig['layout'].update(height=600, width=600, title='Simple Visualization')

# Plot
print "Setting plot..."

py.iplot(fig, filename='simple-visualization')