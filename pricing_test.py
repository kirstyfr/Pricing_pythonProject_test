import pandas as pd
columns = ['Transaction unique identifier',
           'Price',
           'Date of Transfer',
           'Postcode',
           'Property Type',
           'Old/New',
           'Duration',
           'PAON',
           'SAON',
           'Street',
           'Locality',
           'Town/City',
           'District',
           'Country',
           'PPD Category Type',
           'Record Status - monthly file only']
df = pd.read_csv("February_2024_data_dups.txt", delimiter=",",names=columns)

#import subprocess
#subprocess.check_call(["pip", "install", "tabulate"])
#from tabulate import tabulate

# Create new Property ID
df[columns]=df[columns].fillna("")

df['Property_ID']=df['Postcode']+df['PAON']+df['SAON']+df['Street']+df['Town/City']+df['District']+df['Country']
df['Property_Entry_Count'] = df.groupby('Property_ID')['Property_ID'].transform('count')
df = df.sort_values(by=['Property_ID', 'Property_Entry_Count','Date of Transfer'],ascending=True)

p_type_dict = { 'D' : 'Detached',
                'S' : 'Semi-Detached',
                'T' : 'Terraced',
                'F' : 'Flats/Maisonettes',
                'O' : 'Other'}

old_new_dict = {'Y' : 'a newly built property',
                'N' : 'an established residential building'
}

duration_dict = {'F' : 'Freehold',
                 'L' : 'Leasehold'
}

PPD_dict = {'A' : 'Standard Price Paid entry',
            'B' : 'Additional Price Paid entry including transfers under a power of sale/repossessions'
}

record_dict = {
    'A' : 'Addition',
    'C' : 'Change',
    'D' : 'Delete'
}

df['Property Type']=df['Property Type'].map(p_type_dict)
df['Old/New']=df['Old/New'].map(old_new_dict)
df['Duration']=df['Duration'].map(duration_dict)
df['PPD Category Type']=df['PPD Category Type'].map(PPD_dict)
df['Record Status - monthly file only']=df['Record Status - monthly file only'].map(record_dict)

print(df.head(10).to_markdown())
#print(df.dtypes)


