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
totPlayerDF
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
```




<style  type="text/css" >
</style><table id="T_2ad5cd34_d812_11e9_8f94_a0510b157e5c" ><thead>    <tr>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >Number of Unique Items</th>        <th class="col_heading level0 col1" >Average Purchase Price</th>        <th class="col_heading level0 col2" >Number of Purchases</th>        <th class="col_heading level0 col3" >Total Revenue</th>    </tr></thead><tbody>
                <tr>
                        <th id="T_2ad5cd34_d812_11e9_8f94_a0510b157e5clevel0_row0" class="row_heading level0 row0" >0</th>
                        <td id="T_2ad5cd34_d812_11e9_8f94_a0510b157e5crow0_col0" class="data row0 col0" >183</td>
                        <td id="T_2ad5cd34_d812_11e9_8f94_a0510b157e5crow0_col1" class="data row0 col1" >$3.05</td>
                        <td id="T_2ad5cd34_d812_11e9_8f94_a0510b157e5crow0_col2" class="data row0 col2" >780</td>
                        <td id="T_2ad5cd34_d812_11e9_8f94_a0510b157e5crow0_col3" class="data row0 col3" >$2379.77</td>
            </tr>
    </tbody></table>



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
```




<style  type="text/css" >
</style><table id="T_2ada73b4_d812_11e9_bc1a_a0510b157e5c" ><thead>    <tr>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >Total Count</th>        <th class="col_heading level0 col1" >Percentage of Players</th>    </tr>    <tr>        <th class="index_name level0" >Gender</th>        <th class="blank" ></th>        <th class="blank" ></th>    </tr></thead><tbody>
                <tr>
                        <th id="T_2ada73b4_d812_11e9_bc1a_a0510b157e5clevel0_row0" class="row_heading level0 row0" >Male</th>
                        <td id="T_2ada73b4_d812_11e9_bc1a_a0510b157e5crow0_col0" class="data row0 col0" >484</td>
                        <td id="T_2ada73b4_d812_11e9_bc1a_a0510b157e5crow0_col1" class="data row0 col1" >84.03%</td>
            </tr>
            <tr>
                        <th id="T_2ada73b4_d812_11e9_bc1a_a0510b157e5clevel0_row1" class="row_heading level0 row1" >Female</th>
                        <td id="T_2ada73b4_d812_11e9_bc1a_a0510b157e5crow1_col0" class="data row1 col0" >81</td>
                        <td id="T_2ada73b4_d812_11e9_bc1a_a0510b157e5crow1_col1" class="data row1 col1" >14.06%</td>
            </tr>
            <tr>
                        <th id="T_2ada73b4_d812_11e9_bc1a_a0510b157e5clevel0_row2" class="row_heading level0 row2" >Other/ Non-Disclosed</th>
                        <td id="T_2ada73b4_d812_11e9_bc1a_a0510b157e5crow2_col0" class="data row2 col0" >11</td>
                        <td id="T_2ada73b4_d812_11e9_bc1a_a0510b157e5crow2_col1" class="data row2 col1" >1.91%</td>
            </tr>
    </tbody></table>



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

