# bank-data-challenge
Data pipeline to process bank complaint data to provide a score for each bank.

## Approach
We will score each individual complaint based on an evaluation criteria of assigning a integer weight to each possible value
of fields in the record. The weights will be negative for undesirable results and positive for desirable results.
Each Company and Product will have the score of its individual complaints averaged up to form the total score.

## Assumptions
1) Only the single data set provided will be used
    - If we could bring in other data sets such as "number of customers", then we could start using counts of issues and
    complaints to draw conclusions by looking at complaint to number of customer ratios.
2) Due to time constraints, only the "quantitative" fields will be used in the scoring of Companies and Products. 
    - These fields are: Company Response, Consumer disputed? Timely response?
    - With more time, we could look into the more free-form fields such as "Issue" and assign a weight to each one.
    
## Steps Taken
1) The dataset was profiled in a Jupyter Notebook using a Python Pandas Dataframe. By looking at the unique values of
each field, the idea of how the evaluation function and data model would work began to develop. Please [check the Notebook](nb/bank-recommend.ipynb) 
to see my logic and thought process.
2) After a simple evaluation function was developed, an ETL pipeline using Step Functions, Lambdas and DynamoDb 
to apply the evaluation to the data in a scalable way was built.

## The ETL pipeline
First, there is a simple [script](src/load_data.py) to load the data into a dynamodb table (table definition [here](iac/DynamoTable.yaml)). 
There is a StepFunction and Lambdas that iterate thru the data in the table, apply the simple [evaluation function](src/evaluation_function.py) developed 
during initial analysis and add a score to each complaint as a new column in the table. 
- [Lambda/StepFunction Serverless Definition](src/serverless.yaml)
- [Step Function Mapper Code](src/consumer_complaint_mapper.py)
- [Step Function Worker/Processor Code](src/consumer_complaint_processor.py)

## Next Steps
4) Create Better Visualizations
5) Begin to do deeper analysis of the other fields provided in the data. Use statistical analysis to find correlations between Issues, 
company responses and consumer disputes. See if there some products and products have common reoccurring issues.
6) Bring in other datasets to enrich the analysis

## Dependencies Used
- Jupyter and Pandas for initial data analysis
- AWS Step Functions, Lambda and DynamoDB for ETL pipeline
    - Used Serverless.com framework to deploy (step-functions and pseudo-parameters plugins)
    - Used boto3 library for AWS api calls
