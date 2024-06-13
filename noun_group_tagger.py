"""
import os
from nltk.stem import PorterStemmer

TRAIN_FP = './WSJ_02-21.pos-chunk'
DEV_FP = './WSJ_23.pos'
TRAIN_OUTPUT = './training.feature'
DEV_OUTPUT = './test.feature'
RESPONSE_FILE = './WSJ_23.chunk'

porter_stemmer = PorterStemmer()

def feature_values_training(tokens, pos_tags, bio_tags):
    feature_strs = []

    for i in range(len(tokens)):
        if not tokens[i]:
            feature_strs.append('')
        else:
            feature_set = []

            feature_set.append(f'POS={pos_tags[i]}')
            feature_set.append(f'stemmed={porter_stemmer.stem(tokens[i])}')
            feature_set.append(f'capitalized={tokens[i][0].isupper()}')
            feature_set.append(f'token_length={len(tokens[i])}')
            feature_set.append(f'contains_digit={any(char.isdigit() for char in tokens[i])}')

            if i > 1 and tokens[i - 2] and tokens[i - 1]:
                feature_set.append(f'two_before_word={tokens[i - 2]}')
                feature_set.append(f'two_before_POS={pos_tags[i - 2]}')
                feature_set.append(f'two_before_BIO={bio_tags[i - 2]}')
                feature_set.append(f'two_before_stemmed={porter_stemmer.stem(tokens[i - 2])}')
                feature_set.append(f'two_before_capitalized={tokens[i - 2][0].isupper()}')
                feature_set.append(f'two_before_token_length={len(tokens[i - 2])}')
                feature_set.append(f'two_before_contains_digit={any(char.isdigit() for char in tokens[i - 2])}')  # Fixed here
            
            if i > 0 and tokens[i - 1]:
                feature_set.append(f'prev_word={tokens[i - 1]}')
                feature_set.append(f'prev_POS={pos_tags[i - 1]}')
                feature_set.append(f'prev_BIO={bio_tags[i - 1]}')
                feature_set.append(f'prev_stemmed={porter_stemmer.stem(tokens[i - 1])}')
                feature_set.append(f'prev_capitalized={tokens[i - 1][0].isupper()}')
                feature_set.append(f'prev_token_length={len(tokens[i - 1])}')
                feature_set.append(f'prev_contains_digit={any(char.isdigit() for char in tokens[i - 1])}')  # Fixed here

            
            if i < len(tokens) - 1 and tokens[i + 1]:
                feature_set.append(f'next_word={tokens[i + 1]}')
                feature_set.append(f'next_POS={pos_tags[i + 1]}')
                feature_set.append(f'next_BIO={bio_tags[i + 1]}')
                feature_set.append(f'next_stemmed={porter_stemmer.stem(tokens[i + 1])}')
                feature_set.append(f'next_capitalized={tokens[i + 1][0].isupper()}')
                feature_set.append(f'next_token_length={len(tokens[i + 1])}')
                feature_set.append(f'next_contains_digit={any(char.isdigit() for char in tokens[i + 1])}')
            
            if i < len(tokens) - 2 and tokens[i + 2] and tokens[i + 1]:
                feature_set.append(f'two_after_word={tokens[i + 2]}')
                feature_set.append(f'two_after_POS={pos_tags[i + 2]}')
                feature_set.append(f'two_after_BIO={bio_tags[i + 2]}')
                feature_set.append(f'two_after_stemmed={porter_stemmer.stem(tokens[i + 2])}')
                feature_set.append(f'two_after_capitalized={tokens[i + 2][0].isupper()}')
                feature_set.append(f'two_after_token_length={len(tokens[i + 2])}')
                feature_set.append(f'two_after_contains_digit={any(char.isdigit() for char in tokens[i + 2])}')

            to_str = '\t'.join(feature_set)
            feature_strs.append(f'{tokens[i]}\t{to_str}\t{bio_tags[i]}')

    return feature_strs

def feature_values_development(tokens, pos_tags):
    feature_strs = []

    for i in range(len(tokens)):
        if not tokens[i]:
            feature_strs.append('')
        else:
            feature_set = []

            feature_set.append(f'POS={pos_tags[i]}')
            feature_set.append(f'stemmed={porter_stemmer.stem(tokens[i])}')
            feature_set.append(f'capitalized={tokens[i][0].isupper()}')
            feature_set.append(f'token_length={len(tokens[i])}')
            feature_set.append(f'contains_digit={any(char.isdigit() for char in tokens[i])}')

            if i > 1 and tokens[i - 2] and tokens[i - 1]:
                feature_set.append(f'two_before_word={tokens[i - 2]}')
                feature_set.append(f'two_before_POS={pos_tags[i - 2]}')
                feature_set.append(f'two_before_stemmed={porter_stemmer.stem(tokens[i - 2])}')
                feature_set.append(f'two_before_capitalized={tokens[i - 2][0].isupper()}')
                feature_set.append(f'two_before_token_length={len(tokens[i - 2])}')
                feature_set.append(f'two_before_contains_digit={any(char.isdigit() for char in tokens[i - 2])}')
            
            if i > 0 and tokens[i - 1]:
                feature_set.append(f'prev_word={tokens[i - 1]}')
                feature_set.append(f'prev_POS={pos_tags[i - 1]}')
                feature_set.append(f'prev_stemmed={porter_stemmer.stem(tokens[i - 1])}')
                feature_set.append(f'prev_capitalized={tokens[i - 1][0].isupper()}')
                feature_set.append(f'prev_token_length={len(tokens[i - 1])}')
                feature_set.append(f'prev_contains_digit={any(char.isdigit() for char in tokens[i - 1])}')
            
            if i < len(tokens) - 1 and tokens[i + 1]:
                feature_set.append(f'next_word={tokens[i + 1]}')
                feature_set.append(f'next_POS={pos_tags[i + 1]}')
                feature_set.append(f'next_stemmed={porter_stemmer.stem(tokens[i + 1])}')
                feature_set.append(f'next_capitalized={tokens[i + 1][0].isupper()}')
                feature_set.append(f'next_token_length={len(tokens[i + 1])}')
                feature_set.append(f'next_contains_digit={any(char.isdigit() for char in tokens[i + 1])}')
            
            if i < len(tokens) - 2 and tokens[i + 2] and tokens[i + 1]:
                feature_set.append(f'two_after_word={tokens[i + 2]}')
                feature_set.append(f'two_after_POS={pos_tags[i + 2]}')
                feature_set.append(f'two_after_stemmed={porter_stemmer.stem(tokens[i + 2])}')
                feature_set.append(f'two_after_capitalized={tokens[i + 2][0].isupper()}')
                feature_set.append(f'two_after_token_length={len(tokens[i + 2])}')
                feature_set.append(f'two_after_contains_digit={any(char.isdigit() for char in tokens[i + 2])}')

            to_str = '\t'.join(feature_set)
            feature_strs.append(f'{tokens[i]}\t{to_str}')

    return feature_strs

def main():
    with open(TRAIN_FP, 'r') as f:
        tokens_train = []
        pos_tags_train = []
        bio_tags_train = []

        for line in f:
            text = line.strip()
            if not text:
                tokens_train.append('')
                pos_tags_train.append('')
                bio_tags_train.append('')
            else:
                data = text.split('\t')
                tokens_train.append(data[0])
                pos_tags_train.append(data[1])
                bio_tags_train.append(data[2])

    # Extract features from the training data
    features_train = feature_values_training(tokens_train, pos_tags_train, bio_tags_train)

    # Write training features to file
    with open(TRAIN_OUTPUT, 'w') as train_out:
        train_out.write('\n'.join(features_train))

    # Extract features from the test data (DEV_FP is now the test corpus)
    with open(DEV_FP, 'r') as dev_file:
        tokens_test = []
        pos_tags_test = []

        for line in dev_file:
            text = line.strip()
            if not text:
                tokens_test.append('')
                pos_tags_test.append('')
            else:
                data = text.split('\t')
                tokens_test.append(data[0])
                pos_tags_test.append(data[1])

    # Write test features to file (DEV_OUTPUT is now the test.feature file)
    features_test = feature_values_development(tokens_test, pos_tags_test)
    with open(DEV_OUTPUT, 'w') as test_out:
        test_out.write('\n'.join(features_test))

    # Assuming you have already compiled the Java files as described in the instructions
    # Running MEtag.java to create the final response file (WSJ_23.chunk)
    os.system(f"java -cp .:maxent-3.0.0.jar:trove.jar MEtag {DEV_OUTPUT} model.chunk WSJ_23.chunk")

main()
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 16:11:29 2024

@author: oonazhou
"""
import os
from nltk.stem import PorterStemmer

