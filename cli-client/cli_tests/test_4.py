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
    assert result.output == 'Login was successful!\n'

def test_SessionsPerPoint():
    urllib3.disable_warnings()
    runner = CliRunner()
    result = runner.invoke(cli_client.SessionsPerPoint, ['--point', '188-2300 Lacus Rd._0', '--datefrom', '20170303', '--dateto', '20210303'])
    assert result.exit_code == 0
    assert result.output == 'There are no sessions for this point\n'

def test_SessionsPerStation():
    urllib3.disable_warnings()
    runner = CliRunner()
    result = runner.invoke(cli_client.SessionsPerStation, ['--station', '1131 Nec Av.', '--datefrom', '20200301', '--dateto', '20200303'])
    assert result.exit_code == 0
    assert result.output == 'There are no sessions for this Station\n'

def test_SessionsPerEV():
    urllib3.disable_warnings()
    runner = CliRunner()
    result = runner.invoke(cli_client.SessionsPerEV, ['--ev', '29', '--datefrom', '20190101', '--dateto', '20190129'])
    assert result.exit_code == 0
    assert result.output == 'There are no sessions for this vehicle\n'

def test_SessionsPerProvider():
    urllib3.disable_warnings()
    runner = CliRunner()
    result = runner.invoke(cli_client.SessionsPerProvider, ['--provider', '4', '--datefrom', '20200505', '--dateto', '20200630'])
    assert result.exit_code == 0
    assert result.output == 'There are no sessions for this provider\n'

def test_Admin_usermod():
    urllib3.disable_warnings()
    runner = CliRunner()
    result = runner.invoke(cli_client.Admin, ['--usermod', '--username', 'Lefteris', '--passw', None])
    assert result.exit_code == 0
    assert result.output == 'Please provide both the username and the password of the user to be modified or created\n'


def test_Admin_sessionsupd():
    urllib3.disable_warnings()
    runner = CliRunner()
    result = runner.invoke(cli_client.Admin, ['--sessionsupd', '--source', 'aaa.csv', '--passw', 'Lefteris'])
    assert result.exit_code == 0
    assert result.output == 'File does not exist\n'