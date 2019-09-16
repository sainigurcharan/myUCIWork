```python
# importing the pandas library
import pandas as pd
```


```python
# setting up the csv path and import to data frame
filePath = "Resources/purchase_data.csv"
mainDF = pd.read_csv(filePath)
mainDF.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase ID</th>
      <th>SN</th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Lisim78</td>
      <td>20</td>
      <td>Male</td>
      <td>108</td>
      <td>Extraction, Quickblade Of Trembling Hands</td>
      <td>3.53</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Lisovynya38</td>
      <td>40</td>
      <td>Male</td>
      <td>143</td>
      <td>Frenzied Scimitar</td>
      <td>1.56</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Ithergue48</td>
      <td>24</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>4.88</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Chamassasya86</td>
      <td>24</td>
      <td>Male</td>
      <td>100</td>
      <td>Blindscythe</td>
      <td>3.27</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Iskosia90</td>
      <td>23</td>
      <td>Male</td>
      <td>131</td>
      <td>Fury</td>
      <td>1.44</td>
    </tr>
  </tbody>
</table>
</div>



# Players Count

* Total Number of Players


```python
uniquePlayer = mainDF["SN"].nunique()
#print("Total Number of Players: " + str(uniquePlayer))
totPlayerDF = pd.DataFrame({
    "Total Players": [uniquePlayer]},
    columns= ["Total Players"])
totPlayerDF.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>576</td>
    </tr>
  </tbody>
</table>
</div>



# Purchasing Analysis (Total)

* Number of Unique Items
* Average Purchase Price
* Total Number of Purchases
* Total Revenue


```python
uniqueTotalItems = mainDF['Item ID'].nunique()
totPurchase = mainDF['Price'].count()
totRevenue = mainDF["Price"].sum()
avgprice = (totRevenue/totPurchase).round(2)
colName = ["Number of Unique Items", "Average Purchase Price", "Number of Purchases", "Total Revenue"]

# presenting data into Purchasing Analysis data frame to present
purchaseAnalysisDF = pd.DataFrame({"Number of Unique Items": [uniqueTotalItems], 
                              "Average Purchase Price": [avgprice],
                             "Number of Purchases": [totPurchase],
                             "Total Revenue": [totRevenue]},
                              columns=colName)
# format the float columns
purchaseAnalysisDF.style.format({
    "Average Purchase Price": "${:.2f}",
    "Total Revenue": "${:.2f}"})
purchaseAnalysisDF.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Number of Unique Items</th>
      <th>Average Purchase Price</th>
      <th>Number of Purchases</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>183</td>
      <td>3.05</td>
      <td>780</td>
      <td>2379.77</td>
    </tr>
  </tbody>
</table>
</div>



# Gender Demographics

* Percentage and Count of Male Players
* Percentage and Count of Female Players
* Percentage and Count of Other / Non-Disclosed


```python
totPlayer = mainDF["SN"].nunique()
genderMale = mainDF[mainDF["Gender"] == "Male"]["SN"].nunique()
genderFemale = mainDF[mainDF["Gender"] == "Female"]["SN"].nunique()
#genderOther = mainDF[mainDF["Gender"] == "Other / Non-Disclosed"].nunique()
genderOther = totPlayer - (genderMale + genderFemale)
genderMalePerc = ((genderMale/totPlayer)*100)
genderFemalePerc = ((genderFemale/totPlayer)*100)
genderOtherPerc = ((genderOther/totPlayer)*100)
colName = ["Gender", "Total Count", "Percentage of Players"]

# presenting data into Gender Demographics data frame to present
genderDemographicDF = pd.DataFrame({
    "Gender": ["Male", "Female", "Other/ Non-Disclosed"],
    "Total Count": [genderMale, genderFemale, genderOther],
    "Percentage of Players": [genderMalePerc, genderFemalePerc, genderOtherPerc]},
    columns = colName)