TRAIN_FP = './WSJ_02-21.pos-chunk'
DEV_FP = './WSJ_23.pos'
TRAIN_OUTPUT = './training.feature'
DEV_OUTPUT = './test.feature'
RESPONSE_FILE = './WSJ_23.chunk'

porter_stemmer = PorterStemmer()

def feature_values_training(tokens, pos_tags, bio_tags):
    feature_strs = []

    for i in range(len(tokens)):
        if not tokens[i]:
            feature_strs.append('')
        else:
            feature_set = []

            feature_set.append(f'POS={pos_tags[i]}')
            feature_set.append(f'stemmed={porter_stemmer.stem(tokens[i])}')
            feature_set.append(f'capitalized={tokens[i][0].isupper()}')
            feature_set.append(f'token_length={len(tokens[i])}')
            feature_set.append(f'contains_digit={any(char.isdigit() for char in tokens[i])}')

            if i > 1 and tokens[i - 2] and tokens[i - 1]:
                feature_set.append(f'two_before_word={tokens[i - 2]}')
                feature_set.append(f'two_before_POS={pos_tags[i - 2]}')
                feature_set.append(f'two_before_BIO={bio_tags[i - 2]}')
                feature_set.append(f'two_before_stemmed={porter_stemmer.stem(tokens[i - 2])}')
                feature_set.append(f'two_before_capitalized={tokens[i - 2][0].isupper()}')
                feature_set.append(f'two_before_token_length={len(tokens[i - 2])}')
                feature_set.append(f'two_before_contains_digit={any(char.isdigit() for char in tokens[i - 2])}')
            
            if i > 0 and tokens[i - 1]:
                feature_set.append(f'prev_word={tokens[i - 1]}')
                feature_set.append(f'prev_POS={pos_tags[i - 1]}')
                feature_set.append(f'prev_BIO={bio_tags[i - 1]}')
                feature_set.append(f'prev_stemmed={porter_stemmer.stem(tokens[i - 1])}')
                feature_set.append(f'prev_capitalized={tokens[i - 1][0].isupper()}')
                feature_set.append(f'prev_token_length={len(tokens[i - 1])}')
                feature_set.append(f'prev_contains_digit={any(char.isdigit() for char in tokens[i - 1])}')
            
            if i < len(tokens) - 1 and tokens[i + 1]:
                feature_set.append(f'next_word={tokens[i + 1]}')
                feature_set.append(f'next_POS={pos_tags[i + 1]}')
                feature_set.append(f'next_BIO={bio_tags[i + 1]}')
                feature_set.append(f'next_stemmed={porter_stemmer.stem(tokens[i + 1])}')
                feature_set.append(f'next_capitalized={tokens[i + 1][0].isupper()}')
                feature_set.append(f'next_token_length={len(tokens[i + 1])}')
                feature_set.append(f'next_contains_digit={any(char.isdigit() for char in tokens[i + 1])}')
            
            if i < len(tokens) - 2 and tokens[i + 2] and tokens[i + 1]:
                feature_set.append(f'two_after_word={tokens[i + 2]}')
                feature_set.append(f'two_after_POS={pos_tags[i + 2]}')
                feature_set.append(f'two_after_BIO={bio_tags[i + 2]}')
                feature_set.append(f'two_after_stemmed={porter_stemmer.stem(tokens[i + 2])}')
                feature_set.append(f'two_after_capitalized={tokens[i + 2][0].isupper()}')
                feature_set.append(f'two_after_token_length={len(tokens[i + 2])}')
                feature_set.append(f'two_after_contains_digit={any(char.isdigit() for char in tokens[i + 2])}')

            to_str = '\t'.join(feature_set)
            feature_strs.append(f'{tokens[i]}\t{to_str}\t{bio_tags[i]}')

    return feature_strs

