#!/bin/bash
uwsgi --stop wysapi.pid
uwsgi ./uwsgi_wysapi.ini &
