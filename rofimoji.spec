%global         srcname     rofimoji
%global         forgeurl    https://github.com/fdw/rofimoji
Version:        5.1.0
%global         tag         %{version}
%forgemeta

Name:           %{srcname}
Release:        4%{?dist}
Summary:        A character picker for rofi 😀

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch

%global _description %{expand:
How often did you want to insert one of those Unicode emoji only to learn that
there is no nice picker for Linux? Fear no more, this script uses the power of
rofi (and other dmenu-derivatives like wofi) to present exactly the picker you
always wanted. Insert the selected emoji directly, or copy it to the clipboard.
And you can use it to pick any weird character someone got into Unicode, too.}
%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel

# Requirements for X11
Requires:       rofi
Requires:       xsel
Requires:       xclip
Requires:       xdotool

# Requirements for Wayland
Requires:       wofi
Requires:       wl-clipboard
Requires:       wtype

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}
%generate_buildrequires
%pyproject_buildrequires -r

%build
# DEBUG!
ls -alR
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files 'picker'

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/rofimoji
%{_mandir}/man1/%{name}.1*

%changelog
* Thu May 27 2021 Major Hayden <major@mhtx.net> - 5.1.0-4
- Switched to using pyproject-rpm-macros.

* Mon May 24 2021 Major Hayden <major@mhtx.net> - 5.1.0-3
- Added extra X11/Wayland requirements.
- Removed shebangs in rofimoji.py.
- Added wildcard for future man page compression changes.

* Fri May 14 2021 Major Hayden <major@mhtx.net> - 5.1.0-2
- Remove check section since upstream has no tests.

* Fri May 14 2021 Major Hayden <major@mhtx.net> - 5.1.0-1
- Initial build.