# format the float columns
genderDemographicDF = genderDemographicDF.set_index("Gender")
genderDemographicDF.style.format({
    "Total Count": "{:.0f}",
    "Percentage of Players": "{:.2f}%"
})
genderDemographicDF.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Count</th>
      <th>Percentage of Players</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>484</td>
      <td>84.027778</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>81</td>
      <td>14.062500</td>
    </tr>
    <tr>
      <th>Other/ Non-Disclosed</th>
      <td>11</td>
      <td>1.909722</td>
    </tr>
  </tbody>
</table>
</div>



# Purchasing Analysis (Gender)

* The below each broken by gender

    * Purchase Count
    * Average Purchase Price
    * Total Purchase Value
    * Average Purchase Total per Person by Gender


```python
totMalePurchase = mainDF[mainDF["Gender"] == "Male"]["Price"].count()
totFemalePurchase = mainDF[mainDF["Gender"] == "Female"]["Price"].count()
# 'totPurchase' from Purchasing Analysis data above
totOtherPurchase = totPurchase - (totMalePurchase + totFemalePurchase)
malePriceAvg = mainDF[mainDF["Gender"] == "Male"]['Price'].mean()
femalePriceAvg = mainDF[mainDF["Gender"] == "Female"]['Price'].mean()
otherPriceAvg = mainDF[mainDF["Gender"] == "Other / Non-Disclosed"]['Price'].mean()
malePriceTot = mainDF[mainDF["Gender"] == "Male"]['Price'].sum()
femalePriceTot = mainDF[mainDF["Gender"] == "Female"]['Price'].sum()
otherPriceTot = mainDF[mainDF["Gender"] == "Other / Non-Disclosed"]['Price'].sum()
# 'genderMale', 'genderFemale', 'genderOther' from Gender Demographic data above
maleAvgPurchaseTot = malePriceTot/genderMale
femaleAvgPurchaseTot = femalePriceTot/genderFemale
otherAvgPurchaseTot = otherPriceTot/genderOther
colName = ["Gender", "Purchase Count", "Average Purchase Price", "Total Purchase Value", "Avg Purchase Total PP By Gender"]

# presenting data into Purchasing Analysis (Gender) data frame to present
genderPurchaseAnalysisDF = pd.DataFrame({
    "Gender": ["Female", "Male", "Other / Non-Disclosed"], 
    "Purchase Count": [totFemalePurchase, totMalePurchase, totOtherPurchase],
    "Average Purchase Price": [femalePriceAvg, malePriceAvg, otherPriceAvg], 
    "Total Purchase Value": [femalePriceTot, malePriceTot, otherPriceTot],
    "Avg Purchase Total PP By Gender": [femaleAvgPurchaseTot, maleAvgPurchaseTot, otherAvgPurchaseTot]},
    columns = colName)
# format the float columns                                        
genderPurchaseAnalysisDF = genderPurchaseAnalysisDF.set_index("Gender")
genderPurchaseAnalysisDF.style.format({
    "Average Purchase Price": "${:.2f}", 
    "Total Purchase Value": "${:.2f}", 
    "Avg Purchase Total PP By Gender": "${:.2f}"})
genderPurchaseAnalysisDF.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Avg Purchase Total PP By Gender</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>113</td>
      <td>3.203009</td>
      <td>361.94</td>
      <td>4.468395</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>652</td>
      <td>3.017853</td>
      <td>1967.64</td>
      <td>4.065372</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>15</td>
      <td>3.346000</td>
      <td>50.19</td>
      <td>4.562727</td>
    </tr>
  </tbody>
</table>
</div>



# Age Demographics

* The below each broken into bins of 4 years (i.e. <10, 10-14, 15-19, etc.)


```python
ageDemographicBin = [0, 9.99, 14.99, 19.99, 24.99, 29.99, 34.99, 39.99, 99999]
ageDemographicLabel = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

# applying the bin ranges on age
mainDF["Age Range"] = pd.cut(x=mainDF["Age"], bins=ageDemographicBin, labels=ageDemographicLabel)

# total count of each age bin and percentage
totCountAgeDemographic = mainDF["Age Range"].value_counts()
ageDemographicPerc = ((totCountAgeDemographic / uniquePlayer) * 100).round(2)

ageDemographicDF = pd.DataFrame({
    "Total Count": totCountAgeDemographic,
    "Percentage of Players": ageDemographicPerc})

