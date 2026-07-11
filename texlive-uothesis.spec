%global tl_name uothesis
%global tl_revision 25355

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.5.6
Release:	%{tl_revision}.1
Summary:	Class for dissertations and theses at the University of Oregon
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/uothesis
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uothesis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uothesis.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uothesis.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The class generates documents that are suitable for submission to the
Graduate School and conform with the style requirements for
dissertations and theses as laid out in the Fall 2010 UO graduate school
student manual.

