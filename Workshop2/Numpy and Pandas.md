
# Python Lists

## Creating


```python
# this is a python list
a = [42, 7, 13, 24601, 2001, 3.50]
```


```python
# this is a list comprehension -- think of it as a sexy for loop

# the following gives us a list in which we multiplied each element in a by 2
z = [i * 2 for i in a]
z
```




    [84, 14, 26, 49202, 4002, 7.0]



## Indexing


```python
# you can index into it
a[0]
```




    42




```python
# what's the 3rd element?
a[2]
```




    13




```python
# indices can also be negative
# this gives you the last element
a[-1]
```




    3.5



## Slicing


```python
# you can also get subsets of the list with slicing
#     a[start:end]
# [start, end)

# this returns the 3rd and 4th entries (indices 2 and 3 -- note we exclude 4!)
a[2:4]
```




    [13, 24601]




```python
# if you leave one side blank, it automatically goes all the way
# first five:
a[:5]
```




    [42, 7, 13, 24601, 2001]




```python
# how do you get the last three elements?
a[-3:]
```




    [24601, 2001, 3.5]




```python
# slices can also skip numbers
# a[start:end:interval]

# this gives us every other number, starting with the first
a[::2]
```




    [42, 13, 2001]




```python
# the interval can also be negative
# what does that do?

a[::-2]
```




    [3.5, 24601, 7]



# Numpy


```python
import numpy as np
```

## Creating


```python
# numpy arrays can be created from a python list
b = np.array(a)
b
```




    array([4.2000e+01, 7.0000e+00, 1.3000e+01, 2.4601e+04, 2.0010e+03,
           3.5000e+00])



Right now, it looks an awful like a python list, but there are some key points you should know.

numpy arrays are:
- homogeneous (all elements in an array have the same type)
- multidimensional


```python
# Homogeneous: all numpy arrays have an associated data type.
# numbers are usually ints or floats
b.dtype
```




    dtype('float64')




```python
# Multidimensional: numpy arrays can have multiple dimensions, like a nested list.
# We can reshape b into a 3x2 matrix
# Note: this doesn't change b. That's why we assign it to a new variable: m
m = b.reshape(3, 2)
m
```




    array([[4.2000e+01, 7.0000e+00],
           [1.3000e+01, 2.4601e+04],
           [2.0010e+03, 3.5000e+00]])




```python
# Each dimension is called an axis
# The size across each axis is called the shape
# These are two very important concepts!
m.shape
```




    (3, 2)



## Indexing


```python
# We index into numpy arrays much the same way as python lists.
b[0]
```




    42.0




```python
# But N-dimensional arrays mean we can be more expressive with indexing
# This gives us [0th index of axis 0, 1st index of axis 1]
# You can think of this as a grid
# Alternatively, this is like m[0][1]
m[0, 1]
```




    7.0




```python
# We can also pass in multiple indices as a list
# This gives us the 1st, 2nd, and 5th values of b
b[[0, 1, 4]]
```




    array([  42.,    7., 2001.])




```python
# Let's combine these two facts to get the 2nd and 3rd items in the second column of m
m[[1,2],1]
```




    array([2.4601e+04, 3.5000e+00])




```python
# We can also incorporate our previous knowledge of slices.
# So to get the second column
# This gives us the entire range on axis 0, and only the 1st index on axis 1
m[:,1]
```




    array([7.0000e+00, 2.4601e+04, 3.5000e+00])



## Math


```python
# numpy gives us a lot of math functions to work with
# I'll only show you a couple, but you can find them all in the documentation

np.sum(b)  # guess what this does?
```




    26667.5




```python
np.mean(b)  # and this?
```




    4444.583333333333




```python
# for convenience, you can also call
b.mean()
```




    4444.583333333333




```python
# you can also apply these functions to only one axis
# only sum across rows (read: apply the sum to axis 1)
np.sum(m, axis=1)
```




    array([   49. , 24614. ,  2004.5])




```python
# numpy has a concept called podcasting
# It tries to coerce non-matching shapes.
# 2 is a scalar, but we can still multiply m by it
# it just repeats the 2 across all instances of m
m * 2
```




    array([[8.4000e+01, 1.4000e+01],
           [2.6000e+01, 4.9202e+04],
           [4.0020e+03, 7.0000e+00]])



# Pandas


```python
import pandas as pd
```

## Creating

Pandas lets us read all sorts of data into a Dataframe. Think of this as a series of lists. Let's look at an example.


```python
df = pd.read_csv("./cereal.csv")
type(df)
```




    pandas.core.frame.DataFrame




