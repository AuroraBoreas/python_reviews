VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "clsRectangle"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = False
Attribute VB_Exposed = False
Option Explicit

Implements IShape

Private m_length As Double
Private m_width As Double

Public Sub Init(length As Double, width As Double)
    m_length = length
    m_width = width
End Sub

Public Function IShape_Area() As Double
    IShape_Area = m_length * m_width
End Function

Public Function IShape_Circumference() As Double
    IShape_Circumference = (m_length + m_width) * 2
End Function

Public Function IShape_ToString() As String
    IShape_ToString = "Rectangle, length = " & m_length & ",  width = " & m_width
End Function
