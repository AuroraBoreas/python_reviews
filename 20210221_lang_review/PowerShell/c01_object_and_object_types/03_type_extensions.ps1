@"

[type extensions]
----
* why
    since there is no way for a user to create his or her own "adapter" 
    or extend an existing one, 
    we have another mechanism of modifying "object types":
    "type extensions"

* how
    the type system allows users to provide additional code and data
    and add data members, both properties and methods, 
    to objects and object types at runtime;

----

"@

$aliasProps1 = (Get-Process)[0] | Get-Member -type AliasProperty;
$aliasProps1;

$res = (Get-Process)[0].PSExtended | Get-Member;
$res;

$pm = (Get-Process)[0] | get-member -type PropertySet, MemberSet;
$pm;