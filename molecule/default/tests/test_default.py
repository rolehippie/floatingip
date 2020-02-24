import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_config_file(host):
    file = host.file("/etc/network/interfaces.d/90-myinterface.cfg")
    assert file.exists
    assert file.contains("10.13.37.1")