```




<style  type="text/css" >
</style><table id="T_2ae2109e_d812_11e9_83d9_a0510b157e5c" ><thead>    <tr>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >Purchase Count</th>        <th class="col_heading level0 col1" >Average Purchase Price</th>        <th class="col_heading level0 col2" >Total Purchase Value</th>        <th class="col_heading level0 col3" >Avg Purchase Total PP By Gender</th>    </tr>    <tr>        <th class="index_name level0" >Gender</th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>    </tr></thead><tbody>
                <tr>
                        <th id="T_2ae2109e_d812_11e9_83d9_a0510b157e5clevel0_row0" class="row_heading level0 row0" >Female</th>
                        <td id="T_2ae2109e_d812_11e9_83d9_a0510b157e5crow0_col0" class="data row0 col0" >113</td>
                        <td id="T_2ae2109e_d812_11e9_83d9_a0510b157e5crow0_col1" class="data row0 col1" >$3.20</td>
                        <td id="T_2ae2109e_d812_11e9_83d9_a0510b157e5crow0_col2" class="data row0 col2" >$361.94</td>
                        <td id="T_2ae2109e_d812_11e9_83d9_a0510b157e5crow0_col3" class="data row0 col3" >$4.47</td>
            </tr>
            <tr>
                        <th id="T_2ae2109e_d812_11e9_83d9_a0510b157e5clevel0_row1" class="row_heading level0 row1" >Male</th>
                        <td id="T_2ae2109e_d812_11e9_83d9_a0510b157e5crow1_col0" class="data row1 col0" >652</td>
                        <td id="T_2ae2109e_d812_11e9_83d9_a0510b157e5crow1_col1" class="data row1 col1" >$3.02</td>
                        <td id="T_2ae2109e_d812_11e9_83d9_a0510b157e5crow1_col2" class="data row1 col2" >$1967.64</td>
                        <td id="T_2ae2109e_d812_11e9_83d9_a0510b157e5crow1_col3" class="data row1 col3" >$4.07</td>
            </tr>
            <tr>
                        <th id="T_2ae2109e_d812_11e9_83d9_a0510b157e5clevel0_row2" class="row_heading level0 row2" >Other / Non-Disclosed</th>
                        <td id="T_2ae2109e_d812_11e9_83d9_a0510b157e5crow2_col0" class="data row2 col0" >15</td>
                        <td id="T_2ae2109e_d812_11e9_83d9_a0510b157e5crow2_col1" class="data row2 col1" >$3.35</td>
                        <td id="T_2ae2109e_d812_11e9_83d9_a0510b157e5crow2_col2" class="data row2 col2" >$50.19</td>
                        <td id="T_2ae2109e_d812_11e9_83d9_a0510b157e5crow2_col3" class="data row2 col3" >$4.56</td>
            </tr>
    </tbody></table>



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
```




<style  type="text/css" >
</style><table id="T_2ae95d7a_d812_11e9_aa38_a0510b157e5c" ><thead>    <tr>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >Total Count</th>        <th class="col_heading level0 col1" >Percentage of Players</th>    </tr></thead><tbody>
                <tr>
                        <th id="T_2ae95d7a_d812_11e9_aa38_a0510b157e5clevel0_row0" class="row_heading level0 row0" ><10</th>
                        <td id="T_2ae95d7a_d812_11e9_aa38_a0510b157e5crow0_col0" class="data row0 col0" >23</td>
                        <td id="T_2ae95d7a_d812_11e9_aa38_a0510b157e5crow0_col1" class="data row0 col1" >3.99%</td>
            </tr>
            <tr>
                        <th id="T_2ae95d7a_d812_11e9_aa38_a0510b157e5clevel0_row1" class="row_heading level0 row1" >10-14</th>
                        <td id="T_2ae95d7a_d812_11e9_aa38_a0510b157e5crow1_col0" class="data row1 col0" >28</td>
                        <td id="T_2ae95d7a_d812_11e9_aa38_a0510b157e5crow1_col1" class="data row1 col1" >4.86%</td>
            </tr>
            <tr>
                        <th id="T_2ae95d7a_d812_11e9_aa38_a0510b157e5clevel0_row2" class="row_heading level0 row2" >15-19</th>
                        <td id="T_2ae95d7a_d812_11e9_aa38_a0510b157e5crow2_col0" class="data row2 col0" >136</td>
                        <td id="T_2ae95d7a_d812_11e9_aa38_a0510b157e5crow2_col1" class="data row2 col1" >23.61%</td>
            </tr>
            <tr>
                        <th id="T_2ae95d7a_d812_11e9_aa38_a0510b157e5clevel0_row3" class="row_heading level0 row3" >20-24</th>
                        <td id="T_2ae95d7a_d812_11e9_aa38_a0510b157e5crow3_col0" class="data row3 col0" >365</td>
                        <td id="T_2ae95d7a_d812_11e9_aa38_a0510b157e5crow3_col1" class="data row3 col1" >63.37%</td>
            </tr>
            <tr>
                        <th id="T_2ae95d7a_d812_11e9_aa38_a0510b157e5clevel0_row4" class="row_heading level0 row4" >25-29</th>
                        <td id="T_2ae95d7a_d812_11e9_aa38_a0510b157e5crow4_col0" class="data row4 col0" >101</td>
                        <td id="T_2ae95d7a_d812_11e9_aa38_a0510b157e5crow4_col1" class="data row4 col1" >17.53%</td>
            </tr>
            <tr>
                        <th id="T_2ae95d7a_d812_11e9_aa38_a0510b157e5clevel0_row5" class="row_heading level0 row5" >30-34</th>
                        <td id="T_2ae95d7a_d812_11e9_aa38_a0510b157e5crow5_col0" class="data row5 col0" >73</td>
                        <td id="T_2ae95d7a_d812_11e9_aa38_a0510b157e5crow5_col1" class="data row5 col1" >12.67%</td>
            </tr>
            <tr>
                        <th id="T_2ae95d7a_d812_11e9_aa38_a0510b157e5clevel0_row6" class="row_heading level0 row6" >35-39</th>
                        <td id="T_2ae95d7a_d812_11e9_aa38_a0510b157e5crow6_col0" class="data row6 col0" >41</td>
                        <td id="T_2ae95d7a_d812_11e9_aa38_a0510b157e5crow6_col1" class="data row6 col1" >7.12%</td>
            </tr>
            <tr>
                        <th id="T_2ae95d7a_d812_11e9_aa38_a0510b157e5clevel0_row7" class="row_heading level0 row7" >40+</th>
                        <td id="T_2ae95d7a_d812_11e9_aa38_a0510b157e5crow7_col0" class="data row7 col0" >13</td>
                        <td id="T_2ae95d7a_d812_11e9_aa38_a0510b157e5crow7_col1" class="data row7 col1" >2.26%</td>
            </tr>
    </tbody></table>



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
```




<style  type="text/css" >
</style><table id="T_2aecd8f6_d812_11e9_bcfb_a0510b157e5c" ><thead>    <tr>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >Purchase Count</th>        <th class="col_heading level0 col1" >Average Purchase Price</th>        <th class="col_heading level0 col2" >Total Purchase Value</th>        <th class="col_heading level0 col3" >Average Purchase Total Per Person</th>    </tr>    <tr>        <th class="index_name level0" >Age Range</th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>    </tr></thead><tbody>
                <tr>
                        <th id="T_2aecd8f6_d812_11e9_bcfb_a0510b157e5clevel0_row0" class="row_heading level0 row0" ><10</th>
                        <td id="T_2aecd8f6_d812_11e9_bcfb_a0510b157e5crow0_col0" class="data row0 col0" >23</td>
                        <td id="T_2aecd8f6_d812_11e9_bcfb_a0510b157e5crow0_col1" class="data row0 col1" >$3.35</td>
                        <td id="T_2aecd8f6_d812_11e9_bcfb_a0510b157e5crow0_col2" class="data row0 col2" >$77.13</td>
                        <td id="T_2aecd8f6_d812_11e9_bcfb_a0510b157e5crow0_col3" class="data row0 col3" >$4.54</td>
            </tr>
            <tr>
                        <th id="T_2aecd8f6_d812_11e9_bcfb_a0510b157e5clevel0_row1" class="row_heading level0 row1" >10-14</th>
                        <td id="T_2aecd8f6_d812_11e9_bcfb_a0510b157e5crow1_col0" class="data row1 col0" >28</td>
                        <td id="T_2aecd8f6_d812_11e9_bcfb_a0510b157e5crow1_col1" class="data row1 col1" >$2.96</td>
                        <td id="T_2aecd8f6_d812_11e9_bcfb_a0510b157e5crow1_col2" class="data row1 col2" >$82.78</td>
                        <td id="T_2aecd8f6_d812_11e9_bcfb_a0510b157e5crow1_col3" class="data row1 col3" >$3.76</td>
            </tr>
            <tr>
                        <th id="T_2aecd8f6_d812_11e9_bcfb_a0510b157e5clevel0_row2" class="row_heading level0 row2" >15-19</th>
                        <td id="T_2aecd8f6_d812_11e9_bcfb_a0510b157e5crow2_col0" class="data row2 col0" >136</td>
                        <td id="T_2aecd8f6_d812_11e9_bcfb_a0510b157e5crow2_col1" class="data row2 col1" >$3.04</td>
                        <td id="T_2aecd8f6_d812_11e9_bcfb_a0510b157e5crow2_col2" class="data row2 col2" >$412.89</td>
                        <td id="T_2aecd8f6_d812_11e9_bcfb_a0510b157e5crow2_col3" class="data row2 col3" >$3.86</td>
            </tr>
            <tr>
                        <th id="T_2aecd8f6_d812_11e9_bcfb_a0510b157e5clevel0_row3" class="row_heading level0 row3" >20-24</th>
                        <td id="T_2aecd8f6_d812_11e9_bcfb_a0510b157e5crow3_col0" class="data row3 col0" >365</td>
                        <td id="T_2aecd8f6_d812_11e9_bcfb_a0510b157e5crow3_col1" class="data row3 col1" >$3.05</td>
                        <td id="T_2aecd8f6_d812_11e9_bcfb_a0510b157e5crow3_col2" class="data row3 col2" >$1,114.06</td>
                        <td id="T_2aecd8f6_d812_11e9_bcfb_a0510b157e5crow3_col3" class="data row3 col3" >$4.32</td>
            </tr>
            <tr>
                        <th id="T_2aecd8f6_d812_11e9_bcfb_a0510b157e5clevel0_row4" class="row_heading level0 row4" >25-29</th>
                        <td id="T_2aecd8f6_d812_11e9_bcfb_a0510b157e5crow4_col0" class="data row4 col0" >101</td>
                        <td id="T_2aecd8f6_d812_11e9_bcfb_a0510b157e5crow4_col1" class="data row4 col1" >$2.90</td>
                        <td id="T_2aecd8f6_d812_11e9_bcfb_a0510b157e5crow4_col2" class="data row4 col2" >$293.00</td>
                        <td id="T_2aecd8f6_d812_11e9_bcfb_a0510b157e5crow4_col3" class="data row4 col3" >$3.81</td>
            </tr>
            <tr>
                        <th id="T_2aecd8f6_d812_11e9_bcfb_a0510b157e5clevel0_row5" class="row_heading level0 row5" >30-34</th>
                        <td id="T_2aecd8f6_d812_11e9_bcfb_a0510b157e5crow5_col0" class="data row5 col0" >73</td>
                        <td id="T_2aecd8f6_d812_11e9_bcfb_a0510b157e5crow5_col1" class="data row5 col1" >$2.93</td>
                        <td id="T_2aecd8f6_d812_11e9_bcfb_a0510b157e5crow5_col2" class="data row5 col2" >$214.00</td>
                        <td id="T_2aecd8f6_d812_11e9_bcfb_a0510b157e5crow5_col3" class="data row5 col3" >$4.12</td>
            </tr>
            <tr>
                        <th id="T_2aecd8f6_d812_11e9_bcfb_a0510b157e5clevel0_row6" class="row_heading level0 row6" >35-39</th>
                        <td id="T_2aecd8f6_d812_11e9_bcfb_a0510b157e5crow6_col0" class="data row6 col0" >41</td>
                        <td id="T_2aecd8f6_d812_11e9_bcfb_a0510b157e5crow6_col1" class="data row6 col1" >$3.60</td>
                        <td id="T_2aecd8f6_d812_11e9_bcfb_a0510b157e5crow6_col2" class="data row6 col2" >$147.67</td>
                        <td id="T_2aecd8f6_d812_11e9_bcfb_a0510b157e5crow6_col3" class="data row6 col3" >$4.76</td>
            </tr>
            <tr>
                        <th id="T_2aecd8f6_d812_11e9_bcfb_a0510b157e5clevel0_row7" class="row_heading level0 row7" >40+</th>
                        <td id="T_2aecd8f6_d812_11e9_bcfb_a0510b157e5crow7_col0" class="data row7 col0" >13</td>
                        <td id="T_2aecd8f6_d812_11e9_bcfb_a0510b157e5crow7_col1" class="data row7 col1" >$2.94</td>
                        <td id="T_2aecd8f6_d812_11e9_bcfb_a0510b157e5crow7_col2" class="data row7 col2" >$38.24</td>
                        <td id="T_2aecd8f6_d812_11e9_bcfb_a0510b157e5crow7_col3" class="data row7 col3" >$3.19</td>
            </tr>
    </tbody></table>



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
```




<style  type="text/css" >
</style><table id="T_2af169da_d812_11e9_b136_a0510b157e5c" ><thead>    <tr>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >Purchase Count</th>        <th class="col_heading level0 col1" >Average Purchase Price</th>        <th class="col_heading level0 col2" >Total Purchase Value</th>    </tr>    <tr>        <th class="index_name level0" >SN</th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>    </tr></thead><tbody>
                <tr>
                        <th id="T_2af169da_d812_11e9_b136_a0510b157e5clevel0_row0" class="row_heading level0 row0" >Lisosia93</th>
                        <td id="T_2af169da_d812_11e9_b136_a0510b157e5crow0_col0" class="data row0 col0" >5</td>
                        <td id="T_2af169da_d812_11e9_b136_a0510b157e5crow0_col1" class="data row0 col1" >$3.79</td>
                        <td id="T_2af169da_d812_11e9_b136_a0510b157e5crow0_col2" class="data row0 col2" >$18.96</td>
            </tr>
            <tr>
                        <th id="T_2af169da_d812_11e9_b136_a0510b157e5clevel0_row1" class="row_heading level0 row1" >Idastidru52</th>
                        <td id="T_2af169da_d812_11e9_b136_a0510b157e5crow1_col0" class="data row1 col0" >4</td>
                        <td id="T_2af169da_d812_11e9_b136_a0510b157e5crow1_col1" class="data row1 col1" >$3.86</td>
                        <td id="T_2af169da_d812_11e9_b136_a0510b157e5crow1_col2" class="data row1 col2" >$15.45</td>
            </tr>
            <tr>
                        <th id="T_2af169da_d812_11e9_b136_a0510b157e5clevel0_row2" class="row_heading level0 row2" >Chamjask73</th>
                        <td id="T_2af169da_d812_11e9_b136_a0510b157e5crow2_col0" class="data row2 col0" >3</td>
                        <td id="T_2af169da_d812_11e9_b136_a0510b157e5crow2_col1" class="data row2 col1" >$4.61</td>
                        <td id="T_2af169da_d812_11e9_b136_a0510b157e5crow2_col2" class="data row2 col2" >$13.83</td>
            </tr>
            <tr>
                        <th id="T_2af169da_d812_11e9_b136_a0510b157e5clevel0_row3" class="row_heading level0 row3" >Iral74</th>
                        <td id="T_2af169da_d812_11e9_b136_a0510b157e5crow3_col0" class="data row3 col0" >4</td>
                        <td id="T_2af169da_d812_11e9_b136_a0510b157e5crow3_col1" class="data row3 col1" >$3.40</td>
                        <td id="T_2af169da_d812_11e9_b136_a0510b157e5crow3_col2" class="data row3 col2" >$13.62</td>
            </tr>
            <tr>
                        <th id="T_2af169da_d812_11e9_b136_a0510b157e5clevel0_row4" class="row_heading level0 row4" >Iskadarya95</th>
                        <td id="T_2af169da_d812_11e9_b136_a0510b157e5crow4_col0" class="data row4 col0" >3</td>
                        <td id="T_2af169da_d812_11e9_b136_a0510b157e5crow4_col1" class="data row4 col1" >$4.37</td>
                        <td id="T_2af169da_d812_11e9_b136_a0510b157e5crow4_col2" class="data row4 col2" >$13.10</td>
            </tr>
    </tbody></table>



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
```




<style  type="text/css" >
</style><table id="T_2af474d2_d812_11e9_bf89_a0510b157e5c" ><thead>    <tr>        <th class="blank" ></th>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >Purchase Count</th>        <th class="col_heading level0 col1" >Item Price</th>        <th class="col_heading level0 col2" >Total Purchase Value</th>    </tr>    <tr>        <th class="index_name level0" >Item ID</th>        <th class="index_name level1" >Item Name</th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>    </tr></thead><tbody>
                <tr>
                        <th id="T_2af474d2_d812_11e9_bf89_a0510b157e5clevel0_row0" class="row_heading level0 row0" >178</th>
                        <th id="T_2af474d2_d812_11e9_bf89_a0510b157e5clevel1_row0" class="row_heading level1 row0" >Oathbreaker, Last Hope of the Breaking Storm</th>
                        <td id="T_2af474d2_d812_11e9_bf89_a0510b157e5crow0_col0" class="data row0 col0" >12</td>
                        <td id="T_2af474d2_d812_11e9_bf89_a0510b157e5crow0_col1" class="data row0 col1" >$4.23</td>
                        <td id="T_2af474d2_d812_11e9_bf89_a0510b157e5crow0_col2" class="data row0 col2" >$50.76</td>
            </tr>
            <tr>
                        <th id="T_2af474d2_d812_11e9_bf89_a0510b157e5clevel0_row1" class="row_heading level0 row1" >145</th>
                        <th id="T_2af474d2_d812_11e9_bf89_a0510b157e5clevel1_row1" class="row_heading level1 row1" >Fiery Glass Crusader</th>
                        <td id="T_2af474d2_d812_11e9_bf89_a0510b157e5crow1_col0" class="data row1 col0" >9</td>
                        <td id="T_2af474d2_d812_11e9_bf89_a0510b157e5crow1_col1" class="data row1 col1" >$4.58</td>
                        <td id="T_2af474d2_d812_11e9_bf89_a0510b157e5crow1_col2" class="data row1 col2" >$41.22</td>
            </tr>
            <tr>
                        <th id="T_2af474d2_d812_11e9_bf89_a0510b157e5clevel0_row2" class="row_heading level0 row2" >108</th>
                        <th id="T_2af474d2_d812_11e9_bf89_a0510b157e5clevel1_row2" class="row_heading level1 row2" >Extraction, Quickblade Of Trembling Hands</th>
                        <td id="T_2af474d2_d812_11e9_bf89_a0510b157e5crow2_col0" class="data row2 col0" >9</td>
                        <td id="T_2af474d2_d812_11e9_bf89_a0510b157e5crow2_col1" class="data row2 col1" >$3.53</td>
                        <td id="T_2af474d2_d812_11e9_bf89_a0510b157e5crow2_col2" class="data row2 col2" >$31.77</td>
            </tr>
            <tr>
                        <th id="T_2af474d2_d812_11e9_bf89_a0510b157e5clevel0_row3" class="row_heading level0 row3" >82</th>
                        <th id="T_2af474d2_d812_11e9_bf89_a0510b157e5clevel1_row3" class="row_heading level1 row3" >Nirvana</th>
                        <td id="T_2af474d2_d812_11e9_bf89_a0510b157e5crow3_col0" class="data row3 col0" >9</td>
                        <td id="T_2af474d2_d812_11e9_bf89_a0510b157e5crow3_col1" class="data row3 col1" >$4.90</td>
                        <td id="T_2af474d2_d812_11e9_bf89_a0510b157e5crow3_col2" class="data row3 col2" >$44.10</td>
            </tr>
            <tr>
                        <th id="T_2af474d2_d812_11e9_bf89_a0510b157e5clevel0_row4" class="row_heading level0 row4" >19</th>
                        <th id="T_2af474d2_d812_11e9_bf89_a0510b157e5clevel1_row4" class="row_heading level1 row4" >Pursuit, Cudgel of Necromancy</th>
                        <td id="T_2af474d2_d812_11e9_bf89_a0510b157e5crow4_col0" class="data row4 col0" >8</td>
                        <td id="T_2af474d2_d812_11e9_bf89_a0510b157e5crow4_col1" class="data row4 col1" >$1.02</td>
                        <td id="T_2af474d2_d812_11e9_bf89_a0510b157e5crow4_col2" class="data row4 col2" >$8.16</td>
            </tr>
    </tbody></table>



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
```




