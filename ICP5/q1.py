import pandas as pd

train_df = pd.read_csv('./train.csv')

#train_df = train_df.drop(['Ticket', 'Cabin'], axis=1)

#train_df['Survived'].replace(['female','male'],[0,1],inplace=True)

#train_df['Survived'] = train_df['Survived'].apply({'male':1, 'female':0}.get)

train_df['Sex'] = train_df['Sex'].map( {'female': 1, 'male': 0} ).astype(int)


#print(train_df['Sex'])


print(train_df['Survived'].corr(train_df['Sex']))