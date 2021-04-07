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

def test_logout_1():
    urllib3.disable_warnings()
    runner = CliRunner()
    result = runner.invoke(cli_client.logout)
    assert result.exit_code == 0
    assert result.output == 'No user is logged in\n'

def test_SessionsPerPoint():
    urllib3.disable_warnings()
    runner = CliRunner()
    result = runner.invoke(cli_client.SessionsPerPoint, ['--point', '"188-2300 Lacus Rd._0"', '--datefrom', '20170303', '--dateto', '20210303'])
    assert result.exit_code == 0
    assert result.output == 'You must be logged in to execute this command\n'

def test_SessionsPerStation():
    urllib3.disable_warnings()
    runner = CliRunner()
    result = runner.invoke(cli_client.SessionsPerStation, ['--station', '"1131 Nec Av."', '--datefrom', '20150303', '--dateto', '20210303'])
    assert result.exit_code == 0
    assert result.output == 'You must be logged in to execute this command\n'


def test_SessionsPerEV():
    urllib3.disable_warnings()
    runner = CliRunner()
    result = runner.invoke(cli_client.SessionsPerEV, ['--ev', '29', '--datefrom', '20160413', '--dateto', '20210314'])
    assert result.exit_code == 0
    assert result.output == 'You must be logged in to execute this command\n'

def test_SessionsPerProvider():
    urllib3.disable_warnings()
    runner = CliRunner()
    result = runner.invoke(cli_client.SessionsPerProvider, ['--provider', 'Alabama Municipal Electric Authority', '--datefrom', '20130303', '--dateto', '20210320'])
    assert result.exit_code == 0
    assert result.output == 'You must be logged in to execute this command\n'

def test_Admin_usermod():
    urllib3.disable_warnings()
    runner = CliRunner()
    result = runner.invoke(cli_client.Admin, ['--usermod', '--username', 'Lefteris', '--passw', 'Lefteris'])
    assert result.exit_code == 0
    assert result.output == 'You must be logged in and have adminstrator privileges to execute this command\n'

def test_Admin_users():
        urllib3.disable_warnings()
        runner = CliRunner()
        result = runner.invoke(cli_client.Admin, ['--users', 'Lefteris'])
        assert result.exit_code == 0
        assert result.output == 'You must be logged in and have adminstrator privileges to execute this command\n'


def test_Admin_sessionsupd():
    urllib3.disable_warnings()
    runner = CliRunner()
    result = runner.invoke(cli_client.Admin, ['--sessionsupd', '--source', 'aaa.csv', '--passw', 'Lefteris'])
    assert result.exit_code == 0
    assert result.output == 'You must be logged in and have adminstrator privileges to execute this command\n'