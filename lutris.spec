Name:           lutris
Version:	0.5.15
Release:	1
Summary:        Install and play any video game easily
Group:          Games/Other
License:        GPLv3+
URL:            https://lutris.net
#Source0:        http://lutris.net/releases/%{name}_%{version}.tar.xz
Source0:        https://github.com/lutris/lutris/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  pkgconfig(python)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  python3dist(pyxdg)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pygobject)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gtk+-3.0)

Requires:	glib-networking
Requires:	gvfs
Requires:	python-gi

Requires:	python-dbus
Requires:	python-evdev >= 1.6.0
Requires:	python-gobject3
Requires:	python-pyxdg
Requires:	python-yaml
Requires:	xrandr
Requires:	python-requests
Requires:	python-pillow

Requires:	typelib(GDesktopEnums)
Requires:	typelib(GnomeDesktop)
Requires:	typelib(WebKit2)
Requires:	python3dist(distro)
Requires:	python3dist(lxml)
Requires: python3dist(pypresence)
Requires:	%{_lib}gnome-desktop3_20

# Really optional, but it doesn't look good if we get a huge warning dialog
# on startup...
#Vulkan deps for run games in DXVK and D9VK
Requires:	vulkan-loader
Requires:	%mklibname vulkan 1
# Needed to launch x86 games
%ifarch %{x86_64}
Requires:	libvulkan1
Recommends:	vulkan-loader(x86-32)
Requires: libgnutls30
%endif

# Optional deps without huge complaints

Recommends:     python-pyinotify
Recommends:     wine
Recommends:     gamemode
%ifarch %{x86_64}
Recommends:     gamemode(x86-32)
%endif
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
%autosetup -p1 -n %{name}-%{version}

%build
python setup.py build

# Sed to fix filemagic
sed -i setup.py -e "s/python-magic/file-magic/"

%install
python setup.py install --root=%{buildroot}

%files
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/metainfo/net.lutris.Lutris.metainfo.xml
%{_datadir}/applications/net.lutris.Lutris.desktop
%{_mandir}/man1/lutris.1.*
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%{python_sitelib}/%{name}-%{version}-py%{python_version}.egg-info
%{python_sitelib}/%{name}/
