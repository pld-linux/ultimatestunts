# TODO:
# - add .desktop file

%define	src_ver	0731

Summary:	Remake of the famous game stunts
Summary(pl.UTF-8):	Nowa wersja sławnej gry stunts
Name:		ultimatestunts
Version:	0.7.3
Release:	0.1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/ultimatestunts/%{name}-srcdata-%{src_ver}.tar.gz
# Source0-md5:	3231b1d391ee30b1ec8750019c1e1c3e
Patch0:		%{name}-directories.patch
URL:		http://www.ultimatestunts.nl/
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_image-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freealut-devel
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

%description -l pl.UTF-8
UltimateStunts jest nową wersją sławnej gry stunts. Była to
trójwymiarowa gra wyścigowa, z prostą grafiką CGA/EGA/VGA bez tekstur
ani bez cieniowania, lecz dzięki spektakularnym akrobacjom (obroty,
skoki nad mostami, itp.) świetnie się w nią grało.

Ta, nowsza wersja, daje więcej urozmaiceń, takich jak grafika OpenGL,
dźwięk 3D, czy też gra przez Internet.

%prep
%setup -q -n %{name}-srcdata-%{src_ver}
%patch0 -p1
%{__sed} -i 's/fr_FR/fr/' po/LINGUAS
%{__sed} -i 's#@MKINSTALLDIRS@#/usr/share/automake/mkinstalldirs#' po/Makefile.in.in
mv po/fr{_FR,}.po

%build
touch config.rpath
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
