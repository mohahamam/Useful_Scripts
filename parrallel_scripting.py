from pssh.clients import ParallelSSHClient

hosts = ['i7mini', '192.168.0.117']

client = ParallelSSHClient(hosts)

output = client.run_command('hostname')