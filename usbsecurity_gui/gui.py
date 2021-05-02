#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
usbsecurity-gui is the program for the graphical interface of USBSecurity.
"""

import platform
import os
import argparse
from subprocess import CalledProcessError, check_output

import webview
import logging

from re import match

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

about = {}
with open(os.path.join(BASE_DIR, '__version__.py')) as f:
    exec(f.read(), about)

logging.basicConfig(filename='usbsecurity-gui.log',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


def cef_detect():
    if platform.system() == 'Linux':
        try:
            output = check_output('chromium-browser --version', shell=True)
            _match = match('Chromium (?P<version>\d+).\d+.\d+.\d+ .*', output.decode())
            if _match:
                return 66 < int(_match.groupdict()['version'])
        except CalledProcessError:
            pass

        try:
            output = check_output('google-chrome --version', shell=True)
            _match = match('Google Chrome (?P<version>\d+).\d+.\d+.\d+ .*', output.decode())
            if _match:
                return 66 < int(_match.groupdict()['version'])
        except CalledProcessError:
            pass

    if platform.system() == 'Windows':
        try:
            output = check_output('dir /B/AD "C:\Program Files (x86)\Google\Chrome\Application\"|findstr /R /C:"^[0-9].*\..*[0-9]$"', shell=True)
            _match = match('(?P<version>\d+).\d+.\d+.\d+', output.decode())
            if _match:
                return 66 < int(_match.groupdict()['version'])
        except CalledProcessError:
            pass

        try:
            output = check_output('dir /B/AD "C:\Program Files\Google\Chrome\Application\"|findstr /R /C:"^[0-9].*\..*[0-9]$"', shell=True)
            _match = match('(?P<version>\d+).\d+.\d+.\d+', output.decode())
            if _match:
                return 66 < int(_match.groupdict()['version'])
        except CalledProcessError:
            pass

        try:
            output = check_output(
                'dir /B/AD "C:\Program Files (x86)\Google\Chromium\Application\"|findstr /R /C:"^[0-9].*\..*[0-9]$"',
                shell=True)
            _match = match('(?P<version>\d+).\d+.\d+.\d+', output.decode())
            if _match:
                return 66 < int(_match.groupdict()['version'])
        except CalledProcessError:
            pass

        try:
            output = check_output(
                'dir /B/AD "C:\Program Files\Google\Chromium\Application\"|findstr /R /C:"^[0-9].*\..*[0-9]$"',
                shell=True)
            _match = match('(?P<version>\d+).\d+.\d+.\d+', output.decode())
            if _match:
                return 66 < int(_match.groupdict()['version'])
        except CalledProcessError:
            pass

    return False


def parse_args():
    __version__ = about['__version__']

    parser = argparse.ArgumentParser(prog='usbsecurity-gui',
                                     description='usbsecurity-gui is the program for the graphical interface of USBSecurity.')

    parser.add_argument('-v',
                        '--version',
                        action='version',
                        version=f'%(prog)s {__version__}',)
    parser.add_argument('-a',
                        '--author',
                        action='version',
                        version='%(prog)s was created by software developer Alexis Torres Valdes <alexis89.dev@gmail.com>',
                        help="show program's author and exit")

    parser.add_argument('--host',
                        default='127.0.0.1',
                        help='Host server ip address. Default: 127.0.0.1')
    parser.add_argument('--port',
                        type=int,
                        default=8888,
                        help='Server port. Default: 8888')

    return parser.parse_args()


def main():
    args = parse_args()
    host = args.host
    port = args.port

    webview.create_window('USBSecurity', 'http://%s:%s' % (host, port), width=1024, height=600)
    cef_detected = cef_detect()
    if cef_detected:
        try:
            webview.start(gui='cef', user_agent=about['__title__'])
            return
        except Exception as e:
            logger.warning(e)
    webview.start(user_agent=about['__title__'])


if __name__ == '__main__':
    main()
