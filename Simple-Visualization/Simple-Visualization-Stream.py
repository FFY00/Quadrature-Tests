#!/usr/bin/env python
import plotly.plotly as py
import plotly.tools as tls
import time
import numpy as np

start_time = time.time()
elapsed_time = time.time() - start_time

# Streams
stream_ids = tls.get_credentials_file()['stream_ids']
stream_iq = py.Stream(stream_ids[0])
stream_i = py.Stream(stream_ids[1])
stream_q = py.Stream(stream_ids[2])

stream_iq.open()
stream_i.open()
stream_q.open()

# Plot
print "Starting streaming..."

while True:
    stream_iq.write(dict(x=np.sin(elapsed_time), y=np.cos(elapsed_time)))
    stream_i.write(dict(x=np.sin(elapsed_time), y=elapsed_time))
    stream_q.write(dict(x=np.cos(elapsed_time), y=elapsed_time))
    time.sleep(0.2)