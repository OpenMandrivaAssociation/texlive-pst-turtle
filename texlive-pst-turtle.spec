%global tl_name pst-turtle
%global tl_revision 52261

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.02
Release:	%{tl_revision}.1
Summary:	Commands for turtle operations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-turtle
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-turtle.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-turtle.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a PSTricks related package for creating "Turtle" graphics. It
supports the commands forward, back, left, right, penup, and pendown.

