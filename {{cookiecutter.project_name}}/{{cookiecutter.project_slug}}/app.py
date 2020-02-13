# -*- coding: utf-8 -*-
"""
App runner
"""
# System imports
from __future__ import absolute_import
# Third-party imports
import falcon

# Local imports
try:
    from sample.models import SampleResource
    from healthcheck.healthz import HealthCheck  # pragma: nocover
except ImportError:
    from {{ cookiecutter.project_slug }}.sample.models import SampleResource
    from {{ cookiecutter.project_slug }}.healthcheck.healthz import HealthCheck


# Create resources
sample_resource = SampleResource()
health_check = HealthCheck()


# Create falcon app
app = falcon.API()
app.req_options.auto_parse_form_urlencoded = True
app.req_options.strip_url_path_trailing_slash = True
app.add_route('/healthz/', health_check)
app.add_route('/sample_resource', sample_resource)


# Useful for debugging problems in API, it works with pdb
if __name__ == '__main__':
    from wsgiref import simple_server  # NOQA
    httpd = simple_server.make_server('127.0.0.1', 9001, app)
    httpd.serve_forever()
