#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libevent
Version  : 2.1.8.stable
Release  : 23
URL      : https://github.com/libevent/libevent/releases/download/release-2.1.8-stable/libevent-2.1.8-stable.tar.gz
Source0  : https://github.com/libevent/libevent/releases/download/release-2.1.8-stable/libevent-2.1.8-stable.tar.gz
Summary  : libevent is an asynchronous notification event loop library
Group    : Development/Tools
License  : MIT BSD-3-Clause
Requires: libevent-bin
Requires: libevent-lib
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : openssl-dev
BuildRequires : openssl-dev32
BuildRequires : openssl-lib32
BuildRequires : sed
BuildRequires : zlib-dev32

%description
No detailed description available

%package bin
Summary: bin components for the libevent package.
Group: Binaries

%description bin
bin components for the libevent package.


%package dev
Summary: dev components for the libevent package.
Group: Development
Requires: libevent-lib
Requires: libevent-bin
Provides: libevent-devel

%description dev
dev components for the libevent package.


%package dev32
Summary: dev32 components for the libevent package.
Group: Default
Requires: libevent-lib32
Requires: libevent-bin
Requires: libevent-dev

%description dev32
dev32 components for the libevent package.


%package lib
Summary: lib components for the libevent package.
Group: Libraries

%description lib
lib components for the libevent package.


%package lib32
Summary: lib32 components for the libevent package.
Group: Default

%description lib32
lib32 components for the libevent package.


%prep
%setup -q -n libevent-2.1.8-stable
pushd ..
cp -a libevent-2.1.8-stable build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1522779117
export CFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs "
export FCFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs "
export FFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong -mzero-caller-saved-regs "
%configure --disable-static --disable-libevent-regress
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static --disable-libevent-regress   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1522779117
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/event_rpcgen.py

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/include/event2/buffer.h
/usr/include/event2/buffer_compat.h
/usr/include/event2/bufferevent.h
/usr/include/event2/bufferevent_compat.h
/usr/include/event2/bufferevent_ssl.h
/usr/include/event2/bufferevent_struct.h
/usr/include/event2/dns.h
/usr/include/event2/dns_compat.h
/usr/include/event2/dns_struct.h
/usr/include/event2/event-config.h
/usr/include/event2/event.h
/usr/include/event2/event_compat.h
/usr/include/event2/event_struct.h
/usr/include/event2/http.h
/usr/include/event2/http_compat.h
/usr/include/event2/http_struct.h
/usr/include/event2/keyvalq_struct.h
/usr/include/event2/listener.h
/usr/include/event2/rpc.h
/usr/include/event2/rpc_compat.h
/usr/include/event2/rpc_struct.h
/usr/include/event2/tag.h
/usr/include/event2/tag_compat.h
/usr/include/event2/thread.h
/usr/include/event2/util.h
/usr/include/event2/visibility.h
/usr/lib64/libevent.so
/usr/lib64/libevent_core.so
/usr/lib64/libevent_extra.so
/usr/lib64/libevent_openssl.so
/usr/lib64/libevent_pthreads.so
/usr/lib64/pkgconfig/libevent.pc
/usr/lib64/pkgconfig/libevent_core.pc
/usr/lib64/pkgconfig/libevent_extra.pc
/usr/lib64/pkgconfig/libevent_openssl.pc
/usr/lib64/pkgconfig/libevent_pthreads.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libevent.so
/usr/lib32/libevent_core.so
/usr/lib32/libevent_extra.so
/usr/lib32/libevent_openssl.so
/usr/lib32/libevent_pthreads.so
/usr/lib32/pkgconfig/32libevent.pc
/usr/lib32/pkgconfig/32libevent_core.pc
/usr/lib32/pkgconfig/32libevent_extra.pc
/usr/lib32/pkgconfig/32libevent_openssl.pc
/usr/lib32/pkgconfig/32libevent_pthreads.pc
/usr/lib32/pkgconfig/libevent.pc
/usr/lib32/pkgconfig/libevent_core.pc
/usr/lib32/pkgconfig/libevent_extra.pc
/usr/lib32/pkgconfig/libevent_openssl.pc
/usr/lib32/pkgconfig/libevent_pthreads.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libevent-2.1.so.6
/usr/lib64/libevent-2.1.so.6.0.2
/usr/lib64/libevent_core-2.1.so.6
/usr/lib64/libevent_core-2.1.so.6.0.2
/usr/lib64/libevent_extra-2.1.so.6
/usr/lib64/libevent_extra-2.1.so.6.0.2
/usr/lib64/libevent_openssl-2.1.so.6
/usr/lib64/libevent_openssl-2.1.so.6.0.2
/usr/lib64/libevent_pthreads-2.1.so.6
/usr/lib64/libevent_pthreads-2.1.so.6.0.2

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libevent-2.1.so.6
/usr/lib32/libevent-2.1.so.6.0.2
/usr/lib32/libevent_core-2.1.so.6
/usr/lib32/libevent_core-2.1.so.6.0.2
/usr/lib32/libevent_extra-2.1.so.6
/usr/lib32/libevent_extra-2.1.so.6.0.2
/usr/lib32/libevent_openssl-2.1.so.6
/usr/lib32/libevent_openssl-2.1.so.6.0.2
/usr/lib32/libevent_pthreads-2.1.so.6
/usr/lib32/libevent_pthreads-2.1.so.6.0.2
