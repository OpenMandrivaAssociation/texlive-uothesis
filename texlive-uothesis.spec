# revision 25355
# category Package
# catalog-ctan /macros/latex/contrib/uothesis
# catalog-date 2012-02-09 17:36:54 +0100
# catalog-license lppl1.3
# catalog-version 2.5.6
Name:		texlive-uothesis
Version:	2.5.6
Release:	4
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Feb 23 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.5.6-1
+ Revision: 779704
- Update to latest release.

* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.5.5-2
+ Revision: 757322
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.5.5-1
+ Revision: 719855
- texlive-uothesis
- texlive-uothesis
- texlive-uothesis

