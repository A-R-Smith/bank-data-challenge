import csv
from evaluation_function import evalutate_quantitative

DATA = "E:/workspace/bank-data-challenge/data/Consumer_Complaints.csv"

def main():
    count = 0
    print("Starting")
    output = {}
    with open(DATA, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        for row in reader:
            print(row)
            count = count + 1
            score = evalutate_quantitative(row)
            print(score)
            if count > 1000:
                break

            if score.company not in output:
                output[score.company] = {'SumScore': score.score, 'Count': 1}
            else:
                output[score.company]['SumScore'] += score.score
                output[score.company]['Count'] += 1

            if score.product not in output[score.company]:
                output[score.company][score.product] = {'SumScore': score.score, 'Count': 1}
            else:
                output[score.company][score.product]['SumScore'] += score.score
                output[score.company][score.product]['Count'] += 1

    summed_output = output
    for company, value in output.items():
        summed_output[company] = {"Score": value['SumScore']/value[['Count']]}
        for


if __name__ == "__main__":
    main()