<style  type="text/css" >
</style><table id="T_2af6e41a_d812_11e9_9e42_a0510b157e5c" ><thead>    <tr>        <th class="blank" ></th>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >Purchase Count</th>        <th class="col_heading level0 col1" >Item Price</th>        <th class="col_heading level0 col2" >Total Purchase Value</th>    </tr>    <tr>        <th class="index_name level0" >Item ID</th>        <th class="index_name level1" >Item Name</th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>    </tr></thead><tbody>
                <tr>
                        <th id="T_2af6e41a_d812_11e9_9e42_a0510b157e5clevel0_row0" class="row_heading level0 row0" >178</th>
                        <th id="T_2af6e41a_d812_11e9_9e42_a0510b157e5clevel1_row0" class="row_heading level1 row0" >Oathbreaker, Last Hope of the Breaking Storm</th>
                        <td id="T_2af6e41a_d812_11e9_9e42_a0510b157e5crow0_col0" class="data row0 col0" >12</td>
                        <td id="T_2af6e41a_d812_11e9_9e42_a0510b157e5crow0_col1" class="data row0 col1" >$4.23</td>
                        <td id="T_2af6e41a_d812_11e9_9e42_a0510b157e5crow0_col2" class="data row0 col2" >$50.76</td>
            </tr>
            <tr>
                        <th id="T_2af6e41a_d812_11e9_9e42_a0510b157e5clevel0_row1" class="row_heading level0 row1" >82</th>
                        <th id="T_2af6e41a_d812_11e9_9e42_a0510b157e5clevel1_row1" class="row_heading level1 row1" >Nirvana</th>
                        <td id="T_2af6e41a_d812_11e9_9e42_a0510b157e5crow1_col0" class="data row1 col0" >9</td>
                        <td id="T_2af6e41a_d812_11e9_9e42_a0510b157e5crow1_col1" class="data row1 col1" >$4.90</td>
                        <td id="T_2af6e41a_d812_11e9_9e42_a0510b157e5crow1_col2" class="data row1 col2" >$44.10</td>
            </tr>
            <tr>
                        <th id="T_2af6e41a_d812_11e9_9e42_a0510b157e5clevel0_row2" class="row_heading level0 row2" >145</th>
                        <th id="T_2af6e41a_d812_11e9_9e42_a0510b157e5clevel1_row2" class="row_heading level1 row2" >Fiery Glass Crusader</th>
                        <td id="T_2af6e41a_d812_11e9_9e42_a0510b157e5crow2_col0" class="data row2 col0" >9</td>
                        <td id="T_2af6e41a_d812_11e9_9e42_a0510b157e5crow2_col1" class="data row2 col1" >$4.58</td>
                        <td id="T_2af6e41a_d812_11e9_9e42_a0510b157e5crow2_col2" class="data row2 col2" >$41.22</td>
            </tr>
            <tr>
                        <th id="T_2af6e41a_d812_11e9_9e42_a0510b157e5clevel0_row3" class="row_heading level0 row3" >92</th>
                        <th id="T_2af6e41a_d812_11e9_9e42_a0510b157e5clevel1_row3" class="row_heading level1 row3" >Final Critic</th>
                        <td id="T_2af6e41a_d812_11e9_9e42_a0510b157e5crow3_col0" class="data row3 col0" >8</td>
                        <td id="T_2af6e41a_d812_11e9_9e42_a0510b157e5crow3_col1" class="data row3 col1" >$4.88</td>
                        <td id="T_2af6e41a_d812_11e9_9e42_a0510b157e5crow3_col2" class="data row3 col2" >$39.04</td>
            </tr>
            <tr>
                        <th id="T_2af6e41a_d812_11e9_9e42_a0510b157e5clevel0_row4" class="row_heading level0 row4" >103</th>
                        <th id="T_2af6e41a_d812_11e9_9e42_a0510b157e5clevel1_row4" class="row_heading level1 row4" >Singed Scalpel</th>
                        <td id="T_2af6e41a_d812_11e9_9e42_a0510b157e5crow4_col0" class="data row4 col0" >8</td>
                        <td id="T_2af6e41a_d812_11e9_9e42_a0510b157e5crow4_col1" class="data row4 col1" >$4.35</td>
                        <td id="T_2af6e41a_d812_11e9_9e42_a0510b157e5crow4_col2" class="data row4 col2" >$34.80</td>
            </tr>
    </tbody></table>




```python

```
