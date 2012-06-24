
%define	src_ver	0461
%define	data_ver	0461

Summary:	Remake of the famous game stunts
Summary(pl):	Nowa wersja s�awnej gry stunts
Name:		ultimatestunts
Version:	0.4.6
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/ultimatestunts/%{name}-src-%{src_ver}.tar.gz
# Source0-md5:	ad068409b5dde905d481a7dbee702a0f
Source1:	http://dl.sourceforge.net/ultimatestunts/%{name}-data-%{data_ver}.tar.gz
# Source1-md5:	44fcbb1329864f8cf74b4ee75a71bffc
Patch0:		%{name}-directories.patch
Patch1:		%{name}-gcc34.patch
URL:		http://www.ultimatestunts.nl/
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
UltimateStunts jest now� wersj� s�awnej gry stunts. By�a to
tr�jwymiarowa gra wy�cigowa, z prost� grafik� CGA/EGA/VGA bez tekstur
ani bez cieniowania, lecz dzi�ki spektakularnym akrobacj� (obroty,
skoki na mostami, itp.) �wietnie si� w ni� gra�o.

Ta, nowsza wersja daje wi�cej nowych urozmaice�, takich jak grafika
OpenGL, d�wi�k 3D, czy gra przez Internet.

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
%patch1 -p1

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

cp -R cars environment music sounds textures tiles tracks \
	$RPM_BUILD_ROOT%{_datadir}/games/%{name}
install %{name}.conf $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*

%files data
%defattr(644,root,root,755)
%{_datadir}/games/%{name}
