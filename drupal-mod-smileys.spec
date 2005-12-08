%define		modname smileys
Summary:	Drupal Smileys Module
Summary(pl):	Modu³ Smileys dla Drupala
Name:		drupal-mod-%{modname}
Version:	4.6.0
Release:	0.4
License:	GPL v2
Group:		Applications/WWW
Source0:	http://drupal.org/files/projects/%{modname}-%{version}.tar.gz
# Source0-md5:	d6381efeb83f702138c3e125b1d04b84
URL:		http://drupal.org/project/smileys
BuildRequires:	rpmbuild(macros) >= 1.194
Requires:	drupal >= 4.6.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_drupaldir	%{_datadir}/drupal
%define		_moddir		%{_drupaldir}/modules
%define		_htdocs		%{_drupaldir}/htdocs
%define		_podir		%{_drupaldir}/po/%{modname}
%define		_smileysdir	%{_htdocs}/misc/smileys

%description
This is a simple smiley-filter that allows the easy use of graphical
smileys (or 'emoticons') on a Drupal site. It comes with a set of
example smileys, but you can define an unlimited amount of custom
smileys as well.

%description -l pl
To jest prosty filtr u¶mieszków pozwalaj±cy na ³atwe u¿ywanie
graficznych u¶mieszków ("emotikonów") na serwisie Drupala. Jest
dostarczany z zestawem przyk³adowych u¶mieszków, ale mo¿na tak¿e
zdefiniowaæ nieograniczon± liczbê w³asnych.

%package examples
Summary:	Example Smileys for Smileys Module
Summary(pl):	Przyk³adowe u¶mieszki dla modu³u Smileys
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}

%description examples
Example Smileys for Smileys Module.

A word from Author:
Please don't rip the example smileys and use them without this
module. I spent quite some time creating those little buggers.

%description examples -l pl
Przyk³adowe u¶mieszki dla modu³u Smileys.

S³owo od autora:
Proszê nie wyci±gaæ przyk³adowych u¶mieszków i nie u¿ywaæ ich bez tego
modu³u. Spêdzi³em trochê czasu na ich tworzeniu.

%prep
%setup -q -n %{modname}
rm -f LICENSE.txt # GPL v2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_moddir},%{_podir},%{_smileysdir}}

install *.module $RPM_BUILD_ROOT%{_moddir}
install examples/*.{gif,png} $RPM_BUILD_ROOT%{_smileysdir}
cp -a po/*.po $RPM_BUILD_ROOT%{_podir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ "$1" = 1 ]; then
%banner -e %{name} <<EOF
To create Smileys MySQL database tables, import:
zcat %{_docdir}/%{name}-%{version}/%{modname}.mysql.gz | mysql drupal
For Postgresql file is:
%{_docdir}/%{name}-%{version}/%{modname}.pgsql.gz

If you want to use localization, then you need to upload .po files
from %{_podir} via drupal locatization admin.

The example smileys are available from %{name}-examples package.
EOF
fi

%post examples
if [ "$1" = 1 ]; then
%banner -e %{name} <<EOF
To use smileys from this package you need to import definitions:
zcat %{_docdir}/%{name}-examples-%{version}/examples.mysql.gz | mysql drupal
For Postgresql the file is:
%{_docdir}/%{name}-examples-%{version}/examples.pgsql.gz
EOF
fi

%files
%defattr(644,root,root,755)
%doc *.txt po/*.pot
%doc *.txt
%doc %{modname}.{mysql,pgsql}
%{_moddir}/*.module
%{_podir}
%dir %{_smileysdir}

%files examples
%defattr(644,root,root,755)
%doc examples.{mysql,pgsql}
%doc examples/*.txt
%{_smileysdir}/*
