Summary: The Reliable Event Logging Protocol library
Name: librelp
Version: 1.2.12
Release: 1%{?dist}.1
License: GPLv3+
Group: System Environment/Libraries
URL: http://www.rsyslog.com/
Source0: http://download.rsyslog.com/librelp/%{name}-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires: gnutls-devel >= 1.4.0
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Patch1: librelp-1.2.12-rhbz1561232-snprintf.patch

%description
Librelp is an easy to use library for the RELP protocol. RELP (stands
for Reliable Event Logging Protocol) is a general-purpose, extensible
logging protocol.

%package devel
Summary: Development files for the %{name} package
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
Librelp is an easy to use library for the RELP protocol. The
librelp-devel package contains the header files and libraries needed
to develop applications using librelp.

%prep
%setup -q

%patch1 -p1 -b .snprintf

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT/%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun
if [ "$1" = "0" ] ; then
    /sbin/ldconfig
fi

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS README doc/*html
%{_libdir}/librelp.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/librelp.so
%{_libdir}/pkgconfig/relp.pc

%changelog
* Wed Mar 28 2018 Radovan Sroka <rsroka@redhat.com> 1.2.12-1.1
- fixed bad NVR
- resolves rhbz#1561232

* Wed Mar 28 2018 Radovan Sroka <rsroka@redhat.com> 1.2.12-2
- fixed CVE-2018-1000140
- resolves rhbz#1561232

* Mon Feb 13 2017 Radovan Sroka <rsroka@redhat.com> 1.2.12-1
- rebase to 1.2.12
- inevitable update due to rsyslog rebase 
- resolves rhbz#1420716

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 1.2.0-3
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.2.0-2
- Mass rebuild 2013-12-27

* Wed Jul 31 2013 Tomas Heinrich <theinric@redhat.com> - 1.2.0-1
- rebase to 1.2.0
- add gnutls-devel to BuildRequires

* Wed Apr 10 2013 Tomas Heinrich <theinric@redhat.com> - 1.0.3-1
- rebase to 1.0.3

* Thu Apr 04 2013 Tomas Heinrich <theinric@redhat.com> - 1.0.2-1
- rebase to 1.0.2

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Nov 21 2012 Tomas Heinrich <theinric@redhat.com> - 1.0.1-1
- upgrade to upstream version 1.0.1

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 15 2010 Tomas Heinrich <theinric@redhat.com> - 1.0.0-1
- upgrade to upstream version 1.0.0

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed May  7 2008 Tomas Heinrich <theinric@redhat.com> 0.1.1-2
- removed "BuildRequires: autoconf automake"

* Tue Apr 29 2008 Tomas Heinrich <theinric@redhat.com> 0.1.1-1
- initial build
