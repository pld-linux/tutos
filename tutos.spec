Summary:	The Ultimate Team Organisation Software
Summary(pl):	TUTOS - oprogramowanie do organizacji pracy grupowej
Name:		tutos
%define		_realname	TUTOS
Version:	1.2.20040906
Release:	0.2
License:	GPL v2+
Group:		Applications/WWW
Source0:	http://dl.sourceforge.net/tutos/%{_realname}-php-%{version}.tar.bz2
# Source0-md5:	1b4ad35195e30d26afcfca277d480180
# Source0-size:	678564
Source1:        %{name}.conf
Patch0:		%{name}-config.patch
URL:		http://www.tutos.org/
PreReq:		apache
Requires(post,preun):	grep
Requires(preun):	fileutils
Requires:	php-pcre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_tutosdir	%{_datadir}/%{name}

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
#%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_tutosdir}/php/{auth,bugtracking/{help,templates},db,file/help,group/help,invoice/help,layout,ldap/help,localization,mailbox/help,note/{help,templates},rate/help,reminder/{help,templates},resource/help,url/help,watchlist/{help,templates},xml} \
    $RPM_BUILD_ROOT%{_tutosdir}/html/{blue,help,nuke,red} \
    $RPM_BUILD_ROOT%{_tutosdir}/{homepage,repository} \
    $RPM_BUILD_ROOT{%{_tutosdir}/libs/{excel,fpdf/{font,tutorial}},/etc/httpd}

install php/{*.{php,pinc,p3},.htaccess}	$RPM_BUILD_ROOT%{_tutosdir}/php
install php/auth/*.pinc			$RPM_BUILD_ROOT%{_tutosdir}/php/auth
install php/bugtracking/{*.{php,pinc,p3},.htaccess} $RPM_BUILD_ROOT%{_tutosdir}/php/bugtracking
install php/bugtracking/help/{*.html,.htaccess}	$RPM_BUILD_ROOT%{_tutosdir}/php/bugtracking/help
install php/bugtracking/templates/{*.proto.*,.htaccess}	$RPM_BUILD_ROOT%{_tutosdir}/php/bugtracking/templates
install php/db/*.pinc			$RPM_BUILD_ROOT%{_tutosdir}/php/db
install php/file/{*.{php,pinc,p3},.htaccess} $RPM_BUILD_ROOT%{_tutosdir}/php/file
install php/file/help/{*.html,.htaccess} $RPM_BUILD_ROOT%{_tutosdir}/php/file/help
install php/group/{*.{php,pinc,p3},.htaccess} $RPM_BUILD_ROOT%{_tutosdir}/php/group
install php/group/help/{*.html,.htaccess} $RPM_BUILD_ROOT%{_tutosdir}/php/group/help
install php/invoice/{*.{php,pinc,p3},.htaccess}	$RPM_BUILD_ROOT%{_tutosdir}/php/invoice
install php/invoice/help/{*.html,.htaccess} $RPM_BUILD_ROOT%{_tutosdir}/php/invoice/help
install php/layout/*.pinc		$RPM_BUILD_ROOT%{_tutosdir}/php/layout
install php/ldap/{*.{php,pinc,p3},.htaccess} $RPM_BUILD_ROOT%{_tutosdir}/php/ldap
install php/ldap/help/.htaccess		$RPM_BUILD_ROOT%{_tutosdir}/php/ldap/help
install php/localization/*.{pinc,p3}	$RPM_BUILD_ROOT%{_tutosdir}/php/localization
install php/mailbox/{*.{php,pinc,p3},.htaccess}	$RPM_BUILD_ROOT%{_tutosdir}/php/mailbox
install php/mailbox/help/{*.html,.htaccess} $RPM_BUILD_ROOT%{_tutosdir}/php/mailbox/help
install php/note/{*.{php,pinc,p3},.htaccess} $RPM_BUILD_ROOT%{_tutosdir}/php/note
install php/note/help/{*.html,.htaccess}	$RPM_BUILD_ROOT%{_tutosdir}/php/note/help
install php/note/templates/{*.proto.*,.htaccess} $RPM_BUILD_ROOT%{_tutosdir}/php/note/templates
install php/rate/{*.{php,pinc,p3},.htaccess} $RPM_BUILD_ROOT%{_tutosdir}/php/rate
install php/rate/help/{*.html,.htaccess} $RPM_BUILD_ROOT%{_tutosdir}/php/rate/help
install php/reminder/{*.{php,pinc,p3},.htaccess} $RPM_BUILD_ROOT%{_tutosdir}/php/reminder
install php/reminder/help/{*.html,.htaccess} $RPM_BUILD_ROOT%{_tutosdir}/php/reminder/help
install php/reminder/templates/{*.proto.*,.htaccess} $RPM_BUILD_ROOT%{_tutosdir}/php/reminder/templates
install php/resource/{*.{php,pinc,p3},.htaccess} $RPM_BUILD_ROOT%{_tutosdir}/php/resource
install php/resource/help/{*.html,.htaccess} $RPM_BUILD_ROOT%{_tutosdir}/php/resource/help
install php/url/{*.{php,pinc,p3},.htaccess} $RPM_BUILD_ROOT%{_tutosdir}/php/url
install php/url/help/{*.html,.htaccess} $RPM_BUILD_ROOT%{_tutosdir}/php/url/help
install php/watchlist/{*.{php,pinc,p3},.htaccess} $RPM_BUILD_ROOT%{_tutosdir}/php/watchlist
install php/watchlist/help/{*.html,.htaccess} $RPM_BUILD_ROOT%{_tutosdir}/php/watchlist/help
install php/watchlist/templates/{*.proto.*,.htaccess} $RPM_BUILD_ROOT%{_tutosdir}/php/watchlist/templates
install php/xml/*.{php,pinc,p3}		$RPM_BUILD_ROOT%{_tutosdir}/php/xml

install php/config_default.pinc		$RPM_BUILD_ROOT%{_tutosdir}/php/config.php

install html/{*.{html,proto.*,png,gif,css,ico},.htaccess} $RPM_BUILD_ROOT%{_tutosdir}/html
install html/help/{*.html,.htaccess}	$RPM_BUILD_ROOT%{_tutosdir}/html/help
install html/blue/*.{gif,png}		$RPM_BUILD_ROOT%{_tutosdir}/html/blue
install html/nuke/*.{gif,png}		$RPM_BUILD_ROOT%{_tutosdir}/html/nuke
install html/red/*.{gif,png}		$RPM_BUILD_ROOT%{_tutosdir}/html/red

install homepage/{*.html,.htaccess}	$RPM_BUILD_ROOT%{_tutosdir}/homepage

install libs/excel/*.php		$RPM_BUILD_ROOT%{_tutosdir}/libs/excel
install libs/fpdf/fpdf.php		$RPM_BUILD_ROOT%{_tutosdir}/libs/fpdf
install libs/fpdf/font/*.php		$RPM_BUILD_ROOT%{_tutosdir}/libs/fpdf/font
install libs/fpdf/tutorial/logo.png	$RPM_BUILD_ROOT%{_tutosdir}/libs/fpdf/tutorial

install *.sh $RPM_BUILD_ROOT%{_tutosdir}

install apache.conf $RPM_BUILD_ROOT/etc/httpd/tutos.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /etc/httpd/httpd.conf ] && ! grep -q "^Include.*%{name}.conf" /etc/httpd/httpd.conf; then
        echo "Include /etc/httpd/%{name}.conf" >> /etc/httpd/httpd.conf
        if [ -f /var/lock/subsys/httpd ]; then
                /usr/sbin/apachectl restart 1>&2
        fi
elif [ -d /etc/httpd/httpd.conf ]; then
        ln -sf /etc/httpd/%{name}.conf /etc/httpd/httpd.conf/99_%{name}.conf
	if [ -f /var/lock/subsys/httpd ]; then
	        /usr/sbin/apachectl restart 1>&2
		echo "Do not forget tu setup tutos' database!"
	fi
fi

%preun
if [ "$1" = "0" ]; then
        umask 027
        if [ -d /etc/httpd/httpd.conf ]; then
            rm -f /etc/httpd/httpd.conf/99_%{name}.conf
        else
                grep -v "^Include.*%{name}.conf" /etc/httpd/httpd.conf > \
                        /etc/httpd/httpd.conf.tmp
                mv -f /etc/httpd/httpd.conf.tmp /etc/httpd/httpd.conf
        fi
        if [ -f /var/lock/subsys/httpd ]; then
            /usr/sbin/apachectl restart 1>&2
        fi
fi

%files
%defattr(644,root,root,755)
%doc ChangeLog README README.ldap README.nuke ToDo
%config(noreplace) %verify(not size mtime md5) /etc/httpd/tutos.conf
%dir %{_tutosdir}
%attr(755,root,root) %{_tutosdir}/*.sh
%attr(775,root,http) %{_tutosdir}/repository
%{_tutosdir}/html
%{_tutosdir}/homepage
%{_tutosdir}/libs
%dir %{_tutosdir}/php
%{_tutosdir}/php/.htaccess
%{_tutosdir}/php/[!c]*
%{_tutosdir}/php/c[!o]*
%{_tutosdir}/php/co[!n]*
%{_tutosdir}/php/config_default.pinc
%attr(640,root,http) %config(noreplace) %verify(not size mtime md5) %{_tutosdir}/php/config.php
