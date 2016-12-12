#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libevent
Version  : 2.0.22
Release  : 16
URL      : http://downloads.sourceforge.net/levent/libevent-2.0.22-stable.tar.gz
Source0  : http://downloads.sourceforge.net/levent/libevent-2.0.22-stable.tar.gz
Summary  : libevent_pthreads adds pthreads-based threading support to libevent
Group    : Development/Tools
License  : BSD-3-Clause
Requires: libevent-bin
Requires: libevent-lib
BuildRequires : openssl-dev
BuildRequires : sed

%description
0. BUILDING AND INSTALLATION (Briefly)
$ ./configure
$ make
$ make verify   # (optional)
$ sudo make install

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


%package lib
Summary: lib components for the libevent package.
Group: Libraries

%description lib
lib components for the libevent package.


%prep
%setup -q -n libevent-2.0.22-stable

%build
export LANG=C
%configure --disable-static --disable-libevent-regress
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
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
/usr/lib64/libevent.so
/usr/lib64/libevent_core.so
/usr/lib64/libevent_extra.so
/usr/lib64/libevent_openssl.so
/usr/lib64/libevent_pthreads.so
/usr/lib64/pkgconfig/libevent.pc
/usr/lib64/pkgconfig/libevent_openssl.pc
/usr/lib64/pkgconfig/libevent_pthreads.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libevent-2.0.so.5
/usr/lib64/libevent-2.0.so.5.1.9
/usr/lib64/libevent_core-2.0.so.5
/usr/lib64/libevent_core-2.0.so.5.1.9
/usr/lib64/libevent_extra-2.0.so.5
/usr/lib64/libevent_extra-2.0.so.5.1.9
/usr/lib64/libevent_openssl-2.0.so.5
/usr/lib64/libevent_openssl-2.0.so.5.1.9
/usr/lib64/libevent_pthreads-2.0.so.5
/usr/lib64/libevent_pthreads-2.0.so.5.1.9
