Name:           wtype
Version:        0.3
Release:        1%{?dist}
Summary:        xdotool type for wayland
License:        MIT

# NOTE(mhayden): archivename is required here because Fedora looks for the
# source tarball without the `v` from the tag. EPEL packaging expects the `v`
# to be present. Setting it manually allows both to work.
%global         forgeurl    https://github.com/atx/%{name}
%global         tag         v%{version}
%global         archivename %{name}-%{tag}.tar.gz
%forgemeta

URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  libxkbcommon-devel
BuildRequires:  meson
BuildRequires:  wayland-devel

%description
%{summary}

%prep
%autosetup %{name}-%{version}

%build
%meson
%meson_build

%install
%meson_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSE
%doc README.md
%{_bindir}/wtype
%{_mandir}/man1/wtype.1*

%changelog
* Mon May 24 2021 Major Hayden <major@mhtx.net> - 0.3-1
- Initial build.
