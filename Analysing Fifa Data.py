#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


fifa= pd.read_excel('E:\\python\\fifa data of 2022.xlsx')


# ***CHECKING THE TYPE OF DATA WE HAVE TO DEAL WITH:***

# In[3]:


fifa.describe()   #used this function to see the statistical properties of the data


# In[4]:


fifa.info()


# In[5]:


fifa.shape     #to see how many columns and rows are we dealing with 


# In[6]:


fifa.columns   #used to see all the columns of the dataframe


# In[7]:


fifa['overall'].describe


# ***MAKING GRAPHS OF DIFFERENT COLUMNS:***

# In[8]:


fifa['overall'].mean()       #mean is the average of all players present


# ***MAKING A HISTOGRAM TO SEE THE OVERALL RANKING OF ALL THE PLAYERS IN FOOTBALL:***

# In[9]:


#making a histogram 
plt.hist(fifa['overall'], color = "lightblue", ec="red" , bins=[40,50,60,70,80,90,95], label='Ranking of fifa players 2022')
plt.title('Overall rankings')
plt.legend()
plt.xlabel('Overall Rankings')
plt.show()


# ***FINDING THE PERCENTAGE OF FOOT PREFERENCES OF FIFA PLAYERS WITH A PIECHART:***

# In[10]:


#making a pie chart of foot preferences of fifa players 
left=fifa.loc[fifa['preferred_foot']=='Left'].count()[0]
right=fifa.loc[fifa['preferred_foot']=='Right'].count()[0]
labels=['Left Foot','Right Foot']
colors=['#4F6272', '#B7C3F3']
plt.pie([left,right], labels=labels, colors=colors, autopct='%.2f%%',wedgeprops = { 'linewidth' : 3, 'edgecolor' : 'white' })
plt.title('Foot Preferences Of Fifa Players')
plt.show()


# ***FINDING THE PERCENTAGE OF TOTAL NUMBER OF PLAYERS PLAYING AT SPECIFIC POSITIONS IN FOOTBALL WITH A PIECHART:***

# In[11]:


#finding the total number of different positions in fifa2022
GK=fifa.loc[fifa['player_positions']=='GK'].count()[0]  #2132
ST=fifa.loc[fifa['player_positions']=='ST'].count()[0]  #1770
CB=fifa.loc[fifa['player_positions']=='CB'].count()[0]  #2423
print(GK,ST,CB)


# ***FINDING THE PERCENTAGE OF STRIKERS AND CENTER BACKS IN FOOTBALL WITH A PIECHART:***

# In[12]:


ST=fifa.loc[fifa['player_positions']=='ST'].count()[0]
CB=fifa.loc[fifa['player_positions']=='CB'].count()[0]

labels=['Strikers','Center backs']
colors=['#4F6272', '#B7C3F3', '#DD7596']
plt.title('Poistions Of Fifa Players')

plt.pie([ST,CB,], labels=labels ,  colors=colors,autopct='%.2f%%',wedgeprops = { 'linewidth' : 3, 'edgecolor' : 'white' })
plt.show()


# ***FINDING THE PERCENTAGE OF LEFT AND RIGHT WINGERS IN FOOTBALL WITH A PIE CHART:***

# In[13]:


RW=fifa.loc[fifa['player_positions']=='RW'].count()[0]
LW=fifa.loc[fifa['player_positions']=='LW'].count()[0]
colors=['#4F6272', '#B7C3F3']
labels=['Right Wing','Left Wing']
plt.title('Left And Right Wings Of Fifa Players 2022')
plt.pie([RW,LW], labels=labels, colors=colors, autopct='%.2f%%',wedgeprops = { 'linewidth' : 3, 'edgecolor' : 'white' })
plt.show()


# ***COMPARING THE BEST PLAYERS WITH EACHOTHER WITH THEIR OVERALL STRENGTHS BY A BOXPLOT:***

# In[14]:


