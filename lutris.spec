Name:           lutris
Version:        0.5.1.3
Release:        1
Summary:        Install and play any video game easily
Group:          Games/Other
License:        GPLv3+
URL:            http://lutris.net
Source0:        http://lutris.net/releases/%{name}_%{version}.tar.xz

BuildArch:      noarch
BuildRequires:  pkgconfig(python)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  python3egg(pyxdg)
BuildRequires:  python3egg(setuptools)
BuildRequires:  python3egg(pygobject)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gtk+-3.0)

Requires:       glib-networking
Requires:       gvfs
Requires:       python-gi

Requires:       python-dbus
Requires:       python-evdev
Requires:       python-gobject3
Requires:       python-pyxdg
Requires:       python-yaml
Requires:       xrandr
Requires:       python-requests
Requires:       python-pillow

Requires:       typelib(GDesktopEnums)

# Optional deps

Recommends:     python-pyinotify
Recommends:     wine
Recommends:     gamemode
# Not ready (yet)
Recommends:     libstrange

%description
Lutris is a gaming platform for GNU/Linux. Its goal is to make
gaming on Linux as easy as possible by taking care of installing
and setting up the game for the user. The only thing you have to
do is play the game. It aims to support every game that is playable
on Linux.

#Dont use #py_build and #py_install because when launch app you see error: ImportError: No module named lutris.gui.application
#https://github.com/lutris/lutris/issues/1428 (penguin)

%prep
%setup -q -n %{name}
%autopatch -p1

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%{_bindir}/%{name}
%{_bindir}/%{name}-wrapper
%{_datadir}/%{name}/
%{_datadir}/appdata/net.lutris.Lutris.appdata.xml
%{_datadir}/applications/net.lutris.Lutris.desktop
%{_datadir}/polkit-1/actions/*
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%{python_sitelib}/%{name}-%{version}-py%{python_version}.egg-info
%{python_sitelib}/%{name}/
