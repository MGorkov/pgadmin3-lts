Summary:	Graphical client for PostgreSQL
Name:		pgadmin3-lts
Version:	%{version}
Release:	%{buildnumber}%{?dist}
License:	BSD
Group:		Applications/Databases
Source:		ftp://ftp.postgresql.org/pub/pgadmin3/release/v%{version}/src/%{name}-%{version}.tar.gz
URL:		http://www.pgadmin.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	wxGTK3-devel postgresql-devel >= 8.0
BuildRequires:	desktop-file-utils openssl-devel libxml2-devel libxslt-devel
Requires:	wxGTK3

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

%prep
%setup -q

%build
bash bootstrap
./configure --program-suffix=-lts --prefix=/usr --with-wx-version=3.0 CFLAGS=-fPIC CXXFLAGS=-fPIC --with-pgsql=/usr/pgsql-15 --without-sphinx-build
make %{?_smp_mflags} all

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

cp -f ./pkg/debian/pgadmin3.xpm $RPM_BUILD_ROOT/%{_datadir}/%{name}/%{name}.xpm

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/applications

desktop-file-install --dir $RPM_BUILD_ROOT/%{_datadir}/applications \
	--add-category Application\
	--add-category Development\
	./pkg/%{name}.desktop


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc BUGS CHANGELOG LICENSE README.md docs/*
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/*
