%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppetlabs-tomcat
%global commit 67c3ad8d34ecd3187f763cd17d5166ab0c2e04ca
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-tomcat
Version:        6.1.0
Release:        1%{?alphatag}%{?dist}
Summary:        Installs, deploys, and configures Apache Tomcat web services.
License:        ASL 2.0

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
* Tue Sep 28 2021 RDO <dev@lists.rdoproject.org> 6.1.0-1.67c3ad8git
- Update to post 6.1.0 (67c3ad8d34ecd3187f763cd17d5166ab0c2e04ca)



