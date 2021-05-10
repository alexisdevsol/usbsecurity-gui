#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
usbsecurity-gui is the program for the graphical interface of USBSecurity.
"""

#  This module belongs to the usbsecurity-gui project.
#  Copyright (c) 2021 Alexis Torres Valdes
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2.1 of the License, or (at your option) any later version.
#
#   This library is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#   Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#   License along with this library; if not, write to the Free Software
#   Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
#   USA
#
#   Contact: alexis89.dev@gmail.com

import os
import argparse
import textwrap

import webview
import logging

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


def parse_args():
    __version__ = about['__version__']

    parser = argparse.ArgumentParser(prog=about['__title__'], description=about['__description__'])

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
    parser.add_argument('--engine',
                        nargs='?',
                        choices=['gtk', 'qt', 'edgechromium', 'edgehtml', 'mshtml', 'cef'],
                        help=textwrap.dedent('''
                        Platform: GTK; Code: gtk; Render: WebKit; Provider: WebKit2.
                        Platform: macOS; Render: WebKit; Provider: WebKit.WKWebView (bundled with OS).
                        Platform: QT; Code: qt; Render: WebKit; Provider: QtWebEngine / QtWebKit.
                        Platform: Windows; Code: edgechromium; Render: Chromium; Provider: > .NET Framework 4.6.2 and Edge Runtime installed; Browser compatibility: Ever-green Chromium.
                        Platform: Windows; Code: edgehtml; Render: EdgeHTML; Provider: > .NET Framework 4.6.2 and Windows 10 build 17110.
                        Platform: Windows; Code: mshtml; Render: MSHTML; Provider: MSHTML via .NET / System.Windows.Forms.WebBrowser; Browser compatibility: IE11 (Windows 10/8/7).
                        Platform: Windows; Code: cef; Render: CEF; Provider: CEF Python; Browser compatibility: Chrome 66.
                        '''))

    return parser.parse_args()


def main():
    args = parse_args()
    host = args.host
    port = args.port
    engine = args.engine

    webview.create_window('USBSecurity', 'http://%s:%s' % (host, port), width=1024, height=600)
    if engine:
        webview.start(gui=engine, user_agent=about['__title__'])
    else:
        webview.start(user_agent=about['__title__'])


if __name__ == '__main__':
    main()
