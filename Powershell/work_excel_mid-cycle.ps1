

Add-Type -AssemblyName System.windows.forms

$dialog = New-Object System.Windows.Forms.OpenFileDialog
$dialog.Filter = "Excel Files (*.xlsx;*.xls)|*.xlsx;*.xls"
$dialog.Title = "Select your workbook"

#will need to change at work
$dialog.InitialDirectory = "C:\Users\CJ\Documents\GitHub\Scripts\Powershell"


if ($dialog.ShowDialog() -eq "OK") {
    $filepath = $dialog.FileName
    } else {
        Write-Host "No file selected. Exiting..."
        exit
        }


$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false

$wb = $excel.Workbooks.Open($filepath)


$allsheets = @{}

# loop through rows
foreach ($sheet in $wb.Worksheets){

    $sheetname = $sheet.Name
    $usedRange = $sheet.UsedRange

    $rows = $usedRange.Rows.Count


}