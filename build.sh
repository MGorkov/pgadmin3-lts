#!/bin/sh

VERSION=1.23.2
BUILDDIR=.build/rpm

# Get build number
if [ -z "$1" ]; then
	if [ -n "$BUILD_NUMBER" ]; then
		BUILD_NUMBER=$BUILD_NUMBER
	else
		echo "BUILD_NUMBER isn't set."
		echo "Usage: $0 BUILD_NUMBER"
		exit 1
	fi
else
	BUILD_NUMBER=$1;
fi

rm -rf $BUILDDIR
mkdir -p $BUILDDIR/{BUILD,RPMS,SOURCES,SPECS,SRPMS,DEBS,SDEBS}
git archive --format=tar.gz --prefix=pgadmin3-lts-${VERSION}/ -o ${BUILDDIR}/SOURCES/pgadmin3-lts-${VERSION}.tar.gz HEAD

sed -e 's/\r$//' ./pgadmin3-lts.spec > $BUILDDIR/SPECS/pgadmin3-lts.spec

rpmbuild -bb $BUILDDIR/SPECS/pgadmin3-lts.spec \
 --define '_topdir '$(pwd)/$BUILDDIR \
 --define 'version '$VERSION \
 --define 'buildnumber '$BUILD_NUMBER

debbuild -bb pgadmin3-lts.debian.spec \
 --define '_topdir '$(pwd)/$BUILDDIR \
 --define 'version '$VERSION \
 --define 'buildnumber '$BUILD_NUMBER
