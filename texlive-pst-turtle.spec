Name:		texlive-pst-turtle
Version:	52261
Release:	1
Summary:	Commands for "turtle operations"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pst-turtle
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-turtle.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-turtle.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a PSTricks related package for creating "Turtle"
graphics. It supports the commands forward, back, left, right,
penup, and pendown.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/pst-turtle
%{_texmfdistdir}/tex/generic/pst-turtle
%{_texmfdistdir}/dvips/pst-turtle
%doc %{_texmfdistdir}/doc/generic/pst-turtle

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
