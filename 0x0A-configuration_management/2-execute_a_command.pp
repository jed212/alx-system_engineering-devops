# 2-execute_a_command.pp

# Define an exec resource to kill the process "killmenow"
exec { 'killmenow':
  command     => 'pkill -f killmenow',
  path        => '/bin:/usr/bin',
  refreshonly => true,
}

# Create a notify resource to print a message after the command is executed
notify { 'Process killed':
  subscribe => Exec['killmenow'],
}
