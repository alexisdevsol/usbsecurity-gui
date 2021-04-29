# How

usbsecurity-gui is the program for the graphical interface of USBSecurity.

# Prerequisites

## Linux

### GTK

PyGObject is used with GTK. To install dependencies on Ubuntu for both Python 3 and 2

sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0 gir1.2-webkit2-4.0

### QT

PyQt5 is used with QT. pywebview supports both QtWebChannel (newer and preferred) and QtWebKit implementations. Use QtWebChannel, unless it is not available on your system.

To install QT via pip

pip install pyqt5 pyqtwebengine

To install QtWebChannel on Debian-based systems (more modern, preferred)

sudo apt install python3-pyqt5 python3-pyqt5.qtwebengine python3-pyqt5.qtwebchannel libqt5webkit5-dev

To install QtWebKit (legacy, but available for more platforms).

sudo apt install python3-pyqt5 python3-pyqt5.qtwebkit python-pyqt5 python-pyqt5.qtwebkit libqt5webkit5-dev

## Windows

Requires > .NET 4.0

To use with the latest Chromium you need WebView2 Runtime. If you plan to distribute your software, check out distribution guidelines too.

## MacOS

pyobjc

PyObjC comes presintalled with the Python bundled in macOS. For a stand-alone Python installation you have to install it separately. You can also use QT5 in macOS

# Installation

pip3 install usbsecurity-gui

# Usage

Is a console program and runs like a fiend. To get it running open a terminal and run the following command:

$ usbsecurity-gui

# Help

$ usbsecurity-gui -h | --help

