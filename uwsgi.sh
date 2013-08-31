#!/bin/bash

uwsgi -s /tmp/uwsgi.sock --wsgi-file song4.wsgi --chmod-socket=666 -d /var/log/uwsgi.log
