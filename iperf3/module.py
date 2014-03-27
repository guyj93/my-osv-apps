from osv.modules import api

default = api.run("/iperf3.so -s -4 -d")
