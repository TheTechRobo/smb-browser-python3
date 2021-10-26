deb:
	make clean || echo "Failed to remove build directory"
	@echo Writing to DEBFILE...
	cd /home/thetechrobo/smb-browser-python3 &&mkdir build &&cd build && cp -r ../tree . && \
		cp -r ../debian tree/DEBIAN && \
		dpkg-deb --build tree && \
		mv tree.deb smb-browser-python3.deb
	@echo Done ! Please take your debfile.

clean:
	@echo Removing BUILD directory ...
	rm -fRIv /home/thetechrobo/smb-browser-python3/build
	sleep 2

all:
	@echo Please say something\!\!