ageDemographicDF = ageDemographicDF.sort_index()
# format the float columns
ageDemographicDF.style.format({
    "Percentage of Players": "{:.2f}%"})
ageDemographicDF.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Count</th>
      <th>Percentage of Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>23</td>
      <td>3.99</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>28</td>
      <td>4.86</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>136</td>
      <td>23.61</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>365</td>
      <td>63.37</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>101</td>
      <td>17.53</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>73</td>
      <td>12.67</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>41</td>
      <td>7.12</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>13</td>
      <td>2.26</td>
    </tr>
  </tbody>
</table>
</div>



# Age Demographics (Purchase Analysis)

* The below each broken into bins of 4 years (i.e. <10, 10-14, 15-19, etc.)

    * Purchase Count
    * Average Purchase Price
    * Total Purchase Value
    * Average Purchase Total per Person by Age Group


```python
# group by the age range
ageGroupByDF = mainDF.groupby(["Age Range"])
#ageGroupByDF.head()
```


```python
# getting the values: purchase count, average purchase price, total purchase value, average purchase total pp
purchaseCount = ageGroupByDF["Purchase ID"].count()
avgPurchasePrice = ageGroupByDF["Price"].mean()
totPurchaseValue = ageGroupByDF["Price"].sum()
totAgeCount = ageGroupByDF["SN"].nunique()
avgPurchasePricePP = totPurchaseValue/totAgeCount

# create data frame for the above values for Age Purchase Analysis
ageDemographicAnalysisDF = pd.DataFrame({"Purchase Count": purchaseCount,
                                 "Average Purchase Price": avgPurchasePrice,
                                 "Total Purchase Value":totPurchaseValue,
                                 "Average Purchase Total Per Person": avgPurchasePricePP})

# format the float columns
ageDemographicAnalysisDF.style.format({"Average Purchase Price":"${:,.2f}",
                               "Total Purchase Value":"${:,.2f}",
                               "Average Purchase Total Per Person":"${:,.2f}"})
ageDemographicAnalysisDF.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Average Purchase Total Per Person</th>
    </tr>
    <tr>
      <th>Age Range</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>23</td>
      <td>3.353478</td>
      <td>77.13</td>
      <td>4.537059</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>28</td>
      <td>2.956429</td>
      <td>82.78</td>
      <td>3.762727</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>136</td>
      <td>3.035956</td>
      <td>412.89</td>
      <td>3.858785</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>365</td>
      <td>3.052219</td>
      <td>1114.06</td>
      <td>4.318062</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>101</td>
      <td>2.900990</td>
      <td>293.00</td>
      <td>3.805195</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>73</td>
      <td>2.931507</td>
      <td>214.00</td>
      <td>4.115385</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>41</td>
      <td>3.601707</td>
      <td>147.67</td>
      <td>4.763548</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>13</td>
      <td>2.941538</td>
      <td>38.24</td>
      <td>3.186667</td>
    </tr>
  </tbody>
</table>
</div>



# Top Spenders

* Identify the the top 5 spenders in the game by total purchase value, then list (in a table):

    * SN
    * Purchase Count
    * Average Purchase Price
    * Total Purchase Value


```python
# group by the player name
playerGroupByDF = mainDF.groupby(["SN"])
#playerGroupByDF.head()
```


```python
# getting the values: Purchase Count, Average Purchase Price, Total Purchase Value
purchaseCount = playerGroupByDF["Purchase ID"].count()
avgPurchasePrice = playerGroupByDF["Price"].mean()
totalPurchaseValue = playerGroupByDF["Price"].sum()

# create data frame for the above values for Total Spenders
totalSpendersDF = pd.DataFrame({"Purchase Count": purchaseCount,
                             "Average Purchase Price": avgPurchasePrice,
                             "Total Purchase Value":totalPurchaseValue})

# top five spenders from the descending order list
totalSpendersDF = totalSpendersDF.sort_values(["Total Purchase Value"], ascending=False).head()
# format the float columns
totalSpendersDF.style.format({
    "Average Purchase Price":"${:,.2f}",
    "Total Purchase Value":"${:,.2f}"})
