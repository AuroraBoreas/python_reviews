VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "clsComparer"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = False
Attribute VB_Exposed = False
Option Explicit

Public Enum CompareMethod
    Name = 0
    Age = 1
    reference = 2
End Enum

Public Function Compare(obj1 As IPerson, _
                                        obj2 As IPerson, _
                                        Optional method As CompareMethod = 0) As Boolean
    
    Select Case method
        Case Name: Compare = IIf(obj1.Name = obj2.Name, True, False)
        Case Age: Compare = IIf(obj1.Age = obj2.Age, True, False)
        Case reference: Compare = IIf(obj1 Is obj2, True, False)
    End Select
    
End Function
