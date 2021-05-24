Name:           wtype
Version:        0.3
Release:        2%{?dist}
Summary:        xdotool type for Wayland
License:        MIT

# NOTE(mhayden): archivename is required here because Fedora looks for the
# source tarball without the `v` from the tag. EPEL packaging expects the `v`
# to be present. Setting it manually allows both to work.
%global         forgeurl    https://github.com/atx/%{name}
%global         tag         v%{version}
%global         archivename %{name}-%{tag}
%forgemeta

URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(xkbcommon)

%description
%{summary}

%prep
%autosetup %{name}-%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/wtype
%{_mandir}/man1/wtype.1*

%changelog
* Mon May 24 2021 Major Hayden <major@mhtx.net> - 0.3-2
- Remove extension from archivename.
- Use pkgconfig to find build requirements.
- Remove post/postun scriptlets as they're no longer needed.

* Mon May 24 2021 Major Hayden <major@mhtx.net> - 0.3-1
- Initial build.