#now comparing the best players with eachother
messi=fifa.loc[fifa['short_name']=='L. Messi']['overall']
ronaldo=fifa.loc[fifa['short_name']=='Cristiano Ronaldo']['overall']
neymar=fifa.loc[fifa['short_name']=='Neymar Jr']['overall']
labels=['Lional Messi', 'Christiano Ronaldo','Neymar']
colors=['grey', 'yellow']

boxes=plt.boxplot([messi,ronaldo,neymar], labels=labels)
plt.grid()
plt.title('Comparison Of Top Players Of fifa 2022')
plt.ylabel('Overall')
plt.show()



# ***COMPARING TOP CLUBS TO FIND THE STRONGEST AND THE PROBABILITY OF THE CLUB MORE LIKELY TO WIN WITH A BOXPLOT:***

# In[15]:


#comparing different clubs with eachother to find the strongest and the probability of the team which is more likely to win
barcelona= fifa.loc[fifa.club_name == 'FC Barcelona']['overall']
chelsea= fifa.loc[fifa.club_name == 'Chelsea']['overall']
city= fifa.loc[fifa.club_name == 'Manchester City']['overall']
psg= fifa.loc[fifa.club_name== 'Paris Saint-Germain']['overall']

labels=['FC Barcelona','Chelsea', 'Manchester City','PSG']
boxes=plt.boxplot([barcelona,chelsea,city,psg], labels=labels,patch_artist=True)
plt.title('Comparison Of Clubs')
for box in boxes['boxes']:
    box.set(color='#4286f4', linewidth=2)
    box.set(facecolor='#e0e0e0') #while using facecolor write patchartist=True while plotting

plt.show()


# ***CHECKING THE PERCENTAGE OF GOAL KEEPERS IN ALL THE PLAYERS PRESENT IN SOCCER:***

# In[16]:


#checking the percentage of goal keepers in fifa 2022 out of all positions
GK=fifa.loc[fifa['player_positions']=='GK'].count()[0]
ovall=fifa['player_positions'].count()
labels=['Goal Keepers', 'Other Positions']
colors=['#4F6272', '#B7C3F3', '#DD7596']
plt.title('Goal Keepers in Fifa 2022')

plt.pie([GK,ovall], labels=labels ,  colors=colors, autopct='%.2f%%',wedgeprops = { 'linewidth' : 3, 'edgecolor' : 'white' })
 
plt.show()


# ***FINDING THE AVERAGES OF BALL CONTROL OF TOP TEAMS:***

# In[17]:


#finding averages of ball control of top teams
city= fifa.loc[fifa.club_name == 'Manchester City']['skill_ball_control'].mean()
chelsea= fifa.loc[fifa['club_name'] == 'Chelsea']['skill_ball_control'].mean()
psg= fifa.loc[fifa['club_name'] == 'Paris Saint-Germain']['skill_ball_control'].mean()
realmadrid= fifa.loc[fifa['club_name'] == 'Real Madrid CF']['skill_ball_control'].mean()
Barcelona= fifa.loc[fifa['club_name'] == 'FC Barcelona']['skill_ball_control'].mean()
print(f'The average of ball control of Manchester City is: {city}')
print(f'The average of ball control of Chelsea is: {chelsea}')
print(f'The average of ball control of PSG is: {psg}')
print(f'The average of ball control of Real Madrid is: {realmadrid}')
print(f'The average of ball control of Fc Barcelona is: {Barcelona}')


# ***GRAPHING THE AVERAGES OF BALL CONTROL OF TOP TEAMS***

# In[18]:


#plotting the grapn of the averages of ball control of top teams 
city= fifa.loc[fifa.club_name == 'Manchester City']['skill_ball_control'].mean()
chelsea= fifa.loc[fifa['club_name'] == 'Chelsea']['skill_ball_control'].mean()
psg= fifa.loc[fifa['club_name'] == 'Paris Saint-Germain']['skill_ball_control'].mean()
realmadrid= fifa.loc[fifa['club_name'] == 'Real Madrid CF']['skill_ball_control'].mean()
Barcelona= fifa.loc[fifa['club_name'] == 'FC Barcelona']['skill_ball_control'].mean()

