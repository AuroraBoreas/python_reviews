VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "clsManager"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = False
Attribute VB_Exposed = False
Option Explicit

Implements IPerson

Private m_name As String
Private m_age As Integer
Private m_sex As String
Private m_salary As Double

Public Sub Init(Name As String, _
                        Age As Integer, _
                        Sex As String, _
                        Salary As Double)
                                                
    m_name = Name
    m_age = Age
    m_sex = Sex
    m_salary = Salary
End Sub

' getter
Public Property Get Name() As String
    Name = m_name
End Property

Public Property Get Age() As Integer
    Age = m_age
End Property

Public Property Get Sex() As String
    Sex = m_sex
End Property

Public Property Get Salary() As Double
    Salary = m_salary
End Property

' setter
Public Property Let Name(val As String)
    m_name = val
End Property

Public Property Let Age(val As Integer)
    m_age = val
End Property

Public Property Let Sex(val As String)
    m_sex = val
End Property

Public Property Let Salary(val As Double)
    m_salary = val
End Property

' repr
Public Function ToString() As String
    ToString = vbNewLine & "Name: " & m_name & _
                        vbNewLine & "Age: " & m_age & _
                        vbNewLine & "Sex: " & m_sex & _
                        vbNewLine & "Salary: " & m_salary
End Function


' implements
Public Property Get IPerson_Name() As String
    IPerson_Name = m_name
End Property

Public Property Get IPerson_Age() As Integer
    IPerson_Age = m_age
End Property

Public Function IPerson_ToString() As String
    IPerson_ToString = vbNewLine & "Name: " & m_name & _
                        vbNewLine & "Age: " & m_age & _
                        vbNewLine & "Sex: " & m_sex & _
                        vbNewLine & "Salary: " & m_salary
End Function



