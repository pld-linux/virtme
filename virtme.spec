Summary:	An easy way to virtualize the running system
Summary(pl.UTF-8):	Łatwy sposób wirtualizacji działającego systemu
Name:		virtme
Version:	0.1.1
Release:	5
License:	GPL v2
Group:		Applications/System
Source0:	https://www.kernel.org/pub/linux/utils/kernel/virtme/releases/%{name}-%{version}.tar.xz
# Source0-md5:	4714904bafee4b46428724de47027794
URL:		https://github.com/amluto/virtme
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	python3 >= 1:3.3
Requires:	qemu >= 1.6
BuildArch:	noarch
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
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

# omitted by install
install virtme-mkinitramfs $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc DCO-1.1.txt README.md
%attr(755,root,root) %{_bindir}/virtme-configkernel
%attr(755,root,root) %{_bindir}/virtme-mkinitramfs
%attr(755,root,root) %{_bindir}/virtme-prep-kdir-mods
%attr(755,root,root) %{_bindir}/virtme-run
%{py3_sitescriptdir}/virtme
%{py3_sitescriptdir}/virtme-%{version}-py*.egg-info
