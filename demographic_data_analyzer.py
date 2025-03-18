import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race = pd.Series(df['race'])
    race_count = race.value_counts()

    # What is the average age of men?
    age_men = df.loc[df['sex'] == 'Male', 'age']
    average_age_men = round(age_men.mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    degree = df['education'].value_counts()
    degreedf = pd.DataFrame(degree)
    total_degrees = degreedf['education'].sum()
    degreedf['percentage'] = (degreedf['education'] / total_degrees) * 100
    percentage_bachelors = round(degreedf.loc['Bachelors', 'percentage'], 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    phe_list = [degreedf.loc['Bachelors', 'percentage'], degreedf.loc['Masters', 'percentage'], degreedf.loc['Doctorate', 'percentage']]
    higher_education = round(sum(phe_list), 1)
    lower_education = round((100 - sum(phe_list)), 1)

    # percentage with salary >50K
    #hsdf = df.loc[df['salary'] == '>50K']
    ad_val = ['Bachelors', 'Masters', 'Doctorate']
    addf = df.loc[df['education'].isin(ad_val)]
    adv = addf['salary'].value_counts()
    adsdf = pd.DataFrame(adv)
    total_ads = adsdf['salary'].sum()
    adsdf['percentage'] = (adsdf['salary'] / total_ads) * 100
    higher_education_rich = round(adsdf.loc['>50K', 'percentage'], 1)

    ad_val = ['Bachelors', 'Masters', 'Doctorate']
    naddf = df.loc[~df['education'].isin(ad_val)]
    nadv = naddf['salary'].value_counts()
    nadsdf = pd.DataFrame(nadv)
    total_nads = nadsdf['salary'].sum()
    nadsdf['percentage'] = (nadsdf['salary'] / total_nads) * 100
    lower_education_rich = round(nadsdf.loc['>50K', 'percentage'], 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    hv = df['hours-per-week'].value_counts()
    hdf = pd.DataFrame(hv)
    total_h = hdf['hours-per-week'].sum()
    hdf['percentage'] = (hdf['hours-per-week'] / total_h) * 100
    num_min_workers = round(hdf.loc[min_work_hours, 'percentage'], 1)

    mh = df['hours-per-week'].min()
    mhdf = df.loc[df['hours-per-week'] == mh]
    mhv = mhdf['salary'].value_counts()
    mhsdf = pd.DataFrame(mhv)
    total_mhs = mhsdf['salary'].sum()
    mhsdf['percentage'] = (mhsdf['salary'] / total_mhs) * 100
    rich_percentage = round(mhsdf.loc['>50K', 'percentage'], 1)

    # What country has the highest percentage of people that earn >50K?
    csv = df.groupby('native-country')['salary'].value_counts(normalize=True)
    csvhs = csv.loc[slice(None), '>50K']
    csvhse = csvhs.max()
    csvhsl = csvhs[csvhs == csvhse].index.tolist()
    highest_earning_country = csvhsl[0].replace('-', ' ')
    highest_earning_country_percentage = round(csvhse*100, 1)

    # Identify the most popular occupation for those who earn >50K in India.
    hsdf = df.loc[df['salary'] == '>50K']
    hsidf = hsdf.loc[hsdf['native-country'] == 'India']
    hsiov = hsidf['occupation'].value_counts()
    hsio_max = hsiov.max()
    hsio = hsiov[hsiov == hsio_max].index.tolist()
    top_IN_occupation = hsio[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

# Note 1: the "min" operations was implemented with insight from the following webpage: https://www.w3schools.com/python/pandas/ref_df_min.asp
# Note 2: the 'index.tolist()' option was adapted from results to the following Google search: https://www.google.com/search?q=python+pandas+retrieving+index+for+item+in+series&sca_esv=45c41d3e543101a5&sxsrf=AHTn8zqaC0AtJ4RQvmlbLG-immXj1nAsEw%3A1742324999628&ei=B8XZZ62AJrDcwN4PyPmOsQw&ved=0ahUKEwjtn761qpSMAxUwLtAFHci8I8YQ4dUDCBA&uact=5&oq=python+pandas+retrieving+index+for+item+in+series&gs_lp=Egxnd3Mtd2l6LXNlcnAiMXB5dGhvbiBwYW5kYXMgcmV0cmlldmluZyBpbmRleCBmb3IgaXRlbSBpbiBzZXJpZXMyCBAhGKABGMMEMggQIRigARjDBEi_BlDgAViDBHABeAGQAQCYAY8BoAHvAqoBAzAuM7gBA8gBAPgBAZgCA6AC6wHCAgoQABiwAxjWBBhHwgIKECEYoAEYwwQYCpgDAIgGAZAGCJIHAzEuMqAHmQ6yBwMwLjK4B-cB&sclient=gws-wiz-serp
# Note 3: the '.groupby()' option was adapted from results to the following Google search: https://www.google.com/search?q=python+pandas+getting+percentages+of+values+in+column+grouped+by+values+in+a+different+column&sca_esv=45c41d3e543101a5&sxsrf=AHTn8zqHVH_34fnitzR0ghfHPgwWr6cOVw%3A1742324200793&ei=6MHZZ-SGMNPdwN4Pye_GsQY&ved=0ahUKEwjkmsm4p5SMAxXTLtAFHcm3MWYQ4dUDCBA&uact=5&oq=python+pandas+getting+percentages+of+values+in+column+grouped+by+values+in+a+different+column&gs_lp=Egxnd3Mtd2l6LXNlcnAiXXB5dGhvbiBwYW5kYXMgZ2V0dGluZyBwZXJjZW50YWdlcyBvZiB2YWx1ZXMgaW4gY29sdW1uIGdyb3VwZWQgYnkgdmFsdWVzIGluIGEgZGlmZmVyZW50IGNvbHVtbkgAUABYAHAAeACQAQCYAQCgAQCqAQC4AQPIAQCYAgCgAgCYAwCSBwCgBwCyBwC4BwA&sclient=gws-wiz-serp
# Note 4: incorporation of the 'slice(None)' argument in a '.loc()' option was adapted from results to the following Google search: https://www.google.com/search?q=python+pandas+accessing+specific+subindices+from+all+indicies+in+a+series&sca_esv=45c41d3e543101a5&sxsrf=AHTn8zo_sdDZnSjRJQb9onxA7BXowXNOjw%3A1742329075643&ei=89TZZ4aBJ5fKp84PxoSD4Q8&ved=0ahUKEwjGxorNuZSMAxUX5ckDHUbCIPwQ4dUDCBA&uact=5&oq=python+pandas+accessing+specific+subindices+from+all+indicies+in+a+series&gs_lp=Egxnd3Mtd2l6LXNlcnAiSXB5dGhvbiBwYW5kYXMgYWNjZXNzaW5nIHNwZWNpZmljIHN1YmluZGljZXMgZnJvbSBhbGwgaW5kaWNpZXMgaW4gYSBzZXJpZXNIoo8BUABYxY0BcAB4AZABAZgB7QKgAZcXqgEINi4xMC4yLjK4AQPIAQD4AQGYAgCgAgCYAwCSBwCgB_UqsgcAuAcA&sclient=gws-wiz-serp
# Note 5: the '.isin()' option included within a '.loc()' option was adapted from results to the following Google search: https://www.google.com/search?q=python+pandas+selecting+all+rows+with+one+of+several+values+in+a+column&sca_esv=45c41d3e543101a5&sxsrf=AHTn8zoLSVna5AXbfKvZrfnxM4UGRVVryg%3A1742330715038&source=hp&ei=W9vZZ-gJpLnQ8Q-uy6-wCQ&iflsig=ACkRmUkAAAAAZ9npa10UtrCyhA-ddfj2yUACocHFsjKP&ved=0ahUKEwioo-Xav5SMAxWkHDQIHa7lC5YQ4dUDCBo&uact=5&oq=python+pandas+selecting+all+rows+with+one+of+several+values+in+a+column&gs_lp=Egdnd3Mtd2l6IkdweXRob24gcGFuZGFzIHNlbGVjdGluZyBhbGwgcm93cyB3aXRoIG9uZSBvZiBzZXZlcmFsIHZhbHVlcyBpbiBhIGNvbHVtbjIFECEYoAEyBRAhGKABMgUQIRigATIFECEYoAEyBRAhGKsCMgUQIRirAkjongFQAFjPnAFwCXgAkAEAmAHSAaABmzqqAQcxMC40OC4yuAEDyAEA-AEBmAJFoALzO8ICChAjGIAEGCcYigXCAgQQIxgnwgIKEAAYgAQYQxiKBcICCxAAGIAEGJECGIoFwgIQEAAYgAQYsQMYQxiDARiKBcICDRAAGIAEGLEDGEMYigXCAg4QABiABBiRAhixAxiKBcICCBAAGIAEGLEDwgIQEAAYgAQYsQMYgwEYFBiHAsICBRAAGIAEwgIHEAAYgAQYDcICBhAAGA0YHsICCBAAGAgYDRgewgILEAAYgAQYhgMYigXCAggQABiiBBiJBcICBRAAGO8FwgIGEAAYFhgewgIIEAAYgAQYogTCAggQABgWGAoYHsICBRAhGJ8FmAMA4gMFEgExIECSBwcxOS40OC4yoAfeggSyBwcxMC40OC4yuAfWOw&sclient=gws-wiz
