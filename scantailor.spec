Name:		scantailor
Version:	0.9.11
Release:	%mkrel 1
Summary:	Scan processing software
License:	GPLv3
Group:		Graphics
Url:		http://scantailor.sf.net
Source:		%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
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
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}/translations
install -pm755 build/%name  %{buildroot}%{_bindir}/
install -pm644 build/*.qm   %{buildroot}%{_datadir}/%{name}/translations
install -pm644 -D resources/appicon.svg %{buildroot}%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
install -pm644 -D %SOURCE1 %{buildroot}%{_datadir}/applications/%{name}.desktop

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}/translations/*
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.svg
