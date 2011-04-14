PyPandora is a python interface to [Pandora](http://www.pandora.com/) based on [pianobar](http://github.com/PromyLOPh/pianobar)

It can either be used directly as a python module with an incredibly simple interface:

    import pypandora
    pypandora.login(username, password)
    print pypandora.stations
    pypandora.stations[0].play(True)

The rpcs server can be started with python -m "pypandora.rpc_server", by default it listens on port 8123

Mark Rogers has written a [kickass web frontend](http://github.com/f4nt/djpandora) to control the rpc server from your browser.
