#
Summary:	Scenario files for OpenTTD
Name:		openttd-scenarios
Version:	20090404
Release:	1
License:	Mixed
Group:		X11/Applications/Games
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	a57a21cef9c9ebc97be3316939326ff9
Source1:	http://dl.sourceforge.net/openttd/openttd-0.4.8-scenarios.tar.bz2
# Source1-md5:	34e8cb13ce1d4e6b5b24887c628c1ac8
Source2:	http://dl.sourceforge.net/openttd/openttd-0.5.0-scenarios.tar.bz2
# Source2-md5:	37892f1fdded957f956766642a9e877d
URL:		http://www.openttd.com/
Requires:	openttd-data >= 0.7.0-1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Scenario files for OpenTTD.

%prep
%setup -q -a1 -a2
mv openttd-0.4.8-RC1-scenarios/* scenario
mv *.scn scenario

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/openttd

cp -r scenario $RPM_BUILD_ROOT%{_datadir}/openttd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/openttd/scenario/*.scn
%{_datadir}/openttd/scenario/*.tar
%{_datadir}/openttd/scenario/heightmap/*.tar
