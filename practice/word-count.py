
countries = ['Brazil', 'USA', 'Canada', 'India', 'United Kingdom', 'France', 'Germany', 'United States', 'Ireland'];

# Count the country which name starts with I
#  Print all the country in list which starts with I

count = 0
i_country = []
for country in countries:
    if country.startswith('I'):
        count+=1
        i_country.append(country)

print(f"Total country:- {count}", end=' ')
print(i_country)