```python
# head() gives us the first 10 rows in the dataframe (pd.DataFrame)
df.head()
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
      <th>name</th>
      <th>mfr</th>
      <th>type</th>
      <th>calories</th>
      <th>protein</th>
      <th>fat</th>
      <th>sodium</th>
      <th>fiber</th>
      <th>carbo</th>
      <th>sugars</th>
      <th>potass</th>
      <th>vitamins</th>
      <th>shelf</th>
      <th>weight</th>
      <th>cups</th>
      <th>rating</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>100% Bran</td>
      <td>N</td>
      <td>C</td>
      <td>70</td>
      <td>4</td>
      <td>1</td>
      <td>130</td>
      <td>10.0</td>
      <td>5.0</td>
      <td>6</td>
      <td>280</td>
      <td>25</td>
      <td>3</td>
      <td>1.0</td>
      <td>0.33</td>
      <td>68.402973</td>
    </tr>
    <tr>
      <th>1</th>
      <td>100% Natural Bran</td>
      <td>Q</td>
      <td>C</td>
      <td>120</td>
      <td>3</td>
      <td>5</td>
      <td>15</td>
      <td>2.0</td>
      <td>8.0</td>
      <td>8</td>
      <td>135</td>
      <td>0</td>
      <td>3</td>
      <td>1.0</td>
      <td>1.00</td>
      <td>33.983679</td>
    </tr>
    <tr>
      <th>2</th>
      <td>All-Bran</td>
      <td>K</td>
      <td>C</td>
      <td>70</td>
      <td>4</td>
      <td>1</td>
      <td>260</td>
      <td>9.0</td>
      <td>7.0</td>
      <td>5</td>
      <td>320</td>
      <td>25</td>
      <td>3</td>
      <td>1.0</td>
      <td>0.33</td>
      <td>59.425505</td>
    </tr>
    <tr>
      <th>3</th>
      <td>All-Bran with Extra Fiber</td>
      <td>K</td>
      <td>C</td>
      <td>50</td>
      <td>4</td>
      <td>0</td>
      <td>140</td>
      <td>14.0</td>
      <td>8.0</td>
      <td>0</td>
      <td>330</td>
      <td>25</td>
      <td>3</td>
      <td>1.0</td>
      <td>0.50</td>
      <td>93.704912</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Almond Delight</td>
      <td>R</td>
      <td>C</td>
      <td>110</td>
      <td>2</td>
      <td>2</td>
      <td>200</td>
      <td>1.0</td>
      <td>14.0</td>
      <td>8</td>
      <td>-1</td>
      <td>25</td>
      <td>3</td>
      <td>1.0</td>
      <td>0.75</td>
      <td>34.384843</td>
    </tr>
  </tbody>
</table>
</div>




```python
# you can think of each column as a list (or a 1D numpy array)
# in practice, these are called pandas Series (pd.Series)
# you can index into the dataframe with a string to get one column
df["name"]
```




    0                                  100% Bran
    1                          100% Natural Bran
    2                                   All-Bran
    3                  All-Bran with Extra Fiber
    4                             Almond Delight
    5                    Apple Cinnamon Cheerios
    6                                Apple Jacks
    7                                    Basic 4
    8                                  Bran Chex
    9                                Bran Flakes
    10                              Cap'n'Crunch
    11                                  Cheerios
    12                     Cinnamon Toast Crunch
    13                                  Clusters
    14                               Cocoa Puffs
    15                                 Corn Chex
    16                               Corn Flakes
    17                                 Corn Pops
    18                             Count Chocula
    19                        Cracklin' Oat Bran
    20                    Cream of Wheat (Quick)
    21                                   Crispix
    22                    Crispy Wheat & Raisins
    23                               Double Chex
    24                               Froot Loops
    25                            Frosted Flakes
    26                       Frosted Mini-Wheats
    27    Fruit & Fibre Dates; Walnuts; and Oats
    28                             Fruitful Bran
    29                            Fruity Pebbles
                           ...                  
    47                      Multi-Grain Cheerios
    48                          Nut&Honey Crunch
    49                 Nutri-Grain Almond-Raisin
    50                         Nutri-grain Wheat
    51                      Oatmeal Raisin Crisp
    52                     Post Nat. Raisin Bran
    53                                Product 19
    54                               Puffed Rice
    55                              Puffed Wheat
    56                        Quaker Oat Squares
    57                            Quaker Oatmeal
    58                               Raisin Bran
    59                           Raisin Nut Bran
    60                            Raisin Squares
    61                                 Rice Chex
    62                             Rice Krispies
    63                            Shredded Wheat
    64                    Shredded Wheat 'n'Bran
    65                 Shredded Wheat spoon size
    66                                    Smacks
    67                                 Special K
    68                   Strawberry Fruit Wheats
    69                         Total Corn Flakes
    70                         Total Raisin Bran
    71                         Total Whole Grain
    72                                   Triples
    73                                      Trix
    74                                Wheat Chex
    75                                  Wheaties
    76                       Wheaties Honey Gold
    Name: name, Length: 77, dtype: object




```python
type(df["name"])
```




    pandas.core.series.Series



## Pandas Series vs Numpy Arrays


```python
# There are many similarities between pd.Series and np.ndarray
# for example:
df["carbo"].mean()
```




    14.597402597402597




```python
# In fact, we can turn pd.Series into a numpy array
# again, this returns a numpy array -- df["carbo"] doesn't change.
df["carbo"].to_numpy()
```




    array([ 5. ,  8. ,  7. ,  8. , 14. , 10.5, 11. , 18. , 15. , 13. , 12. ,
           17. , 13. , 13. , 12. , 22. , 21. , 13. , 12. , 10. , 21. , 21. ,
           11. , 18. , 11. , 14. , 14. , 12. , 14. , 13. , 11. , 15. , 15. ,
           17. , 13. , 12. , 11.5, 14. , 17. , 20. , 21. , 12. , 12. , 16. ,
           16. , 16. , 17. , 15. , 15. , 21. , 18. , 13.5, 11. , 20. , 13. ,
           10. , 14. , -1. , 14. , 10.5, 15. , 23. , 22. , 16. , 19. , 20. ,
            9. , 16. , 15. , 21. , 15. , 16. , 21. , 13. , 17. , 17. , 16. ])




```python
# The key difference is that Series are indexed
# See the 0, 1, ... 76 on the left? That is the index of each item.
# Right now they are just positions, but theoretically they can be any unique identifier for the row
# Think: ID, username, etc
df["carbo"].index
```




    RangeIndex(start=0, stop=77, step=1)



## Indexing into DataFrames and Series


```python
# Indexing is a little bit different in pandas.
# One parallel to what you've been used to is .loc[]
# this is the row at index 0
df.loc[0]
```




    name        100% Bran
    mfr                 N
    type                C
    calories           70
    protein             4
    fat                 1
    sodium            130
    fiber              10
    carbo               5
    sugars              6
    potass            280
    vitamins           25
    shelf               3
    weight              1
    cups             0.33
    rating         68.403
    Name: 0, dtype: object




```python
# multiple indices work
df.loc[[1, 2, 3]]
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
      <th>name</th>
      <th>mfr</th>
      <th>type</th>
      <th>calories</th>
      <th>protein</th>
      <th>fat</th>
      <th>sodium</th>
      <th>fiber</th>
      <th>carbo</th>
      <th>sugars</th>
      <th>potass</th>
      <th>vitamins</th>
      <th>shelf</th>
      <th>weight</th>
      <th>cups</th>
      <th>rating</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>100% Natural Bran</td>
      <td>Q</td>
      <td>C</td>
      <td>120</td>
      <td>3</td>
      <td>5</td>
      <td>15</td>
      <td>2.0</td>
      <td>8.0</td>
      <td>8</td>
      <td>135</td>
      <td>0</td>
      <td>3</td>
      <td>1.0</td>
      <td>1.00</td>
      <td>33.983679</td>
    </tr>
    <tr>
      <th>2</th>
      <td>All-Bran</td>
      <td>K</td>
      <td>C</td>
      <td>70</td>
      <td>4</td>
      <td>1</td>
      <td>260</td>
      <td>9.0</td>
      <td>7.0</td>
      <td>5</td>
      <td>320</td>
      <td>25</td>
      <td>3</td>
      <td>1.0</td>
      <td>0.33</td>
      <td>59.425505</td>
    </tr>
    <tr>
      <th>3</th>
      <td>All-Bran with Extra Fiber</td>
      <td>K</td>
      <td>C</td>
      <td>50</td>
      <td>4</td>
      <td>0</td>
      <td>140</td>
      <td>14.0</td>
      <td>8.0</td>
      <td>0</td>
      <td>330</td>
      <td>25</td>
      <td>3</td>
      <td>1.0</td>
      <td>0.50</td>
      <td>93.704912</td>
    </tr>
  </tbody>
