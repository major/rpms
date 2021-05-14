%global srcname i3pystatus

%global forgeurl https://github.com/enkore/i3pystatus
Version:        3.35
%global tag     %{version}
%forgemeta

Name:           %{srcname}
Release:        2%{?dist}
Summary:        A complete replacement for i3status

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch

%global _description %{expand:
i3pystatus is a large collection of status modules compatible with i3bar from
the i3 window manager.}
%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
Requires:       python3-psutil
Requires:       python3-pytz
BuildRequires:  python3-devel
BuildRequires:  python3-mock
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%pytest

%files -n python3-%{srcname}
%license MIT-LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/
%{_bindir}/%{srcname}
%{_bindir}/%{srcname}-setting-util

%changelog
* Fri May 14 2021 Major Hayden <major@mhtx.net> - 3.35-2
- Add psutil and pytz requirements.

* Fri May 14 2021 Major Hayden <major@mhtx.net> - 3.35-1
- Initial build.