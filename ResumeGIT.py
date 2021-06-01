#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 10:55:30 2021

@author: aleksanderbielinski
"""


Header = 'This is Python Generated CV'
Name = 'Aleksander Bielinski'
Title = 'MSc Financial Technology Student'
Address = 'Glasgow, Scotland,\nwww.linkedin.com/in/AleksanderBiel\nhttps://github.com/AleksanderB-hub'
Educationhead = 'Education'
Eduone = 'MSc Financial Technology'
Eduonetime = '2020-Present'
Eduonemodules = 'Programming For Financial Technology (79%)\nBecoming an Effective Financial Technology Analyst (75%)\nBig Data Fundamentals (80%), Data Analytics (82%)\nFundamentals of Machine Learning for Data Analytics (78%)\nStochastic Modelling For Analytics (74%)'
Edutwo = 'BSc Economics and Finance (First Class Honorous)'
Edutwotime = '2017-2020'
Edutwomodules = 'Equity and Fixed Income Valuation (82%)\nInvestment and Portfolio Management (92%)\nFinancial Econometrics (89%)\nInternational Financial Derivatives (97%)\nDevelopments in Advanced Microeconomics (87%)'

Experienceoneheader = 'Work Experience'
Jobone = 'Line Cook- Grounded Kitchen Limited'
jobonetime = 'August 2019- August 2020'
jobonedesc = '-Being part of expanding business, offering my help and expertise\n-Working in a fast-paced work environment'
jobtwo = 'Food Delivery Person- Deliveroo'
jobtwotime = 'August 2018 - October 2019'
jobtwodesc = '-Competent at planning and making delivery schedules\n and adhering to them\n-Researching the food market to ensure that the best income\n streams are continously accessed' 
jobthree = 'Front of House- Peter Pizzeria Leicester'
jobthreetime ='September 2017 - January 2019'
jobthreedesc = '-Offering excellent customer service, being responsible for bookings\n-Working as a part of a team and supporting the traning of new staff\n members\n-Responsible for the cash register balancing\n-Dealing with customer complainds and enquires in a proffessional\n manner'

SkillsHeader = 'Skills'
SkillsDesc = '-Python (Pandas, NumPy,\n Sci-kit Learn, Matplotlib,\n Seaborn)\n-Data Visualization\n-Data Cleaning\n-Solidity (Smart Conctracts)\n-R (Hadleyverse Packages,\n Bayesian Beleif Netowrks)\n-NetLogo\n (Agent Based Moddeling)\n-Excel (Datasets,\n Pivot Tables),\n-Bloomberg Terminal\n (Data Analysis,\n Equity Screening,\n Time-Series Visualisation)\n-MS Office (Advanced)'
ExtrasTitle = 'Societies &\nTranning Courses'
extraone = '-DMU Stock Exchange Society\n (Beign able to discuss\n investtment oppurtunities and\n economic conditions with minds\n alike)'
extratwo = '-Ampify Boot Camp Simulation\n (Experience the realities of\n working in the industry from\n the perspective os asset\n manager, investment bank and\n hedge fund , learned the role of\n psyhology in trading)'

Certificationshead = 'Certificates'
certificatedesc = '-Bloomber Market Concepts\n (BMC)\n -Level 4 Diploma in Trading &\n Financial Market Analysis'

languageshead = 'Languages'
languagesdesc = ' Polish (Native), English (Fluent),\n French (Basic)'
Interestshead = 'Interests'
interestslist = ' Stock Market, Blokchain,\n FinTech, Cooking'

import matplotlib.pyplot as plt 
#%matplotlib inline

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'Verdana'
fig, ax = plt.subplots(figsize = (9,11),edgecolor='blue')




ax.axvline(x=0.5, ymin=0, ymax=1, color='#007ACC', alpha=0.0, linewidth=50)
plt.axvline(x=.99, color='#003dcc', alpha=0.5, linewidth=300)
plt.axhline(y=.88, xmin=0, xmax=1, color='#ffffff', linewidth=3)

ax.set_facecolor('white')

plt.axis('off')

plt.annotate(Header, (.02,.98), weight='regular', fontsize=7, alpha=.3)
plt.annotate(Name, (.02,.94), weight='bold', fontsize=20)
plt.annotate(Title, (.02,.91), weight='regular', fontsize=14)
plt.annotate(Address, (.700,.920), weight='regular', fontsize=8, color='#ffffff')

plt.annotate(Educationhead, (.02,.86), weight='bold', fontsize=12, color='#003dcc')
plt.annotate(Eduone, (.02,.832), weight='bold', fontsize=10)
plt.annotate(Eduonetime, (.02,.81), weight='regular', fontsize=9, alpha=.6)
plt.annotate(Eduonemodules, (.04,.72), weight='regular', fontsize=9)
plt.annotate(Edutwo, (.02,.69), weight='bold', fontsize=10)
plt.annotate(Edutwotime, (.02,.667), weight='regular', fontsize=9, alpha=.6)
plt.annotate(Edutwomodules, (.04,.58), weight='regular', fontsize=9)

plt.annotate(Experienceoneheader, (.02,.54), weight='bold', fontsize=12, color='#003dcc')
plt.annotate(Jobone, (.02,.508), weight='bold', fontsize=10)
plt.annotate(jobonetime, (.02,.485), weight='regular', fontsize=9, alpha=.6)
plt.annotate(jobonedesc, (.04,.445), weight='regular', fontsize=9)
plt.annotate(jobtwo, (.02,.41), weight='bold', fontsize=10)
plt.annotate(jobtwotime, (.02,.39), weight='regular', fontsize=9, alpha=.6)
plt.annotate(jobtwodesc, (.04,.316), weight='regular', fontsize=9)
plt.annotate(jobthree, (.02,.280), weight='bold', fontsize=10)
plt.annotate(jobthreetime, (.02,.263), weight='regular', fontsize=9, alpha=.6)
plt.annotate(jobthreedesc, (.04,.15), weight='regular', fontsize=9)

plt.annotate(SkillsHeader, (.7,.85), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(SkillsDesc, (.7,.55), weight='regular', fontsize=9, color='#ffffff')

plt.annotate(Certificationshead, (.7,.52), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(certificatedesc, (.7,.45), weight='regular', fontsize=9, color='#ffffff')

plt.annotate(ExtrasTitle, (.7,.40), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(extraone, (.7,.31), weight='regular', fontsize=9, color='#ffffff')
plt.annotate(extratwo, (.7,.187), weight='regular', fontsize=9, color='#ffffff')

plt.annotate(languageshead, (.7,.16), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(languagesdesc, (.7,.125), weight='regular', fontsize=9, color='#ffffff')

plt.annotate(Interestshead, (.7,.10), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(interestslist, (.7,.066), weight='regular', fontsize=9, color='#ffffff')


#plt.savefig('AleksanderBielinskiCV.png', dpi=300, bbox_inches='tight')