labels=['Manchester City','Chelsea','PSG','Real Madrid','Barcelona']
x=plt.plot([city,chelsea,psg,realmadrid,Barcelona],'ro', color='darkcyan', markersize=28)
plt.grid()
#plt.xlabel('Top Teams')
plt.ylabel('Averages Of Ball Control')
plt.xticks([0,1,2,3,4],['Man City','Chelsea','PSG','Real Madrid','Barcelona'])
plt.yticks([60,65,70,75,80,85])
plt.title('Averages Of Ball Control Of Top Teams')

plt.legend()
plt.show()


# ***FINDING THE WEAK FOOT AVERAGES OF TOP CLUBS:***

# In[19]:


#finding the weak foot averages of top teams
city= fifa.loc[fifa.club_name == 'Manchester City']['weak_foot'].mean()
chelsea= fifa.loc[fifa['club_name'] == 'Chelsea']['weak_foot'].mean()
psg= fifa.loc[fifa['club_name'] == 'Paris Saint-Germain']['weak_foot'].mean()
realmadrid= fifa.loc[fifa['club_name'] == 'Real Madrid CF']['weak_foot'].mean()
Barcelona= fifa.loc[fifa['club_name'] == 'FC Barcelona']['weak_foot'].mean()
print(f'The average of weak foot of Manchester City is: {city}')
print(f'The average of weak foot of Chelsea is: {chelsea}')
print(f'The average of weak foot of PSG is: {psg}')
print(f'The average of weak foot of Real Madrid is: {realmadrid}')
print(f'The average of weak foot of Fc Barcelona is: {Barcelona}')


# ***GRAPHING THE WEAK FOOT AVERAGES OF TOP CLUBS:***

# In[20]:


#Graphing the weak foot averages of top teams
city= fifa.loc[fifa.club_name == 'Manchester City']['weak_foot'].mean()
chelsea= fifa.loc[fifa['club_name'] == 'Chelsea']['weak_foot'].mean()
psg= fifa.loc[fifa['club_name'] == 'Paris Saint-Germain']['weak_foot'].mean()
realmadrid= fifa.loc[fifa['club_name'] == 'Real Madrid CF']['weak_foot'].mean()
Barcelona= fifa.loc[fifa['club_name'] == 'FC Barcelona']['weak_foot'].mean()
x=([city,chelsea,psg,realmadrid,Barcelona])
plt.title('Weak Foot Averages Of Top Teams')
labels=['Manchester City','Chelsea','PSG','Real Madrid','Barcelona']
x=plt.plot([city,chelsea,psg,realmadrid,Barcelona],'ro', color='deepskyblue', markersize=28)
plt.grid()
#plt.xlabel('Top Teams')
plt.ylabel('Averages Of Weak Foot')
plt.xticks([0,1,2,3,4],['Man City','Chelsea','PSG','Real Madrid','Barcelona'])
plt.yticks([2.5,3,3.5,4])

plt.legend()
plt.show()


# ***ENTER THE NAME OF THE PLAYER AND GET ALL HIS INFORMATION:***

# In[27]:


#getting all the information of every player 
a=input('''The name of the player is: ''')

name=fifa.loc[fifa['short_name']== a]['overall'].sum()
nationality=fifa.loc[fifa['short_name']== a]['nationality_name'].sum()
team=fifa.loc[fifa['short_name']== a]['club_name'].sum()
pos=fifa.loc[fifa['short_name']== a]['club_position'].sum()
weight=fifa.loc[fifa['short_name']== a]['weight_kg'].sum()
height=fifa.loc[fifa['short_name']== a]['height_cm'].sum()
foot=fifa.loc[fifa['short_name']== a]['preferred_foot'].sum()
skillm=fifa.loc[fifa['short_name']== a]['skill_moves'].sum()
shooting=fifa.loc[fifa['short_name']== a]['shooting'].sum()
spassing=fifa.loc[fifa['short_name']== a]['attacking_short_passing'].sum()
dribbling=fifa.loc[fifa['short_name']== a]['dribbling'].sum()
header=fifa.loc[fifa['short_name']== a]['attacking_heading_accuracy'].sum()
lpassing=fifa.loc[fifa['short_name']== a]['skill_long_passing'].sum()
ballcontrol=fifa.loc[fifa['short_name']== a]['skill_ball_control'].sum()
sprint=fifa.loc[fifa['short_name']== a]['movement_sprint_speed'].sum()
stamina=fifa.loc[fifa['short_name']== a]['power_stamina'].sum()
reaction=fifa.loc[fifa['short_name']== a]['movement_reactions'].sum()
jumping=fifa.loc[fifa['short_name']== a]['power_jumping'].sum()
longshots=fifa.loc[fifa['short_name']== a]['power_long_shots'].sum()
balance=fifa.loc[fifa['short_name']== a]['movement_balance'].sum()
weakfoot=fifa.loc[fifa['short_name']== a]['weak_foot'].sum()

