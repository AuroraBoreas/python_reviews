VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "clsCircle"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = False
Attribute VB_Exposed = False
Option Explicit

Implements IShape

Private m_radius As Double
Const m_pi As Double = 3.1415926

Public Sub Init(radius As Double)
    m_radius = radius
End Sub

Public Function IShape_Area() As Double
    IShape_Area = m_pi * m_radius * m_radius
End Function

Public Function IShape_Circumference() As Double
    IShape_Circumference = m_pi * m_radius * 2
End Function

Public Function IShape_ToString() As String
    IShape_ToString = "Circle, radius = " & m_radius
End Function
