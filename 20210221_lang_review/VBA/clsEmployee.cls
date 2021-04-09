Option Explicit

implements IPerson

Private m_Name As String
Private m_Sex As String
Private m_Age As Integer

Public Sub init(ByVal name As String, ByVal sex As String, ByVal age As Integer)
    m_Name = name
    m_Sex = sex
    m_Age = age
End Sub

' getter
Public Property Get name() As String
    name = m_Name
End Property

Public Property Get sex() As String
    sex = m_Sex
End Property

Public Property Get age() As Integer
    age = m_Age
End Property

' setter
Public Property Let name(ByVal val As String)
    m_Name = val
End Property

Public Property Let sex(ByVal val As String)
    m_Sex = val
End Property

Public Property Let age(ByVal val As Integer)
    m_Age = val
End Property

' method
Public Function ToString() As String
    ToString = vbCrLf & "Name: " & m_Name & vbCrLf & "Sex: " & m_Sex & vbCrLf & "Age: " & m_Age
End Function

' implements IPerson methods
public Property Get IPerson_Name() as String
    IPerson_Name = m_Name
end Property

public Property Get IPerson_Age() as Integer
    IPerson_Age = m_Age
end Property
