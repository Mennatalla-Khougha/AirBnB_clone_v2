#sets up the web servers for the deployment of web_static.

if ! which('nginx') {
  exec { 'update':
    command     => '/usr/bin/apt-get update',
  }
  -> package { 'nginx':
    ensure => installed,
  }
}
-> exec {'mkdir':
command  => '/usr/bin/mkdir -p /data/web_static/shared',
provider => shell,
}
-> exec {'mkdir':
command  => '/usr/bin/mkdir -p /data/web_static/releases/test',
provider => shell,
}
-> exec {'echo':
command  => '/usr/bin/echo "Hello world" >  /data/web_static/releases/test/index.html',
provider => shell,
}
-> exec {'ln':
command  => '/usr/bin/ln -sf /data/web_static/releases/test /data/web_static/current',
provider => shell,
}
-> exec {'chown':
command  => '/usr/bin/chown -R ubuntu:ubuntu /data/',
provider => shell,
}
-> exec {'sed':
command  => '/usr/bin/sed -i "/server_name _;/a \
\
    location /hbnb_static/ { \
        alias /data/web_static/current/;\
        index index.html;\
    }" /etc/nginx/sites-available/default',
provider => shell,
}
-> exec {'restart':
command  => '/usr/bin/service nginx restart',
provider => shell,
}
