# Increase number of limit for request
file { '/etc/default/nginx':
  ensure  => file,
  content => "ULIMIT='-n 2048'\n",
}

exec { 'restart_nginx':
  command  => 'service nginx restart',
  refreshonly => true,
}
