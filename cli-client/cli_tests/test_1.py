import pytest
import cli_client
import urllib3
from click.testing import CliRunner
urllib3.disable_warnings()

def test_healthcheck():
    urllib3.disable_warnings()
    runner = CliRunner()
    result = runner.invoke(cli_client.healthcheck)
    assert result.exit_code == 0
    assert result.output == 'Database is connected\n'

def test_login():
    urllib3.disable_warnings()
    runner = CliRunner()
    result = runner.invoke(cli_client.login, ['--username', 'Lefteris', '--passw', 'Lefteris'])
    assert result.exit_code == 0
    assert result.output == 'User already logged in\n'


def test_logout_1():
    urllib3.disable_warnings()
    runner = CliRunner()
    result = runner.invoke(cli_client.logout)
    assert result.exit_code == 0
    assert result.output == 'User is now logged out\n'

def test_logout_2():
    urllib3.disable_warnings()
    runner = CliRunner()
    result = runner.invoke(cli_client.logout)
    assert result.exit_code == 0
    assert result.output == 'No user is logged in\n'