def feature_values_development(tokens, pos_tags, response_file):
    feature_strs = []

    with open(response_file, 'r') as response_f:
        responses = response_f.readlines()

    for i, (token, pos_tag) in enumerate(zip(tokens, pos_tags)):
        if not token:
            feature_strs.append('')
        else:
            feature_set = []

            feature_set.append(f'POS={pos_tag}')
            feature_set.append(f'stemmed={porter_stemmer.stem(token)}')
            feature_set.append(f'capitalized={token[0].isupper()}')
            feature_set.append(f'token_length={len(token)}')
            feature_set.append(f'contains_digit={any(char.isdigit() for char in token)}')

            # Append the corresponding BIO tag from the model's response
            response_data = responses[i].strip().split('\t')
            bio_tag = response_data[-1]
            feature_set.append(f'BIO={bio_tag}')

            if i > 1 and tokens[i - 2] and tokens[i - 1]:
                # Add features for two words before
                feature_set.append(f'two_before_word={tokens[i - 2]}')
                feature_set.append(f'two_before_POS={pos_tags[i - 2]}')
                feature_set.append(f'two_before_stemmed={porter_stemmer.stem(tokens[i - 2])}')
                feature_set.append(f'two_before_capitalized={tokens[i - 2][0].isupper()}')
                feature_set.append(f'two_before_token_length={len(tokens[i - 2])}')
                feature_set.append(f'two_before_contains_digit={any(char.isdigit() for char in tokens[i - 2])}')

            if i > 0 and tokens[i - 1]:
                # Add features for the previous word
                feature_set.append(f'prev_word={tokens[i - 1]}')
                feature_set.append(f'prev_POS={pos_tags[i - 1]}')
                feature_set.append(f'prev_stemmed={porter_stemmer.stem(tokens[i - 1])}')
                feature_set.append(f'prev_capitalized={tokens[i - 1][0].isupper()}')
                feature_set.append(f'prev_token_length={len(tokens[i - 1])}')
                feature_set.append(f'prev_contains_digit={any(char.isdigit() for char in tokens[i - 1])}')

            if i < len(tokens) - 1 and tokens[i + 1]:
                # Add features for the next word
                feature_set.append(f'next_word={tokens[i + 1]}')
                feature_set.append(f'next_POS={pos_tags[i + 1]}')
                feature_set.append(f'next_stemmed={porter_stemmer.stem(tokens[i + 1])}')
                feature_set.append(f'next_capitalized={tokens[i + 1][0].isupper()}')
                feature_set.append(f'next_token_length={len(tokens[i + 1])}')
                feature_set.append(f'next_contains_digit={any(char.isdigit() for char in tokens[i + 1])}')

            if i < len(tokens) - 2 and tokens[i + 2] and tokens[i + 1]:
                # Add features for two words after
                feature_set.append(f'two_after_word={tokens[i + 2]}')
                feature_set.append(f'two_after_POS={pos_tags[i + 2]}')
                feature_set.append(f'two_after_stemmed={porter_stemmer.stem(tokens[i + 2])}')
                feature_set.append(f'two_after_capitalized={tokens[i + 2][0].isupper()}')
                feature_set.append(f'two_after_token_length={len(tokens[i + 2])}')
                feature_set.append(f'two_after_contains_digit={any(char.isdigit() for char in tokens[i + 2])}')

            to_str = '\t'.join(feature_set)
            feature_strs.append(f'{token}\t{to_str}')

    return feature_strs


