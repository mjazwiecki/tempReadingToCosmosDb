import logging
import azure.functions as func


def main(event: func.EventHubEvent, doc: func.Out[func.Document]):
    logging.info('Function triggered to process a message:  %s', event.get_body())
    logging.info('  EnqueuedTimeUtc = %s', event.enqueued_time)
    logging.info('  SequenceNumber = %s', event.sequence_number)
    logging.info('  Offset = %s', event.offset)


    request_body = event.get_body()
    doc.set(func.Document.from_json(request_body))

