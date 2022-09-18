#!/usr/bin/env bash
sleep 20
if [ $(mysql -h $MYSQL_HOST -u $MYSQL_USER -p$MYSQL_PASSWORD $MYSQL_DATABASE -bse "SELECT COUNT(*) FROM information_schema.tables WHERE table_schema='$MYSQL_DATABASE';") -gt 0 ] ; then
  echo -e "No need to run migrations"
else
  # python migrate.py db init && python migrate.py db migrate && python migrate.py db upgrade
  export FLASK_APP=run.py
  flask db init && flask db migrate && flask db upgrade
  echo -e "database successfully created"
fi
export FLASK_APP=run.py
flask run --host=0.0.0.0
# sleep 5
# pip install polling
# python app/api/datadaemon.py