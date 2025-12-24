Name:           rewaita
Version:        1.1.0
Release:        1%{?dist}
Summary:        A tool for recoloring GTK4/LibAdwaita apps to popular color schemes
License:        GPL-3.0-or-later
URL:            https://github.com/SwordPuffin/Rewaita
Source0:        https://github.com/SwordPuffin/Rewaita/archive/refs/tags/v%{version}.tar.gz#/Rewaita-%{version}.tar.gz
Patch0:         fix-autostart.patch
BuildArch:      noarch

BuildRequires:  libvulkan1
BuildRequires:  meson >= 1.0.0
BuildRequires:  python3-base
BuildRequires:  desktop-file-utils
BuildRequires:  appstream-glib
BuildRequires:  gtk4-tools
BuildRequires:  pkgconfig(gio-2.0)

Requires:       gtk4
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       python3-Pillow
Requires:       python3-numpy
Requires:       typelib(GtkSource) = 5
Requires:       typelib(Adw) = 1
Requires:       xdg-desktop-portal-gtk
Recommends:     gnome-shell-extension-user-theme

%description
Rewaita allows you to customize the appearance of GTK4 and
LibAdwaita applications by applying different color palettes and themes.

%prep
%autosetup -n Rewaita-%{version} -p1

%build
%meson
%meson_build

%install
%meson_install

desktop-file-validate %{buildroot}%{_datadir}/applications/io.github.swordpuffin.rewaita.desktop

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/io.github.swordpuffin.rewaita.metainfo.xml

%check
%meson_test

%files
%license COPYING
%doc README.md
%{_bindir}/rewaita
%{_datadir}/rewaita/
%{_datadir}/applications/io.github.swordpuffin.rewaita.desktop
%{_datadir}/dbus-1/services/io.github.swordpuffin.rewaita.service
%{_datadir}/glib-2.0/schemas/io.github.swordpuffin.rewaita.gschema.xml
%{_datadir}/icons/hicolor/*/apps/io.github.swordpuffin.rewaita.*
%{_datadir}/icons/hicolor/scalable/actions/brush-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/code-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/external-link-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/hammer-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/leaf-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/reload-symbolic.svg
%{_datadir}/icons/hicolor/symbolic/apps/io.github.swordpuffin.rewaita-symbolic.svg
%{_datadir}/metainfo/io.github.swordpuffin.rewaita.metainfo.xml
%lang(nl) %{_datadir}/locale/nl/LC_MESSAGES/rewaita.mo
%lang(ru) %{_datadir}/locale/ru/LC_MESSAGES/rewaita.mo
%lang(tr) %{_datadir}/locale/tr/LC_MESSAGES/rewaita.mo

%changelog