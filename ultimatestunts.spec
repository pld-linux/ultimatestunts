
%define	src_ver	0441
%define	data_ver	0431

Summary:	Remake of the famous game stunts
Summary(pl):	Nowa wersja s³awnej gry stunts
Name:		ultimatestunts
Version:	0.4.4
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/%{name}/%{name}-src-%{src_ver}.tar.gz
# Source0-md5:	21b8ff9caab83f1abd7dd57728f832d1
Source1:	http://dl.sourceforge.net/%{name}/%{name}-data-%{data_ver}.tar.gz
# Source1-md5:	0b8bfcc05f1525067e13c8b6b81aafd3
Patch0:		%{name}-directories.patch
URL:		http://ultimatestunts.sourceforge.net/
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

%package data
Summary:	Data files for UltimateStunts
Summary(pl):	Pliki z danymi dla UltimateStunts
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description data
Data files for UltimateStunts.

%description data -l pl
Pliki z danymi dla UltimateStunts.

%prep
%setup -q -n %{name}-src-%{src_ver} -a 1
%patch0 -p1

%build
rm -rf autom4te.cache
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/games/%{name},%{_sysconfdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -R backgrounds cars music sounds textures tiles tracks \
	$RPM_BUILD_ROOT%{_datadir}/games/%{name}
install %{name}.conf $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/*

%files data
%defattr(644,root,root,755)
%{_datadir}/games/%{name}
