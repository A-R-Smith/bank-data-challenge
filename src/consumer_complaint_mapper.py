"""
Consumer Complaint Mapper
This function splits the input dynamodb table into segments for the workers to process in parallel.
It then passes which segment each worker needs to process to each worker in the Map StepFunction

"""
TOTAL_SEGMENTS = 16


def handler(_event, _context):
    return {"segments": [{"segment": x, "total": TOTAL_SEGMENTS} for x in range(TOTAL_SEGMENTS)]}
