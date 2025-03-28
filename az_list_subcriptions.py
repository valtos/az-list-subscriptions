#!/usr/bin/env python3
# This shebang line allows the script to be run as an executable, using the Python 3 interpreter.

import os
import time
# Importing necessary modules: 'os' for environment variables and 'time' for tracking execution time.

from azure.identity import ClientSecretCredential
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.subscription import SubscriptionClient
# Importing Azure SDK modules for authentication and managing subscriptions.

DEBUG = False
# A debug flag that can be used to enable or disable debug mode.

# Fetching Azure credentials from environment variables.
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
tenant_id = os.getenv("TENANT_ID")

# Creating a credential object using the fetched Azure credentials.
credentialsazure = ClientSecretCredential(tenant_id, client_id, client_secret)

def list_az_filtered_subscriptions():
    # Function to list Azure subscriptions, filtering out those with "SANDBOX" in their display name.
    
    subscription_client = SubscriptionClient(credentialsazure)
    # Initializing the SubscriptionClient with the credentials.

    subscriptions = list(subscription_client.subscriptions.list())
    # Fetching the list of subscriptions.

    filtered_subscriptions = [
        subscription for subscription in subscriptions
        if "SANDBOX" not in subscription.display_name
    ]
    # Filtering out subscriptions that contain "SANDBOX" in their display name.

    # Sort filtered subscriptions by display name.
    filtered_subscriptions.sort(key=lambda x: x.display_name)

    return filtered_subscriptions
    # Returning the filtered and sorted list of subscriptions.

# Tracking the start time of the operation.
start_time_azure = time.time()

# Calling the function to get the filtered subscriptions.
azure_subscriptions = list_az_filtered_subscriptions()

# Printing the header for the CSV format.
print("display_name,subscription_id,state")

# Printing the details of each subscription.
for subscription in azure_subscriptions:
    print(subscription.display_name + "," + subscription.subscription_id + "," + subscription.state)

# Tracking the end time of the operation.
end_time_azure = time.time()

# Calculating and displaying the execution time.
execution_time = end_time_azure - start_time_azure
print(f"Execution time: {execution_time:.2f} seconds")