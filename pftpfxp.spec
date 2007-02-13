# TODO:
# - make subpackage with autoconnect
#
Summary:	pftpfxp - a command line FXP client
Summary(pl.UTF-8):	pftpfxp - klient FXP działający z linii poleceń
Name:		pftpfxp
Version:	0.11.4mew6
Release:	2
License:	unknown
Group:		Applications/Networking
Source0:	http://pftpmew.tanesha.net/content/%{name}-v%{version}.tgz
# Source0-md5:	22528192327488a372a6de1f5d2709dc
URL:		http://pftpmew.tanesha.net/
BuildRequires:	ncurses-devel
BuildRequires:	ncurses-ext-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pftpfxp is a command line FXP client.

%description -l pl.UTF-8
pftpfxp jest klientem FXP działającym z linii poleceń.

%prep
%setup -q -c

%build
cd %{name}-mew
./configure lnx \
	--openssldir /usr/include/openssl

%{__make} dynamic \
	CPP="%{__cc}" \
	CPPFLAGS="%{rpmcflags} -Wall -D_REENTRANT -DTLS -I../include -I/usr/include/ncurses" \
	LINKFLAGS="-lpanel -lncurses -lpthread -lssl -lcrypto -lstdc++ -ldl"

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
