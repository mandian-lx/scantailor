Name:		scantailor
Version:	0.9.11.1
Release:	%mkrel 1
Summary:	Scan processing software
License:	GPLv3+
Group:		Graphics
Url:		http://scantailor.sf.net
Source0:	http://downloads.sourceforge.net/project/scantailor/%{name}/%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	glib2-devel
BuildRequires:	libxfixes-devel
BuildRequires:	jpeg-devel
BuildRequires:	tiff-devel
BuildRequires:	qt4-devel

%description
Scan Tailor is an interactive post-processing tool for scanned pages. It
performs operations such as page splitting, deskewing, adding/removing borders,
and others. You give it raw scans, and you get pages ready to be printed
or assembled into a PDF or DJVU file. Scanning, optical character recognition,
and assembling multi-page documents are out of scope of this project.

%prep
%setup -q

%build
%cmake
%make

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}/translations
install -pm755 build/%name  %{buildroot}%{_bindir}/
install -pm644 build/*.qm   %{buildroot}%{_datadir}/%{name}/translations
install -pm644 -D resources/appicon.svg %{buildroot}%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
install -pm644 -D %SOURCE1 %{buildroot}%{_datadir}/applications/%{name}.desktop

%if %{mdvver} >= 201200
%find_lang %{name} --with-qt
%define langfile %{name}.lang
%endif

%files %{?langfile:-f %{langfile}}
%defattr(-,root,root,-)
%doc COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.svg
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/translations/
%if %{mdvver} <= 201100
%{_datadir}/%{name}/translations/*
%endif


%changelog
* Sun Mar 11 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.9.11.1-1mdv2011.0
+ Revision: 784101
- new version 0.9.11.1

* Wed Jan 18 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.9.11-1
+ Revision: 762220
- new version 0.9.11

* Sat Jan 01 2011 Александр Казанцев <kazancas@mandriva.org> 0.9.9.2-1mdv2011.0
+ Revision: 627083
- initial release

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.1 packages

* Mon Apr 19 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.9.8-1mdv2010.1
+ Revision: 536858
- update to 0.9.8

* Thu Feb 25 2010 Michael Scherer <misc@mandriva.org> 0.9.7.2-1mdv2010.1
+ Revision: 510898
- adapt and clean rpm from MIB


* Fri Feb 05 2010 Andrey Bondrov <bondrov@math.dvgu.ru> 0.9.7.2-69.1mib2009.1
- First build for MIB users
