#!/bin/sh

BIN_DIR=`dirname $0`
export PROJECT_ROOT="${BIN_DIR}/.."

export CONFIG_NAME=development
export FLASK_APP=src/app.py
export FLASK_PORT=8000
app_name=bapymonitor
VIRTUALENV=$app_name

if [ ! -d ${HOME}/.virtualenvs/${VIRTUALENV} ]; then
      python${PY_VERSION} -m venv "${HOME}/.virtualenvs/${VIRTUALENV}"
  fi
  . ${HOME}/.virtualenvs/${VIRTUALENV}/bin/activate

cd ${PROJECT_ROOT}

uwsgi --master --http 0.0.0.0:${FLASK_PORT} --python-auto-reload 1 --honour-stdin --enable-threads --wsgi-file ${FLASK_APP}
