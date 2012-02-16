%define modulename rgl
%define version 0.87
%define r_library %{_libdir}/R/library
%define _requires_exceptions libR.so

Summary:	3D visualization device system (OpenGL) for R
Name:		R-cran-%{modulename}
Version:	%{version}
Release:	%mkrel 1
License:	GPLv2
Group:		Sciences/Mathematics
Url:		http://cran.r-project.org/web/packages/%{modulename}/index.html
Source0:	http://cran.r-project.org/src/contrib/%{modulename}_%{version}.tar.gz
BuildRequires:	R-base
BuildRequires:	mesaglu-devel
BuildRequires:	png-devel
BuildRequires:	zlib-devel
BuildRequires:	freetype2-devel
Requires:	R-base
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The package contains 3D visualization device system (OpenGL) for R.

%prep
%setup -q -c

%build

R CMD build %{modulename}

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{r_library}

# install
R CMD INSTALL %{modulename} --library=%{buildroot}/%{r_library}

# provided by R-base
rm -rf %{buildroot}/%{r_library}/R.css

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{r_library}/%{modulename}
