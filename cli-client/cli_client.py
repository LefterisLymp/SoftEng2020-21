import pprint

import click
import datetime
from click_option_group import optgroup, RequiredMutuallyExclusiveOptionGroup
import requests
import json
import os
import os.path
from os import path
from os.path import expanduser
import urllib3
import re

# @click.option('--count', default=1, help='Number of greetings.')
# @click.option('--name', prompt='Your name',
#              help='The person to greet.')
urllib3.disable_warnings()

home = expanduser("~")
tokenpath = "%s\softeng20bAPI.token" % home


@click.group()
def main():
    pass


@click.command(name='healthcheck', help='Check connection with database')
def healthcheck():
    url = 'http://localhost:5000/evcharge/api/admin/healthCheck'
    res = requests.get(url, verify=False)
    if res.status_code == 400:
        click.echo("Database is not connected")
    else:
        click.echo("Database is connected")


@main.command(name='resetsessions', help='Resets the database')
def resetsessions():
    url = 'http://localhost:5000/evcharge/api/admin/resetsessions'
    res = requests.post(url, verify=False)
    status = res.json()
    if status['status'] == 'OK':
        click.echo("Database Reset Succeeded")
    else:
        click.echo("Database Reset Failed")


@main.command(name='login', help='User login')
@click.option('--username', required=True, type=str, help='Username')
@click.option('--passw', required=True, type=str, help='Password')
def login(username, passw):
    if path.exists(tokenpath):
        click.echo('User already logged in')

    else:
        url = 'http://localhost:5000/evcharge/api/login'
        d = {'username': username, 'password': passw}
        res = requests.post(url, data=d, headers={'Content-Type': 'application/x-www-form-urlencoded'}, verify=False)
        if res.status_code == 200:
            token = res.json()
            f = open(tokenpath, "w+")
            json.dump(token, f)
            f.close()
            click.echo('Login was successful!')
        else:
            click.echo(res.text)


@main.command(name='logout', help='User Logout')
def logout():
    if path.exists(tokenpath):
        f = open(tokenpath, 'r')
        token = json.load(f)
        url = 'http://localhost:5000/evcharge/api/logout'
        res = requests.post(url, headers={'X-OBSERVATORY-AUTH': token['token']}, verify=False)
        f.close()
        os.remove(tokenpath)
        if res.status_code == 200:
            click.echo('User is now logged out')
        else:
            click.echo(res.text)

    else:
        click.echo('No user is logged in')


@main.command(name='SessionsPerPoint', help='Charging Sessions per Point')
@click.option('--point', required=True, help='Point of charging')
@click.option('--datefrom', required=True, help='Date Session Starts')
@click.option('--dateto', required=True, help='Date Session Ends')
@click.option('--format', default='json',
              help='Format in which the data appears, can be either json (default) or csv')
def SessionsPerPoint(point, datefrom, dateto, format):
    if format not in ['json', 'csv']:
        click.echo("Format")
    datefrom = datetime.datetime.strptime(datefrom, '%Y%m%d').strftime('%Y-%m-%d')
    dateto = datetime.datetime.strptime(dateto, '%Y%m%d').strftime('%Y-%m-%d')
    url = 'http://localhost:5000/evcharge/api/SessionsPerPoint/' + point + "/" + datefrom + "/" + dateto
    if path.exists(tokenpath):
        f = open(tokenpath, 'r')
        token = json.load(f)
        f.close()
        res = requests.get(url, headers={'X-OBSERVATORY-AUTH': token['token']}, verify=False)
        if res.status_code == 200 and format == 'json':
            pprint.pprint(res.json())
        elif res.status_code == 200 and format == 'csv':
            click.echo(res.text)
        else:
            click.echo(res.text)
    else:
        click.echo("You must be logged in to execute this command")


@main.command(name='SessionsPerStation', help='Charging Sessions per Station')
@click.option('--station', required=True, help='Station of charging')
@click.option('--datefrom', required=True, help='Date Session Starts')
@click.option('--dateto', required=True, help='Date Session Ends')
@click.option('--format', default='json',
              help='Format in which the data appears, can be either json (default) or csv')
def SessionsPerStation(station, datefrom, dateto, format):
    if format not in ['json', 'csv']:
        click.echo("Format")
    datefrom = datetime.datetime.strptime(datefrom, '%Y%m%d').strftime('%Y-%m-%d')
    dateto = datetime.datetime.strptime(dateto, '%Y%m%d').strftime('%Y-%m-%d')
    url = 'http://localhost:5000/evcharge/api/SessionsPerStation/' + station + "/" + datefrom + "/" + dateto
    if path.exists(tokenpath):
        f = open(tokenpath, 'r')
        token = json.load(f)
        f.close()
        res = requests.get(url, headers={'X-OBSERVATORY-AUTH': token['token']}, verify=False)
        if res.status_code == 200 and format == 'json':
            pprint.pprint(res.json())
        elif res.status_code == 200 and format == 'csv':
            click.echo(res.text)
        else:
            click.echo(res.text)
    else:
        click.echo("You must be logged in to execute this command")


@main.command(name='SessionsPerEV', help='Charging Sessions per Ev')
@click.option('--ev', required=True, help='Ev of charging')
@click.option('--datefrom', required=True, help='Date Session Starts')
@click.option('--dateto', required=True, help='Date Session Ends')
@click.option('--format', default='json',
              help='Format in which the data appears, can be either json (default) or csv')
