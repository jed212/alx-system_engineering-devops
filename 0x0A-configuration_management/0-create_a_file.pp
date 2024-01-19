# 0-create_a_file.pp

# Create a file in the directory /tmp
file { '/tmp/school':
  ensure     => present,
  mode       => '0744',
  owner      => 'www-data',
  group      => 'www-data',
  content    => 'I love Puppet',
}