</table>
</div>




```python
# caveat: remember that pandas doesn't require zero-indexing. indices can be anything.
# this means slicing might not work all the time (what would df.loc["asdf":"hjkl"] even mean?)
# in the cases that you actually want to index by row number, you can always do that with .iloc[]
# again, this will behave the same as .loc[] with our dataset because our data is 0-indexed
df.iloc[0]
```




    name        100% Bran
    mfr                 N
    type                C
    calories           70
    protein             4
    fat                 1
    sodium            130
    fiber              10
    carbo               5
    sugars              6
    potass            280
    vitamins           25
    shelf               3
    weight              1
    cups             0.33
    rating         68.403
    Name: 0, dtype: object




```python
# We can also use boolean indexing by passing a list of booleans like so:
df[[True] + [False] * 76]
# Let me explain:
# - [True] + [False] * 76 gives us a list that looks like [True, False, ..., False] with 1 True and 76 Falses
# - This matches the number of rows in our data (77)
# - pandas returns all the rows with a corresponding True (in this case, only the first one)
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
      <th>name</th>
      <th>mfr</th>
      <th>type</th>
      <th>calories</th>
      <th>protein</th>
      <th>fat</th>
      <th>sodium</th>
      <th>fiber</th>
      <th>carbo</th>
      <th>sugars</th>
      <th>potass</th>
      <th>vitamins</th>
      <th>shelf</th>
      <th>weight</th>
      <th>cups</th>
      <th>rating</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>100% Bran</td>
      <td>N</td>
      <td>C</td>
      <td>70</td>
      <td>4</td>
      <td>1</td>
      <td>130</td>
      <td>10.0</td>
      <td>5.0</td>
      <td>6</td>
      <td>280</td>
      <td>25</td>
      <td>3</td>
      <td>1.0</td>
      <td>0.33</td>
      <td>68.402973</td>
    </tr>
  </tbody>
</table>
</div>




```python
# This is powerful because we can also make comparisons with Series and values.
df["protein"] > 3
```




    0      True
    1     False
    2      True
    3      True
    4     False
    5     False
    6     False
    7     False
    8     False
    9     False
    10    False
    11     True
    12    False
    13    False
    14    False
    15    False
    16    False
    17    False
    18    False
    19    False
    20    False
    21    False
    22    False
    23    False
    24    False
    25    False
    26    False
    27    False
    28    False
    29    False
          ...  
    47    False
    48    False
    49    False
    50    False
    51    False
    52    False
    53    False
    54    False
    55    False
    56     True
    57     True
    58    False
    59    False
    60    False
    61    False
    62    False
    63    False
    64    False
    65    False
    66    False
    67     True
    68    False
    69    False
    70    False
    71    False
    72    False
    73    False
    74    False
    75    False
    76    False
    Name: protein, Length: 77, dtype: bool




```python
# Combining these two things, we have a very expressive way of filtering.
# This gives us all the rows in which the protein is greater than 3.
df[df["protein"] > 3]
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
      <th>name</th>
      <th>mfr</th>
      <th>type</th>
      <th>calories</th>
      <th>protein</th>
      <th>fat</th>
      <th>sodium</th>
      <th>fiber</th>
      <th>carbo</th>
      <th>sugars</th>
      <th>potass</th>
      <th>vitamins</th>
      <th>shelf</th>
      <th>weight</th>
      <th>cups</th>
      <th>rating</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>100% Bran</td>
      <td>N</td>
      <td>C</td>
      <td>70</td>
      <td>4</td>
      <td>1</td>
      <td>130</td>
      <td>10.0</td>
      <td>5.0</td>
      <td>6</td>
      <td>280</td>
      <td>25</td>
      <td>3</td>
      <td>1.0</td>
      <td>0.33</td>
      <td>68.402973</td>
    </tr>
    <tr>
      <th>2</th>
      <td>All-Bran</td>
      <td>K</td>
      <td>C</td>
      <td>70</td>
      <td>4</td>
      <td>1</td>
      <td>260</td>
      <td>9.0</td>
      <td>7.0</td>
      <td>5</td>
      <td>320</td>
      <td>25</td>
      <td>3</td>
      <td>1.0</td>
      <td>0.33</td>
      <td>59.425505</td>
    </tr>
    <tr>
      <th>3</th>
      <td>All-Bran with Extra Fiber</td>
      <td>K</td>
      <td>C</td>
      <td>50</td>
      <td>4</td>
      <td>0</td>
      <td>140</td>
      <td>14.0</td>
      <td>8.0</td>
      <td>0</td>
      <td>330</td>
      <td>25</td>
      <td>3</td>
      <td>1.0</td>
      <td>0.50</td>
      <td>93.704912</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Cheerios</td>
      <td>G</td>
      <td>C</td>
      <td>110</td>
      <td>6</td>
      <td>2</td>
      <td>290</td>
      <td>2.0</td>
      <td>17.0</td>
      <td>1</td>
      <td>105</td>
      <td>25</td>
      <td>1</td>
      <td>1.0</td>
      <td>1.25</td>
      <td>50.764999</td>
    </tr>
    <tr>
      <th>41</th>
      <td>Life</td>
      <td>Q</td>
      <td>C</td>
      <td>100</td>
      <td>4</td>
      <td>2</td>
      <td>150</td>
      <td>2.0</td>
      <td>12.0</td>
      <td>6</td>
      <td>95</td>
      <td>25</td>
      <td>2</td>
      <td>1.0</td>
      <td>0.67</td>
      <td>45.328074</td>
    </tr>
    <tr>
      <th>43</th>
      <td>Maypo</td>
      <td>A</td>
      <td>H</td>
      <td>100</td>
      <td>4</td>
      <td>1</td>
      <td>0</td>
      <td>0.0</td>
      <td>16.0</td>
      <td>3</td>
      <td>95</td>
      <td>25</td>
      <td>2</td>
      <td>1.0</td>
      <td>1.00</td>
      <td>54.850917</td>
    </tr>
    <tr>
      <th>44</th>
      <td>Muesli Raisins; Dates; &amp; Almonds</td>
      <td>R</td>
      <td>C</td>
      <td>150</td>
      <td>4</td>
      <td>3</td>
      <td>95</td>
      <td>3.0</td>
      <td>16.0</td>
      <td>11</td>
      <td>170</td>
      <td>25</td>
      <td>3</td>
      <td>1.0</td>
      <td>1.00</td>
      <td>37.136863</td>
    </tr>
    <tr>
      <th>45</th>
      <td>Muesli Raisins; Peaches; &amp; Pecans</td>
      <td>R</td>
      <td>C</td>
      <td>150</td>
      <td>4</td>
      <td>3</td>
      <td>150</td>
      <td>3.0</td>
      <td>16.0</td>
      <td>11</td>
      <td>170</td>
      <td>25</td>
      <td>3</td>
      <td>1.0</td>
      <td>1.00</td>
      <td>34.139765</td>
    </tr>
    <tr>
      <th>56</th>
      <td>Quaker Oat Squares</td>
      <td>Q</td>
      <td>C</td>
      <td>100</td>
      <td>4</td>
      <td>1</td>
      <td>135</td>
      <td>2.0</td>
      <td>14.0</td>
      <td>6</td>
      <td>110</td>
      <td>25</td>
      <td>3</td>
      <td>1.0</td>
      <td>0.50</td>
      <td>49.511874</td>
    </tr>
    <tr>
      <th>57</th>
      <td>Quaker Oatmeal</td>
      <td>Q</td>
      <td>H</td>
      <td>100</td>
      <td>5</td>
      <td>2</td>
      <td>0</td>
      <td>2.7</td>
      <td>-1.0</td>
      <td>-1</td>
      <td>110</td>
      <td>0</td>
      <td>1</td>
      <td>1.0</td>
      <td>0.67</td>
      <td>50.828392</td>
    </tr>
    <tr>
      <th>67</th>
      <td>Special K</td>
      <td>K</td>
      <td>C</td>
      <td>110</td>
      <td>6</td>
      <td>0</td>
      <td>230</td>
      <td>1.0</td>
      <td>16.0</td>
      <td>3</td>
      <td>55</td>
      <td>25</td>
      <td>1</td>
      <td>1.0</td>
      <td>1.00</td>
      <td>53.131324</td>
    </tr>
  </tbody>
