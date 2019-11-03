import csv
import boto3
from evaluation_function import evalutate_quantitative

DATA = "E:/workspace/bank-data-challenge/data/small_set.csv"

DYNAMO_TABLE = "ConsumerComplaints"
def main():
    print("Starting")
    dynamo_client = boto3.client("dynamodb")
    with open(DATA, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        for row in reader:
            print(row)
            dynamo_row = {}
            for key, val in row.items():
                if val:
                    dynamo_row[key] = {"S": val}
                # print(key, ":", val)
            dynamo_client.put_item(TableName=DYNAMO_TABLE, Item=dynamo_row)


if __name__ == "__main__":
    main()