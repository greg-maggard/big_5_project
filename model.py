import pandas as pd
import numpy as np


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

def metric_condensation(df):
    #Isolating column names for openness:
    openness_questions = openness.keys()
    #Isolating column names for conscientiousness:
    conscientiousness_questions = conscientiousness.keys()
    #Isolating column names for extroversion:
    extroversion_questions = extroversion.keys()
    #Isolating column names for agreeableness:
    agreeableness_questions = agreeableness.keys()
    #Isolating column names for neuroticism:
    neuroticism_questions = neuroticism.keys()

    #Creating empty DataFrame objet for metric totals:
    metric_totals_df = pd.DataFrame()
    #Creating column for individual openness scores:
    metric_totals_df['openness'] = df[openness_questions].sum(axis = 1)
    #Creating column for individual conscientiousness scores:
    metric_totals_df['conscientiousness'] = df[conscientiousness_questions].sum(axis = 1)
    #Creating column for individual extroversion scores:
    metric_totals_df['extroversion'] = df[extroversion_questions].sum(axis = 1)
    #Creating column for individual agreeableness scores:
    metric_totals_df['agreeableness'] = df[agreeableness_questions].sum(axis = 1)
    #Creating column for individual neuroticism scores:
    metric_totals_df['neuroticism'] = df[neuroticism_questions].sum(axis = 1)
    return metric_totals_df