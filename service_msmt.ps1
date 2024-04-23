Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

# Create a new form
$form = New-Object System.Windows.Forms.Form
$form.Text = "Remote Service Manager"
$form.Size = New-Object System.Drawing.Size(500,500) # Adjusted form height to accommodate TextBox
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
$dataGridView.Size = New-Object System.Drawing.Size(480, 320)
$dataGridView.AllowUserToAddRows = $false
$dataGridView.ReadOnly = $true

# Define columns for the DataGridView
$serviceNameColumn = New-Object System.Windows.Forms.DataGridViewTextBoxColumn
$serviceNameColumn.HeaderText = "Service Name"
$serviceNameColumn.Name = "ServiceName"

$serviceStatusColumn = New-Object System.Windows.Forms.DataGridViewTextBoxColumn
$serviceStatusColumn.HeaderText = "Status"
$serviceStatusColumn.Name = "Status"

# Add columns to the DataGridView
$dataGridView.Columns.Add($serviceNameColumn)
$dataGridView.Columns.Add($serviceStatusColumn)

# Create Start button
$startButton = New-Object System.Windows.Forms.Button
$startButton.Location = New-Object System.Drawing.Point(10, 370) # Adjusted Start button position
$startButton.Size = New-Object System.Drawing.Size(150, 30)
$startButton.Text = "Start Service"
$startButton.Add_Click({
    Perform-ServiceTask -Action "Start"
})

# Create Stop button
$stopButton = New-Object System.Windows.Forms.Button
$stopButton.Location = New-Object System.Drawing.Point(180, 370) # Adjusted Stop button position
$stopButton.Size = New-Object System.Drawing.Size(150, 30)
$stopButton.Text = "Stop Service"
$stopButton.Add_Click({
    Perform-ServiceTask -Action "Stop"
})

# Create Restart button
$restartButton = New-Object System.Windows.Forms.Button
$restartButton.Location = New-Object System.Drawing.Point(350, 370) # Adjusted Restart button position
$restartButton.Size = New-Object System.Drawing.Size(150, 30)
$restartButton.Text = "Restart Service"
$restartButton.Add_Click({
    Perform-ServiceTask -Action "Restart"
})

# Create Refresh button
$refreshButton = New-Object System.Windows.Forms.Button
$refreshButton.Location = New-Object System.Drawing.Point(10, 410) # Adjusted Refresh button position
$refreshButton.Size = New-Object System.Drawing.Size(480, 30)
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
$form.Controls.Add($refreshButton)

# Define function to refresh the DataGridView
function Refresh-DataGridView {
    $dataGridView.Rows.Clear()
    $services = Invoke-Command -ComputerName $serverTextBox.Text -ScriptBlock {
        Get-Service | Select-Object DisplayName, Status
    }
    foreach ($service in $services) {
        $dataGridView.Rows.Add($service.DisplayName, $service.Status)
    }
}

# Function to connect to the remote server and refresh DataGridView
function Connect-ToServer {
    Refresh-DataGridView
}

# Function to perform service management task on the remote server
function Perform-ServiceTask {
    param(
        [string]$Action
    )
    if ($dataGridView.SelectedRows.Count -eq 0) {
        [System.Windows.Forms.MessageBox]::Show("Please select a service.", "Error", [System.Windows.Forms.MessageBoxButtons]::OK, [System.Windows.Forms.MessageBoxIcon]::Error)
        return
    }
    $selectedService = $dataGridView.SelectedRows[0].Cells["ServiceName"].Value
    Invoke-Command -ComputerName $serverTextBox.Text -ScriptBlock {
        param($serviceName, $action)
        if ($action -eq "Start") {
            Start-Service -Name $serviceName
        } elseif ($action -eq "Stop") {
            Stop-Service -Name $serviceName
        } elseif ($action -eq "Restart") {
            Restart-Service -Name $serviceName
        }
    } -ArgumentList $selectedService, $Action
}

# Start the form
$form.ShowDialog() | Out-Null
