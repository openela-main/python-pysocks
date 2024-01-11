%global distname PySocks
%global flatname pysocks
%global sum     A Python SOCKS client module

Name:               python-pysocks
Version:            1.6.8
Release:            3%{?dist}
Summary:            %{sum}

License:            BSD
URL:                https://github.com/Anorov/PySocks
Source0:            https://files.pythonhosted.org/packages/source/P/PySocks/PySocks-%{version}.tar.gz
BuildArch:          noarch


%description
A fork of SocksiPy with bug fixes and extra features.

Acts as a drop-in replacement to the socket module. Featuring:

- SOCKS proxy client for Python 2.6 - 3.x
- TCP and UDP both supported
- HTTP proxy client included but not supported or recommended (you should use
  urllib2's or requests' own HTTP proxy interface)
- urllib2 handler included.


%package -n python%{python3_pkgversion}-%{flatname}
Summary:            %{sum}
BuildRequires:      python%{python3_pkgversion}-devel
BuildRequires:      python%{python3_pkgversion}-setuptools
BuildRequires:      python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{flatname}}

# This package doesn't actually exist... but if it did, we would conflict with
# it.
Conflicts:  python%{python3_pkgversion}-SocksiPy


%description -n python%{python3_pkgversion}-%{flatname}
A fork of SocksiPy with bug fixes and extra features.

Acts as a drop-in replacement to the socket module. Featuring:

- SOCKS proxy client for Python 2.6 - 3.x
- TCP and UDP both supported
- HTTP proxy client included but not supported or recommended (you should use
  urllib2's or requests' own HTTP proxy interface)
- urllib2 handler included.


%prep
%autosetup -n %{distname}-%{version}

%build
%py3_build


%install
%py3_install


#%%check
## No tests included in the tarball...
## https://github.com/Anorov/PySocks/issues/37
#%%{__python3} setup.py test


%files -n python%{python3_pkgversion}-%{flatname}
%doc README.md
%license LICENSE
%{python3_sitelib}/socks.py*
%{python3_sitelib}/sockshandler.py*
%{python3_sitelib}/__pycache__/*socks*
%{python3_sitelib}/%{distname}-%{version}-*


%changelog
* Wed Jul 11 2018 Petr Viktorin <pviktori@redhat.com> - 1.6.8-3
- Remove the Python 2 subpackage
  https://bugzilla.redhat.com/show_bug.cgi?id=1590407

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 22 2017 Kevin Fenzi <kevin@scrye.com> - 1.6.8-1
- Update to 1.6.8. Fixes bug #1528490

* Mon Sep 11 2017 Carl George <carl@george.computer> - 1.6.7-1
- Latest upstream
- Add setuptools dependency

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 1.5.7-3
- Rebuild for Python 3.6

* Mon Nov 28 2016 Tim Orling <ticotimo@gmail.com> - 1.5.7-2
- Ship python34-pysocks in EL6

* Sat Sep 17 2016 Kevin Fenzi <kevin@scrye.com> - 1.5.7-1
- Update to 1.5.7

* Fri Sep 16 2016 Orion Poplawski <orion@cora.nwra.com> - 1.5.6-6
- Ship python34-pysocks in EPEL7

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.6-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Jul 15 2016 Ralph Bean <rbean@redhat.com> - 1.5.6-4
- Change our conflicts on python-SocksiPy to an obsoletes/provides.
  https://bugzilla.redhat.com/show_bug.cgi?id=1334407

* Mon May 09 2016 Ralph Bean <rbean@redhat.com> - 1.5.6-3
- Fix typo in explicit conflicts.

* Tue May 03 2016 Ralph Bean <rbean@redhat.com> - 1.5.6-2
- We don't actually need setuptools here.

* Mon May 02 2016 Ralph Bean <rbean@redhat.com> - 1.5.6-1
- Initial package for Fedora
