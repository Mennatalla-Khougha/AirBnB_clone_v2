#sets up the web servers for the deployment of web_static.

if ! which('nginx') {
  exec { 'update':
    command  => 'apt-get update',
    provider => shell,
  }
  -> package { 'nginx':
    ensure => installed,
  }
}
-> exec {'mkdir':
command  => 'mkdir -p /data/web_static/shared',
provider => shell,
}
-> exec {'mkdir':
command  => 'mkdir -p /data/web_static/releases/test',
provider => shell,
}
-> exec {'echo':
command  => 'echo "Hello world" >  /data/web_static/releases/test/index.html',
provider => shell,
}
-> exec {'ln':
command  => 'ln -sf /data/web_static/releases/test /data/web_static/current',
provider => shell,
}
-> exec {'chown':
command  => 'chown -R ubuntu:ubuntu /data/',
provider => shell,
}
-> exec {'sed':
command  => 'sudo sed -i "/server_name _;/a \
\\
    location /hbnb_static/ { \\
        alias /data/web_static/current/;\\
        index index.html;\\
    }" /etc/nginx/sites-available/default',
provider => shell,
}
-> exec {'restart':
command  => 'sudo service nginx restart',
provider => shell,
}
