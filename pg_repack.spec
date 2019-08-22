Name:           pg_repack
Version:        1.4.4        
Release:        1%{?dist}
Summary:        Reorganize tables in PostgreSQL databases without any locks

License:        BSD
URL:            http://reorg.github.io/%{name}/
Source0:        https://github.com/reorg/%{name}/archive/ver_1.4.4.tar.gz

BuildRequires:  postgresql, gcc, openssl-devel, postgresql-server, postgresql-libs, postgresql-devel
BuildRequires:  readline-devel, zlib-devel, postgresql-static

%description
pg_repack can re-organize tables on a postgres
database without any locks so that
you can retrieve or update rows in tables
being reorganized.
The module is developed to be a better
alternative of CLUSTER and VACUUM FULL.

%prep
%setup -n %{name}-ver_%{version}


%build
make %{?_smp_mflags}


%install
%make_install


%files
%{_bindir}/%{name}
%{_libdir}/pgsql/%{name}.so
%{_datadir}/pgsql/extension/%{name}.control
%{_datadir}/pgsql/extension/%{name}--%{version}.sql



%changelog
* Wed Aug 21 2019 Filip Januš <fjanus@redhat.com> 1.4.4-1
- Initial packaging 