</table>
</div>



## Manipulating Series

Often when we're preprocessing data, we want to make uniform changes to a specific column. We can do this by applying functions.


```python
# Suppose we want to make the cereals more appetizing.
# Let's add "Delicious " to the beginning of every name.

# The pattern is we define a function for a single entry
def make_delicious(name):
    return "Delicious " + name

# and then call apply on the series to apply the function to each element in the series
df["name"].apply(make_delicious)
```




    0                                  Delicious 100% Bran
    1                          Delicious 100% Natural Bran
    2                                   Delicious All-Bran
    3                  Delicious All-Bran with Extra Fiber
    4                             Delicious Almond Delight
    5                    Delicious Apple Cinnamon Cheerios
    6                                Delicious Apple Jacks
    7                                    Delicious Basic 4
    8                                  Delicious Bran Chex
    9                                Delicious Bran Flakes
    10                              Delicious Cap'n'Crunch
    11                                  Delicious Cheerios
    12                     Delicious Cinnamon Toast Crunch
    13                                  Delicious Clusters
    14                               Delicious Cocoa Puffs
    15                                 Delicious Corn Chex
    16                               Delicious Corn Flakes
    17                                 Delicious Corn Pops
    18                             Delicious Count Chocula
    19                        Delicious Cracklin' Oat Bran
    20                    Delicious Cream of Wheat (Quick)
    21                                   Delicious Crispix
    22                    Delicious Crispy Wheat & Raisins
    23                               Delicious Double Chex
    24                               Delicious Froot Loops
    25                            Delicious Frosted Flakes
    26                       Delicious Frosted Mini-Wheats
    27    Delicious Fruit & Fibre Dates; Walnuts; and Oats
    28                             Delicious Fruitful Bran
    29                            Delicious Fruity Pebbles
                                ...                       
    47                      Delicious Multi-Grain Cheerios
    48                          Delicious Nut&Honey Crunch
    49                 Delicious Nutri-Grain Almond-Raisin
    50                         Delicious Nutri-grain Wheat
    51                      Delicious Oatmeal Raisin Crisp
    52                     Delicious Post Nat. Raisin Bran
    53                                Delicious Product 19
    54                               Delicious Puffed Rice
    55                              Delicious Puffed Wheat
    56                        Delicious Quaker Oat Squares
    57                            Delicious Quaker Oatmeal
    58                               Delicious Raisin Bran
    59                           Delicious Raisin Nut Bran
    60                            Delicious Raisin Squares
    61                                 Delicious Rice Chex
    62                             Delicious Rice Krispies
    63                            Delicious Shredded Wheat
    64                    Delicious Shredded Wheat 'n'Bran
    65                 Delicious Shredded Wheat spoon size
    66                                    Delicious Smacks
    67                                 Delicious Special K
    68                   Delicious Strawberry Fruit Wheats
    69                         Delicious Total Corn Flakes
    70                         Delicious Total Raisin Bran
    71                         Delicious Total Whole Grain
    72                                   Delicious Triples
    73                                      Delicious Trix
    74                                Delicious Wheat Chex
    75                                  Delicious Wheaties
    76                       Delicious Wheaties Honey Gold
    Name: name, Length: 77, dtype: object




