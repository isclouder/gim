%global __os_install_post %{nil}

Name: gim
Version: %{client_version}
Release: 1
Summary: gim module

Group: GUL
License: gim
URL: http:// 
Source: %{name}-%{version}.tar.gz
Autoprov: no
Autoreq: no

%description
desktop

%prep
%setup -q

%post
depmod -a

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/lib/modules/4.11.0-45.6.1.el7a.x86_64/kernel/drivers/gpu/drm/amd/amdgpu/
cp -rf *.ko %{buildroot}/usr/lib/modules/4.11.0-45.6.1.el7a.x86_64/kernel/drivers/gpu/drm/amd/amdgpu/
mkdir -p %{buildroot}/etc/modprobe.d/
cp -rf gim.conf %{buildroot}/etc/modprobe.d/
mkdir -p %{buildroot}/etc/sysconfig/modules/
cp -rf gim.modules %{buildroot}/etc/sysconfig/modules/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/lib/modules/4.11.0-45.6.1.el7a.x86_64/kernel/drivers/gpu/drm/amd/amdgpu/*
/etc/modprobe.d/gim.conf
/etc/sysconfig/modules/gim.modules
