#!/bin/bash
CURPATH=`pwd`

rm -rf ./rpmbuild

echo "%client_version 1.0" > /etc/rpm/macros.mcos-tp-client
echo '%debug_package %{nil}' > ~/.rpmmacros

mkdir -p ./rpmbuild/SOURCES
tar zcf ./rpmbuild/SOURCES/gim-1.0.tar.gz ./gim-1.0
rpmbuild -bb --define="%_topdir `pwd`/rpmbuild" ${CURPATH}/gim.spec
