
from ansible.runner import Runner
from ansible.inventory import Inventory


class VinzRunner(Runner):
    """
    Extending Ansible Runner to deal with a lot of the
    boilerplate code.
    """

    private_key = '/Users/mikedavis/.ssh/id_vinz'

    def __init__(self,
                 hosts,
                 module_name=None,
                 module_args=None,
                 ):

        if not isinstance(hosts, list):
            hosts = [hosts]

        inventory = Inventory(hosts)

        arguments = {
            'pattern': '*',
            'inventory': inventory,
            'remote_user': 'root',
            'module_name': module_name,
            'private_key_file': self.private_key
        }

        if module_args:
            arguments['module_cmds'] = module_args

        return super(VinzRunner, self).__init__(**arguments)

    def run(self):
        results = super(VinzRunner, self).run()
        parsed_results = self.parse_results(results)
        return parsed_results

    def parse_results(self, results):
        return results


def example():
    """
    Simple example of the VinzRunner.
    """

    # Eventually, this will be need to be pulled out of the database.
    # Just need to make a list of hosts.  DNS names and IPv4 addresses.  No IPv6.
    hosts = ['vinz-ubuntu.student.iastate.edu']

    runner = VinzRunner(hosts, module_name='ping')
    results = runner.run()
    print results
