%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppetlabs-tomcat
%global commit 8d96971ca1c58219f856ba8c5cc1af1de95c27a6
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-tomcat
Version:        1.6.0
Release:        2%{?alphatag}%{?dist}
Summary:        Installs, deploys, and configures Apache Tomcat web services.
License:        Apache 2.0

URL:            https://github.com/puppetlabs/puppetlabs-tomcat

Source0:        https://github.com/puppetlabs/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet-stdlib
Requires:       puppet-concat
Requires:       puppet-staging
Requires:       puppet >= 2.7.0

%description
Installs, deploys, and configures Apache Tomcat web services.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/tomcat/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/tomcat/



%files
%{_datadir}/openstack-puppet/modules/tomcat/


%changelog
* Tue Nov 15 2016 Alfredo Moralejo <amoralej@redhat.com> 1.6.0-2.8d96971.git
- Newton update 1.6.0 (8d96971ca1c58219f856ba8c5cc1af1de95c27a6)

* Wed Oct 26 2016 Jon Schlueter <jschluet@redhat.com> 1.6.0-1
- Update to 1.6.0

* Thu Sep 22 2016 Haikel Guemar <hguemar@fedoraproject.org> - 1.5.0-1.c8c6613.git
- Newton update 1.5.0 (c8c66135f7140b91a2bb4e59672a067678cfa782)


