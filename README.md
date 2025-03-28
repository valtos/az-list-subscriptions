# Azure Subscription Filter Script

## Overview
This script lists Azure subscriptions, filters out those with "SANDBOX" in their display name, and outputs the details in CSV format.

## Prerequisites
- Python 3.x
- Azure SDK for Python
- Environment variables for Azure credentials:
  - `CLIENT_ID`
  - `CLIENT_SECRET`
  - `TENANT_ID`

## Installation
1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required Python packages:
    ```sh
    pip install azure-identity azure-mgmt-network azure-mgmt-subscription azure-mgmt-resource
    ```

## Usage
1. Set the environment variables for Azure credentials:
    ```sh
    export CLIENT_ID=<your-client-id>
    export CLIENT_SECRET=<your-client-secret>
    export TENANT_ID=<your-tenant-id>
    ```

2. Run the script:
    ```sh
    ./azure_subscription_filter.py
    ```

## Output
The script will print the filtered subscriptions in CSV format with the following columns:
- Display Name
- Subscription ID
- State

Additionally, it will display the execution time at the end.

## Example
```sh
Display Name,Subscription ID,State
Example Subscription 1,12345678-1234-1234-1234-123456789012,Enabled
Example Subscription 2,87654321-4321-4321-4321-210987654321,Disabled
Execution time: 2.34 seconds