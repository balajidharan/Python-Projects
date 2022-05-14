import dash
from dash import dcc
from dash import html
from pandas_datareader.data import DataReader
import time
from collections import deque
import plotly.graph_objs as go
import random
from dash.dependencies import Output, Input

app = dash.Dash('System performance')

# Rand data queue
max_length = 50
times = deque(maxlen=max_length)
CPU = deque(maxlen=max_length)
Gpu1 = deque(maxlen=max_length)
GPU = deque(maxlen=max_length)
RAM = deque(maxlen=max_length)
Disk = deque(maxlen=max_length)
wifi = deque(maxlen=max_length)

# Data drop down dict
data_dict = {"CPU Performance":CPU,
"GPU1": Gpu1,
"GPU0": GPU,
"RAM":RAM,
"Disk":Disk,
"Wifi":wifi}


# feeding random data
def update_obd_values(times, CPU, Gpu1, GPU, RAM, Disk, wifi):

    times.append(time.time())
    if len(times) == 1:
        #starting relevant values
        CPU.append(random.randrange(180,230))
        Gpu1.append(random.randrange(95,115))
        GPU.append(random.randrange(170,220))
        RAM.append(random.randrange(1000,9500))
        Disk.append(random.randrange(30,140))
        wifi.append(random.randrange(10,90))
    else:
        for data_of_interest in [CPU, Gpu1, GPU, RAM, Disk, wifi]:
            data_of_interest.append(data_of_interest[-1]+data_of_interest[-1]*random.uniform(-0.0001,0.0001))

    return times, CPU, Gpu1, GPU, RAM, Disk, wifi

times, CPU, Gpu1, GPU, RAM, Disk, wifi = update_obd_values(times, CPU, Gpu1, GPU, RAM, Disk, wifi)

app.layout = html.Div([
    html.Div([
        html.H2('System performance',
                style={'float': 'left',
                       }),
        ]),
    dcc.Dropdown(id='system-data-name',
                 options=[{'label': s, 'value': s}
                          for s in data_dict.keys()],
                 value=['GPU0','CPU Performance','GPU1'],
                 multi=True
                 ),
    html.Div(children=html.Div(id='graphs'), className='row'),
    dcc.Interval(
        id='graph-update',
        interval=100),
    ], className="container",style={'width':'98%','margin-left':10,'margin-right':10,'max-width':50000})


@app.callback(
    Output('graphs','children'),
    [Input('system-data-name', 'value'), Input('graph-update', 'n_intervals')],
    )
def update_graph(data_names,intervals):
    graphs = []
    update_obd_values(times, CPU, Gpu1, GPU, RAM, Disk, wifi)
    if len(data_names)>2:
        class_choice = 'col s12 m6 l4'
    elif len(data_names) == 2:
        class_choice = 'col s12 m6 l6'
    else:
        class_choice = 'col s12'


    for data_name in data_names:

        data = go.Scatter(
            x=list(times),
            y=list(data_dict[data_name]),
            name='Scatter',
            fill="tozeroy",
            fillcolor="#6897bb"
            )

        graphs.append(html.Div(dcc.Graph(
            id=data_name,
            animate=True,
            figure={'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(times),max(times)]),
                                                        yaxis=dict(range=[min(data_dict[data_name]),max(data_dict[data_name])]),
                                                        margin={'l':50,'r':1,'t':45,'b':1},
                                                        title='{}'.format(data_name))}
            ), className=class_choice))

    return graphs



external_css = ["https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css"]
for css in external_css:
    app.css.append_css({"external_url": css})

external_js = ['https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js']
for js in external_css:
    app.scripts.append_script({'external_url': js})


if __name__ == '__main__':
    app.run_server(debug=True)