%global tl_name mailing
%global tl_revision 77241

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0d
Release:	%{tl_revision}.1
Summary:	Macros for mail merging
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mailing
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mailing.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mailing.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mailing.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package is for use when sending a large number of letters, all with
the same body text. The package's \addressfile command is used to
specify who the letter is to be sent to; the body of the \mailingtext
command specifies the text of the letters, possibly using macros defined
in the \addressfile.

