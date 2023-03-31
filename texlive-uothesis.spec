Name:		texlive-uothesis
Version:	25355
Release:	2
Summary:	Class for dissertations and theses at the University of Oregon
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/uothesis
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uothesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uothesis.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uothesis.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class generates documents that are suitable for submission
to the Graduate School and conform with the style requirements
for dissertations and theses as laid out in the Fall 2010 UO
graduate school student manual.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/uothesis/uothesis.cls
%doc %{_texmfdistdir}/doc/latex/uothesis/README
%doc %{_texmfdistdir}/doc/latex/uothesis/README.txt
%doc %{_texmfdistdir}/doc/latex/uothesis/acs-uothesis.bib
%doc %{_texmfdistdir}/doc/latex/uothesis/uothesis.hd
%doc %{_texmfdistdir}/doc/latex/uothesis/uothesis.pdf
#- source
%doc %{_texmfdistdir}/source/latex/uothesis/uothesis.dtx
%doc %{_texmfdistdir}/source/latex/uothesis/uothesis.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
