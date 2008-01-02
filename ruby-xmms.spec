%define rbname xmms
%define version 0.1.2
%define release %mkrel 3

Summary: XMMS bindings for Ruby
Name: ruby-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: GPL
URL: http://www.pablotron.org/software/xmms-ruby/
Source0: http://www.pablotron.org/download/%{rbname}-ruby-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: ruby-devel >= 1.6
BuildRequires: xmms-devel >= 1.2.6

%description
XMMS bindings for Ruby. 

%prep
%setup -q -n %{rbname}-ruby-%{version}

%build
ruby extconf.rb
make

%install
[ "%{buildroot}" != "/" ] && %__rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc README COPYING ChangeLog doc
%{ruby_sitearchdir}/xmms.so

