Name:           lutris
Version:        0.3.8
Release:        1
Summary:        Install and play any video game easily
Group:          Games/Other
License:        GPLv3+
URL:            http://lutris.net
Source0:        http://lutris.net/releases/%{name}_%{version}.tar.xz

BuildArch:      noarch
BuildRequires:  librsvg
BuildRequires:  python
BuildRequires:  python-pyxdg
BuildRequires:	python-gi
BuildRequires:	python-gobject
Requires:       glib-networking
Requires:       gvfs
Requires:       python-gi
Requires:       python-pyxdg
Requires:       python-yaml
Requires:       xrandr

%description
Lutris is a gaming platform for GNU/Linux. Its goal is to make
gaming on Linux as easy as possible by taking care of installing
and setting up the game for the user. The only thing you have to
do is play the game. It aims to support every game that is playable
on Linux.

%prep
%setup -qn %{name}

%build
python setup.py build

%install
python setup.py install --root=%{buildroot} --skip-build

# SVG icon is broken in Qt applications, we use PNGs for now
pushd %{buildroot}%{_iconsdir}/hicolor
  for size in 16 32 48 64 128 256; do
    mkdir -p ${size}x${size}/apps
    rsvg-convert scalable/apps/%{name}.svg -w ${size} -o ${size}x${size}/apps/%{name}.png
  done
  rm -f scalable/apps/%{name}.svg
popd

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/apps.%{name}.gschema.xml
%{_datadir}/%{name}/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/polkit-1/actions/*
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{py_puresitedir}/%{name}-%{version}-py2.7.egg-info
%{py_puresitedir}/%{name}/
