for i in {5..10};
  do
  for j in {5..10};
    do
    printf '%s\n' '[uwsgi]' 'http = 127.0.0.1:9345' 'wsgi-file = tbcSite/wsgi.py' 'master = True' 'workers = '${i} 'gevent = '${j} >uwsgi.py.ini.txt
    jmeter -n -t prueba.jmx
    sleep 15;
  done
done
