@"

[object adapters]
----
* .NET objects
* Active Directory data
* Windows Management Instrumentation classes and objects

+ why?
A mechanism will make those look and work just like .NET objects do.
PS calls that mechanism "object adaptation";

+ how?
when a "foreign object" comes along, the shell wraps it in a native .NET object
that serves as a view of the original object;

the view object is of the "PSObject" type object and
uses the adapter to get properties and methods;

+ note
most of the time, a "PSObject" behaves just like the original object,
and the user can hardly tell difference..

if we need the "original object", 
we can always get it using the special "PSBase" properties.

----

"@

# example-01: access properties w/o "object adapter" using WMI;
$wmi_caption = (Get-WmiObject win32_process)[0].PSBase.Properties['Caption'].Value;
$wmi_caption;
# example-02: access props with "object adapter";
(Get-WmiObject win32_process)[0].Caption;

# DirectoryEntryAdapter
# this adaptor works with the windows active directory in a similar way to the "ManagementObjectAdapter";

$user = [ADSI]"WinNT://./ZhangLiang,user";
# access prop w/o PSObject
$user.PSBase.Properties["Name"];
# access prop with PSObject
$user.Name;

# DataRowAdapter
$ds = New-Object Data.DataSet;
$ds.ReadXml("src\c01_object_and_object_types\data.xml");
# access with "object adapter"
$ds.Tables[0].Rows[0].Name;
# access w/o "object adapter"
$ds.Tables[0].Rows[0].PSBase["Name"];

# DataRowViewAdapter
# this guy works in the same way as "DataRowAdapter"
# the only difference is that it adapts ADO.NET DataRowView Objects;

# XmlNodeAdapter
$xmlDoc = New-Object xml.xmldocument;
$xmlDoc.Load("src\c01_object_and_object_types\data.xml");
$xmlDoc.Users.User[0];

# comAdapter
$ie = New-Object -COM InternetExplorer.Application;
$ie.Visible = $true;