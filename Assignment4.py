
# coding: utf-8

# # Assignment 4
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# This assignment requires that you to find **at least** two datasets on the web which are related, and that you visualize these datasets to answer a question with the broad topic of **economic activity or measures** (see below) for the region of **Dubai, Dubai, United Arab Emirates**, or **United Arab Emirates** more broadly.
# 
# You can merge these datasets with data from different regions if you like! For instance, you might want to compare **Dubai, Dubai, United Arab Emirates** to Ann Arbor, USA. In that case at least one source file must be about **Dubai, Dubai, United Arab Emirates**.
# 
# You are welcome to choose datasets at your discretion, but keep in mind **they will be shared with your peers**, so choose appropriate datasets. Sensitive, confidential, illicit, and proprietary materials are not good choices for datasets for this assignment. You are welcome to upload datasets of your own as well, and link to them using a third party repository such as github, bitbucket, pastebin, etc. Please be aware of the Coursera terms of service with respect to intellectual property.
# 
# Also, you are welcome to preserve data in its original language, but for the purposes of grading you should provide english translations. You are welcome to provide multiple visuals in different languages if you would like!
# 
# As this assignment is for the whole course, you must incorporate principles discussed in the first week, such as having as high data-ink ratio (Tufte) and aligning with Cairo’s principles of truth, beauty, function, and insight.
# 
# Here are the assignment instructions:
# 
#  * State the region and the domain category that your data sets are about (e.g., **Dubai, Dubai, United Arab Emirates** and **economic activity or measures**).
#  * You must state a question about the domain category and region that you identified as being interesting.
#  * You must provide at least two links to available datasets. These could be links to files such as CSV or Excel files, or links to websites which might have data in tabular form, such as Wikipedia pages.
#  * You must upload an image which addresses the research question you stated. In addition to addressing the question, this visual should follow Cairo's principles of truthfulness, functionality, beauty, and insightfulness.
#  * You must contribute a short (1-2 paragraph) written justification of how your visualization addresses your stated research question.
# 
# What do we mean by **economic activity or measures**?  For this category you might look at the inputs or outputs to the given economy, or major changes in the economy compared to other regions.
# 
# ## Tips
# * Wikipedia is an excellent source of data, and I strongly encourage you to explore it for new data sources.
# * Many governments run open data initiatives at the city, region, and country levels, and these are wonderful resources for localized data sources.
# * Several international agencies, such as the [United Nations](http://data.un.org/), the [World Bank](http://data.worldbank.org/), the [Global Open Data Index](http://index.okfn.org/place/) are other great places to look for data.
# * This assignment requires you to convert and clean datafiles. Check out the discussion forums for tips on how to do this from various sources, and share your successes with your fellow students!
# 
# ## Example
# Looking for an example? Here's what our course assistant put together for the **Ann Arbor, MI, USA** area using **sports and athletics** as the topic. [Example Solution File](./readonly/Assignment4_example.pdf)

# In[1]:

get_ipython().magic('matplotlib notebook')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# In[ ]:

def pick_data(a):
    b=pd.read_excel(a,'Data',skiprows = 3,na_values="...",parse_cols="A:D,AS:BI")
    return b
ARE=pick_data('API_ARE_DS2_en_excel_v2.xls')
IND=pick_data('API_IND_DS2_en_excel_v2.xls')
ARE_GDP=ARE[ARE['Indicator Code']=='NY.GDP.MKTP.KD.ZG']
ARE_GDP
IND_GDP=IND[IND['Indicator Code']=='NY.GDP.MKTP.KD.ZG']
IND_GDP
GDP=ARE_GDP.append(IND_GDP,ignore_index=False)
GDP=GDP.drop(['Country Code','Indicator Name','Indicator Code'],axis=1)
GDP=GDP.set_index('Country Name')
GDP.loc['United Arab Emirates']
plt.figure()

plt.plot(GDP.loc['United Arab Emirates'])
plt.plot(GDP.loc['India'])
plt.tick_params(left='off',bottom='off')
for spine in plt.gca().spines.values():
    spine.set_visible(False)
plt.legend(frameon=False,loc=4)
vals=plt.gca().get_yticks()
plt.gca().set_yticklabels(['{:3.2f}%'.format(x) for x in vals])
plt.title('GDP growth% INDIA vs UAE (2000-2016)')
plt.savefig('GDP growth% INDIA vs UAE (2000-2016)')



# In[ ]:



