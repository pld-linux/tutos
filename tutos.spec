Summary:	The Ultimate Team Organisation Software
Summary(pl):	TUTOS - oprogramowanie do organizacji pracy grupowej
Name:		tutos
Version:	1.1.20030715
Release:	0.1
License:	GPL v2+
Group:		Applications/WWW
Vendor:		Gero Kohnert <gokohnert@users.sourceforge.net>
Source0:	http://dl.sourceforge.net/%{name}/%{name}-php-%{version}.tar.bz2
# Source0-md5:	03c13ad482a398539ce53f7037dbfa30
Patch0:		%{name}-config.patch
URL:		http://www.tutos.org/
PreReq:		apache
Requires(post,preun):	grep
Requires(preun):	fileutils
Requires:	php-pcre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_tutosdir	/home/services/httpd/html/tutos

%description
TUTOS is a webbased groupware or ERP/CRM suite that provides the users
with:
- personal and group calendars
- addressbook
- projectmanagement
- filemanagement
- taskmanagement
- bugtracking
- notes
- installation management
- mail interface

%description -l pl
TUTOS (The Ultimate Team Organisation Software) jest opartym na WWW
oprogramowaniem do pracy grupowej (ERP/CRM), udostêpniaj±cym
u¿ytkownikom:
- osobiste i grupowe kalendarze
- ksi±¿kê adresow±
- zarz±dzanie projektami
- zarz±dzanie plikami
- zarz±dzanie zadaniami
- ¶ledzenie b³êdów
- notatki
- zarz±dzanie instalacj±
- interfejs do poczty elektronicznej.

TUTOS zosta³ przet³umaczony równie¿ na jêzyk polski.

%prep
%setup -q -n %{name}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_tutosdir}/{php/{auth,db,file,group,invoice,layout,ldap,localization,mailbox,note,resource,url,watchlist},html/{help,blue,red},homepage,documentation/{user_manual,admin_manual,book0},repository},/etc/httpd}

install php/{*.{php,pinc,p3},.htaccess}	$RPM_BUILD_ROOT%{_tutosdir}/php
install php/auth/*.pinc			$RPM_BUILD_ROOT%{_tutosdir}/php/auth
install php/db/*.pinc			$RPM_BUILD_ROOT%{_tutosdir}/php/db
install php/file/*.{php,pinc,p3}	$RPM_BUILD_ROOT%{_tutosdir}/php/file
install php/group/*.{php,pinc,p3}	$RPM_BUILD_ROOT%{_tutosdir}/php/group
install php/invoice/*.{php,pinc,p3}	$RPM_BUILD_ROOT%{_tutosdir}/php/invoice
install php/layout/*.pinc		$RPM_BUILD_ROOT%{_tutosdir}/php/layout
install php/ldap/*.{php,pinc,p3}	$RPM_BUILD_ROOT%{_tutosdir}/php/ldap
install php/localization/*.{pinc,p3}	$RPM_BUILD_ROOT%{_tutosdir}/php/localization
install php/mailbox/*.{php,pinc,p3}	$RPM_BUILD_ROOT%{_tutosdir}/php/mailbox
install php/note/*.{php,pinc,p3}	$RPM_BUILD_ROOT%{_tutosdir}/php/note
install php/resource/*.{php,pinc,p3}	$RPM_BUILD_ROOT%{_tutosdir}/php/resource
install php/url/*.{php,pinc,p3}		$RPM_BUILD_ROOT%{_tutosdir}/php/url
install php/watchlist/*.{php,pinc,p3}	$RPM_BUILD_ROOT%{_tutosdir}/php/watchlist
install php/config_default.pinc		$RPM_BUILD_ROOT%{_tutosdir}/php/config.pinc

install html/{*.{html,proto.*,png,gif,css},.htaccess} $RPM_BUILD_ROOT%{_tutosdir}/html
install html/help/{*.html,.htaccess}	$RPM_BUILD_ROOT%{_tutosdir}/html/help
install html/blue/*.{gif,png}		$RPM_BUILD_ROOT%{_tutosdir}/html/blue
install html/red/*.gif			$RPM_BUILD_ROOT%{_tutosdir}/html/red

install homepage/{*.html,.htaccess}	$RPM_BUILD_ROOT%{_tutosdir}/homepage

install documentation/user_manual/*.png	$RPM_BUILD_ROOT%{_tutosdir}/documentation/user_manual
install documentation/admin_manual/*.png $RPM_BUILD_ROOT%{_tutosdir}/documentation/admin_manual
install documentation/book0/*.html	$RPM_BUILD_ROOT%{_tutosdir}/documentation/book0

install *.sh $RPM_BUILD_ROOT%{_tutosdir}

install apache.conf $RPM_BUILD_ROOT/etc/httpd/tutos.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /etc/httpd/httpd.conf ] && \
    ! grep -q "^Include.*/tutos.conf" /etc/httpd/httpd.conf; then
	echo "Include /etc/httpd/tutos.conf" >> /etc/httpd/httpd.conf
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
	echo "Do not forget tu setup tutos' database!"
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
	echo "Do not forget tu setup tutos' database!"
fi

%preun
if [ "$1" = "0" ]; then
	umask 027
	grep -E -v "^Include.*tutos.conf" /etc/httpd/httpd.conf > \
		/etc/httpd/httpd.conf.tmp
	mv -f /etc/httpd/httpd.conf.tmp /etc/httpd/httpd.conf
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%files
%defattr(644,root,root,755)
%doc README README.ldap ToDo ChangeLog
%config(noreplace) %verify(not size mtime md5) /etc/httpd/tutos.conf
%dir %{_tutosdir}
%attr(755,root,root) %{_tutosdir}/*.sh
%attr(775,root,http) %{_tutosdir}/repository
%{_tutosdir}/html
%{_tutosdir}/homepage
%{_tutosdir}/documentation
%dir %{_tutosdir}/php
%{_tutosdir}/php/.htaccess
%{_tutosdir}/php/[^c]*
%{_tutosdir}/php/c[^o]*
%{_tutosdir}/php/co[^n]*
%{_tutosdir}/php/config_default.pinc
%attr(640,root,http) %config(noreplace) %verify(not size mtime md5) %{_tutosdir}/php/config.pinc
