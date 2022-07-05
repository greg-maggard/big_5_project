import pandas as pd
import numpy as np
import matplotlib as plt

# Creating dictionaries that list the question IDs in columns as keys, with their corresponding text as values:

extroversion = {"EXT1" : "I am the life of the party.",
"EXT2" : "I don't talk a lot.",
"EXT3" : "I feel comfortable around people.",
"EXT4" : "I keep in the background.",
"EXT5" : "I start conversations.",
"EXT6" : "I have little to say.",
"EXT7" : "I talk to a lot of different people at parties.",
"EXT8" : "I don't like to draw attention to myself.",
"EXT9" : "I don't mind being the center of attention.",
"EXT10" : "I am quiet around strangers."}

neuroticism = {"EST1" : "I get stressed out easily.",
"EST2" : "I am relaxed most of the time.",
"EST3" : "I worry about things.",
"EST4" : "I seldom feel blue.",
"EST5" : "I am easily disturbed.",
"EST6" : "I get upset easily.",
"EST7" : "I change my mood a lot.",
"EST8" : "I have frequent mood swings.",
"EST9" : "I get irritated easily.",
"EST10" : "I often feel blue."}

agreeableness = {"AGR1" : "I feel little concern for others.",
"AGR2" : "I am interested in people.",
"AGR3" : "I insult people.",
"AGR4" : "I sympathize with others' feelings.",
"AGR5" : "I am not interested in other people's problems.",
"AGR6" : "I have a soft heart.",
"AGR7" : "I am not really interested in others.",
"AGR8" : "I take time out for others.",
"AGR9" : "I feel others' emotions.",
"AGR10" : "I make people feel at ease."}
           
conscientiousness = {"CSN1" : "I am always prepared.",
"CSN2" : "I leave my belongings around.",
"CSN3" : "I pay attention to details.",
"CSN4" : "I make a mess of things.",
"CSN5" : "I get chores done right away.",
"CSN6" : "I often forget to put things back in their proper place.",
"CSN7" : "I like order.",
"CSN8" : "I shirk my duties.",
"CSN9" : "I follow a schedule.",
"CSN10" : "I am exacting in my work."}

openness = {"OPN1" : "I have a rich vocabulary.",
"OPN2" : "I have difficulty understanding abstract ideas.",
"OPN3" : "I have a vivid imagination.",
"OPN4" : "I am not interested in abstract ideas.",
"OPN5" : "I have excellent ideas.",
"OPN6" : "I do not have a good imagination.",
"OPN7" : "I am quick to understand things.",
"OPN8" : "I use difficult words.",
"OPN9" : "I spend time reflecting on things.",
"OPN10" : "I am full of ideas."}

##Graphing Mean Score of Each Category:

def metric_means(df):

    '''
    Calculates the mean value for each of the metrics, across the dataset. 
    Returns a DataFrame of the metrics and their corresponding mean values. 
    '''

    #Calculating mean openness:
    mean_openness = 0
    for i in openness.keys():
        mean_openness += df[i].mean()

    #Calculating mean conscientiousness:
    mean_conscientiousness = 0
    for i in conscientiousness.keys():
        mean_conscientiousness += df[i].mean()

    #Calculating mean extroversion:
    mean_extroversion = 0
    for i in extroversion.keys():
        mean_extroversion += df[i].mean()
        
    #Calculating mean agreeableness:    
    mean_agreeableness = 0
    for i in agreeableness.keys():
        mean_agreeableness += df[i].mean()

    #Calculating mean neuroticism:
    mean_neuroticism = 0
    for i in neuroticism.keys():
        mean_neuroticism += df[i].mean()

    ##Creating DataFrame of Metric Means:
    # Creating List of Metrics:
    metric_names = ['openness', 'conscientiousness','extroversion', 'agreeableness', 'neuroticism']
    #Creating list of metric means:
    metric_means = [mean_openness, mean_conscientiousness, mean_extroversion, mean_agreeableness, mean_neuroticism]
    #Creating empty DataFrame object:
    metric_means_df = pd.DataFrame()
    #Creating column of metric names from list:
    metric_means_df['metric_names'] = pd.DataFrame(metric_names)
    #Creatgin column of metric means from list:
    metric_means_df['means'] = metric_means

    return metric_means_df

#Creating a function that will undo reverse-scoring for better visibility in correlation:
def undo_reverse_scoring(df):

    # Identifying which questions are reverse-coded:
    reverse_coded = ["EXT2","EXT4","EXT6","EXT8","EXT10","EST2","EST4","AGR1","AGR3","AGR5","AGR7","CSN2","CSN4","CSN6","CSN8","OPN2","OPN4","OPN6"]

    '''
    Takes in the DataFrame of Big 5 responses. 
    Subtracts all values in reverse-coded columns from 6 (1 higher than their max) in order to flip the values, then writes over those values 
    to effectively undo the reverse-coding. 
    Return dataframe with reverse-coding removed for better visibility in correlation plot.
    '''
    df[reverse_coded] = 6 - df[reverse_coded]
    return df