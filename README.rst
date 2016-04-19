A API
==================

An API for things (AKA Aarons API)

Install
-------
    sudo python setup.py install

    configure in /etc/aapi/aapi.conf

    for ssl make certs in /etc/pki/aapi, and uncomment the http_server ssl stuff
    in bin/aapi

Usage
-----

    aapi [-h] [-d] [-f] [-P [PIDFILE]]
    
    A API daemon
    
    optional arguments:
      -h, --help            show this help message and exit
      -d, --daemon          run in the background
      -f, --foreground      run in the foreground
      -P, --pidfile FILE    pid file for use with service script

Start manually

    sudo aapi -d
    
Start with the service script

    sudo service aapi start
