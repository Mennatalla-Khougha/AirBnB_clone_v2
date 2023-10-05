#sets up the web servers for the deployment of web_static.

exec { 'update':
  command => 'apt-get update',
  provider => shell,
}
-> exec { 'install':
  command => 'apt-get -y install nginx',
  provider => shell,
}
-> exec {'mkdir':
command  => 'mkdir -p /data/web_static/shared',
provider => shell,
}
-> exec {'mkdir_test':
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
command  => 'sed -i "s|server_name _;|server_name _; 
    location /hbnb_static/ { 
        alias /data/web_static/current/;
        index index.html;
    }" /etc/nginx/sites-available/default',
provider => shell,
}
-> exec {'restart':
command  => 'sudo service nginx restart',
provider => shell,
}
