Attribute VB_Name = "Module1"
Sub myStockData()

    Dim rowCnt_1  As Double
    Dim oPrice As Double
    Dim yrChange As Double
    Dim perChange As Double
    'Dim preRowValue As String
    Dim currentWS As Worksheet
    
    For Each currentWS In ActiveWorkbook.Worksheets
        'Initial each variable for each worksheet
        currentWS.Activate
        rowCnt_1 = 0
        oPrice = 0
        yrChange = 0
        perChange = 0
        
        'Header column labels .Interior.ColorIndex = 4
        Range("J1").Value = "Ticker"
        Range("K1").Value = "Yearly Change"
        Range("L1").Value = "Percent Change"
        Range("M1").Value = "Total Volume"
        Range("P1").Value = "Greatest"
        Range("P2").Value = "% Increase"
        Range("P3").Value = "% Decrease"
        Range("P4").Value = "Total Volume"
        Range("Q1").Value = "Ticker"
        Range("R1").Value = "Value"
        'Header bgcolor
        Range("J1:M1").Interior.ColorIndex = 41
        Range("P1:R1").Interior.ColorIndex = 41
        Range("J1:M1").Select
        Selection.Font.Bold = True
        Range("P1:R1").Select
        Selection.Font.Bold = True
        Range("P2:P4").Select
        Selection.Font.Bold = True
        Range("A1").Select
        
        rowCnt_1 = 2
        'preRowValue = Cells(rowCnt_1, 1).Value
        'Cells(rowCnt_1, 10).Value = preRowValue
        oPrice = Cells(rowCnt_1, 3).Value
        lastRow = currentWS.Cells(Rows.Count, 1).End(xlUp).Row
        
        Dim totVolume As Double
        totVolume = 0
        
        'Iterating through each row to do the manipulations
        For rowCnt_2 = 2 To lastRow
            'MsgBox ("Current row: " + Str(rowCnt_2))
            'MsgBox ("Printing row: " + Str(rowCnt_1))
            If Cells(rowCnt_2 + 1, 1).Value <> Cells(rowCnt_2, 1).Value Then
                totVolume = totVolume + Cells(rowCnt_2, 7).Value
                Cells(rowCnt_1, 13).Value = totVolume                       'Total Volume
                Cells(rowCnt_1, 10).Value = Cells(rowCnt_2, 1).Value        'Ticker
                
                yrChange = Cells(rowCnt_2, 6).Value - oPrice
                Cells(rowCnt_1, 11).Value = yrChange                        'Yearly Change
                Cells(rowCnt_1, 11).NumberFormat = "0.000000000"
                If (Cells(rowCnt_2, 6).Value = 0 And oPrice = 0) Then
                    perChange = 0
                ElseIf (Cells(rowCnt_2, 6).Value <> 0 And oPrice = 0) Then
                    perChange = 1
                Else
                    perChange = yrChange / oPrice
                    Cells(rowCnt_1, 12).Value = perChange                   'Percent Change
                    Cells(rowCnt_1, 12).NumberFormat = "0.00%"
                End If
                rowCnt_1 = rowCnt_1 + 1
                oPrice = Cells(rowCnt_2 + 1, 3).Value
                totVolume = 0
                
            Else
                totVolume = totVolume + Cells(rowCnt_2, 7).Value
                
            End If
            
         Next rowCnt_2
         
         'Conditional formatting for color green and red
         lastRow = currentWS.Cells(Rows.Count, 10).End(xlUp).Row
         For rowCnt_2 = 2 To lastRow
            If (Cells(rowCnt_2, 11).Value >= 0) Then
                Cells(rowCnt_2, 11).Interior.ColorIndex = 4
                
            ElseIf (Cells(rowCnt_2, 11).Value < 0) Then
                Cells(rowCnt_2, 11).Interior.ColorIndex = 3
                
            End If
         
         Next rowCnt_2
         
         'Percent increase/ decrease/ total volume
         lastRow = currentWS.Cells(Rows.Count, 10).End(xlUp).Row
         For rowCnt_2 = 2 To lastRow
            If Cells(rowCnt_2, 12).Value = Application.WorksheetFunction.Max(currentWS.Range("L2:L" & lastRow)) Then
                Range("Q2").Value = Cells(rowCnt_2, 10).Value
                Range("R2").Value = Cells(rowCnt_2, 12).Value
                Range("R2").NumberFormat = "0.00%"
            ElseIf Cells(rowCnt_2, 12).Value = Application.WorksheetFunction.Min(currentWS.Range("L2:L" & lastRow)) Then
                Range("Q3").Value = Cells(rowCnt_2, 10).Value
                Range("R3").Value = Cells(rowCnt_2, 12).Value
                Range("R3").NumberFormat = "0.00%"
            ElseIf Cells(rowCnt_2, 13).Value = Application.WorksheetFunction.Max(currentWS.Range("M2:M" & lastRow)) Then
                Range("Q4").Value = Cells(rowCnt_2, 10).Value
                Range("R4").Value = Cells(rowCnt_2, 13).Value
            End If
         
         Next rowCnt_2
         'Auto fit the columns to adjust large values
         currentWS.Columns("A:R").AutoFit
         
     Next currentWS

End Sub

