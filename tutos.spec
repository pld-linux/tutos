Summary:	The Ultimate Team Organisation Software
Name:		tutos
Version:	1.0.20020917
Release:	1
License:	GPL v2+
Group:		Applications/Databases/Interfaces
Source0:	http://download.sourceforge.net/%{name}/%{name}-php-%{version}.tar.bz2
Patch0:		%{name}-config.patch
URL:		http://www.tutos.org/
Vendor:		Gero Kohnert <gokohnert@users.sourceforge.net>
Requires:	apache
Requires:	php-pcre
Buildarch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_tutosdir	/home/httpd/html/tutos

%description
TUTOS is a webbased groupware or ERP/CRM suite that provides the users
with
- personal and group calendars
- addressbook
- projectmanagement
- filemanagement
- taskmanagement
- bugtracking
- notes
- installation management
- mail interface

%prep
%setup -q -n %{name}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_tutosdir}/{php/{group,invoice,note,resource,watchlist},html/{help,blue,red},homepage,documentation/{user_manual,admin_manual,book0},repository},%{_sysconfdir}/httpd}

install php/{*.{php,pinc,p3},.htaccess}	$RPM_BUILD_ROOT%{_tutosdir}/php
install php/group/*.{php,pinc,p3}	$RPM_BUILD_ROOT%{_tutosdir}/php/group
install php/invoice/*.{php,pinc,p3}	$RPM_BUILD_ROOT%{_tutosdir}/php/invoice
install php/note/*.{php,pinc,p3}	$RPM_BUILD_ROOT%{_tutosdir}/php/note
install php/resource/*.{php,pinc,p3}	$RPM_BUILD_ROOT%{_tutosdir}/php/resource
install php/watchlist/*.{php,pinc,p3}	$RPM_BUILD_ROOT%{_tutosdir}/php/watchlist
install php/config_default.pinc		$RPM_BUILD_ROOT%{_tutosdir}/php/config.pinc

install html/{*.{html,proto.*,png,gif,css},.htaccess,faxheader} $RPM_BUILD_ROOT%{_tutosdir}/html
install html/help/{*.html,.htaccess}	$RPM_BUILD_ROOT%{_tutosdir}/html/help
install html/blue/*.gif			$RPM_BUILD_ROOT%{_tutosdir}/html/blue
install html/red/*.gif			$RPM_BUILD_ROOT%{_tutosdir}/html/red

install homepage/{*.html,.htaccess}	$RPM_BUILD_ROOT%{_tutosdir}/homepage

install documentation/user_manual/*.png	$RPM_BUILD_ROOT%{_tutosdir}/documentation/admin_manual
install documentation/admin_manual/*.png $RPM_BUILD_ROOT%{_tutosdir}/documentation/admin_manual
install documentation/book0/*.html	$RPM_BUILD_ROOT%{_tutosdir}/documentation/book0

install *.sh $RPM_BUILD_ROOT%{_tutosdir}

install apache.conf $RPM_BUILD_ROOT%{_sysconfdir}/httpd/tutos.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_sysconfdir}/httpd/httpd.conf ] && \
    ! grep -q "^Include.*/tutos.conf" %{_sysconfdir}/httpd/httpd.conf; then
	echo "Include /etc/httpd/tutos.conf" >> %{_sysconfdir}/httpd/httpd.conf
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun
if [ "$1" = "0" ]; then
	grep -E -v "^Include.*tutos.conf" %{_sysconfdir}/httpd/httpd.conf > \
		{_sysconfdir}/httpd/httpd.conf.tmp
	mv -f %{_sysconfdir}/httpd/httpd.conf.tmp %%{_sysconfdir}/httpd/httpd.conf
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%files
%defattr(644,root,root,755)
%doc README ToDo ChangeLog
%config %{_sysconfdir}/httpd/tutos.conf
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
