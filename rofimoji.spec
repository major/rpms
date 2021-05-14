%global srcname rofimoji

%global forgeurl https://github.com/fdw/rofimoji
Version:        5.1.0
%global tag     %{version}
%forgemeta

Name:           %{srcname}
Release:        2%{?dist}
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
Requires:       rofi
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/picker/
%{_bindir}/rofimoji
%{_mandir}/man1/%{name}.1.gz

%changelog
* Fri May 14 2021 Major Hayden <major@mhtx.net> - 5.1.0-2
- Remove check section since upstream has no tests.

* Fri May 14 2021 Major Hayden <major@mhtx.net> - 5.1.0-1
- Initial build.