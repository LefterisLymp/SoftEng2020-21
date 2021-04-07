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

def test_Admin_users():
    urllib3.disable_warnings()
    runner = CliRunner()
    result = runner.invoke(cli_client.Admin, ['--users', 'Lefteris'])
    assert result.exit_code == 0
    assert 'Lefteris' in result.output


def test_logout_1():
    urllib3.disable_warnings()
    runner = CliRunner()
    result = runner.invoke(cli_client.logout)
    assert result.exit_code == 0
    assert result.output == 'No user is logged in\n'

def test_Admin_users():
    urllib3.disable_warnings()
    runner = CliRunner()
    result = runner.invoke(cli_client.Admin, ['--users', 'Xaris'])
    assert result.exit_code == 0
    assert result.output == 'You must be logged in and have adminstrator privileges to execute this command\n'


def test_Logout():
    urllib3.disable_warnings()
    runner = CliRunner()
    result = runner.invoke(cli_client.logout)
    assert result.exit_code == 0
    assert result.output == 'No user is logged in\n'




