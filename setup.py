# On Python for Series 60, use the SIS files instead.

from distutils.core import setup, Extension
import platform
import sys

LINUX = sys.platform.startswith("linux")
MAC = sys.platform.startswith("darwin")
if MAC:
    RELEASE = [int(b) for b in  platform.release().split(".")]

def getpackagedir():
    if MAC:
        return "src/mac"
    elif LINUX:
        return "src/linux"
    else:
        raise Exception("Unsupported platform")

def getextensions():
    if LINUX:
        linux_ext = Extension("_lightblueutil",
            libraries=["bluetooth"], # C libraries
            sources=["src/linux/lightblue_util.c"]
            )
        linux_obex_ext = Extension("_lightblueobex",
            define_macros=[('LIGHTBLUE_DEBUG', '0')],	# set to '1' to print debug messges
            libraries=["bluetooth", "openobex"], # C libraries
            sources=["src/linux/lightblueobex_client.c",
                     "src/linux/lightblueobex_server.c",
                     "src/linux/lightblueobex_main.c"],
            )
        return [linux_ext, linux_obex_ext]
    return []

packages  = ["lightblue",]
package_dir = {"lightblue":getpackagedir()}

if MAC and RELEASE >= [10,6,0]:
    packages.append("LightAquaBlue")
    package_dir["LightAquaBlue"]="src/LightAquaBlue"

# install the main library
setup(name="lightblue",
    version="0.4.1",
    author="Bea Lam",
    author_email="blammit@gmail.com",
    url="http://lightblue.sourceforge.net",
    description="Cross-platform Python Bluetooth library for Mac OS X, GNU/Linux and Python for Series 60.",
    long_description="LightBlue is a cross-platform Python Bluetooth library for Mac OS X, GNU/Linux and Python for Series 60. It provides support for device and service discovery (with and without end-user GUIs), a standard socket interface for RFCOMM sockets, sending and receiving of files over OBEX, advertising of RFCOMM and OBEX services, and access to local device information.",
    license="GPL",
    packages=packages,
    package_dir=package_dir,
    ext_modules=getextensions(),
    classifiers = [ "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "License :: OSI Approved :: GNU General Public License v3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries",
        "Topic :: System :: Networking",
        "Topic :: Communications",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Other OS" ]
    )


def install_LightAquaBlue():
    import os, sys
    from os import path
    dstroot = "/" if not hasattr(sys, 'real_prefix') else \
       path.dirname(path.dirname(sys.prefix))

    if RELEASE >= [10, 6, 0]:
        os.chdir("src/mac/LightAquaBlue-10.6.0")
    else:
        os.chdir("src/mac/LightAquaBlue-10.5.0")
    args = ['xcodebuild', 'install', 
        '-target', 'LightAquaBlue',
        '-configuration', 'Release',
        'DSTROOT=%s' % dstroot,
        'INSTALL_PATH=/Library/Frameworks',
        'DEPLOYMENT_LOCATION=YES' ]
    print " ".join(args)
    os.system(" ".join(args))


# On Mac, install LightAquaBlue framework
# if you want to install the framework somewhere other than /Library/Frameworks
# make sure the path is also changed in LightAquaBlue.py (in src/mac)
if MAC:
    if "install" in sys.argv:
        install_LightAquaBlue()
