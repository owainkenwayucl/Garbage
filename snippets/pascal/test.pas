Program test;

uses 
	classes, sysutils, IniFiles;

const 
	SECTION = 'testing';

var
	INI: TINIFILE;
	Locomotive, Location: String;

begin

	INI := TINIFile.Create('test.ini');
	Locomotive := INI.ReadString(SECTION,'Locomotive','');
	Location := INI.ReadString(SECTION,'Location','');

	writeln('Locomotive:  ',Locomotive);
	writeln('Location:    ',Location);
	INI.Free;
end.
