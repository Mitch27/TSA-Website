#!/usr/bin/env python
import sys, os

# Change this path to reflect the real directory where your django-project lives
projects_location = "/home/t/ts/tsa/public_html/projects"
project_name = "tsa"

sys.path.insert(0, projects_location)
sys.path.insert(1, os.path.join(projects_location, project_name))
os.chdir(projects_location)

os.environ['DJANGO_SETTINGS_MODULE'] = "%s.settings" % project_name

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
