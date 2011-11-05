# revision 23485
# category Package
# catalog-ctan /macros/latex/contrib/uothesis
# catalog-date 2011-07-20 11:02:46 +0200
# catalog-license lppl1.3
# catalog-version 2.5.5
Name:		texlive-uothesis
Version:	2.5.5
Release:	1
Summary:	Class for dissertations and theses at the University of Oregon
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/uothesis
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uothesis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uothesis.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uothesis.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The class generates documents that are suitable for submission
to the Graduate School and conform with the style requirements
for dissertations and theses as laid out in the Fall 2010 UO
graduate school student manual.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