totalSpendersDF.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Lisosia93</th>
      <td>5</td>
      <td>3.792000</td>
      <td>18.96</td>
    </tr>
    <tr>
      <th>Idastidru52</th>
      <td>4</td>
      <td>3.862500</td>
      <td>15.45</td>
    </tr>
    <tr>
      <th>Chamjask73</th>
      <td>3</td>
      <td>4.610000</td>
      <td>13.83</td>
    </tr>
    <tr>
      <th>Iral74</th>
      <td>4</td>
      <td>3.405000</td>
      <td>13.62</td>
    </tr>
    <tr>
      <th>Iskadarya95</th>
      <td>3</td>
      <td>4.366667</td>
      <td>13.10</td>
    </tr>
  </tbody>
</table>
</div>



# Most Popular Items

* Identify the 5 most popular items by purchase count, then list (in a table):

    * Item ID
    * Item Name
    * Purchase Count
    * Item Price
    * Total Purchase Value


```python
# get data frame for the items and group by on Item ID and Item Name
itemsDF = mainDF[["Item ID", "Item Name", "Price"]].groupby(["Item ID", "Item Name"])
totItemPurchaseCount = itemsDF["Price"].count()
totItemPurchaseValue = itemsDF["Price"].sum()
perItemPrice = totItemPurchaseValue/totItemPurchaseCount

itemsDF = pd.DataFrame({"Purchase Count": totItemPurchaseCount, 
                                   "Item Price": perItemPrice,
                                   "Total Purchase Value":totItemPurchaseValue})

# top five popular items from the descending order list
topPopularItemsDF = itemsDF.sort_values(["Purchase Count"], ascending=False).head()
# format the float columns
topPopularItemsDF.style.format({"Item Price":"${:,.2f}",
                                "Total Purchase Value":"${:,.2f}"})
topPopularItemsDF.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>178</th>
      <th>Oathbreaker, Last Hope of the Breaking Storm</th>
      <td>12</td>
      <td>4.23</td>
      <td>50.76</td>
    </tr>
    <tr>
      <th>145</th>
      <th>Fiery Glass Crusader</th>
      <td>9</td>
      <td>4.58</td>
      <td>41.22</td>
    </tr>
    <tr>
      <th>108</th>
      <th>Extraction, Quickblade Of Trembling Hands</th>
      <td>9</td>
      <td>3.53</td>
      <td>31.77</td>
    </tr>
    <tr>
      <th>82</th>
      <th>Nirvana</th>
      <td>9</td>
      <td>4.90</td>
      <td>44.10</td>
    </tr>
    <tr>
      <th>19</th>
      <th>Pursuit, Cudgel of Necromancy</th>
      <td>8</td>
      <td>1.02</td>
      <td>8.16</td>
    </tr>
  </tbody>
</table>
</div>



# Most Profitable Items

* Identify the 5 most profitable items by total purchase value, then list (in a table):

    * Item ID
    * Item Name
    * Purchase Count
    * Item Price
    * Total Purchase Value


```python
# top five profitable items from the descending order list
topPopularItemsDF = itemsDF.sort_values(["Total Purchase Value"], ascending=False).head()
# format the float columns
topPopularItemsDF.style.format({"Item Price":"${:,.2f}",
                                "Total Purchase Value":"${:,.2f}"})
topPopularItemsDF.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>178</th>
      <th>Oathbreaker, Last Hope of the Breaking Storm</th>
      <td>12</td>
      <td>4.23</td>
      <td>50.76</td>
    </tr>
    <tr>
      <th>82</th>
      <th>Nirvana</th>
      <td>9</td>
      <td>4.90</td>
      <td>44.10</td>
    </tr>
    <tr>
      <th>145</th>
      <th>Fiery Glass Crusader</th>
      <td>9</td>
      <td>4.58</td>
      <td>41.22</td>
    </tr>
    <tr>
      <th>92</th>
      <th>Final Critic</th>
      <td>8</td>
      <td>4.88</td>
      <td>39.04</td>
    </tr>
    <tr>
      <th>103</th>
      <th>Singed Scalpel</th>
      <td>8</td>
      <td>4.35</td>
      <td>34.80</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
