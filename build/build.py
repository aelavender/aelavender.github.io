#!/usr/bin/env python

import os
import jinja2
import yaml

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'resume.yml')) as f:
    res = yaml.load(f)

with open(os.path.join(here, 'resume.html.j2')) as f:
    template = jinja2.Template(f.read(), autoescape=True)

with open(os.path.join(here, '../index.html'), 'w') as f:
    f.write(template.render(d=res))
