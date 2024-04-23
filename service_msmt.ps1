Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

# Create a new form
$form = New-Object System.Windows.Forms.Form
$form.Text = "Remote Service Manager"
$form.Size = New-Object System.Drawing.Size(600,500) # Adjusted form height to accommodate TextBox
$form.FormBorderStyle = [System.Windows.Forms.FormBorderStyle]::FixedSingle
$form.MaximizeBox = $false

# Create TextBox for entering server name
$serverTextBox = New-Object System.Windows.Forms.TextBox
$serverTextBox.Location = New-Object System.Drawing.Point(10, 10)
$serverTextBox.Size = New-Object System.Drawing.Size(350, 20)
$serverTextBox.Text = "localhost" # Default server name
$form.Controls.Add($serverTextBox)

# Create Submit button
$submitButton = New-Object System.Windows.Forms.Button
$submitButton.Location = New-Object System.Drawing.Point(370, 10)
$submitButton.Size = New-Object System.Drawing.Size(120, 20)
$submitButton.Text = "Connect"
$submitButton.Add_Click({
    Connect-ToServer
})
$form.Controls.Add($submitButton)

# Create DataGridView to display services
$dataGridView = New-Object System.Windows.Forms.DataGridView
$dataGridView.Location = New-Object System.Drawing.Point(10, 40) # Adjusted DataGridView position
$dataGridView.Size = New-Object System.Drawing.Size(570, 320)
$dataGridView.AllowUserToAddRows = $false
$dataGridView.ReadOnly = $true

# Define columns for the DataGridView
$serviceNameColumn = New-Object System.Windows.Forms.DataGridViewTextBoxColumn
$serviceNameColumn.HeaderText = "Service Name"
$serviceNameColumn.Name = "ServiceName"

$serviceStatusColumn = New-Object System.Windows.Forms.DataGridViewTextBoxColumn
$serviceStatusColumn.HeaderText = "Status"
$serviceStatusColumn.Name = "Status"

$serviceTypeColumn = New-Object System.Windows.Forms.DataGridViewTextBoxColumn
$serviceTypeColumn.HeaderText = "Type"
$serviceTypeColumn.Name = "Type"

$servicePIDColumn = New-Object System.Windows.Forms.DataGridViewTextBoxColumn
$servicePIDColumn.HeaderText = "PID"
$servicePIDColumn.Name = "PID"

# Add columns to the DataGridView
$dataGridView.Columns.Add($serviceNameColumn)
$dataGridView.Columns.Add($serviceStatusColumn)
$dataGridView.Columns.Add($serviceTypeColumn)
$dataGridView.Columns.Add($servicePIDColumn)

# Create Start button
$startButton = New-Object System.Windows.Forms.Button
$startButton.Location = New-Object System.Drawing.Point(10, 370) # Adjusted Start button position
$startButton.Size = New-Object System.Drawing.Size(120, 30)
$startButton.Text = "Start Service"
$startButton.Add_Click({
    Perform-ServiceTask -Action "Start"
})

# Create Stop button
$stopButton = New-Object System.Windows.Forms.Button
$stopButton.Location = New-Object System.Drawing.Point(140, 370) # Adjusted Stop button position
$stopButton.Size = New-Object System.Drawing.Size(120, 30)
$stopButton.Text = "Stop Service"
$stopButton.Add_Click({
    Perform-ServiceTask -Action "Stop"
})

# Create Restart button
$restartButton = New-Object System.Windows.Forms.Button
$restartButton.Location = New-Object System.Drawing.Point(270, 370) # Adjusted Restart button position
$restartButton.Size = New-Object System.Drawing.Size(120, 30)
$restartButton.Text = "Restart Service"
$restartButton.Add_Click({
    Perform-ServiceTask -Action "Restart"
})

# Create Kill button
$killButton = New-Object System.Windows.Forms.Button
$killButton.Location = New-Object System.Drawing.Point(400, 370) # Adjusted Kill button position
$killButton.Size = New-Object System.Drawing.Size(120, 30)
$killButton.Text = "Kill Service"
$killButton.Add_Click({
    Kill-Service
})

# Create Refresh button
$refreshButton = New-Object System.Windows.Forms.Button
$refreshButton.Location = New-Object System.Drawing.Point(10, 410) # Adjusted Refresh button position
$refreshButton.Size = New-Object System.Drawing.Size(570, 30)
$refreshButton.Text = "Refresh"
$refreshButton.Add_Click({
    Refresh-DataGridView
})

# Add controls to form
$form.Controls.Add($serverTextBox)
$form.Controls.Add($submitButton)
$form.Controls.Add($dataGridView)
$form.Controls.Add($startButton)
$form.Controls.Add($stopButton)
$form.Controls.Add($restartButton)
$form.Controls.Add($killButton)
$form.Controls.Add($refreshButton)

# Define function to refresh the DataGridView
function Refresh-DataGridView {
    $dataGridView.Rows.Clear()
    $services = Invoke-Command -ComputerName $serverTextBox.Text -ScriptBlock {
        Get-Service | Select-Object DisplayName, @{Name="Status";
