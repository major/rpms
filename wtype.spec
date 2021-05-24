%global forgeurl https://github.com/atx/wtype
Version:        0.3
%global tag     v%{version}
%forgemeta

Name:           wtype
Release:        1%{?dist}
Summary:        xdotool type for wayland

License:        MIT
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
%autosetup

%build
ls -alR
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
