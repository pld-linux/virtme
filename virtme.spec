Summary:	An easy way to virtualize the running system
Summary(pl.UTF-8):	Łatwy sposób wirtualizacji działającego systemu
Name:		virtme
Version:	0.0.2
Release:	2
License:	GPL v2
Group:		Applications/System
Source0:	https://www.kernel.org/pub/linux/utils/kernel/virtme/releases/%{name}-%{version}.tar
# Source0-md5:	a64ac6427408b576af8c5f1997e4b9c2
URL:		https://github.com/amluto/virtme
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	python3 >= 1:3.3
Requires:	qemu >= 1.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Virtme is a set of simple tools to run a virtualized Linux kernel that
uses the host Linux distribution or a simple rootfs instead of a whole
disk image.

%description -l pl.UTF-8
Virtme to zestaw prostych narzędzi do uruchamiania wirtualizowanego
jądra Linuksa z wykorzystaniem dystrybucji Linuksa hosta lub prostego
rootfs-a zamiast całego obrazu dysku.

%prep
%setup -q

%build
%{__python3} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python3} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

# omitted by install
install virtme-mkinitramfs $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc DCO-1.1.txt README.md
%attr(755,root,root) %{_bindir}/virtme-configkernel
%attr(755,root,root) %{_bindir}/virtme-mkinitramfs
%attr(755,root,root) %{_bindir}/virtme-run
%dir %{_datadir}/virtme-guest-0
%attr(755,root,root) %{_datadir}/virtme-guest-0/virtme-init
%attr(755,root,root) %{_datadir}/virtme-guest-0/virtme-loadmods
%attr(755,root,root) %{_datadir}/virtme-guest-0/virtme-udhcpc-script
%{py3_sitescriptdir}/virtme
%{py3_sitescriptdir}/virtme-0.0.1-py*.egg-info
