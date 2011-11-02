Name:		texlive-mailing
Version:	20061228
Release:	1
Summary:	Macros for mail merging
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mailing
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mailing.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mailing.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mailing.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package is for use when sending a large number of letters,
all with the same body text. The package's \addressfile command
is used to specify who the letter's to be sent to; the body of
the \mailingtext command specifies the text of the letters,
possibly using macros defined in the \addressfile.

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
