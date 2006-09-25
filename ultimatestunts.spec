# TODO:
# - add .desktop file

%define	src_ver	0621

Summary:	Remake of the famous game stunts
Summary(pl):	Nowa wersja s³awnej gry stunts
Name:		ultimatestunts
Version:	0.6.2
Release:	0.1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/ultimatestunts/%{name}-srcdata-%{src_ver}.tar.gz
# Source0-md5:	173c9e915d4bcaf7206d8b872b387ad9
Patch0:		%{name}-directories.patch
URL:		http://www.ultimatestunts.nl/
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ode-devel
BuildRequires:	sed >= 4.0
Obsoletes:	ultimatestunts-data
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
UltimateStunts is a remake of the famous game stunts. It was a 3D
racing game, with simple CGA/EGA/VGA graphics and no texture or smooth
shading, but because of the spectacular stunts (loopings, bridges to
jump over, etc.) it was really fun to play.

The remake provides more modern features, like openGL graphics, 3D
sound and Internet multiplaying.

%description -l pl
UltimateStunts jest now± wersj± s³awnej gry stunts. By³a to
trójwymiarowa gra wy¶cigowa, z prost± grafik± CGA/EGA/VGA bez tekstur
ani bez cieniowania, lecz dziêki spektakularnym akrobacjom (obroty,
skoki nad mostami, itp.) ¶wietnie siê w ni± gra³o.

Ta, nowsza wersja daje wiêcej nowych urozmaiceñ, takich jak grafika
OpenGL, d¼wiêk 3D, czy gra przez Internet.

%prep
%setup -q -n %{name}-srcdata-%{src_ver}
%patch0 -p1
sed -i 's/fr_FR/fr/' po/LINGUAS
mv po/fr{_FR,}.po

%build
%{__aclocal}
%{__autoconf}
%{__automake}
# config.h.in created manually, touch it so make will not call autoheader
touch config.h.in
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/games/%{name},%{_sysconfdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	localedir=%{_datadir}/locale \
	usdatadir=$RPM_BUILD_ROOT%{_datadir}/games/%{name}

rm -rf $RPM_BUILD_ROOT%{_datadir}/games/%{name}/lang
find $RPM_BUILD_ROOT%{_datadir}/games/%{name} -name CVS | xargs rm -rf

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.conf
%{_datadir}/games/%{name}
