.PHONY: module
module: src
	echo '/iperf3.so: $${MODULE_DIR}/iperf3.so' > usr.manifest
	echo '/usr/lib/libiperf.so.0: $${MODULE_DIR}/libiperf.so.0.0.0' >> usr.manifest
	: > bootfs.manifest

.PHONY: src
src:
	./GET

clean:
	rm -rf iperf-* *.tar.gz iperf3.so iperf3 *.manifest *.pyc libiperf.so*
