%global srcname i3pystatus

# NOTE(mhayden): Instructions in the repo say to install from git.
# No more releases are planned.
%global         forgeurl    https://github.com/enkore/i3pystatus
%global         commit      177a00b8742996f2ad95cea298494fb8ec286bf2
%global         shortcommit %(c=%{commit}; echo ${c:0:7}) 
%global         commitdate  20210429
%forgemeta

Name:           %{srcname}
Version:        3.3.5
Release:        0.4.%{commitdate}git%{shortcommit}%{?dist}
Summary:        A complete replacement for i3status

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}
Patch0:         i3pystatus-mock.patch

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
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version} -p0

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
* Mon May 24 2021 Major Hayden <major@mhtx.net> - 3.35-0.4.20210429git177a00b
- Switching to git snapshot source.

* Mon May 24 2021 Major Hayden <major@mhtx.net> - 3.35-3
- Remove python3-mock as depdendency and patch source to use built-in unittest.mock.

* Fri May 14 2021 Major Hayden <major@mhtx.net> - 3.35-2
- Add psutil and pytz requirements.

* Fri May 14 2021 Major Hayden <major@mhtx.net> - 3.35-1
- Initial build.