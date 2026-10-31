from pathlib import Path
r=Path(__file__).resolve().parents[1]/'.ferramentas/apt'
for d in ['etc/apt.conf.d','etc/sources.list.d','etc/preferences.d','state/lists/partial','cache/archives/partial','log']:(r/d).mkdir(parents=True,exist_ok=True)
(r/'etc/sources.list').write_text('deb [signed-by=/usr/share/keyrings/debian-archive-keyring.gpg] https://deb.debian.org/debian trixie main\n')
settings={'Dir::Etc':str(r/'etc'),'Dir::Etc::parts':str(r/'etc/apt.conf.d'),'Dir::Etc::main':str(r/'etc/empty.conf'),'Dir::Etc::sourcelist':str(r/'etc/sources.list'),'Dir::Etc::sourceparts':str(r/'etc/sources.list.d','etc/preferences.d'),'Dir::State':str(r/'state'),'Dir::State::lists':str(r/'state/lists'),'Dir::State::status':'/var/lib/dpkg/status','Dir::Cache':str(r/'cache'),'Dir::Cache::archives':str(r/'cache/archives'),'Dir::Log':str(r/'log'),'APT::Sandbox::User':'agent','Debug::NoLocking':'true'}
(r/'apt.conf').write_text(''.join(k+' "'+v+'";\n' for k,v in settings.items()))
print(r/'apt.conf')
