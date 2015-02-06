%global packname  rgl
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.93.996
Release:          2
Summary:          3D visualization device system (OpenGL)
Group:            Sciences/Mathematics
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/rgl_0.93.996.tar.gz
Requires:         R-stats R-grDevices 
Requires:         R-MASS 
BuildRequires:    R-devel Rmath-devel texlive-latex R-stats R-grDevices
BuildRequires:    R-MASS 
BuildRequires:    png-devel
BuildRequires:    pkgconfig(gl)
BuildRequires:    pkgconfig(glu)
%rename R-cran-rgl

%description
3D visualization device (OpenGL)

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/demodata
%{rlibdir}/%{packname}/fonts
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/textures
%{rlibdir}/%{packname}/WebGL


