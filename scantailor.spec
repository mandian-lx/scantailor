%define ver %(echo %version | tr \. \_ )

Summary:	An interactive post-processing tool for scanned pages
Name:		scantailor
Version:	0.9.12.1
Release:	0
License:	GPLv3+ or LGPLv2.1
Group:		Office
URL:		http://scantailor.org/
Source0:	https://github.com/%{name}/%{name}/archive/RELEASE_%{ver}.tar.gz
#Source0:	https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	boost-devel
BuildRequires:	desktop-file-utils
BuildRequires:	imagemagick
BuildRequires:	jpeg-devel
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(QtCore)
BuildRequires:	pkgconfig(QtGui)
BuildRequires:	pkgconfig(QtXml)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xrender)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(zlib)

%description
Scan Tailor is an interactive post-processing tool for scanned pages. It
performs operations such as page splitting, deskewing, adding/removing
borders, and others. You give it raw scans, and you get pages ready to be
printed or assembled into a PDF or DJVU file. Scanning, optical character
recognition, and assembling multi-page documents are out of scope of this
project.

%files -f %{name}.lang
%{_bindir}/%{name}
%{_bindir}/%{name}-cli
%{_datadir}/applications/%{product}-%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%{_datadir}/pixmaps/%{name}.xpm
%doc resources/icons/COPYING
%doc COPYING

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-RELEASE_%{ver}

# .desktop
cat > %{product}-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
GenericName="Scan Tailor"
Comment="An interactive post-processing tool for scanned pages"
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=false
Categories=Office;Graphics;Scanning;RasterGraphics;
X-Vendor=%{vendor}
EOF

%build
%cmake
%make

%install
%make_install -C build

# icons
for d in 16 32 48 64 128 256 512
do
	install -dm 0755 %{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/
	convert -scale ${d}x${d} resources/appicon.svg \
		%{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/%{name}.png
done
#  pixmap
install -dm 0755 %{buildroot}%{_datadir}/pixmaps/
convert -size 32x32 resources/appicon.svg \
	%{buildroot}%{_datadir}/pixmaps/%{name}.xpm
#  scalable
install -dm 0755 %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
install -pm 0644 resources/appicon.svg \
	%{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

# desktop file
install -dm 0755 %{buildroot}%{_datadir}/applications/
desktop-file-install \
	--dir %{buildroot}%{_datadir}/applications \
	%{product}-%{name}.desktop

# locales
%find_lang %{name} --with-qt

