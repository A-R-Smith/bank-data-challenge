"""
Consumer Complain Processor
This function is pass a certain segment of the table to process.
It will iterate thru all rows in its segment, apply the evaluation function and then put the score as a new column on
the row

"""
import boto3
from evaluation_function import evalutate_quantitative

TABLE_NAME = "ConsumerComplaints"


def handler(event, _context):
    print(event)

    # get which segment this worker will process
    segment = event["segment"]
    total_segments = event["total"]

    # initialize clients
    dynamo = boto3.client("dynamodb")
    paginator = dynamo.get_paginator("scan")

    # initialize batch, this allows for us to bath dynamodb table calls to avoid overloading the table writers
    item_batch = []
    batch_count = 0

    # Start paginating thru table
    for page in paginator.paginate(TableName=TABLE_NAME, Segment=segment, TotalSegments=total_segments):
        for item in page['Items']:

            # Execute evaluation function
            item['score'] = {"S": evalutate_quantitative(item)}

            # batch up records
            item_batch.append({'PutRequest': {'Item': item}})
            batch_count = batch_count + 1
            if batch_count % 25 == 0:
                dynamo.batch_write_item(RequestItems={TABLE_NAME: item_batch})
                item_batch = []
                print(batch_count)

    # when done, write the last batch
    if item_batch:
        dynamo.batch_write_item(RequestItems={TABLE_NAME: item_batch})
