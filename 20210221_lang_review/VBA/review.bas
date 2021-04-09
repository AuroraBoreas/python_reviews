Option Explicit

Public Enum Colors
    [_first] = 1
    red = 1
    blue
    green
    yellow
    purple
    [_last]
End Enum

public type EmployeeRecord
    ID as Integer
    Name as string * 20
    Address as String * 30
    Phone as long
    HireDate as Date
end type

Public Sub Main()
    ' variable
    Call VariableDemo
    ' function
    Call FunctionDemo
    ' statement
    Call StatementDemo
    ' control flow
    Call ControlflowDemo
    ' loop
    Call LoopDemo
    ' class
    Call ClassDemo
    ' interface
    call IterfaceImplementsDemo
    ' container
    Call ContainerDemo
    ' fileIO
    Call FileIODemo
    ' regexp
    call StringPatternMatch   '

End Sub

Private Sub VariableDemo()
    ' var
    ' data types
    ' type conversion
    ' reflection
    
    Dim a As Byte: a = 125
    Dim b As Integer: b = 69
    Dim c As Long: c = 1234567890
    Dim e As Double: e = 6.718
    Dim f As Date: f = #3/1/2021#
    Dim g: g = #5:05:24 PM#
    
    Debug.Print a
    Debug.Print b
    Debug.Print c
    Debug.Print e
    Debug.Print Format(f, "short date")
    Debug.Print Format(f, "long date")
    Debug.Print Format(g, "long time")
    Debug.Print Format(g, "short time")
    
    Debug.Print CInt(e)
    Debug.Print CDbl(b)

    Debug.Print VarType(b), TypeName(b)

End Sub

Private Sub FunctionDemo()
    ' funciton: a block of reusable code with or w/o return_value
    ' regular function:
    ' [x] overloading,
    ' [x] function inside function,
    ' [x] lambda,
    ' [x] immediate function,
    ' [x] function pointer

    ' [*] ref, val,
    ' [*] params,
    ' [*] return_type is array type
    Dim numbers As Variant: numbers = Array(1, 2, 3, 4, 5)
    Dim str As String: str = "hello world"
    Call ArgRefVal(numbers, str)
    Debug.Print numbers(1), str

    Call ArgParmas(1, 2, 3)

    Dim res As Variant: res = ReturnTypeIsArray()
    Debug.Print res(0)
End Sub

Private Sub ArgRefVal(ByRef a As Variant, ByVal b As String)
    Debug.Print a(1)
    a(1) = 42
    b = b & "!"
    Debug.Print b
End Sub

Private Sub ArgParmas(ParamArray args() As Variant)
    Dim tmp As Variant
    For Each tmp In args
        Debug.Print tmp
    Next tmp
End Sub

Private Function ReturnTypeIsArray() As Variant
    ReturnTypeIsArray = Array("hello", "world")
End Function

Private Sub StatementDemo()
    ' Arithmetic
    ' Relational
    ' Logical
    ' Access
    ' Bitwise
    ' Assign
    ' Cast
    ' Operator for storage
    ' Operator for other
    Dim x As Integer: x = 42
    Dim y As Integer: y = 69
    ' arithmetic
    Debug.Print "x = " & x & ", y = " & y & ", x + y = " & (x + y)
    Debug.Print "x = " & x & ", y = " & y & ", x - y = " & (x - y)
    Debug.Print "x = " & x & ", y = " & y & ", x * y = " & (x * y)
    Debug.Print "x = " & x & ", y = " & y & ", x / y = " & (x / y)
    Debug.Print "x = " & x & ", y = " & y & ", x mod y = " & (x Mod y)
    ' relational
    Debug.Print "x = " & x & ", y = " & y & ", x == y : " & (x = y)
    'Debug.Print "x = " & x & ", y = " & y & ", x != y : " & (x != y)
    Debug.Print "x = " & x & ", y = " & y & ", x < y : " & (x < y)
    Debug.Print "x = " & x & ", y = " & y & ", x <= y : " & (x <= y)
    Debug.Print "x = " & x & ", y = " & y & ", x > y : " & (x > y)
    Debug.Print "x = " & x & ", y = " & y & ", x >= y : " & (x >= y)
    ' logic
    Debug.Print "x = " & x & ", y = " & y & ", x=1 and y=1 : " & (x = 1 And y = 1)
    Debug.Print "x = " & x & ", y = " & y & ", x=1 or y=1 : " & (x = 1 Or y = 1)
    Debug.Print "x = " & x & ", y = " & y & ", not y=1 : " & (Not y = 1)
    ' access: .
    ' bitwise
    Debug.Print "x = " & x & ", y = " & y & ", x & y : " & (x And y)
    Debug.Print "x = " & x & ", y = " & y & ", x | y : " & (x Or y)
    Debug.Print "x = " & x & ", y = " & y & ", x ^ y : " & (x Xor y)
    Debug.Print "x = " & x & ", y = " & y & ", ~x : " & (Not x)
    ' cast: no
    ' op for storage: new
    ' op for other: .

