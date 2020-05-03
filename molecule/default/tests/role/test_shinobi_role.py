from typing import Dict, Callable

import takeltest
from shinobi_client import ShinobiClient
from testinfra.host import Host

from .._common import create_example_email_and_password, SHINOBI_HOST

testinfra_hosts = takeltest.hosts()


def test_containers_running(host: Host):
    containers = host.docker.get_containers(name="shinobi")
    assert len(containers) == 2


def test_shinobi_ui_available(host: Host, testvars: Dict):
    shinobi = host.addr(SHINOBI_HOST)
    assert shinobi.port(testvars["shinobi_host_port"]).is_reachable


def test_shinobi_super_user(shinobi_client: ShinobiClient):
    email, password = create_example_email_and_password()
    shinobi_client.user.create(email, password)
    assert shinobi_client.user.get(email) is not None


def test_shinobi_user(testvars: Dict, does_user_exist: Callable[[str], bool], shinobi_client: ShinobiClient):
    for user in testvars["shinobi_users"]:
        assert does_user_exist(user["email"])
        assert shinobi_client.api_key.get(user["email"], user["password"]) is not None


def test_shinobi_monitors(testvars: Dict, shinobi_client: ShinobiClient):
    user_password_map = {user["email"]: user["password"] for user in testvars["shinobi_users"]}
    for monitor in testvars["shinobi_monitors"]:
        for user_email in monitor["users"]:
            monitor_orm = shinobi_client.monitor(user_email, user_password_map[user_email])
            retrieved_monitor = monitor_orm.get(monitor["id"])
            test_identifier = (user_email, monitor["id"])
            assert retrieved_monitor is not None, test_identifier
            assert retrieved_monitor["path"] == monitor["configuration"]["path"], test_identifier