print(f'The player has an overall strength of {name}/100')
print(f'his nationality is {nationality}')
print(f'his club is {team}')
print(f'his playing position in club is {pos}')
print(f'his weight is {weight}kgs')
print(f'his height is {height}cm')
print(f'his preffered foot is {foot}')
print(f'his skill moves level is {skillm}/10')
print(f'his shooting skills are {shooting}/100')
print(f'his short passing skills are {spassing}/100')
print(f'his dribbling skills are {dribbling}/100')   
print(f'his heading skills are {header}/100') 
print(f'his long passing skills are {lpassing}/100')
print(f'his ball control skills are {ballcontrol}/100')
print(f'his sprint speed is {sprint}/100')
print(f'his power stamina is {stamina}/100')
print(f'his reaction time is {reaction}/100')
print(f'his jumping skills are {jumping}/100')
print(f'his long shots power is {longshots}/100')
print(f'his movement balance is {balance}/100')
print(f'his weak foot skills are {weakfoot}/10')


# ***ENTER THE NAME OF THE PLAYER TO SEE ALL OF HIS STRENGTHS IN A GRAPH:***

# In[29]:


#ENTER THE NAME OF PLAYER TO SEE HIS DATA 
a=input('''The name of the player is: ''')

shooting=fifa.loc[fifa['short_name']== a]['shooting'].sum()
spassing=fifa.loc[fifa['short_name']== a]['attacking_short_passing'].sum()
dribbling=fifa.loc[fifa['short_name']== a]['dribbling'].sum()
lpassing=fifa.loc[fifa['short_name']== a]['skill_long_passing'].sum()
ballcontrol=fifa.loc[fifa['short_name']== a]['skill_ball_control'].sum()
sprint=fifa.loc[fifa['short_name']== a]['movement_sprint_speed'].sum()
stamina=fifa.loc[fifa['short_name']== a]['power_stamina'].sum()
reaction=fifa.loc[fifa['short_name']== a]['movement_reactions'].sum()
jumping=fifa.loc[fifa['short_name']== a]['power_jumping'].sum()
longshots=fifa.loc[fifa['short_name']== a]['power_long_shots'].sum()
balance=fifa.loc[fifa['short_name']== a]['movement_balance'].sum()

#GRAPHING THE DATA
plt.figure(figsize=(12, 4), dpi=500)
plt.plot([shooting,spassing,dribbling,lpassing,ballcontrol,sprint,stamina,reaction,jumping,longshots,balance], marker='o', color='darkturquoise',markersize=8, label=a)
plt.xticks([0,1,2,3,4,5,6,7,8,9,10],['Shoot','Short Pass','Dribble','Long Pass','Ball Control','Sprint','Stamina','Reaction','Jump','Longshot','Balance'])  
plt.yticks([50,60,70,80,90,100])
plt.title('Players Analysis')
plt.legend()
plt.grid()
plt.show()      







# ***COMPARISON OF MESSI AND RONALDO WITH GRAPH:***

# In[23]:


#COMPARISON GRAPHS
#-------------------------------------------------------------------------------------------------------------------