End Sub

Private Sub ControlflowDemo()
    ' if...elseif...else
    ' select...case
    ' on error goto xxx

    Dim res As Integer: res = IfelseDemo(5)
    Debug.Print res

    Call SelectCaseDemo(Colors.green)

    Call ErrorHandlerDemo

End Sub

Private Function IfelseDemo(ByVal n As Integer) As Integer
    If n < 2 Then
        IfelseDemo = 1
    Else
        IfelseDemo = n * IfelseDemo(n - 1)
    End If
End Function

Private Sub SelectCaseDemo(ByVal c As Colors)
    Select Case c
        Case Is = 1: Debug.Print "red"
        Case Is = 2: Debug.Print "blue"
        Case Is = 3: Debug.Print "green"
        Case Is = 4: Debug.Print "yellow"
        Case Is = 5: Debug.Print "purple"
    End Select
End Sub

Private Sub ErrorHandlerDemo()
    Dim a As Integer: a = 42
    Dim b As Double: b = 0#

    On Error GoTo errmsg
    Debug.Print a / b
Exit Sub
errmsg:
    Debug.Print Err.Number, Err.Description
    Debug.Print "enter errgblock"
End Sub


Private Sub LoopDemo()
    ' for
    ' for each
    ' while
    ' do loop until
    ' do while...loop

    Dim col As New Collection
    col.Add "apple"
    col.Add "orange"
    col.Add "pearl"
    col.Add "watermelon"
    
    Debug.Print vbNewLine & "for loop"
    Dim i As Integer
    For i = 1 To col.Count
        Debug.Print col(i)
    Next i

    Debug.Print vbNewLine & "for each"
    Dim item As Variant
    For Each item In col
        Debug.Print item
    Next item

    Debug.Print vbNewLine & "while loop"
    i = col.Count
    While i > 0
        Debug.Print col(i)
        i = i - 1
    Wend

    Debug.Print vbNewLine & "do...loop until"
    i = 1
    Do
        Debug.Print col(i)
        i = i + 1
    Loop Until i > col.Count

    Debug.Print vbNewLine & "do while...loop"
    i = 1
    do while i < col.count + 1
        debug.print col(i)
        i = i + 1
        if i = 3 then exit do
    loop 

    Set col = Nothing

End Sub

Private Sub ContainerDemo()
    ' array
    ' arraylist
    ' collection
    ' dictionary
    ' stack
    ' queue

    dim numbers() as Integer

    redim preserve numbers(0 to 5)
    numbers(0) = 1
    numbers(1) = 2
    numbers(2) = 4
    numbers(3) = 8
    numbers(4) = 16
    numbers(5) = 32

    redim preserve numbers(0 to 10)
    numbers(6) = 64
    numbers(7) = 128

    dim var as Variant
    for each var in numbers
        debug.print var
    next var

    erase numbers

End Sub

Private Sub FileIODemo()

End Sub

Private Sub ClassDemo()
    Dim p As New clsManager
    p.init "ZL", "male", 34
    
    Debug.Print p.ToString()
    Set p = Nothing
End Sub

Private Sub IterfaceImplementsDemo()
    Dim p1 As New clsEmployee
    p1.init "ZL", "male", 35
    
    Dim p2 As New clsManager
    p2.init "SCY", "female", 35
    
    Dim col As New Collection
    col.Add p1
    col.Add p2
    
    Dim p As New IPerson
    For Each p In col
        Debug.Print TypeName(p), p.Name, p.Age
    Next p
    
    Dim cmp As New Comparer
    Debug.Print cmp.Compare(p1, p2, Name)
    
    Set p1 = Nothing
    Set p2 = Nothing
    Set col = Nothing
End Sub

private sub FileIODemo()
    Dim path As String: path = "myText.txt"
    Dim FileNo As Integer: FileNo = FreeFile
    
    Open path For Output As FileNo
    Print #FileNo, "Hello"
    Print #FileNo, "ZL"
    Print #FileNo, "SCY"
    Close FileNo
end sub

private sub TypeDemo()
    ' enum
    ' type: it is similar with struct type;
    dim MyRecord as EmployeeRecord
    MyRecord.id = 123

    debug.print MyRecord.id

end sub

Private Sub StringPatternMatch()
    ' regexp
    Dim DataFormat$: DataFormat = "yyyy-mm-dd"
    Dim Pattern$: Pattern = "[\/]"
    
    Debug.Print DataFormat Like Pattern
End Sub