def SessionsPerEV(ev, datefrom, dateto, format):
    if format not in ['json', 'csv']:
        click.echo("Format")
    datefrom = datetime.datetime.strptime(datefrom, '%Y%m%d').strftime('%Y-%m-%d')
    dateto = datetime.datetime.strptime(dateto, '%Y%m%d').strftime('%Y-%m-%d')
    url = 'http://localhost:5000/evcharge/api/SessionsPerEV/' + ev + "/" + datefrom + "/" + dateto
    if path.exists(tokenpath):
        f = open(tokenpath, 'r')
        token = json.load(f)
        f.close()
        res = requests.get(url, headers={'X-OBSERVATORY-AUTH': token['token']}, verify=False)
        if res.status_code == 200 and format == 'json':
            pprint.pprint(res.json())
        elif res.status_code == 200 and format == 'csv':
            click.echo(res.text)
        else:
            click.echo(res.text)

    else:
        click.echo("You must be logged in to execute this command")


@main.command(name='SessionsPerProvider', help='Charging Sessions per Provider')
@click.option('--provider', required=True, help='Provider of P'
                                                'rovider')
@click.option('--datefrom', required=True, help='Date Session Starts')
@click.option('--dateto', required=True, help='Date Session Ends')
@click.option('--format', default='json',
              help='Format in which the data appears, can be either json (default) or csv')
def SessionsPerProvider(provider, datefrom, dateto, format):
    if format not in ['json', 'csv']:
        click.echo("Format")
    datefrom = datetime.datetime.strptime(datefrom, '%Y%m%d').strftime('%Y-%m-%d')
    dateto = datetime.datetime.strptime(dateto, '%Y%m%d').strftime('%Y-%m-%d')
    url = 'http://localhost:5000/evcharge/api/SessionsPerProvider/' + provider + "/" + datefrom + "/" + dateto
    if path.exists(tokenpath):
        f = open(tokenpath, 'r')
        token = json.load(f)
        f.close()
        res = requests.get(url, headers={'X-OBSERVATORY-AUTH': token['token']}, verify=False)
        if res.status_code == 200 and format == 'json':
            pprint.pprint(res.json())
        elif res.status_code == 200 and format == 'csv':
            click.echo(res.text)
        else:
            click.echo(res.text)
    else:
        click.echo("You must be logged in to execute this command")


@main.command(name='Admin', help='Adminstrator functions')
@optgroup.group('AdminActionGroup', cls=RequiredMutuallyExclusiveOptionGroup)
@optgroup.option('--usermod', is_flag=True,  type=str, help='Create new user, or change password if user already exists')
@optgroup.option('--users', type=str, help='Show user status')
@optgroup.option('--healthcheck', is_flag=True , type=str, help='Check connection with database')
@optgroup.option('--resetsessions', is_flag=True, type=str, help='Resets the database')
@optgroup.option('--sessionsupd', is_flag=True, type=str, help='Uploads a CSV file')
@click.option('--username', type=str, help='Username of user to be added or modified')
@click.option('--passw', type=str, help='Password of user to be added or modified')
@click.option('--source', type=str, help='Upload CSV file with charge data')
def Admin(usermod, users, source, healthcheck, resetsessions, username, passw,sessionsupd):
    if usermod != None:
        if username != None and passw != None:
            url = 'http://localhost:5000/evcharge/api/admin/usermod/' + username + '/' + passw
            if path.exists(tokenpath):
                f = open(tokenpath, 'r')
                token = json.load(f)
                f.close()
                d = {'user_username': username, 'password': passw}
                res = requests.post(url, headers={'X-OBSERVATORY-AUTH': token['token']},verify=False)
                status = res.json()
                if status['message'] == 'password modified':
                    click.echo("Password modified")
                    return click.echo(token)
                elif status['message'] == 'new user created':
                    click.echo("New user created")
                    return click.echo(token)
                else:
                    return click.echo(status['message'])
            else:
                click.echo("You must be logged in and have adminstrator privileges to execute this command")
        else:
            click.echo("Please provide both the username and the password of the user to be modified or created")


    elif users != None:
        url = 'http://localhost:5000/evcharge/api/admin/users/' + users
        if path.exists(tokenpath):
            f = open(tokenpath, 'r')
            token = json.load(f)
            f.close()
            res = requests.get(url, headers={'X-OBSERVATORY-AUTH': token['token'], 'Content-Type': 'application/x-www-form-urlencoded'}, verify=False)
            click.echo(res.text)
            res_b = res.json()
            result_b = res_b["message"]["username"]
            click.echo(result_b)
            click.echo(token["token"])
        else:
            click.echo("You must be logged in and have adminstrator privileges to execute this command")

    elif sessionsupd != None:
        if source != None:
            url = 'http://localhost:5000/evcharge/api/admin/system/sessionsupd' + source
            if path.exists(tokenpath):
                f = open(tokenpath, 'r')
                token = json.load(f)
                f.close()
                if path.exists(source):
                    uploadfile = {'file': open(source, 'rb')}
                    res = requests.post(url, headers={'X-OBSERVATORY-AUTH': token['token']}, files=uploadfile,verify=False)
                    if res.status_code == 400:
                        click.echo(res.text())
                    elif res.status_code == 401:
                        click.echo(res.text())
                    pprint.pprint(res.json())
                else:
                    click.echo("File does not exist")
            else:
                click.echo("You must be logged in and have adminstrator privileges to execute this command")
        else:
            click.echo("Please provide source parameter")


    elif healthcheck != None:
        url = 'http://localhost:5000/evcharge/api/admin/healthCheck'
        res = requests.get(url, verify=False)
        if res.status_code == 400:
            click.echo("Database is not connected")
        else:
            click.echo("Database is connected")


    elif resetsessions != None:
        url = 'http://localhost:5000/evcharge/api/admin/resetsessions'
        res = requests.post(url, verify=False)
        status = res.json()
        if status['status'] == 'OK':
            click.echo("Database Reset Succeeded")
        else:
            click.echo("Database Reset Failed")

if __name__ == '__main__':
    main()