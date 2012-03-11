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
