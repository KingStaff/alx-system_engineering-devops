# Increase the amount of traffic an Nginx server can handle

# Increase the U LIMIT of the default file
exec { 'fix nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  # Specify the path for the sed command
  path    => '/usr/local/bin/:/bin/'
}

# restart Nginx service
-> exec { 'nginx-restart':
  # Restart Nginx service
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d/'
}
