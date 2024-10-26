from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.ext.flask.flask_middleware import FlaskMiddleware
from opencensus.trace.samplers import ProbabilitySampler

Instrumentation_key='8e5e5f52-4e6a-4bd1-9360-db6637e0bbc1'
from flask import Flask

app =Flask(__name__)

middleware = FlaskMiddleware(app,
            exporter=AzureExporter(connection_string='InstrumentationKey=8e5e5f52-4e6a-4bd1-9360-db6637e0bbc1;IngestionEndpoint=https://centralindia-0.in.applicationinsights.azure.com/;LiveEndpoint=https://centralindia.livediagnostics.monitor.azure.com/;ApplicationId=d3697058-b164-449d-9160-7db7a7937a00'),
            sampler=ProbabilitySampler(1.0),)
@app.route("/")
def hello_word():
    return "Learning AZURE through skillup"

if __name__== "__main__":
    app.run(debug=True)