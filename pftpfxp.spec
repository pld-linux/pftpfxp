# TODO:
# - make subpackage with autoconnect
#
Summary:	pftpfxp - a command line FXP client
Summary(pl):	pftpfxp - klient FXP dzia³aj±cy z linii poleceñ
Name:		pftpfxp
Version:	0.11.4mew5e
Release:	1
License:	unknown
Group:		Applications/Networking
Source0:	http://pftpmew.tanesha.net/content/%{name}-v%{version}.tgz
# Source0-md5:	e74f9beb26bb485690e5d0a547565728
URL:		http://pftpmew.tanesha.net/
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pftpfxp is a command line FXP client.

%description -l pl
pftpfxp jest klientem FXP dzia³aj±cym z linii poleceñ.

%prep
%setup -q -c
cd %{name}-mew
./configure lnx \
	--openssldir /usr/include/openssl

%{__make} CPP=%{__cc} \
	CPPFLAGS="%{rpmcflags} -Wall -D_REENTRANT -I../include -I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name}-mew/pftp $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{name}-mew/{old,.pftp/*,README.MEW}
%attr(755,root,root) %{_bindir}/%{name}
