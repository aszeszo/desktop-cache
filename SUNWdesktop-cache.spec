#
# spec file for package SUNWdesktop-cache
#
# includes module(s): desktop-cache
#
# Owner: erwannc

%include Solaris.inc

Name:         SUNWdesktop-cache
License:      Other
Group:        System/Libraries
Version:      0.1
Summary:      desktop-cache is a set of SMF services used to update the various GNOME desktop caches.
Source:       desktop-cache-smf-services-%{version}.tar.bz2
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
Docdir:	      %{_defaultdocdir}/doc
SUNW_BaseDir: /
SUNW_Copyright: %{name}.copyright

%include default-depend.inc

%prep
%setup -q -n desktop-cache-smf-services-%version

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
  CPUS=1
fi

libtoolize --copy --force
aclocal $ACLOCAL_FLAGS
automake -a -c -f 
autoconf
./configure --libdir=/lib \
	    --sysconfdir=/var
make -j $CPUS

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean 
rm -rf $RPM_BUILD_ROOT

%files 
# don't use %_localstatedir here, because this is an absolute path
# defined by another package, so it has to be /var/svc even if this
# package's %_localstatedir is redefined
%defattr (-, root, sys)
%dir %attr (0755, root, sys) /var
/var/svc/*
%defattr (-, root, bin)
%dir %attr (0755, root, lib) /lib
/lib/svc/*

%changelog
* Tue Jun 3 2008 - erwann.chenede@sun.com
- Initial spec

