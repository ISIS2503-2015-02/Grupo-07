for i in {1..1};
  do
  for j in {1..1};
    do
    sudo uwsgi --ini uwsgi.py.ini.txt --touch-reload=uwsgi.py.ini.txt;
  done
done
