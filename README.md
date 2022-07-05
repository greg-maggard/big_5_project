# Big 5 Personality Clustering Project
By: Greg Maggard

## Introduction:
This project intends to use K-Means clustering to identify potential personality groupings that may be found in user responses to a personality metric, which is based on the [Big 5 Personality Model](https://en.wikipedia.org/wiki/Big_Five_personality_traits). This online assessment, hosted by the Open-Source Psychometrics Project can be found [here](https://openpsychometrics.org/tests/IPIP-BFFM/).


### The Data:
This dataset was acquired from Kaggle, and can be found [here](https://www.kaggle.com/datasets/tunguz/big-five-personality-test).

The [Big 5 Personality Questionnaire](https://openpsychometrics.org/tests/IPIP-BFFM/), as presented on the Open-Source Pscyhometrics Project site, asks its users 50 questions, with 10 questions each dedicated to the following categories:
- Openness (OPN)
- Conscientiousness (CSN)
- Extroversion (EXT)
- Agreeableness (AGR)
- Emotional Stability (EST) 
    - *Note: This verbiage refers to the metric more commonly titled "Neuroticism." This project will therefore refer to 'emotional stability' as 'neuroticism.'

## Wrangling:

### Wrangling Takeaways:
1. The data was acquired from a CSV of around 1M responses found on Kaggle. 
2. Columns containing metadata about user, includings things like how long it took the user to select each answer, their computer screen size, and their estimated latitudinal/longitudinal location were eliminated. 
3. Responses that contained either null values or '0.0', indicating no response, were eliminated. 
4. For the sake of data integrity, responses that came from non-unique IP addresses were eliminated. This was a fairly large chunk of the data, but left 603,322 responses in place for analysis.
5. Since clustering is an unsupervised machine learning process, no train/validate/test split is necessary.

## Exploration:
#### Questions Considered:
- How are each of these questions answered on average, and what does the average person's result from this questionnaire look like? 
- Are these metrics related to one another - is being high in one associated with being low in another?

#### Key Exploration Summary and Takeaways:
- Reverse coded questions, highlighted in <span style='color:purple'>purple</span>, do appear to have inverse distributions to the regularly-coded questions. This would seem to indicate that they are for the most part measuring a similar trait.
- The average responded proved to be lower in extroversion and neuroticism, slightly higher in conscientiousness and agreeableness, and highest in openness to experience. 

## Modeling:
### Modeling Takeaways:
- Feature engineering proved helpful, reducing the number of features down from 50 to 5, and significantly improving the model's ability to delineate between clusters. 
- There appear to be 5 fairly distinct groupings of personality types within the data from the Big 5 questionnaire. 

## Conclusion:
Throughout the course of this project, it was interesting to see the relationships between different aspects of the questionnaire. Naturally, it was expected to find similarities or differences between combinations of the overall metrics. However, potentially just as interested was the finding that there were even differences in the correlations between questions on the same metric, indicating that perhaps the questions were not all adequately measuring the same thing.

The K-Means clustering algorithm showed that, rather appropriately, there are potentially five personality groupings that are revealed by the Big 5 personality test. Although clustering does not allow us to make predictions in the way that a supervised machine learning model might, it does provide some visibility into how we might categorize personality types according to Big 5 data.

##Going Forward/Ideas For Next Steps:
Given more time, I would like to continue to refine this project. 
- These groupings are not easily labeled, although it may ultimately prove worthwhile to try to find the average response across the multiple metrics for each cluster, and try to manually label each personality grouping based on those findings. 
- It would be interesting to try to build in some functionality that would allow an individual to provide answers to the questionnaire, and immediately see the cluster to which the model thinks they should be assigned. 
- If time and resources were no object, I would love to do something similar with another personality test, perhaps the MBTI, and see how those already-defined personality classifications correlate with the clusters provided by this model. 
- I would also love to look into the reliability and validity of the test itself. My background in Psychology left me with the knowledge that the BIg 5 is one of the more trustworthy personality metrics, yet it was interesting to see that some of the questions even within the same metric did not appear to correlate with one another as one might think they should. 

# Data Dictionary
- Note: This data dictionary is heavily borrowed from the data dictionary included with the original dataset, which is the file named ['codebook.txt'](https://github.com/greg-maggard/big_5_project/blob/main/codebook.txt) in this repository.

### Extroversion:
- EXT1:	I am the life of the party.
- EXT2:	I don't talk a lot.
- EXT3:	I feel comfortable around people.
- EXT4:	Ikeep in the background.
- EXT5:	I start conversations.
- EXT6:	I have little to say.
- EXT7:	I talk to a lot of different people at parties.
- EXT8:	I don't like to draw attention to myself.
- EXT9:	I don't mind being the center of attention.
- EXT10:	I am quiet around strangers.

### Neuroticism ('Emotional Stability'):
- EST1:	I get stressed out easily.
- EST2:	I am relaxed most of the time.
- EST3:	I worry about things.
- EST4:	I seldom feel blue.
- EST5:	I am easily disturbed.
- EST6:	I get upset easily.
- EST7:	I change my mood a lot.
- EST8:	I have frequent mood swings.
- EST9:	I get irritated easily.
- EST10:	I often feel blue.

### Agreeableness:
- AGR1:	I feel little concern for others.
- AGR2:	I am interested in people.
- AGR3:	I insult people.
- AGR4:	I sympathize with others' feelings.
- AGR5:	I am not interested in other people's problems.
- AGR6:	I have a soft heart.
- AGR7:	I am not really interested in others.
- AGR8:	I take time out for others.
- AGR9:	I feel others' emotions.
- AGR10:	I make people feel at ease.

### Conscientiousness:
- CSN1:	I am always prepared.
- CSN2:	I leave my belongings around.
- CSN3:	I pay attention to details.
- CSN4:	I make a mess of things.
- CSN5:	I get chores done right away.
- CSN6:	I often forget to put things back in their proper place.
- CSN7:	I like order.
- CSN8:	I shirk my duties.
- CSN9:	I follow a schedule.
- CSN10:	I am exacting in my work.

### Openness:
- OPN1:	I have a rich vocabulary.
- OPN2:	I have difficulty understanding abstract ideas.
- OPN3:	I have a vivid imagination.
- OPN4:	I am not interested in abstract ideas.
- OPN5:	I have excellent ideas.
- OPN6:	I do not have a good imagination.
- OPN7:	I am quick to understand things.
- OPN8:	I use difficult words.
- OPN9:	I spend time reflecting on things.
- OPN10:	I am full of ideas.