#data for messi
shooting=fifa.loc[fifa['short_name']== 'L. Messi']['shooting'].sum()
spassing=fifa.loc[fifa['short_name']== 'L. Messi']['attacking_short_passing'].sum()
dribbling=fifa.loc[fifa['short_name']== 'L. Messi']['dribbling'].sum()
lpassing=fifa.loc[fifa['short_name']=='L. Messi' ]['skill_long_passing'].sum()
ballcontrol=fifa.loc[fifa['short_name']== 'L. Messi']['skill_ball_control'].sum()
sprint=fifa.loc[fifa['short_name']== 'L. Messi']['movement_sprint_speed'].sum()
stamina=fifa.loc[fifa['short_name']== 'L. Messi']['power_stamina'].sum()
reaction=fifa.loc[fifa['short_name']== 'L. Messi']['movement_reactions'].sum()
jumping=fifa.loc[fifa['short_name']== 'L. Messi']['power_jumping'].sum()
longshots=fifa.loc[fifa['short_name']== 'L. Messi']['power_long_shots'].sum()
balance=fifa.loc[fifa['short_name']== 'L. Messi']['movement_balance'].sum()

#plotting the data
plt.figure(figsize=(12, 4), dpi=500)
plt.plot([shooting,spassing,dribbling,lpassing,ballcontrol,sprint,stamina,reaction,jumping,longshots,balance], label='Lional Messi', marker='o', color='darkturquoise',markersize=8)

y=[0,20,40,60,80,100]


#-----------------------------------------------------------------------------------------------------------------------
#data for ronaldo
shooting2=fifa.loc[fifa['short_name']== 'Cristiano Ronaldo']['shooting'].sum()
spassing2=fifa.loc[fifa['short_name']== 'Cristiano Ronaldo']['attacking_short_passing'].sum()
dribbling2=fifa.loc[fifa['short_name']== 'Cristiano Ronaldo']['dribbling'].sum()
lpassing2=fifa.loc[fifa['short_name']=='Cristiano Ronaldo' ]['skill_long_passing'].sum()
ballcontrol2=fifa.loc[fifa['short_name']== 'Cristiano Ronaldo']['skill_ball_control'].sum()
sprint2=fifa.loc[fifa['short_name']== 'Cristiano Ronaldo']['movement_sprint_speed'].sum()
stamina2=fifa.loc[fifa['short_name']== 'Cristiano Ronaldo']['power_stamina'].sum()
reaction2=fifa.loc[fifa['short_name']== 'Cristiano Ronaldo']['movement_reactions'].sum()
jumping2=fifa.loc[fifa['short_name']== 'Cristiano Ronaldo']['power_jumping'].sum()
longshots2=fifa.loc[fifa['short_name']== 'Cristiano Ronaldo']['power_long_shots'].sum()
balance2=fifa.loc[fifa['short_name']== 'Cristiano Ronaldo']['movement_balance'].sum()

#plotting the data
plt.plot([shooting2,spassing2,dribbling2,lpassing2,ballcontrol2,sprint2,stamina2,reaction2,jumping2,longshots2,balance2], label='Christiano Ronaldo',marker='o', color='peru', markersize=8)


#----------------------------------------------------------------------------------------------------------------------------
plt.xticks([0,1,2,3,4,5,6,7,8,9,10],['Shoot','Short Pass','Dribble','Long Pass','Ball Control','Sprint','Stamina','Reaction','Jump','Longshot','Balance'])  
plt.yticks([50,60,70,80,90,100])
plt.title('Comparison Of Players')
plt.legend()
plt.grid()
plt.show()      


# ***WRITE THE NAME OF THE PLAYER WHOM YOU WANT TO COMPARE WITH THE TOP 2 PLAYERS:***

# In[31]:


#data for messi
shooting=fifa.loc[fifa['short_name']== 'L. Messi']['shooting'].sum()
spassing=fifa.loc[fifa['short_name']== 'L. Messi']['attacking_short_passing'].sum()
dribbling=fifa.loc[fifa['short_name']== 'L. Messi']['dribbling'].sum()
lpassing=fifa.loc[fifa['short_name']=='L. Messi' ]['skill_long_passing'].sum()
ballcontrol=fifa.loc[fifa['short_name']== 'L. Messi']['skill_ball_control'].sum()
sprint=fifa.loc[fifa['short_name']== 'L. Messi']['movement_sprint_speed'].sum()
stamina=fifa.loc[fifa['short_name']== 'L. Messi']['power_stamina'].sum()
reaction=fifa.loc[fifa['short_name']== 'L. Messi']['movement_reactions'].sum()
jumping=fifa.loc[fifa['short_name']== 'L. Messi']['power_jumping'].sum()
longshots=fifa.loc[fifa['short_name']== 'L. Messi']['power_long_shots'].sum()
balance=fifa.loc[fifa['short_name']== 'L. Messi']['movement_balance'].sum()

#plotting the data
plt.figure(figsize=(12, 4), dpi=500)
plt.plot([shooting,spassing,dribbling,lpassing,ballcontrol,sprint,stamina,reaction,jumping,longshots,balance], label='Lional Messi', marker='o', color='darkturquoise',markersize=8)

y=[0,20,40,60,80,100]
#-----------------------------------------------------------------------------------------------------------------------
#data for ronaldo
shooting2=fifa.loc[fifa['short_name']== 'Cristiano Ronaldo']['shooting'].sum()
spassing2=fifa.loc[fifa['short_name']== 'Cristiano Ronaldo']['attacking_short_passing'].sum()
dribbling2=fifa.loc[fifa['short_name']== 'Cristiano Ronaldo']['dribbling'].sum()
lpassing2=fifa.loc[fifa['short_name']=='Cristiano Ronaldo' ]['skill_long_passing'].sum()
ballcontrol2=fifa.loc[fifa['short_name']== 'Cristiano Ronaldo']['skill_ball_control'].sum()
sprint2=fifa.loc[fifa['short_name']== 'Cristiano Ronaldo']['movement_sprint_speed'].sum()
stamina2=fifa.loc[fifa['short_name']== 'Cristiano Ronaldo']['power_stamina'].sum()
reaction2=fifa.loc[fifa['short_name']== 'Cristiano Ronaldo']['movement_reactions'].sum()
jumping2=fifa.loc[fifa['short_name']== 'Cristiano Ronaldo']['power_jumping'].sum()
longshots2=fifa.loc[fifa['short_name']== 'Cristiano Ronaldo']['power_long_shots'].sum()
balance2=fifa.loc[fifa['short_name']== 'Cristiano Ronaldo']['movement_balance'].sum()

#plotting the data
plt.plot([shooting2,spassing2,dribbling2,lpassing2,ballcontrol2,sprint2,stamina2,reaction2,jumping2,longshots2,balance2], label='Christiano Ronaldo',marker='o', color='peru', markersize=8)
#--------------------------------------------------------------------------------------------------------------------------
#adding a graph of your own player
a=input('''The name of the player is: ''')
#name=fifa.loc[fifa['short_name']== a]['overall'].sum()
#weight=fifa.loc[fifa['short_name']== a]['weight_kg'].sum()
#height=fifa.loc[fifa['short_name']== a]['height_cm'].sum()
#skillm=fifa.loc[fifa['short_name']== a]['skill_moves'].sum()
shooting3=fifa.loc[fifa['short_name']== a]['shooting'].sum()
spassing3=fifa.loc[fifa['short_name']== a]['attacking_short_passing'].sum()
dribbling3=fifa.loc[fifa['short_name']== a]['dribbling'].sum()
lpassing3=fifa.loc[fifa['short_name']== a]['skill_long_passing'].sum()
ballcontrol3=fifa.loc[fifa['short_name']== a]['skill_ball_control'].sum()
sprint3=fifa.loc[fifa['short_name']== a]['movement_sprint_speed'].sum()
stamina3=fifa.loc[fifa['short_name']== a]['power_stamina'].sum()
reaction3=fifa.loc[fifa['short_name']== a]['movement_reactions'].sum()
jumping3=fifa.loc[fifa['short_name']== a]['power_jumping'].sum()
longshots3=fifa.loc[fifa['short_name']== a]['power_long_shots'].sum()
balance3=fifa.loc[fifa['short_name']== a]['movement_balance'].sum()
#weakfoot=fifa.loc[fifa['short_name']== a]['weak_foot'].sum()
#plt.figure(figsize=(12, 4), dpi=500)
plt.plot([shooting3,spassing3,dribbling3,lpassing3,ballcontrol3,sprint3,stamina3,reaction3,jumping3,longshots3,balance3], marker='o', color='salmon',markersize=8, label=a)

