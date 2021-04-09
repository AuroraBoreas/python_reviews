VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "Comparer"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = False
Attribute VB_Exposed = False
Option Explicit

Public Enum CompareMethod
    Circumference = 0
    Area = 1
    Reference = 2
End Enum

Public Function Compare(obj1 As IShape, _
                                        obj2 As IShape, _
                                        Optional method As CompareMethod = 0)

    Select Case method
        Case Circumference: Compare = IIf(obj1.Circumference() >= obj2.Circumference(), True, False)
        Case Area: Compare = IIf(obj1.Area() = obj2.Area(), True, False)
        Case Reference: Compare = IIf(obj1 Is obj2, True, False)
    End Select

End Function
