Name:		texlive-unigrazpub
Version:	64797
Release:	1
Summary:	LaTeX templates for University of Graz Library Publishing Services
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/unigrazpub
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unigrazpub.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unigrazpub.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unigrazpub.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a LaTeX class matching the preparation
guidelines of the Library Publishing Services of University of
Graz. The bundle also includes a comprehensive set of example
files for books and collections.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/unigrazpub
%{_texmfdistdir}/tex/latex/unigrazpub
%doc %{_texmfdistdir}/doc/latex/unigrazpub

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