#----------------------------------------------------------------------------------------------------------------------------
plt.xticks([0,1,2,3,4,5,6,7,8,9,10],['Shoot','Short Pass','Dribble','Long Pass','Ball Control','Sprint','Stamina','Reaction','Jump','Longshot','Balance'])  
plt.yticks([50,60,70,80,90,100])
plt.title('Comparison Of Players')
plt.legend()
plt.grid()
plt.show()      


# ***WRITE THE NAME OF THE PLAYERS WHOM YOU WANT TO COMPARE:***

# In[33]:


#Comparing 2 players
a=input('''The name of the player is: ''')

shooting3=fifa.loc[fifa['short_name']== a]['shooting'].sum()
spassing3=fifa.loc[fifa['short_name']== a]['attacking_short_passing'].sum()
dribbling3=fifa.loc[fifa['short_name']== a]['dribbling'].sum()
lpassing3=fifa.loc[fifa['short_name']== a]['skill_long_passing'].sum()
ballcontrol3=fifa.loc[fifa['short_name']== a]['skill_ball_control'].sum()
sprint3=fifa.loc[fifa['short_name']== a]['movement_sprint_speed'].sum()
stamina3=fifa.loc[fifa['short_name']== a]['power_stamina'].sum()
reaction3=fifa.loc[fifa['short_name']== a]['movement_reactions'].sum()
jumping3=fifa.loc[fifa['short_name']== a]['power_jumping'].sum()
longshots3=fifa.loc[fifa['short_name']== a]['power_long_shots'].sum()
balance3=fifa.loc[fifa['short_name']== a]['movement_balance'].sum()

plt.figure(figsize=(12, 4), dpi=500)
plt.plot([shooting3,spassing3,dribbling3,lpassing3,ballcontrol3,sprint3,stamina3,reaction3,jumping3,longshots3,balance3], marker='o', color='teal',markersize=8, label=a)

#-----------------------------------------------------------------------------------------
b=input('''The name of the player is: ''')

shooting4=fifa.loc[fifa['short_name']== b]['shooting'].sum()
spassing4=fifa.loc[fifa['short_name']== b]['attacking_short_passing'].sum()
dribbling4=fifa.loc[fifa['short_name']== b]['dribbling'].sum()
lpassing4=fifa.loc[fifa['short_name']== b]['skill_long_passing'].sum()
ballcontrol4=fifa.loc[fifa['short_name']== b]['skill_ball_control'].sum()
sprint4=fifa.loc[fifa['short_name']== b]['movement_sprint_speed'].sum()
stamina4=fifa.loc[fifa['short_name']== b]['power_stamina'].sum()
reaction4=fifa.loc[fifa['short_name']== b]['movement_reactions'].sum()
jumping4=fifa.loc[fifa['short_name']== b]['power_jumping'].sum()
longshots4=fifa.loc[fifa['short_name']== b]['power_long_shots'].sum()
balance4=fifa.loc[fifa['short_name']== b]['movement_balance'].sum()

plt.plot([shooting4,spassing4,dribbling4,lpassing4,ballcontrol4,sprint4,stamina4,reaction4,jumping4,longshots4,balance4], marker='o', color='peru',markersize=8, label=b)

#-----------------------------------------------------------------------------------------------------
plt.xticks([0,1,2,3,4,5,6,7,8,9,10],['Shoot','Short Pass','Dribble','Long Pass','Ball Control','Sprint','Stamina','Reaction','Jump','Longshot','Balance'])  
plt.yticks([50,60,70,80,90,100])
plt.title('Comparison Of Players')
plt.legend()
plt.grid()
plt.show()      


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




