# Observations
* Analysing the given purchase data, out of unique 576 players the major portion is male players who are enjoying the big percentage 84%, where female percentage is quite low at 14% and Others/ Non-Disclosed are negligible.

* Analysing the Age demographic data shows that age between 20-24 has the maximum number of players purchasing the game.

* Analysing the most popular and most profitable item, the Oathbreaker & Last Hope of the Breaking Storm enjoys the top rank out of all the items.
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
purchaseAnalysisDF["Average Purchase Price"] = purchaseAnalysisDF["Average Purchase Price"].map('${:.2f}'.format)
purchaseAnalysisDF["Total Revenue"] = purchaseAnalysisDF["Total Revenue"].map('${:.2f}'.format)
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
      <td>$3.05</td>
      <td>780</td>
      <td>$2379.77</td>
    </tr>
  </tbody>
</table>
</div>



# Gender Demographics

* Percentage and Count of Male Players
* Percentage and Count of Female Players
* Percentage and Count of Other / Non-Disclosed


```python
# set data frame group by Gender
genderGroupByDF = mainDF.groupby(["Gender"])
totCount = genderGroupByDF["SN"].nunique().sum()
totCountByGender = genderGroupByDF["SN"].nunique()
percOfPlayers = (totCountByGender/totCount) * 100
genderDemographicDF = pd.DataFrame({
    "Total Count": totCountByGender,
    "Percentage of Players": percOfPlayers
})

# sort by the percentage of players
genderDemographicDF = genderDemographicDF.sort_values(["Percentage of Players"], ascending=False).head()

# format the float columns
genderDemographicDF["Percentage of Players"] = genderDemographicDF["Percentage of Players"].map('{:.2f}%'.format)
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
      <td>84.03%</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>81</td>
      <td>14.06%</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>11</td>
      <td>1.91%</td>
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
# set data frame group by Gender
purchaseCount = genderGroupByDF["Gender"].count()
avgPurchasePrice = genderGroupByDF["Price"].mean()
totPurchasePrice = genderGroupByDF["Price"].sum()
totAgeCount = genderGroupByDF["SN"].nunique()
avgTotPurchasePPGender = totPurchasePrice/totAgeCount

# presenting data into Purchasing Analysis (Gender) data frame to present
genderPurchaseAnalysisDF = pd.DataFrame({
    "Purchase Count": purchaseCount,
    "Average Purchase Price": avgPurchasePrice,
    "Total Purchase Value": totPurchasePrice,
    "Avg Purchase Total PP By Gender": avgTotPurchasePPGender
})

# format the float columns
genderPurchaseAnalysisDF["Average Purchase Price"] = genderPurchaseAnalysisDF["Average Purchase Price"].map('${:.2f}'.format)
genderPurchaseAnalysisDF["Total Purchase Value"] = genderPurchaseAnalysisDF["Total Purchase Value"].map('${:.2f}'.format)
genderPurchaseAnalysisDF["Avg Purchase Total PP By Gender"] = genderPurchaseAnalysisDF["Avg Purchase Total PP By Gender"].map('${:.2f}'.format)
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
      <td>$3.20</td>
      <td>$361.94</td>
      <td>$4.47</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>652</td>
      <td>$3.02</td>
      <td>$1967.64</td>
      <td>$4.07</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>15</td>
      <td>$3.35</td>
      <td>$50.19</td>
      <td>$4.56</td>
    </tr>
  </tbody>
</table>
</div>



# Age Demographics

* The below each broken into bins of 4 years (i.e. <10, 10-14, 15-19, etc.)


```python
# creating bins anf labels
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
ageDemographicDF["Percentage of Players"] = ageDemographicDF["Percentage of Players"].map('{:.2f}%'.format)
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
      <td>3.99%</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>28</td>
      <td>4.86%</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>136</td>
      <td>23.61%</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>365</td>
      <td>63.37%</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>101</td>
      <td>17.53%</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>73</td>
      <td>12.67%</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>41</td>
      <td>7.12%</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>13</td>
      <td>2.26%</td>
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
ageDemographicAnalysisDF["Average Purchase Price"] = ageDemographicAnalysisDF["Average Purchase Price"].map('${:.2f}'.format)
ageDemographicAnalysisDF["Total Purchase Value"] = ageDemographicAnalysisDF["Total Purchase Value"].map('${:.2f}'.format)
ageDemographicAnalysisDF["Average Purchase Total Per Person"] = ageDemographicAnalysisDF["Average Purchase Total Per Person"].map('${:.2f}'.format)
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
      <td>$3.35</td>
      <td>$77.13</td>
      <td>$4.54</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>28</td>
      <td>$2.96</td>
      <td>$82.78</td>
      <td>$3.76</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>136</td>
      <td>$3.04</td>
      <td>$412.89</td>
      <td>$3.86</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>365</td>
      <td>$3.05</td>
      <td>$1114.06</td>
      <td>$4.32</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>101</td>
      <td>$2.90</td>
      <td>$293.00</td>
      <td>$3.81</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>73</td>
      <td>$2.93</td>
      <td>$214.00</td>
      <td>$4.12</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>41</td>
      <td>$3.60</td>
      <td>$147.67</td>
      <td>$4.76</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>13</td>
      <td>$2.94</td>
      <td>$38.24</td>
      <td>$3.19</td>
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
totalSpendersDF["Average Purchase Price"] = totalSpendersDF["Average Purchase Price"].map('${:.2f}'.format)
totalSpendersDF["Total Purchase Value"] = totalSpendersDF["Total Purchase Value"].map('${:.2f}'.format)
totalSpendersDF.head(10)
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
      <td>$3.79</td>
      <td>$18.96</td>
    </tr>
    <tr>
      <th>Idastidru52</th>
      <td>4</td>
      <td>$3.86</td>
      <td>$15.45</td>
    </tr>
    <tr>
      <th>Chamjask73</th>
      <td>3</td>
      <td>$4.61</td>
      <td>$13.83</td>
    </tr>
    <tr>
      <th>Iral74</th>
      <td>4</td>
      <td>$3.40</td>
      <td>$13.62</td>
    </tr>
    <tr>
      <th>Iskadarya95</th>
      <td>3</td>
      <td>$4.37</td>
      <td>$13.10</td>
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
topPopularItemsDF["Item Price"] = topPopularItemsDF["Item Price"].map('${:.2f}'.format)
topPopularItemsDF["Total Purchase Value"] = topPopularItemsDF["Total Purchase Value"].map('${:.2f}'.format)
topPopularItemsDF.head(10)
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
      <td>$4.23</td>
      <td>$50.76</td>
    </tr>
    <tr>
      <th>145</th>
      <th>Fiery Glass Crusader</th>
      <td>9</td>
      <td>$4.58</td>
      <td>$41.22</td>
    </tr>
    <tr>
      <th>108</th>
      <th>Extraction, Quickblade Of Trembling Hands</th>
      <td>9</td>
      <td>$3.53</td>
      <td>$31.77</td>
    </tr>
    <tr>
      <th>82</th>
      <th>Nirvana</th>
      <td>9</td>
      <td>$4.90</td>
      <td>$44.10</td>
    </tr>
    <tr>
      <th>19</th>
      <th>Pursuit, Cudgel of Necromancy</th>
      <td>8</td>
      <td>$1.02</td>
      <td>$8.16</td>
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
topPopularItemsDF["Item Price"] = topPopularItemsDF["Item Price"].map('${:.2f}'.format)
topPopularItemsDF["Total Purchase Value"] = topPopularItemsDF["Total Purchase Value"].map('${:.2f}'.format)
topPopularItemsDF.head(10)
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
      <td>$4.23</td>
      <td>$50.76</td>
    </tr>
    <tr>
      <th>82</th>
      <th>Nirvana</th>
      <td>9</td>
      <td>$4.90</td>
      <td>$44.10</td>
    </tr>
    <tr>
      <th>145</th>
      <th>Fiery Glass Crusader</th>
      <td>9</td>
      <td>$4.58</td>
      <td>$41.22</td>
    </tr>
    <tr>
      <th>92</th>
      <th>Final Critic</th>
      <td>8</td>
      <td>$4.88</td>
      <td>$39.04</td>
    </tr>
    <tr>
      <th>103</th>
      <th>Singed Scalpel</th>
      <td>8</td>
      <td>$4.35</td>
      <td>$34.80</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