```python
# this returns the changes, but doesn't apply them in place.
# that means on our original dataframe, the cereals are still bland
df.head()
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
      <th>name</th>
      <th>mfr</th>
      <th>type</th>
      <th>calories</th>
      <th>protein</th>
      <th>fat</th>
      <th>sodium</th>
      <th>fiber</th>
      <th>carbo</th>
      <th>sugars</th>
      <th>potass</th>
      <th>vitamins</th>
      <th>shelf</th>
      <th>weight</th>
      <th>cups</th>
      <th>rating</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>100% Bran</td>
      <td>N</td>
      <td>C</td>
      <td>70</td>
      <td>4</td>
      <td>1</td>
      <td>130</td>
      <td>10.0</td>
      <td>5.0</td>
      <td>6</td>
      <td>280</td>
      <td>25</td>
      <td>3</td>
      <td>1.0</td>
      <td>0.33</td>
      <td>68.402973</td>
    </tr>
    <tr>
      <th>1</th>
      <td>100% Natural Bran</td>
      <td>Q</td>
      <td>C</td>
      <td>120</td>
      <td>3</td>
      <td>5</td>
      <td>15</td>
      <td>2.0</td>
      <td>8.0</td>
      <td>8</td>
      <td>135</td>
      <td>0</td>
      <td>3</td>
      <td>1.0</td>
      <td>1.00</td>
      <td>33.983679</td>
    </tr>
    <tr>
      <th>2</th>
      <td>All-Bran</td>
      <td>K</td>
      <td>C</td>
      <td>70</td>
      <td>4</td>
      <td>1</td>
      <td>260</td>
      <td>9.0</td>
      <td>7.0</td>
      <td>5</td>
      <td>320</td>
      <td>25</td>
      <td>3</td>
      <td>1.0</td>
      <td>0.33</td>
      <td>59.425505</td>
    </tr>
    <tr>
      <th>3</th>
      <td>All-Bran with Extra Fiber</td>
      <td>K</td>
      <td>C</td>
      <td>50</td>
      <td>4</td>
      <td>0</td>
      <td>140</td>
      <td>14.0</td>
      <td>8.0</td>
      <td>0</td>
      <td>330</td>
      <td>25</td>
      <td>3</td>
      <td>1.0</td>
      <td>0.50</td>
      <td>93.704912</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Almond Delight</td>
      <td>R</td>
      <td>C</td>
      <td>110</td>
      <td>2</td>
      <td>2</td>
      <td>200</td>
      <td>1.0</td>
      <td>14.0</td>
      <td>8</td>
      <td>-1</td>
      <td>25</td>
      <td>3</td>
      <td>1.0</td>
      <td>0.75</td>
      <td>34.384843</td>
    </tr>
  </tbody>
</table>
</div>




```python
# we can fix this by assigning the new names to the column.
df["name"] = df["name"].apply(make_delicious)
df.head()
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
      <th>name</th>
      <th>mfr</th>
      <th>type</th>
      <th>calories</th>
      <th>protein</th>
      <th>fat</th>
      <th>sodium</th>
      <th>fiber</th>
      <th>carbo</th>
      <th>sugars</th>
      <th>potass</th>
      <th>vitamins</th>
      <th>shelf</th>
      <th>weight</th>
      <th>cups</th>
      <th>rating</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Delicious 100% Bran</td>
      <td>N</td>
      <td>C</td>
      <td>70</td>
      <td>4</td>
      <td>1</td>
      <td>130</td>
      <td>10.0</td>
      <td>5.0</td>
      <td>6</td>
      <td>280</td>
      <td>25</td>
      <td>3</td>
      <td>1.0</td>
      <td>0.33</td>
      <td>68.402973</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Delicious 100% Natural Bran</td>
      <td>Q</td>
      <td>C</td>
      <td>120</td>
      <td>3</td>
      <td>5</td>
      <td>15</td>
      <td>2.0</td>
      <td>8.0</td>
      <td>8</td>
      <td>135</td>
      <td>0</td>
      <td>3</td>
      <td>1.0</td>
      <td>1.00</td>
      <td>33.983679</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Delicious All-Bran</td>
      <td>K</td>
      <td>C</td>
      <td>70</td>
      <td>4</td>
      <td>1</td>
      <td>260</td>
      <td>9.0</td>
      <td>7.0</td>
      <td>5</td>
      <td>320</td>
      <td>25</td>
      <td>3</td>
      <td>1.0</td>
      <td>0.33</td>
      <td>59.425505</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Delicious All-Bran with Extra Fiber</td>
      <td>K</td>
      <td>C</td>
      <td>50</td>
      <td>4</td>
      <td>0</td>
      <td>140</td>
      <td>14.0</td>
      <td>8.0</td>
      <td>0</td>
      <td>330</td>
      <td>25</td>
      <td>3</td>
      <td>1.0</td>
      <td>0.50</td>
      <td>93.704912</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Delicious Almond Delight</td>
      <td>R</td>
      <td>C</td>
      <td>110</td>
      <td>2</td>
      <td>2</td>
      <td>200</td>
      <td>1.0</td>
      <td>14.0</td>
      <td>8</td>
      <td>-1</td>
      <td>25</td>
      <td>3</td>
      <td>1.0</td>
      <td>0.75</td>
      <td>34.384843</td>
    </tr>
  </tbody>
</table>
</div>




