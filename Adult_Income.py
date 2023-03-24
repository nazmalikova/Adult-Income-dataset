#!/usr/bin/env python
# coding: utf-8

# # Adult Income Dataset

# In[1]:


import pandas as pd
import numpy as np


# 1. Сколько мужчин и женщин (признак sex) представлено в этом наборе данных?
# 
# 2. Каков средний возраст (признак age) женщин?
# 
# 3. Какова доля граждан Германии (признак native-country)?
# 
# 4-5. Каковы средние значения и среднеквадратичные отклонения возраста тех, кто получает более 50K в год (признак salary) и тех, кто получает менее 50K в год?
# 
# 6. Правда ли, что люди, которые получают больше 50k, имеют как минимум высшее образование? (признак education – Bachelors, Prof-school, Assoc-acdm, Assoc-voc, Masters или Doctorate)
# 
# 7. Выведите статистику возраста для каждой расы (признак race) и каждого пола. Используйте groupby и describe. Найдите таким образом максимальный возраст мужчин расы Amer-Indian-Eskimo.
# 
# 8. Среди кого больше доля зарабатывающих много (>50K): среди женатых или холостых мужчин (признак marital-status)? Женатыми считаем тех, у кого marital-status начинается с Married (Married-civ-spouse, Married-spouse-absent или Married-AF-spouse), остальных считаем холостыми.
# 
# 9. Какое максимальное число часов человек работает в неделю (признак hours-per-week)? Сколько людей работают такое количество часов и каков среди них процент зарабатывающих много?
# 
# 10. Посчитайте среднее время работы (hours-per-week) зарабатывающих мало и много (salary) для каждой страны (native-country).

# In[3]:


df = pd.read_csv('adult.csv')
df.head()


# In[122]:


print(df.shape[0])


# In[8]:


print(df.columns)


# In[10]:


print(df.info())


# In[11]:


df.describe()


# 1. Сколько мужчин и женщин (признак sex) представлено в этом наборе данных?
# Ответ: 32650 мужчин и 16192 женщин

# In[15]:


df.gender.value_counts()


# 2. Каков средний возраст (признак age) женщин?
# Ответ: 36.93
# 

# In[121]:


df[df['gender']=='Female'].age.mean()


# 3. Какова доля граждан Германии (признак native-country)?
# Ответ: 0.42%

# In[21]:


df['native-country'].value_counts(normalize=True)


# 4-5. Каковы средние значения и среднеквадратичные отклонения возраста тех, кто получает более 50K в год (признак salary) и тех, кто получает менее 50K в год?
# Ответ: <=50K : средние значения- 36.87 и среднеквадратичные отклонения - 14.10; >50K: средние значения- 44.28 и среднеквадратичные отклонения - 10.56

# In[31]:


df.income.value_counts()


# In[28]:


df.groupby(by=df['income'])['age'].mean()


# In[30]:


df.groupby(by=['income'])['age'].std()


# 6. Правда ли, что люди, которые получают больше 50k, имеют как минимум высшее образование? (признак education – Bachelors, Prof-school, Assoc-acdm, Assoc-voc, Masters или Doctorate)
# Ответ: нет, только 57.8% людей с зарплатой больше 50k имеют высшее образование

# In[34]:


pd.crosstab(df['income'],df['education'])


# In[51]:


df['high education'] = df['education'].isin(['Bachelors', 'Prof-school', 'Assoc-acdm', 'Assoc-voc', 'Masters', 'Doctorate'])
df[df['income']=='>50K']['high education'].value_counts(normalize=True)


# 7. Выведите статистику возраста для каждой расы (признак race) и каждого пола. Используйте groupby и describe. Найдите таким образом максимальный возраст мужчин расы Amer-Indian-Eskimo.
# Ответ: 82
# 

# In[69]:


df.groupby(by=['race','gender'])['age'].describe()


# In[76]:


df[(df['race']=='Amer-Indian-Eskimo') & (df['gender']=='Male')]['age'].max()


# 8. Среди кого больше доля зарабатывающих много (>50K): среди женатых или холостых мужчин (признак marital-status)? Женатыми считаем тех, у кого marital-status начинается с Married (Married-civ-spouse, Married-spouse-absent или Married-AF-spouse), остальных считаем холостыми.
# Ответ: Среди женатых - 89.9%
# 

# In[123]:


df['marital-status'].unique()


# In[78]:


df['married']=df['marital-status'].isin(['Married-civ-spouse', 'Married-spouse-absent', 'Married-AF-spouse'])
df['married'].value_counts()


# In[88]:


df[(df['gender']=='Male')&(df['income']=='>50K')]['married'].value_counts(normalize=True)


# 9. Какое максимальное число часов человек работает в неделю (признак hours-per-week)? Сколько людей работают такое количество часов и каков среди них процент зарабатывающих много?
# Ответ: Максимальное число часов человек работает в неделю - 99, 137 людей работают 99 часов, cреди них 29.9% зарабатывают много
# 
# 

# In[92]:


max_hours = df['hours-per-week'].max()
print('Максимальное число часов человек работает в неделю -', str(max_hours))


# In[124]:


print(df[df['hours-per-week']== max_hours].shape[0], 'людей работают', str(max_hours),'часов')


# In[126]:


share = df[(df['hours-per-week']== max_hours)&(df['income']=='>50K')].shape[0]/df[df['hours-per-week']== max_hours].shape[0] * 100
print('Среди них '+str(round(share,1))+'% зарабатывают много')


# 10. Посчитайте среднее время работы (hours-per-week) зарабатывающих мало и много (salary) для каждой страны (native-country).

# In[115]:


df.pivot_table(values='hours-per-week', index=['native-country'], columns=['income'], aggfunc = np.mean)


# In[ ]:




