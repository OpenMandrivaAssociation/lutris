Name:           lutris
Version:        0.4.21
Release:        1
Summary:        Install and play any video game easily
Group:          Games/Other
License:        GPLv3+
URL:            http://lutris.net
Source0:        http://lutris.net/releases/%{name}_%{version}.tar.xz

BuildArch:      noarch
BuildRequires:  python3
BuildRequires:  python3-gobject3
BuildRequires:  python3-pyxdg

Requires:       python3-dbus
Requires:       python3-evdev
Requires:       python3-gobject3
Requires:       python3-pyxdg
Requires:       python3-yaml
Requires:       xrandr
Recommends:     python3-pyinotify

%description
Lutris is a gaming platform for GNU/Linux. Its goal is to make
gaming on Linux as easy as possible by taking care of installing
and setting up the game for the user. The only thing you have to
do is play the game. It aims to support every game that is playable
on Linux.

%prep
%setup -q -n %{name}
%autopatch -p1

%build
%py3_build

%install
%py3_install

%files
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/polkit-1/actions/*
%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{name}/
