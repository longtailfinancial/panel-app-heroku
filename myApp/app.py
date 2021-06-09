# pip install -r requirements
# panel serve app.py --auto --show
import hvplot.pandas
import holoviews as hv
import panel as pn

pn.extension(sizing_mode="stretch_width")
hv.extension("bokeh")

accent_color = "#FF6600"

# Import model and model_view
from model import Model, model_view

# Merging web components
pn.template.FastListTemplate(
    site="myApp",
    title="Template app",
    favicon=""
    #logo="",
    #busy_indicator,
    header_background=accent_color,
    main=[
        model_view(),
        # add more views,
    ],
).servable()
# Add more parameters from here 
# https://panel.holoviz.org/reference/templates/FastGridTemplate.html