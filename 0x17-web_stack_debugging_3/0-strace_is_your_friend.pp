# A script that replace strings ".phpp" with ".php" extension.
file { '/var/www/html/wp-settings.php':
  ensure  => present,
  content => inline_template('<%= File.read("/var/www/html/wp-settings.php").gsub(/\.phpp/, ".php") %>'),
}