def main():
    with open(TRAIN_FP, 'r') as f:
        tokens_train = []
        pos_tags_train = []
        bio_tags_train = []

        for line in f:
            text = line.strip()
            if not text:
                tokens_train.append('')
                pos_tags_train.append('')
                bio_tags_train.append('')
            else:
                data = text.split('\t')
                tokens_train.append(data[0])
                pos_tags_train.append(data[1])
                bio_tags_train.append(data[2])

    # Extract features from the training data
    features_train = feature_values_training(tokens_train, pos_tags_train, bio_tags_train)

    # Write training features to file
    with open(TRAIN_OUTPUT, 'w') as train_out:
        train_out.write('\n'.join(features_train))

    # Extract features from the test data (DEV_FP is now the test corpus)
    with open(DEV_FP, 'r') as dev_file:
        tokens_test = []
        pos_tags_test = []

        for line in dev_file:
            text = line.strip()
            if not text:
                tokens_test.append('')
                pos_tags_test.append('')
            else:
                data = text.split('\t')
                tokens_test.append(data[0])
                pos_tags_test.append(data[1])

    # Write test features to file (DEV_OUTPUT is now the test.feature file)
    #features_test = feature_values_development(tokens_test, pos_tags_test)
    
    features_test = feature_values_development(tokens_test, pos_tags_test, RESPONSE_FILE)

    
    with open(DEV_OUTPUT, 'w') as test_out:
        test_out.write('\n'.join(features_test))

    # Assuming you have already compiled the Java files as described in the instructions
    # Running MEtag.java to create the final response file (WSJ_23.chunk)
    os.system(f"java -cp .:maxent-3.0.0.jar:trove.jar MEtag {DEV_OUTPUT} model.chunk WSJ_23.chunk")

main()

