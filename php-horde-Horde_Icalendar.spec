# TODO
# - system locale dir
%define		status		stable
%define		pearname	Horde_Icalendar
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - iCalendar API
Name:		php-horde-Horde_Icalendar
Version:	1.0.0
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.horde.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	a4abf90a9384b7853605e6761fc6389b
URL:		http://pear.horde.org/package/Horde_Icalendar/
BuildRequires:	php-channel(pear.horde.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php-channel(pear.horde.org)
Requires:	php-horde-Horde_Date < 2.0.0
Requires:	php-horde-Horde_Exception < 2.0.0
Requires:	php-horde-Horde_Mime < 2.0.0
Requires:	php-horde-Horde_Support < 2.0.0
Requires:	php-horde-Horde_Translation < 2.0.0
Requires:	php-horde-Horde_Util < 2.0.0
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides an API for dealing with iCalendar data.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc docs/Horde_Icalendar/*
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/Horde/Icalendar.php
%{php_pear_dir}/Horde/Icalendar
%{php_pear_dir}/data/Horde_Icalendar