```python
# here's another example.
# Jackson is a skeptic and doesn't believe calling things "Delicious" makes them taste better.
# But he does think adding sugar will make them taste better.
# How can we add 10 grams of sugar to every cereal?
df["sugars"] = df["sugars"] + 10
df.head()
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
      <th>name</th>
      <th>mfr</th>
      <th>type</th>
      <th>calories</th>
      <th>protein</th>
      <th>fat</th>
      <th>sodium</th>
      <th>fiber</th>
      <th>carbo</th>
      <th>sugars</th>
      <th>potass</th>
      <th>vitamins</th>
      <th>shelf</th>
      <th>weight</th>
      <th>cups</th>
      <th>rating</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Delicious 100% Bran</td>
      <td>N</td>
      <td>C</td>
      <td>70</td>
      <td>4</td>
      <td>1</td>
      <td>130</td>
      <td>10.0</td>
      <td>5.0</td>
      <td>26</td>
      <td>280</td>
      <td>25</td>
      <td>3</td>
      <td>1.0</td>
      <td>0.33</td>
      <td>68.402973</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Delicious 100% Natural Bran</td>
      <td>Q</td>
      <td>C</td>
      <td>120</td>
      <td>3</td>
      <td>5</td>
      <td>15</td>
      <td>2.0</td>
      <td>8.0</td>
      <td>28</td>
      <td>135</td>
      <td>0</td>
      <td>3</td>
      <td>1.0</td>
      <td>1.00</td>
      <td>33.983679</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Delicious All-Bran</td>
      <td>K</td>
      <td>C</td>
      <td>70</td>
      <td>4</td>
      <td>1</td>
      <td>260</td>
      <td>9.0</td>
      <td>7.0</td>
      <td>25</td>
      <td>320</td>
      <td>25</td>
      <td>3</td>
      <td>1.0</td>
      <td>0.33</td>
      <td>59.425505</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Delicious All-Bran with Extra Fiber</td>
      <td>K</td>
      <td>C</td>
      <td>50</td>
      <td>4</td>
      <td>0</td>
      <td>140</td>
      <td>14.0</td>
      <td>8.0</td>
      <td>20</td>
      <td>330</td>
      <td>25</td>
      <td>3</td>
      <td>1.0</td>
      <td>0.50</td>
      <td>93.704912</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Delicious Almond Delight</td>
      <td>R</td>
      <td>C</td>
      <td>110</td>
      <td>2</td>
      <td>2</td>
      <td>200</td>
      <td>1.0</td>
      <td>14.0</td>
      <td>28</td>
      <td>-1</td>
      <td>25</td>
      <td>3</td>
      <td>1.0</td>
      <td>0.75</td>
      <td>34.384843</td>
    </tr>
  </tbody>
</table>
</div>



## Groups and Aggregates

When we have lots and lots of data, it's more useful to look at aggregate statistics like the mean or median. But sometimes we lose too much detail aggregating across the whole dataset.

The solution is to aggregate across groups. For example, maybe we're less interested in the mean calorie count of all cereals and more interested in the mean for each manufacturer.


```python
# First, we can see how many (and which) unique manufacturers there are
# Note: this gives us a numpy array
df["mfr"].unique()
```




    array(['N', 'Q', 'K', 'R', 'G', 'P', 'A'], dtype=object)




```python
# Now let's group by the manufacturers
# This gives us a groupby object across the dataframe
mfrs = df.groupby("mfr")
mfrs
```




    <pandas.core.groupby.generic.DataFrameGroupBy object at 0x7f78839de690>




```python
# what happens if we try to access the calories column?
mfrs["calories"]
```




    <pandas.core.groupby.generic.SeriesGroupBy object at 0x7f78839de550>




```python
# now let's try to get the mean
mfrs["calories"].mean()
```




    mfr
    A    100.000000
    G    111.363636
    K    108.695652
    N     86.666667
    P    108.888889
    Q     95.000000
    R    115.000000
    Name: calories, dtype: float64




```python
# we can also aggregate across multiple columns, and even use different aggregations
# let's get the average calorie count but the maximum protein
mfrs[["calories", "protein"]].agg({"calories": "mean", "protein": "max"})
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
      <th>calories</th>
      <th>protein</th>
    </tr>
    <tr>
      <th>mfr</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>100.000000</td>
      <td>4</td>
    </tr>
    <tr>
      <th>G</th>
      <td>111.363636</td>
      <td>6</td>
    </tr>
    <tr>
      <th>K</th>
      <td>108.695652</td>
      <td>6</td>
    </tr>
    <tr>
      <th>N</th>
      <td>86.666667</td>
      <td>4</td>
    </tr>
    <tr>
      <th>P</th>
      <td>108.888889</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Q</th>
      <td>95.000000</td>
      <td>5</td>
    </tr>
    <tr>
      <th>R</th>
      <td>115.000000</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



# Exercises

Unless otherwise noted, these should be one line of code.


```python
# here is a Python list:

a = [1, 2, 3, 4, 5, 6]

# get a list containing the last 3 elements of a
print(a[-3:])
# reverse the list
print(a[::-1])
# get a list where each entry in a is squared (so the new list is [1, 4, 9, 16, 25, 36])
print([i**2 for i in a])
```

    [4, 5, 6]
    [6, 5, 4, 3, 2, 1]
    [1, 4, 9, 16, 25, 36]



```python
# create a numpy array from this list
b = np.array(a)
```


```python
# find the mean of b
b.mean()
```




    3.5




```python
# change b from a length-6 list to a 2x3 matrix
b = b.reshape((2,3))
```


```python
# find the mean value of each row
np.mean(b, axis = 1)
```




    array([2., 5.])




```python
# find the mean value of each column
np.mean(b, axis = 0)
```




    array([2.5, 3.5, 4.5])




```python
# find the third column of b
b[:,2]
```




    array([3, 6])




```python
# get a list where each entry in b is cubed (so the new numpy array is [1, 4, 9, 16, 25, 36])
# use a different (numpy-specific) approach
b ** 2
```




    array([[ 1,  4,  9],
           [16, 25, 36]])




```python
# load in the "starbucks.csv" dataset
data = pd.read_csv('starbucks.csv')
```


