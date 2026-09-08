import azure.functions as func
import logging
import json
app=func.FunctionApp()

@app.blob_trigger(
    arg_name="my_file",
    path="testcontainer/inputs/{name}",
    connection="prajeetstorage1_STORAGE"
)
@app.blob_output(
    arg_name="outputblob",
    path="testcontainer/processed/{name}",
    connection="prajeetstorage1_STORAGE"
)
@app.queue_output(
    arg_name="queue_message",
    queue_name="file-processing-queue",
    connection="prajeetstorage1_STORAGE"
)
def func_blob(my_file: func.InputStream, outputblob: func.Out[str] ,queue_message: func.Out[str]):
    try:
        file_content=my_file.read().decode("utf-8")
        logging.info(f"Processing file: {my_file.name}")
        logging.info(f"Original content: {file_content}")

        processed_content=file_content.upper()
        logging.info(f"Processed Content: {processed_content}")
        outputblob.set(processed_content)
        queue_data={
            "file_name": my_file.name,
            "status":"processed"
        }
        queue_message.set(json.dumps(queue_data))
        logging.info("Message added to queue successfully")
    except Exception as e:
        logging.error(f"Error processing {my_file.name}:{e}")
@app.queue_trigger(
    arg_name="msg",
    queue_name="file-processing-queue",
    connection="prajeetstorage1_STORAGE"
)
def process_queue(msg: func.QueueMessage):
    message = msg.get_body().decode("utf-8")
    queue_data=json.loads(message)
    file_name=queue_data["file_name"]
    status=queue_data["status"]
    logging.info(f"File name: {file_name}\nStatus: {status}")





