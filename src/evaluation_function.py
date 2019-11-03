# Weights for "Company Response"
response_weights = {
    'Closed with monetary relief': 3,
    'Closed with non-monetary relief': 2,
    'Closed with relief': 2,
    'Closed with explanation': 1,
    'Closed without relief': -1,
    'Closed': -1,
    'In progress': 0,
    'Untimely response': -2,
    'N/A': 0,
    'nan': 0,
    None: 0
}

# Weights for "Consumer disputed?"
disputed_weights = {
    'No': 2,
    'Yes': -2,
    'N/A': 0,
    'nan': 0,
    None: 0
}

# Weights for "Timely response?"
timely_weights = {
    'No': -2,
    'Yes': 2,
    'N/A': 0,
    'nan': 0,
    None: 0
}


def evalutate_quantitative(row)->int:
    """
    Provides score for a single record of bank consumer data looking only at the "Quantitative" fields

    :param row: a single complaint record
    :return: int score
    """
    score = 0
    score = score + timely_weights[str(row['Timely response?']['S'])]
    score = score + disputed_weights[str(row['Consumer disputed?']['S'])]
    score = score + response_weights[str(row['Company response to consumer']['S'])]

    return score