```python
# this is nutritional info for starbucks items
# let's see if we can answer some questions

# what is the average # calories across all items?
data.Calories.mean()
```




    193.87190082644628




```python
# how many different categories of beverages are there?
len(data.Beverage_category.unique())
```




    9




```python
# what is the average # calories for each beverage category?
data.groupby('Beverage_category').agg({'Calories': 'mean'})
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
      <th>Calories</th>
    </tr>
    <tr>
      <th>Beverage_category</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Classic Espresso Drinks</th>
      <td>140.172414</td>
    </tr>
    <tr>
      <th>Coffee</th>
      <td>4.250000</td>
    </tr>
    <tr>
      <th>Frappuccino® Blended Coffee</th>
      <td>276.944444</td>
    </tr>
    <tr>
      <th>Frappuccino® Blended Crème</th>
      <td>233.076923</td>
    </tr>
    <tr>
      <th>Frappuccino® Light Blended Coffee</th>
      <td>162.500000</td>
    </tr>
    <tr>
      <th>Shaken Iced Beverages</th>
      <td>114.444444</td>
    </tr>
    <tr>
      <th>Signature Espresso Drinks</th>
      <td>250.000000</td>
    </tr>
    <tr>
      <th>Smoothies</th>
      <td>282.222222</td>
    </tr>
    <tr>
      <th>Tazo® Tea Drinks</th>
      <td>177.307692</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.columns
```




    Index(['Beverage_category', 'Beverage', 'Beverage_prep', 'Calories',
           ' Total Fat (g)', 'Trans Fat (g) ', 'Saturated Fat (g)', ' Sodium (mg)',
           ' Total Carbohydrates (g) ', 'Cholesterol (mg)', ' Dietary Fibre (g)',
           ' Sugars (g)', ' Protein (g) ', 'Vitamin A (% DV) ', 'Vitamin C (% DV)',
           ' Calcium (% DV) ', 'Iron (% DV) ', 'Caffeine (mg)'],
          dtype='object')




```python
# what beverage preparation includes the most sugar?
data.loc[data[' Sugars (g)'].idxmax(axis = 0), 'Beverage_prep']
```




    'Venti Nonfat Milk'




```python
data.head()
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
      <th>Beverage_category</th>
      <th>Beverage</th>
      <th>Beverage_prep</th>
      <th>Calories</th>
      <th>Total Fat (g)</th>
      <th>Trans Fat (g)</th>
      <th>Saturated Fat (g)</th>
      <th>Sodium (mg)</th>
      <th>Total Carbohydrates (g)</th>
      <th>Cholesterol (mg)</th>
      <th>Dietary Fibre (g)</th>
      <th>Sugars (g)</th>
      <th>Protein (g)</th>
      <th>Vitamin A (% DV)</th>
      <th>Vitamin C (% DV)</th>
      <th>Calcium (% DV)</th>
      <th>Iron (% DV)</th>
      <th>Caffeine (mg)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Coffee</td>
      <td>Brewed Coffee</td>
      <td>Short</td>
      <td>3</td>
      <td>0.1</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.3</td>
      <td>0%</td>
      <td>0%</td>
      <td>0%</td>
      <td>0%</td>
      <td>175</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Coffee</td>
      <td>Brewed Coffee</td>
      <td>Tall</td>
      <td>4</td>
      <td>0.1</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>10</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.5</td>
      <td>0%</td>
      <td>0%</td>
      <td>0%</td>
      <td>0%</td>
      <td>260</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Coffee</td>
      <td>Brewed Coffee</td>
      <td>Grande</td>
      <td>5</td>
      <td>0.1</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>10</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1.0</td>
      <td>0%</td>
      <td>0%</td>
      <td>0%</td>
      <td>0%</td>
      <td>330</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Coffee</td>
      <td>Brewed Coffee</td>
      <td>Venti</td>
      <td>5</td>
      <td>0.1</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>10</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1.0</td>
      <td>0%</td>
      <td>0%</td>
      <td>2%</td>
      <td>0%</td>
      <td>410</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Classic Espresso Drinks</td>
      <td>Caffè Latte</td>
      <td>Short Nonfat Milk</td>
      <td>70</td>
      <td>0.1</td>
      <td>0.1</td>
      <td>0.0</td>
      <td>5</td>
      <td>75</td>
      <td>10</td>
      <td>0</td>
      <td>9</td>
      <td>6.0</td>
      <td>10%</td>
      <td>0%</td>
      <td>20%</td>
      <td>0%</td>
      <td>75</td>
    </tr>
  </tbody>
</table>
</div>




```python
# what is the average % daily value calcium content for each beverage?
# HINT: make sure your columns have the datatypes you want
# (you can use more than one line for this one)
def percent_to_number(x):
    return(int(x.strip('%')))

