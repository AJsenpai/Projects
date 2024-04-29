Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

# Create a new form
$form = New-Object System.Windows.Forms.Form
$form.Text = "Remote Service Manager"
$form.Size = New-Object System.Drawing.Size(600,530) # Adjusted form height to accommodate TextBox
$form.FormBorderStyle = [System.Windows.Forms.FormBorderStyle]::FixedSingle
$form.MaximizeBox = $false

# Create TextBox for entering server names and service names
$serverServiceTextBox = New-Object System.Windows.Forms.TextBox
$serverServiceTextBox.Location = New-Object System.Drawing.Point(10, 10)
$serverServiceTextBox.Size = New-Object System.Drawing.Size(480, 20)
$serverServiceTextBox.Text = "localhost, Spooler" # Default server and service names
$form.Controls.Add($serverServiceTextBox)

# Create Submit button
$submitButton = New-Object System.Windows.Forms.Button
$submitButton.Location = New-Object System.Drawing.Point(500, 10)
$submitButton.Size = New-Object System.Drawing.Size(80, 20)
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

# Create Refresh button
$refreshButton = New-Object System.Windows.Forms.Button
$refreshButton.Location = New-Object System.Drawing.Point(10, 370) # Adjusted Refresh button position
$refreshButton.Size = New-Object System.Drawing.Size(570, 30)
$refreshButton.Text = "Refresh"
$refreshButton.Add_Click({
    Refresh-DataGridView
})

# Add controls to form
$form.Controls.Add($serverServiceTextBox)
$form.Controls.Add($submitButton)
$form.Controls.Add($dataGridView)
$form.Controls.Add($refreshButton)

# Define function to refresh the DataGridView
function Refresh-DataGridView {
    $dataGridView.Rows.Clear()
    $serversServices = $serverServiceTextBox.Text.Split(",")
    foreach ($serverService in $serversServices) {
        $server, $service = $serverService.Trim().Split("`n")
        $serviceData = Invoke-Command -ComputerName $server -ScriptBlock {
            param($serviceName)
            Get-Service $serviceName | Select-Object DisplayName, @{Name="Status"; Expression={if($_.Status -eq "Running"){ "Running" } elseif($_.Status -eq "Stopped"){ "Stopped" } elseif($_.Status -eq "Paused"){ "Paused" } else { "Unknown" }}}, @{Name="Type"; Expression={if($_.ServiceType -eq "Win32OwnProcess"){ "Own Process" } elseif($_.ServiceType -eq "Win32ShareProcess"){ "Shared Process" } else { "Kernel Driver" }}}, ID
        } -ArgumentList $service
        foreach ($data in $serviceData) {
            $servicePID = (Get-WmiObject Win32_Service -ComputerName $server | Where-Object {$_.Name -eq $data.DisplayName}).ProcessID
            $dataGridView.Rows.Add($data.DisplayName, $data.Status, $data.Type, $servicePID)
        }
    }
}

# Function to connect to the remote server(s) and fetch service data
function Connect-ToServer {
    Refresh-DataGridView
}

# Start the form
$form.ShowDialog() | Out-Null