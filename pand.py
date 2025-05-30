import pandas as pd
# print(pd.__version__)


di={"name":["def","man","don"],"roll no":[1,2,3]}
li=[("name",10),("hit",22)]
f=pd.DataFrame([{'A': 1, 'B': 2}, {'A': 3, 'B': 4}])
df=pd.DataFrame(li)
print(df)

d=pd.read_csv("D:\\jagadeesh\\powerautomate\\files\\covid_india.csv")
df=pd.DataFrame(d)



#  Data Inspection & Exploration
a=df.head(10)
b=df.tail(10)
c=df.describe()
c=df.info()
print(df.columns)
print(df.dtypes)
print(df.memory_usage())
print(df.shape)
e=df[0:10:2]
f=df["Deaths"]
f=df[['Name of State / UT', 'Active Cases']]
f=df[['Name of State / UT', 'Active Cases']][0:10:2]
for j in df.iterrows():
    print(j)
    print("----------------------")


# # Indexing
# f=df.set_index("Degree")
f=df.reset_index()
f=df.sort_index()
f=df.sort_values('Active Cases')
df.columns.name= "fields"
# df.index.name= "row_id"
# print(f)
# pd.set_option('display.max_columns', None)
# print(df)



# Aggregation & Grouping
data = {
    'department': ['HR', 'HR', 'IT', 'IT', 'Sales', 'Sales'],
    'employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'salary': [50000, 55000, 70000, 72000, 40000, 42000]
}

df = pd.DataFrame(data)
a=df.groupby('department')['salary'].mean()
a=df.groupby('department')['salary'].sum()
a=df.groupby('department')['salary'].agg(['min', 'max', 'mean'])
a=df.groupby(['department', 'employee'])['salary'].sum()
a=df.groupby('department').agg(
    total_salary=('salary', 'sum'),
    avg_salary=('salary', 'mean'),
    employee_count=('employee', 'count')
)
a=df['avg_dept_salary'] = df.groupby('department')['salary'].transform('nunique')

print(a)



# Aggregation & Grouping
df1 = pd.DataFrame({'id': [1, 2], 'name': ['Alice', 'Bob']})
df2 = pd.DataFrame({'id': [1, 3], 'salary': [50000, 70000]})

df=pd.merge(df1, df2, on='id', how='inner')
df=pd.merge(df1, df2, on='id', how='right')
print(df)
df1=pd.DataFrame({"name":["ram","jon"]},index=[1,2])
df2=pd.DataFrame({"salary":[2000,5000]},index=[1,2])
d=df1.join(df2)
d=pd.concat([df1, df2], axis=1)

print(d) 


# Pivot Tables && crosstab
data = {
    'Department': ['HR', 'HR', 'IT', 'IT', 'Finance', 'Finance'],
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Gender':['Male','Male','Female','Male','Female','Male'],
    'Salary': [50000, 60000, 70000, 80000, 90000, 100000],
    'Year': [2023, 2024, 2023, 2024, 2023, 2024]
}

df = pd.DataFrame(data)
pivot = df.pivot_table(values='Salary', index='Department', columns='Year', aggfunc='mean')
cross= pd.crosstab(df['Gender'],df['Department'])
print(cross)


d=pd.read_csv("D:\\jagadeesh\\powerautomate\\files\\covid_india.csv")
df=pd.DataFrame(d)

# loc
f=df.loc[1]
f=df.loc[3,['Active Cases','Deaths']]
f=df.loc[1:10:2]
f=df.loc[2:12,'Deaths']
f=df.loc[5:16,['Name of State / UT','Active Cases']]
f=df.loc[df['Deaths']<400]
print(f)

# iloc
f=df.iloc[3,5]
f=df.iloc[1:13,2:5]
f=df.iloc[:,[1,3,5]]
f=df.iloc[[1,3,5],[1,4]]

# sorting
f=df.sort_values('Deaths')
f=df.sort_values(['Active Cases','Deaths'])

f=df['death_perc']=df['Deaths'] / df['Total Confirmed cases'] *100
f=df.drop(columns='death_perc',inplace=True)

f=df.duplicated()
f=df.fillna(000)
f=df.drop_duplicates()
f=df.dropna()
print(f)

# exporting
df.to_csv("D:\\jagadeesh\\powerautomate\\files\\covid_india.csv",index=False)