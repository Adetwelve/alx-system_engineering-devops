# Increase number of limit for request
{ 'change_ulimit':
  command => "echo 'ULIMIT=\"-n 2048\"' > /etc/default/nginx && service nginx restart",
  onlyif  => "grep -q '^ULIMIT=\"-n 2048\"' /etc/default/nginx",
}
