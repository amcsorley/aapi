A API
==================

An API for things (AKA Aarons API)

Install
-------
    sudo python setup.py install

    configure in /etc/aapi/aapi.conf

    for ssl make certs in /etc/pki/aapi, and uncomment the http_server ssl stuff
    in bin/aapi

    openssl command to make certs looks like
    /usr/bin/openssl req -x509 -newkey rsa:2048 -keyout /etc/pki/aapi/key.pem -out /etc/pki/aapi/cert.pem -days 3650 -nodes -config /etc/pki/aapi/openssl.cnf

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

Code
----

    bin/aapi starts the http service in run_service(), this is where you would uncomment things for ssl

    bin/aapi defines the available end points in Application([]), a class is defined for each end point


