Option Explicit

Public Enum CompareMethod
    name = 0
    age = 1
    reference = 2
End Enum

Public Function Compare(ByRef obj1 As IPerson, _
                        ByRef obj2 As IPerson, _
                        Optional method As CompareMethod = 0) As Boolean

    Select Case method
    Case name:
        Compare = IIf(obj1.name = obj2.name, True, False)
    Case age:
        Compare = IIf(obj1.age = obj2.age, True, False)
    Case reference:
        Compare = IIf(obj1 Is obj2, True, False)

    End Select
End Function
