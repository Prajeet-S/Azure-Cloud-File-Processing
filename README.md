# Azure Cloud File Processing System

A serverless file processing system built using Azure Blob Storage, Azure Functions, and Azure Queue Storage.

## Architecture

File uploaded to Blob Storage
        ↓
Blob Trigger
        ↓
File Processing
        ↓
Processed file stored in Blob Storage
        ↓
Message sent to Azure Queue
        ↓
Queue Trigger
        ↓
Message processed and logged

## Technologies Used

- Python
- Azure Functions
- Azure Blob Storage
- Azure Queue Storage
- Azure Functions Core Tools
- Azure CLI

## Features

- Automatically detects newly uploaded files
- Processes uploaded file content
- Stores processed files in Azure Blob Storage
- Sends processing status through Azure Queue Storage
- Processes queue messages asynchronously
- Uses JSON-based queue messages
- Implements error handling and logging
- Tested Azure Queue retry and poison queue behavior

## How It Works

1. A file is uploaded to the `inputs/` path in Azure Blob Storage.
2. The Blob Trigger automatically starts the Azure Function.
3. The function reads and processes the file.
4. The processed file is stored in the `processed/` path.
5. A JSON message containing the file name and status is sent to Azure Queue Storage.
6. The Queue Trigger receives the message and processes it.
7. Processing information is recorded using logging.

## Error Handling

The project was tested with an intentional queue-processing failure to understand Azure Queue retry behavior and poison queues.

## Project Status

**Completed**