Name:    scantailor
Version: 0.9.7.2
Release: %mkrel 1
Summary: Scan processing software
License: GPLv3
Group:   Graphics
Url:           http://scantailor.sf.net
Source:        %{name}-%{version}.tar.gz
Source1:       %{name}.desktop
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: boost-devel
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: glib2-devel
BuildRequires: libxfixes-devel
BuildRequires: jpeg-devel
BuildRequires: tiff-devel
BuildRequires: qt4-devel

%description
Scantailor is a book scan processing software. It
splits scanned pages, aligns, and converts to b/w from
grayscale. It has GUI interface. Analogs of this
program are ScanKromsator (written by kamerade bolega,
currently discontinued), BookRestorer.

%prep
%setup -q

%build
cp resources/appicon.svg %{name}.svg
%cmake
%make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}/translations
install -pm755 build/%name  %{buildroot}%{_bindir}/
install -pm644 build/*.qm   %{buildroot}%{_datadir}/%{name}/translations
install -pm644 -D %{name}.svg %{buildroot}%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
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

