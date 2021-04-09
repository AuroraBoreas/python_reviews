Attribute VB_Name = "Module_UT"
Option Explicit

Public Sub UT()
    Dim p1 As New clsEmployee
    p1.Init "ZZ", 34, "male", 1.618
    
    Debug.Print p1.ToString()
    
    Dim p2 As New clsManager
    p2.Init "ZL", 35, "male", 3.141
    
    Dim coll As New Collection
    coll.Add p1
    coll.Add p2
    
    Dim p As IPerson
    For Each p In coll
        Debug.Print vbNewLine, TypeName(p), p.ToString()
    Next p
    
    Dim cmp As New clsComparer
    Debug.Print vbNewLine, cmp.Compare(p1, p2, CompareMethod.reference)
    
    Set p1 = Nothing
    Set p2 = Nothing
    Set cmp = Nothing
    
End Sub