data[' Calcium (% DV) '] = data[' Calcium (% DV) '].apply(percent_to_number)
```


```python
data.groupby('Beverage').agg({' Calcium (% DV) ': 'mean'})
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
      <th>Calcium (% DV)</th>
    </tr>
    <tr>
      <th>Beverage</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Banana Chocolate Smoothie</th>
      <td>20.000000</td>
    </tr>
    <tr>
      <th>Brewed Coffee</th>
      <td>0.500000</td>
    </tr>
    <tr>
      <th>Caffè Americano</th>
      <td>1.500000</td>
    </tr>
    <tr>
      <th>Caffè Latte</th>
      <td>35.000000</td>
    </tr>
    <tr>
      <th>Caffè Mocha (Without Whipped Cream)</th>
      <td>30.000000</td>
    </tr>
    <tr>
      <th>Cappuccino</th>
      <td>22.500000</td>
    </tr>
    <tr>
      <th>Caramel</th>
      <td>11.000000</td>
    </tr>
    <tr>
      <th>Caramel (Without Whipped Cream)</th>
      <td>12.000000</td>
    </tr>
    <tr>
      <th>Caramel Apple Spice (Without Whipped Cream)</th>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>Caramel Macchiato</th>
      <td>28.333333</td>
    </tr>
    <tr>
      <th>Coffee</th>
      <td>12.333333</td>
    </tr>
    <tr>
      <th>Espresso</th>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>Hot Chocolate (Without Whipped Cream)</th>
      <td>35.000000</td>
    </tr>
    <tr>
      <th>Iced Brewed Coffee (With Classic Syrup)</th>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>Iced Brewed Coffee (With Milk &amp; Classic Syrup)</th>
      <td>8.000000</td>
    </tr>
    <tr>
      <th>Java Chip</th>
      <td>11.666667</td>
    </tr>
    <tr>
      <th>Java Chip (Without Whipped Cream)</th>
      <td>12.555556</td>
    </tr>
    <tr>
      <th>Mocha</th>
      <td>11.000000</td>
    </tr>
    <tr>
      <th>Mocha (Without Whipped Cream)</th>
      <td>12.000000</td>
    </tr>
    <tr>
      <th>Orange Mango Banana Smoothie</th>
      <td>10.000000</td>
    </tr>
    <tr>
      <th>Shaken Iced Tazo® Tea (With Classic Syrup)</th>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>Shaken Iced Tazo® Tea Lemonade (With Classic Syrup)</th>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>Skinny Latte (Any Flavour)</th>
      <td>33.750000</td>
    </tr>
    <tr>
      <th>Strawberries &amp; Crème (Without Whipped Cream)</th>
      <td>15.000000</td>
    </tr>
    <tr>
      <th>Strawberry Banana Smoothie</th>
      <td>10.000000</td>
    </tr>
    <tr>
      <th>Tazo® Chai Tea Latte</th>
      <td>21.666667</td>
    </tr>
    <tr>
      <th>Tazo® Full-Leaf Red Tea Latte (Vanilla Rooibos)</th>
      <td>20.833333</td>
    </tr>
    <tr>
      <th>Tazo® Full-Leaf Tea Latte</th>
      <td>20.833333</td>
    </tr>
    <tr>
      <th>Tazo® Green Tea Latte</th>
      <td>39.166667</td>
    </tr>
    <tr>
      <th>Tazo® Tea</th>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>Vanilla Bean (Without Whipped Cream)</th>
      <td>11.250000</td>
    </tr>
    <tr>
      <th>Vanilla Latte (Or Other Flavoured Latte)</th>
      <td>32.916667</td>
    </tr>
    <tr>
      <th>White Chocolate Mocha (Without Whipped Cream)</th>
      <td>41.250000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# It's bulking season. What drink should Jackson get so that he maximizes protein but minimizes fat?
# (you can use more than one line for this one)
data.sort_values(by = [' Protein (g) ',' Total Fat (g)'], ascending=[False, True]).head()
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
      <th>Beverage_category</th>
      <th>Beverage</th>
      <th>Beverage_prep</th>
      <th>Calories</th>
      <th>Total Fat (g)</th>
      <th>Trans Fat (g)</th>
      <th>Saturated Fat (g)</th>
      <th>Sodium (mg)</th>
      <th>Total Carbohydrates (g)</th>
      <th>Cholesterol (mg)</th>
      <th>Dietary Fibre (g)</th>
      <th>Sugars (g)</th>
      <th>Protein (g)</th>
      <th>Vitamin A (% DV)</th>
      <th>Vitamin C (% DV)</th>
      <th>Calcium (% DV)</th>
      <th>Iron (% DV)</th>
      <th>Caffeine (mg)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>172</th>
      <td>Smoothies</td>
      <td>Banana Chocolate Smoothie</td>
      <td>Grande Nonfat Milk</td>
      <td>280</td>
      <td>2.5</td>
      <td>1.5</td>
      <td>0.0</td>
      <td>5</td>
      <td>150</td>
      <td>53</td>
      <td>7</td>
      <td>34</td>
      <td>20.0</td>
      <td>10%</td>
      <td>15%</td>
      <td>20</td>
      <td>0%</td>
      <td>Varies</td>
    </tr>
    <tr>
      <th>173</th>
      <td>Smoothies</td>
      <td>Banana Chocolate Smoothie</td>
      <td>2% Milk</td>
      <td>300</td>
      <td>5.0</td>
      <td>2.5</td>
      <td>0.1</td>
      <td>15</td>
      <td>160</td>
      <td>53</td>
      <td>7</td>
      <td>34</td>
      <td>20.0</td>
      <td>8%</td>
      <td>15%</td>
      <td>20</td>
      <td>20%</td>
      <td>15</td>
    </tr>
    <tr>
      <th>174</th>
      <td>Smoothies</td>
      <td>Banana Chocolate Smoothie</td>
      <td>Soymilk</td>
      <td>290</td>
      <td>4.5</td>
      <td>1.5</td>
      <td>0.0</td>
      <td>5</td>
      <td>150</td>
      <td>51</td>
      <td>7</td>
      <td>31</td>
      <td>19.0</td>
      <td>6%</td>
      <td>15%</td>
      <td>20</td>
      <td>20%</td>
      <td>15</td>
    </tr>
    <tr>
      <th>83</th>
      <td>Signature Espresso Drinks</td>
      <td>White Chocolate Mocha (Without Whipped Cream)</td>
      <td>Venti Nonfat Milk</td>
      <td>450</td>
      <td>7.0</td>
      <td>6.0</td>
      <td>0.0</td>
      <td>10</td>
      <td>310</td>
      <td>78</td>
      <td>0</td>
      <td>74</td>
      <td>19.0</td>
      <td>25%</td>
      <td>2%</td>
      <td>60</td>
      <td>2%</td>
      <td>150</td>
    </tr>
    <tr>
      <th>84</th>
      <td>Signature Espresso Drinks</td>
      <td>White Chocolate Mocha (Without Whipped Cream)</td>
      <td>2% Milk</td>
      <td>510</td>
      <td>15.0</td>
      <td>9.0</td>
      <td>0.2</td>
      <td>35</td>
      <td>330</td>
      <td>77</td>
      <td>0</td>
      <td>74</td>
      <td>19.0</td>
      <td>20%</td>
      <td>4%</td>
      <td>60</td>
      <td>2%</td>
      <td>150</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
