# Noun Group Tagger

## Description

Develop a Noun Group tagger, focusing on feature selection rather than the algorithm. 

## Files
- WSJ_CHUNKFILES.zip: Includes training, development, test, and answer key files.
- MAX_ENT_files.zip: Contains necessary Java files and scripts for running the MaxEnt trainer and classifier.

## Steps

- Create a program to process the input files and generate feature-value pairs for the MaxEnt trainer and classifier. Create training.feature from WSJ_02-21.pos-chunk. Create test.feature from WSJ_24.pos.
- Compile and run MEtrain.java with the training feature file as input to produce a MaxEnt model. Use maxent-3.0.0.jar and trove.jar in the classpath.
- Use MEtag to generate system output from the test feature file and the generated model.
- Score the results using score.chunk.py.
- Create a test.feature file from WSJ_23.pos and repeat step 3 to produce the final response file (WSJ_23.chunk).

## Features and Format

- Each line of features corresponds to a line in the input file.
- Features are tab-separated values with the token (word, punctuation, etc.) as the first field.
- Features may include POS, word itself, stemmed version, features of previous/following words, sentence beginning/ending indicators, capitalization, etc.
- For the training file, the last field should be the BIO tag (B-NP, I-NP, or O).
- Evalution: (1) Accuracy is measured based on correct BIO tags. (2) Precision, Recall, and F-measure assess Noun Group performance. (3) Grades are assigned based on F-measure, with specific thresholds for points.
