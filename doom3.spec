Name:           doom3
Version:        1.3.1.1304
Release:        7
Summary:        Doom 3
License:        Proprietary
URL:            http://www.idsoftware.com/
BuildArch:      noarch

Source0:	    %{name}.tar.gz
# Doom 3: Retail game data
Source1:        %{name}-pak000.pk4
Source2:        %{name}-pak001.pk4
Source3:        %{name}-pak002.pk4
Source4:        %{name}-pak003.pk4
Source5:        %{name}-pak004.pk4
Source6:        %{name}-docs.tar.gz
# Doom 3 RoE: Retail game data
Source7:        %{name}-roe-pak000.pk4
Source8:        %{name}-roe-docs.tar.gz
# Patch files
Source9:        %{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  tar
Requires:       doom3-engine >= %{version}

%description
Science has unlocked the gates to the unknown, and now only one man stands
between Hell and Earth. A sci-fi horror masterpiece, DOOM 3 is like nothing you
have experienced. Dramatic storyline, pulse-pounding action, incredible
graphics, and revolutionary technology combine to draw you into the most
frightening and gripping first person gaming experience ever created.

The ruins of an ancient martian civilization have unlocked the secrets to
teleportation, and the UAC will stop at nothing to harness this world-altering
technology. As part of a marine detachment sent to protect the facility, your
duty seemed simple enough... until the invasion. Now, in an epic clash against
pure evil you must fight to understand who is with you, who is against you, and
what must be done to stop this nightmare from reaching earth.

%package roe
Summary:        Doom 3: Resurrection of Evil
Requires:       doom3-engine >= %{version}
Requires:       doom3 = %{version}-%{release}

%description roe
The gripping expansion pack for DOOM 3 takes you even further into the the
DOOM universe. Two years following the unexplained disaster on Mars, the UAC
returns to the abandoned facility to investigate a mysterious beacon buried
deep in the ruins of the ancient civilization.

* Battle six new demons including the hunters
* Fight in all new 8-player capture the flag arenas
* Wield new weapons including the double barreled shotgun
* Possess demonic powers to use against the enemy
* Control time to defeat the enemy and evade deadly traps
* Harness the force of gravity to control your environment
* Battle through the ancient ruins and into the horrifying depths of hell

%prep
%setup -q -c -n doom3 -a 6 -a 8 -a 9

%install
cp -fr usr %{buildroot}

# Doom 3
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
install -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/%{name}/base/pak000.pk4
install -p -m 644 %{SOURCE2} %{buildroot}%{_datadir}/%{name}/base/pak001.pk4
install -p -m 644 %{SOURCE3} %{buildroot}%{_datadir}/%{name}/base/pak002.pk4
install -p -m 644 %{SOURCE4} %{buildroot}%{_datadir}/%{name}/base/pak003.pk4
install -p -m 644 %{SOURCE5} %{buildroot}%{_datadir}/%{name}/base/pak004.pk4
install -p -m 644 base/*pk4 %{buildroot}%{_datadir}/%{name}/base

# Resurrection of Evil
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-roe.desktop
install -p -m 644 %{SOURCE7} %{buildroot}%{_datadir}/%{name}/d3xp/pak000.pk4
install -p -m 644 d3xp/*pk4 %{buildroot}%{_datadir}/%{name}/d3xp

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache -f %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache -f %{_datadir}/icons/hicolor &>/dev/null || :

%files
%{!?_licensedir:%global license %%doc}
%license License.txt
%doc help.htm htm images manual.htm
%doc MSR.txt readme.txt README
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/base
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*

%files roe
%{!?_licensedir:%global license %%doc}
%license License.txt
%doc deu enu esp fra ita README
%{_bindir}/%{name}-roe
%{_datadir}/%{name}/d3xp
%{_datadir}/applications/%{name}-roe.desktop

%changelog
* Thu Jul 02 2020 Simone Caronni <negativo17@gmail.com> - 1.3.1.1304-7
- Remove dist and NoSource tags.

* Sat Jan 23 2016 Simone Caronni <negativo17@gmail.com> - 1.3.1.1304-6
- Add license macro.

* Fri Nov 15 2013 Simone Caronni <negativo17@gmail.com> - 1.3.1.1304-5
- Removed obsolete tags.

* Sun Aug 05 2012 Simone Caronni <negativo17@gmail.com> - 1.3.1.1304-4
- Avoid useless unpacking in prep section, install unpacked pk4 directly.

* Tue Jul 17 2012 Simone Caronni <negativo17@gmail.com> - 1.3.1.1304-3
- First build.
