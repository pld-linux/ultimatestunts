
%define	src_ver	0551

Summary:	Remake of the famous game stunts
Summary(pl):	Nowa wersja s³awnej gry stunts
Name:		ultimatestunts
Version:	0.5.5
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/ultimatestunts/%{name}-srcdata-%{src_ver}.tar.gz
# Source0-md5:	fc2098a0cad33408e9acf339924488c8
Patch0:		%{name}-directories.patch
#Patch1:		%{name}-gcc34.patch
URL:		http://www.ultimatestunts.nl/
Obsoletes:	%{name}-data
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ode-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_noautoreqdep libGL.so.1 libGLU.so.1

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
ani bez cieniowania, lecz dziêki spektakularnym akrobacj± (obroty,
skoki na mostami, itp.) ¶wietnie siê w ni± gra³o.

Ta, nowsza wersja daje wiêcej nowych urozmaiceñ, takich jak grafika
OpenGL, d¼wiêk 3D, czy gra przez Internet.

%prep
%setup -q -n %{name}-srcdata-%{src_ver}
%patch0 -p1
#%%patch1 -p1

%build
# Warning: internal automake voodoo performed
#rm -rf autom4te.cache
%{__aclocal}
%{__autoconf}
#%%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/games/%{name},%{_sysconfdir}}

%{__make} install \
	bindir=$RPM_BUILD_ROOT/%{_bindir} \
	datadir=$RPM_BUILD_ROOT/%{_datadir}

rm -f $RPM_BUILD_ROOT%{_datadir}/games/%{name}/data/Makefile*

ln -s %{_datadir}/games/%{name}/ultimatestunts.conf $RPM_BUILD_ROOT%{_sysconfdir}/ultimatestunts.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/*
# Just a symlink
%attr(755,root,root) %{_sysconfdir}/*
%config(noreplace) %verify(not size mtime md5) %{_datadir}/games/%{name}/*.conf
%attr(755,root,root) %{_datadir}/games/%{name}/%{name}
%attr(755,root,root) %{_datadir}/games/%{name}/stunts*
%attr(755,root,root) %{_datadir}/games/%{name}/trackedit
%{_datadir}/games/%{name}
