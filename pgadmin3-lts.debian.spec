Summary:			Graphical client for PostgreSQL
Name:					pgadmin3-lts
Version:			%{version}
Release:			%{buildnumber}
License:			BSD
Group:				Applications/Databases
Source:				ftp://ftp.postgresql.org/pub/pgadmin3/release/v%{version}/src/%{name}-%{version}.tar.gz
URL:					http://www.pgadmin.org/
Packager:			Maksim Gorkov <me.gorkov@tensor.ru>
AutoReqProv:	no
Requires:			libpq5 libsdl1.2-dev libmspack0t64 libjpeg62

%description
pgAdmin III is a powerful administration and development
platform for the PostgreSQL database, free for any use.
It is designed to answer the needs of all users,
from writing simple SQL queries to developing complex
databases. The graphical interface supports all PostgreSQL
features and makes administration easy.

pgAdmin III is designed to answer the needs of all users,
from writing simple SQL queries to developing complex databases.
The graphical interface supports all PostgreSQL features and
makes administration easy. The application also includes a syntax
highlighting SQL editor, a server-side code editor, an
SQL/batch/shell job scheduling agent, support for the Slony-I
replication engine and much more. No additional drivers are
required to communicate with the database server.

%package docs
Summary:	Documentation for pgAdmin3
Group:		Applications/Databases
Requires:	%{name} = %{version}

%description docs
This package contains documentation for various languages,
which are in html format.

%define debug_package %{nil}
%define __os_install_post %{nil}
%define _build_id_links none

%install
cd %{_topdir}/BUILD/%{name}-%{version}
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

cp -f ./pkg/pgadmin3.png $RPM_BUILD_ROOT/%{_datadir}/%{name}/%{name}.png
mkdir -p $RPM_BUILD_ROOT/%{_libdir}
for f in libpng15.so.15 libtiff.so.5 libtiffxx.so.5 libjbig.so.2.0 libwx_baseu-3.0.so.0 libwx_baseu-3.0.so.0 libwx_baseu_net-3.0.so.0 libwx_baseu_net-3.0.so.0 libwx_baseu_xml-3.0.so.0 libwx_baseu_xml-3.0.so.0 libwx_gtk3u_adv-3.0.so.0 libwx_gtk3u_adv-3.0.so.0 libwx_gtk3u_aui-3.0.so.0 libwx_gtk3u_aui-3.0.so.0 libwx_gtk3u_core-3.0.so.0 libwx_gtk3u_core-3.0.so.0 libwx_gtk3u_html-3.0.so.0 libwx_gtk3u_html-3.0.so.0 libwx_gtk3u_stc-3.0.so.0 libwx_gtk3u_stc-3.0.so.0 libwx_gtk3u_xrc-3.0.so.0 libwx_gtk3u_xrc-3.0.so.0
	do
		cp /usr/lib64/$f $RPM_BUILD_ROOT/%{_libdir}/
	done
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/applications

desktop-file-install --dir $RPM_BUILD_ROOT/%{_datadir}/applications --add-category Application --add-category Development ./pkg/%{name}.desktop


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc BUGS CHANGELOG LICENSE README.md docs/*
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/*
%{_libdir}/*
