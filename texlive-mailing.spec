# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/mailing
# catalog-date 2006-12-28 00:57:12 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-mailing
Version:	20061228
Release:	6
Summary:	Macros for mail merging
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mailing
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mailing.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mailing.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mailing.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is for use when sending a large number of letters,
all with the same body text. The package's \addressfile command
is used to specify who the letter's to be sent to; the body of
the \mailingtext command specifies the text of the letters,
possibly using macros defined in the \addressfile.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/mailing/mailing.sty
%doc %{_texmfdistdir}/doc/latex/mailing/mailing.pdf
%doc %{_texmfdistdir}/doc/latex/mailing/manifest.txt
#- source
%doc %{_texmfdistdir}/source/latex/mailing/mailing.dtx
%doc %{_texmfdistdir}/source/latex/mailing/mailing.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20061228-2
+ Revision: 753678
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20061228-1
+ Revision: 718940
- texlive-mailing
- texlive-mailing
- texlive-mailing
- texlive-mailing

