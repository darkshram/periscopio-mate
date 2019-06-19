Name:          periscopio-mate
Version:       1.18.1
Release:       2%{?dist}
Summary:       Python module to download subtitles for a given video file.
Group:         Applications/Multimedia
License:       GPLv2+
URL:           https://github.com/darkshram/periscopio
Source0:       https://github.com/darkshram/periscopio/archives/%{name}-%{version}.tar.xz
BuildArch:     noarch

BuildRequires: python2-devel
BuildRequires: python2-setuptools
BuildRequires: python-BeautifulSoup
BuildRequires: gettext

Requires:      python-caja
Requires:      notify-python
Requires:      caja

Obsoletes:     periscopio < 1.18.1

%description
A Python2 module to search and download subtitles, forked from Periscope by
Patrick Dessalle.

%prep
%autosetup -p1

%build
%py2_build

%install
%py2_install
mkdir -p %{buildroot}%{_datadir}/caja-python/extensions/
install -m 0755 bin/periscopio-caja/periscopio-caja.py* \
    %{buildroot}%{_datadir}/caja-python/extensions/

# Translations.
for n in po/*.mo ; do
        mkdir -p %{buildroot}/%{_datadir}/locale/`basename $n .mo`/
        install -p -D -m0644 $n %{buildroot}/%{_datadir}/locale/`basename $n .mo`/LC_MESSAGES/periscopio-caja.mo
done

%find_lang periscopio-caja

%files -f periscopio-caja.lang
%doc AUTHORS.md NEWS.md README.md
%license LICENSE.md
%{_bindir}/periscopio
%{_datadir}/caja-python/extensions/periscopio-caja*
%{python2_sitelib}/periscopio.py*
%{python2_sitelib}/periscopio/
%{python2_sitelib}/periscopio-%{version}*

%changelog
* Wed Jun 19 2019 Joel Barrios <http://www.alcancelibre.org/> - 1.18.1-2
- Rebuild for python-caja 1.22.0.

* Mon Dec 11 2017 Joel Barrios <http://www.alcancelibre.org/> - 1.18.1-1
- Update to 1.18.1.
- Localization now works.
- Added spanish, german, english and french support.

* Sun Dec 10 2017 Joel Barrios <http://www.alcancelibre.org/> - 1.18.0-1
- Initial build.
