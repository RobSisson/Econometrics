import numpy as np
import scipy as sp
from scipy.stats import gmean
import pandas as pd
from decimal import *


def Value(
        price, quantity
):

    array = []
    for i, item in enumerate(price):
        array.append(price[i]*quantity[i])

    result = np.sum(array)

    return result


"""
Price Index Formulas
"""


# prices_Quantities is a dictionary matching prices to Quantities
# price - a list of t1 prices
# quantity - quantities corresponding to the t1 price list
#
# t2_price - a list of t2 prices
# t2_quantity - quantities corresponding to the t2 price list

# Geometric Mean Index

# N a period of time
# Pn is price per unit in period N
# Qn is the quantity produced in period N
# Vn is the value of the units produced in period N, calculated by Pn*Qn


def Geometric_Mean_Index_Not_Iterative(
        price, quantity, t2_price
):
    # Not iterative; test for result?

    return np.prod((t2_price / price) ** (price * quantity)) ** (
                1 / np.sum(price * quantity))


def Geometric_Mean_Index_Weighted(
        price, quantity, t2_price
):
    # Weighted Geo Mean Index
    # product of ( (t2_price[i]/price[i]) to the power of
    # (price[i]*quantity[i] / sum of (price*quantity)) ),
    # where i is between 1 and the length of price
    # product done last (incorrect order?)
    array_weighted=()

    for i, item in enumerate(price):
        power=item * quantity[i] / np.sum(price * quantity)
        # power is price[i]*quantity[i]/np.sum(price*quantity)
        brackets=t2_price[i] / item
        # brackets is t2_price[i] / price[i]
        array_weighted.append(brackets ** power)

    weighted_geo_mean_result=np.prod(array_weighted)
    return weighted_geo_mean_result


def Single_Geometric_Mean_Index_Unweighted(
        price, quantity, t2_price
):
    # Single Value? t1d on https://mathworld.wolfram.com/GeometricMeanIndex.html

    unit_value=price * quantity

    product=np.prod((t2_price / price) ** unit_value)

    single_gm=product ** 1 / np.sum(unit_value)

    return single_gm


def Series_Geometric_Mean_Index_Unweighted(
        price, quantity, t2_price
):
    # Unweighted Geo Mean Index
    # (product of t2_price[i]/price[i], where i = 1 to length of price) to the power of 1/length of price)
    # rooting done last (correct order?)
    array_simple=()

    for i in enumerate(price):
        unit_value_of_i_at_time=price[i] * quantity[i]

        np.prod((t2_price[i] / price[i]) ** unit_value_of_i_at_time)

        1 / np.sum()

    for index, item in enumerate(price):
        array_simple.append(t2_price[index] / item)

    simple_geo_mean_result=Geometric_Mean(np.prod(array_simple))

    return simple_geo_mean_result

    # Below can be added to the above to avoid errors due to different lengths of price and t2_price
    #
    # len_price=len(price)
    # len_t2_price=len(t2_price)
    #
    # length = len_price
    #
    # if len_price != len_t2_price:
    #     print('There are ' + str(len_price) + ' in price, while ' + str(len_t2_price) + ' in len_t2_price. Adjust data if possible.')
    #
    #     length_difference=len_price-len_t2_price
    #
    #     if length_difference > 0:
    #         length = len_t2_price
    #         print('For now, the first '+str(len_t2_price)+' will be processed.')
    #     else:
    #         length = len_price
    #         print('For now, the first '+str(len_price)+' will be processed.')


# -------- Unweighted / Elementary Indicies
""" Unweighted, or "elementary", price indices only compare prices of a single type of good between two periods. 
They do not make any use of quantities or expenditure weights. 

They are called "elementary" because they are often used at the lower levels of aggregation for more comprehensive 
price indices. 

In such a case, they are not indices but merely an intermediate stage in the calculation of an index. 

At these lower levels, it is argued that weighting is not necessary since only one type of good is being aggregated.
 
However this implicitly assumes that only one type of the good is available (e.g. only one brand and one package size
of frozen peas) and that it has not changed in quality etc between time periods."""


# https://en.wikipedia.org/wiki/Gian_Rinaldo_Carli
# The Carli index for i = 1,.…, n products.
# It is defined as the simple, or unweighted, arithmetic mean of the price relatives, or price ratios,
# for the two periods, 0 and t, to be compared.

# 1 / n ( Sum of (t2_price[i]/price[i]) )
def Carli_Price_Index(
        price, t2_price
):
    array=[]
    for i, item in enumerate(price):
        array.append(t2_price[i] / price[i])

    sum_total=np.sum(array)

    result=sum_total / len(price)  # result = (1/len(price))*sum_total

    return result


def Dutot_Price_Index(
        price, t2_price
):
    t2_price_sum = np.sum(t2_price) / len(t2_price)
    price_sum = np.sum(price) / len(price)

    result=t2_price_sum / price_sum

    return result


def Jevons_Price_Index(
        price, t2_price
):
    # Method 1: Unweighted geometric mean of the price relative
    array=[]

    for i, item in enumerate(price):
        array.append(t2_price[i] / price[i])

    method_1=np.prod(array) ** (1.0 / len(t2_price))

    # Method 2: Ratio of the unweighted geometric mean prices

    method_2=(np.prod(t2_price) ** (1.0 / len(t2_price))) / (np.prod(price) ** (1.0 / len(price)))

    # print(method_2)

    return method_1



def Current_to_Current_Index(
        type, data
):
    result=[1]

    print('Computing individual values for '+str(len(data))+' values')

    for i, item in enumerate(data):
        try:
            if type == 'C':
                result.append(Carli_Price_Index(data[i], data[i+1]))
            elif type == 'D':
                result.append(Dutot_Price_Index(data[i], data[i+1]))
            elif type == 'J':
                result.append(Jevons_Price_Index(data[i], data[i+1]))
            else:
                print('Please insert either C, D, or J')
        except:
            print('All values calculated')

    return result


# !!! Combine current to current, chained, and direct index into one function?




# Type can be any of the following:
# C = Carli
# D = Dutot
# J = Jevons

# data can either be a list of lists, a numpy array, or a pandas dataframe


def Chained_Elementary_Aggregates(
        type, data
):
    result=[1]

    print('Computing individual values for '+str(len(data))+' values')

    for i, item in enumerate(data):
        try:
            if type == 'C':
                result.append(Carli_Price_Index(data[i], data[i+1]))
                print(data[i])
                print(data[i+1])
                print(Carli_Price_Index(data[i], data[i+1]))
            elif type == 'D':
                result.append(Dutot_Price_Index(data[i], data[i+1]))
            elif type == 'J':
                result.append(Jevons_Price_Index(data[i], data[i+1]))
            else:
                print('Please insert either C, D, or J')
        except:
            print('All values calculated')

    final=[]

    for i, item in enumerate(result):
        final.append(np.prod(result[0:i+1]))
        if type == 'C':
            print('asdfosd')
            print(np.prod(result[0:i+1]))


    if type == 'C':
        print('here')
        print(final)

    return final


def Direct_Index_On_t1(
        type, price_data
):
    result=[1]

    print('Computing individual values for '+str(len(price_data))+' values')

    for i, item in enumerate(price_data):
        try:
            if type == 'C':
                result.append(Carli_Price_Index(price_data[0], price_data[i+1]))
            elif type == 'D':
                result.append(Dutot_Price_Index(price_data[0], price_data[i+1]))
            elif type == 'J':
                result.append(Jevons_Price_Index(price_data[0], price_data[i+1]))
            else:
                print('Please insert either C, D, or J')
        except:
            print('All values calculated')

    return result


def Arithmetic_Mean_Series(
        data
):
    result=[]

    for i, item in enumerate(data):
        result.append(np.mean(data[i]))

    return result


# Self-Calculated Geo Mean (can also use scipy 'gmean' function)
def Geometric_Mean(iterable):
    numpy_array=np.array(iterable)
    return numpy_array.prod() ** (1.0 / len(numpy_array))


#   return root(np.sum(array),len(array)) Alt method using root function
# def root(number, power):
#     res = np.power(np.abs(number),1./power)
#     return res

# Minimising overflow chances (only required for values above 1.7976931348623157e+308 in 64 bit Python)
def Geometric_Mean_Overflow(iterable):
    a=np.log(iterable)
    return np.exp(a.mean())


def Geometric_Mean_Series(
        type, data
):
    result=[]

    for i, item in enumerate(data):
        if type == 'N':
            result.append(Geometric_Mean(data[i]))
        elif type == 'O':
            result.append(Geometric_Mean_Overflow(data[i]))
        else:
            print('Please insert either N or O')

    return result


# def Current_to_Previous_Price_Relatives(
#         data
# ):
#     result=[]
#     for i, product in enumerate(data):
#         for a, item in enumerate(product):
#             try:
#                 result.append(item / data[i][a])
#             except:
#                 print('Collected')
#     return result


def Current_to_Previous_Price_Relatives(
        data
):
    result=np.zeros_like(data)
    # print(result)
    for list_number, column in enumerate(data):
        for product_number, product in enumerate(column):
            try:
                result[list_number+1, product_number]=(data[list_number+1][product_number] / product)
            except:
                a=0
    for i, product in enumerate(result[0]):
        result[0, i]=1

    return result


def Current_to_Reference_Price_Relatives(
        data, reference_column
):
    result=np.zeros_like(data)
    for list_number, column in enumerate(data):
        for product_number, product in enumerate(column):
            try:
                result[list_number, product_number]=(product / data[reference_column][product_number])
            except:
                a=0
    for i, product in enumerate(result[0]):
        result[0, i]=1

    return result


def Share_of_Actual_Expenditure(
        price, quantity
):
    array=[]

    for i, item in enumerate(quantity):
        array.append(quantity[i] * price[i] / (sum(quantity[i] * price[i])))

    return array




# Lowe Index
# If quantity = quantity ---> Laspeyres Index
# If quantity = t2_quantity ---> Paasche Index
# Transitive
# Sum of Pt+1 * Qb / Sum of P0 * Qb            Sum of Pt+1 * Qb
# ---------------------------------     =     -----------------    =     P Lowe  T, T+1
# Sum of qt * Qb / Sum of P0 * Qb              Sum of qt * Qb
#

# Lowe >= Laspeyres >= Fisher >= Paasche

def Lowe_Price_Index(
    price, t2_price, quantity_any_time # can be between t1 and t2
):
    t1 = []
    t2 = []

    for i, item in enumerate(price):
        t1.append(price[i]*quantity_any_time[i])
        t2.append(t2_price[i] * quantity_any_time[i])

    return np.sum(t2) / np.sum(t1)


def Chain_Lowe_Price_Index(
    price, t2_price, quantity_at_minus_constant # can be between 0 and t
):
    t1 = []
    t2 = []

    for i, item in enumerate(price):
        t1.append(price[i]*quantity_any_time[i])
        t2.append(t2_price[i] * quantity_any_time[i])

    return np.sum(t2) / np.sum(t1)

#  Laspeyres >= the geometric Laspeyres and Paasche >= the ordinary Paasche

# Laspeyres - 1871
# https://en.wikipedia.org/wiki/%C3%89tienne_Laspeyres
# Compares the total cost of the same basket of final goods, with the t1 quantity, at the t1 and t2 prices.

# Sum of Pt2 * Qt1
# ----------------
# Sum of Pt1 * Qt1

def Laspeyres_Price_Index(
        price, quantity, t2_price
):
    t1=[]
    t2=[]

    for i, item in enumerate(price):
        t1.append(price[i] * quantity[i])
        t2.append(t2_price[i] * quantity[i])

    result= (np.sum(t2) / np.sum(t1))
    
    # array = []
    # for i, item in enumerare(price):
    #     array.append((price[i]/t2_price[i]) * Share_of_Actual_Expenditure(price[i], quantity[i]))
    # 
    # result_1 = np.sum(array)

    return result

price = pd.read_csv('Price.csv')
quantity = pd.read_csv('Quantity.csv')

period_list = price.columns.values
period_list = period_list[1:]
print(period_list)
array=[]

for i, period in enumerate(period_list):
    if i+1 != len(period_list):
        price_list = price['Period 1'].tolist()
        quantity_list = quantity['Period 1'].tolist()
        price_2_list = price[period_list[i+1]].tolist()
        array.append(Laspeyres_Price_Index(price_list, quantity_list, price_2_list))

print(array)
# print(Laspeyres_Price_Index([1,1,1,1,1,1], [1,1,2,1,4.5,0.5], [1.2,3,1.3,0.7,1.4,0.8]))


carl=[]

for i, period in enumerate(period_list):
    if i+1 != len(period_list):
        price_list = price['Period 1'].tolist()
        quantity_list = quantity['Period 1'].tolist()
        price_2_list = price[period_list[i+1]].tolist()
        carl.append(Carli_Price_Index(price_list, price_2_list))
print('carl')
print(carl)

jev=[]

for i, period in enumerate(period_list):
    if i+1 != len(period_list):
        price_list = price['Period 1'].tolist()
        quantity_list = quantity['Period 1'].tolist()
        price_2_list = price[period_list[i+1]].tolist()
        jev.append(Jevons_Price_Index(price_list, price_2_list))
print('jev')
print(jev)


# Passche - 1874
# https://en.wikipedia.org/wiki/Hermann_Paasche
# Compares the total cost of the same basket of final goods, with the t2 quantity, at the t1 and t2 prices.

# Sum of Pt2 * Qt2
# ----------------
# Sum of Pt1 * Qt2

def Paasche_Price_Index(
        price, t2_price, t2_quantity
):
    t1=[]
    t2=[]

    for i, item in enumerate(price):
        t1.append(price[i] * t2_quantity[i])
        t2.append(t2_price[i] * t2_quantity[i])

    result=np.sum(t2) / np.sum(t1)

    return result

# Sum of W(Pt2 * Qt1)
# -------------------
# Sum of W(Pt1 * Qt1)

p = []
for i, period in enumerate(period_list):
    if i+1 != len(period_list):
        price_list=price['Period 1'].tolist()
        quantity_2_list=quantity[period_list[i+1]].tolist()
        price_2_list=price[period_list[i+1]].tolist()
        p.append(Paasche_Price_Index(price_list, price_2_list, quantity_2_list))

print('pas')
print(p)

def Laspeyres_Price_Index_Weight(
        price, quantity, t2_price, t2_quantity,
):
    array = []

    weight = Share_of_Actual_Expenditure(quantity)

    for i, item in enumerate(price):
        t1.append(weight[i] * (price[i] * quantity[i]))
        t2.append(weight[i] * (t2_price[i] * quantity[i]))

    result=np.sum(array)

    return result


def Share_of_Quantity(
        quantity
):
    array = []

    for i, item in enumerate(quantity):
        array.append(quantity[i] / np.sum(quantity))

    return array


def Geometric_Laspeyres_Index(
        price, weight, t2_price
):
    array=[]

    for i, item in enumerate(price):
        array.append(t2_price[i] ** weight[i] / price[i] ** weight[i])

    method_1=np.prod(array)

    top=[]
    bot=[]

    for i, item in enumerate(t2_price):
        top.append(t2_price[i] ** weight[i])

    for i, item in enumerate(price):
        bot.append(price[i] ** weight[i])

    method_2=np.prod(top) / np.prod(bot)

    return method_1

# Lowe's Develops into:
# The Fisher price index, the Törnqvist price index and the Walsh price index are superlative indices.
# A basic characteristic of these indices is that they are symmetric indices.


# Fisher Index
def Fisher_Price_Index(
        price, quantity, t2_price, t2_quantity
):
    # if weight == 1:
    #     weight = []
    #     for i in price:
    #         weight.append(1/len(price))
    #     print(weight)

    result=np.sqrt(Laspeyres_Price_Index(price, quantity, t2_price) *
                   Paasche_Price_Index(price, t2_price, t2_quantity))
    return result


# -------- Superlative Indices
# Superlative indices are price or quantity indices that are ‘exact’ for a flexible aggregator.
# A flexible aggregator is a second-order approximation to an arbitrary production, cost, utility or distance function.
# Exactness implies that a particular index number can be directly derived from a specific flexible aggregator.
#

# Törnqvist Index (ö changed in function name for ease of calling)
def Tornqvist_Price_Index(
        price, t2_price, share, t2_share
):
    array = []

    for i in enumerate(price):
        array.append((t2_price[i]/price[i])**Average_Share_Of_Expenditure(share, t2_share)[i])

    result = np.prod(array)
    return result

def Average_Share_Of_Expenditure(
        share, t2_share
):
    array = []
    for i in enumerate(share):
        array.append((share[i]+t2_share[i])/2)

    return array

# Walsh Index
# Commodities are to be weighted according to their importance, or their full values.
# But the problem of axiometry always involves at least two periods.
# There is a first period, and there is a second period which is compared with it.
# Price variations have taken place between the two, and these are to be averaged
# to get the amount of their variation as a whole.
# But the weights of the commodities at the second period are apt to be different from
# their weights at the first period.
# Which weights, then, are the right ones – those of the first period? Or those of the
# second? Or should there be a combination of the two sets?
# There is no reason for preferring either the first or the second.
# Then the combination of both would seem to be the proper answer.
# And this combination itself involves an averaging of the weights of the two periods (Walsh, 1921a, p. 90)).

# As Walsh (1901, p. 105; 1921a) primarily states that a mean of the quantities is required, though does recommend
# the use of the Geometric Mean, all means available within the Walsh_Price_Index function;
# selectable with the following mean_types (editable below):
# 'G' --> Geometric Mean (Walsh_Price_Index)
# 'A' --> Arithmetic Mean (Marshall-Edgeworth Index)
# 'R' --> Mean of Order r (edit r_value below)
# 'H' --> Harmonic Mean (Not yet installed !!!)


r_value = 1

mean_type = 'G'

def Walsh_Price_Index(
        price, quantity, t2_price, t2_quantity,
):
    t1 = []
    t2 = []

    mean_quantity =[]

    for i, item in enumerate(price):
        if mean_type == 'G':
            mean_quantity.append(np.sqrt((quantity[i]*t2_quantity[i])))
        elif mean_type == 'A':
            mean_quantity.append((quantity[i] * t2_quantity[i])/2)
        elif mean_type == 'R':
            mean_quantity.append(((1/2*quantity[i]**r_value) + (1/2*t2_quantity[i]**r_value))**(1/r_value))
        # elif mean_type == 'H':
        #     mean_quantity.append((quantity[i] * t2_quantity[i]) / 2)
        else:
            print('Please insert either G, A or H as the mean_type')
        
        t1.append(price[i] * mean_quantity[i])
        t2.append(t2_price[i] * mean_quantity[i])

    result = np.sum(t2) / np.sum(t1)

    return result


# 'G' --> Geometric Mean (Walsh_Price_Index)
# 'A' --> Arithmetic Mean (Marshall-Edgeworth Index)
# 'R' --> Mean of Order r (edit r_value below)
# 'H' --> Harmonic Mean (Not yet installed !!!)


r_value=1

mean_type='G'


def Walsh_Price_Index_Practical(
        price, quantity, t2_price, t2_quantity,
):
    t1=[]
    t2=[]

    mean_quantity=[]

    for i, item in enumerate(price):
        if mean_type == 'G':
            mean_quantity.append(np.sqrt((quantity[i] * t2_quantity[i])))
        elif mean_type == 'A':
            mean_quantity.append((quantity[i] * t2_quantity[i]) / 2)
        elif mean_type == 'R':
            mean_quantity.append(
                ((1 / 2 * quantity[i] ** r_value)+(1 / 2 * t2_quantity[i] ** r_value)) ** (1 / r_value))
        # elif mean_type == 'H':
        #     mean_quantity.append((quantity[i] * t2_quantity[i]) / 2)
        else:
            print('Please insert either G, A or H as the mean_type')

        t1.append(price[i] * mean_quantity[i])
        t2.append(t2_price[i] * mean_quantity[i])

    result=np.sum(t2) / np.sum(t1)

    return result


# Marshall-Edgeworth Index
# The function mean(a, b) could be the arithmetic mean, (1/2)a+(1/2)b,
# in which case Walsh's equation reduces to the Marshall (1887) and Edgeworth (1925)
# price index Marshal_Edgeworth_Price_Index, which was the pure price index preferred by Knibbs (1924, p. 56):

# There is a potential problem with the use of the Edgeworth–Marshall price index that has
# been noticed in the context of using the formula to make international comparisons of prices.
# If the price levels of a very large country are compared to the price levels of a
# small country using formula, then the quantity vector of the large country may totally overwhelm the
# influence of the quantity vector corresponding to the# small country.

# In technical terms, the Edgeworth–Marshall formula is not homogeneous of degree 0 in the
# components of both q0 and q1.

# To prevent this problem from occurring in the use of the pure price index
# PK (p0, p1, q0, q1) defined by equation, it is asked
# that Lowe satisfy the following invariance to proportional
# changes in current quantities test:

# P(p0, p1, q0, λq1) = P(p0, p1, q0, q1) for all p0, p1, q0, q1 and all λ > 0

# The two tests, the time reversal test

# P(p1, p0, q1, q0) = 1/P(p0, p1, q0, q1)

# and the invariance test (above), make it possible to determine the
# precise functional form for the pure price index Lowe defined by formula: the pure price index PK must
# be the Walsh index PW defined by formula (15.19).33

def Marshall_Edgeworth_Price_Index(
        price, quantity, t2_price, t2_quantity
):
    t1 = []
    t2 = []

    arithmetic_mean_quantity =[]

    for i, item in enumerate(price):
        arithmetic_mean_quantity.append((quantity[i]*t2_quantity[i])/2)
        t1.append(price[i]* arithmetic_mean_quantity[i])
        t2.append(t2_price[i] * arithmetic_mean_quantity[i])

    result = np.sum(t2) / np.sum(t1)

    return result





#
# pie_weight=np.array(
#     [[0.25, 0.25, 0.25, 0.25], [0.25, 0.25, 0.25, 0.25], [0.25, 0.25, 0.25, 0.25], [0.25, 0.25, 0.25, 0.25], [0.25, 0.25, 0.25, 0.25], [0.25, 0.25, 0.25, 0.25], [0.25, 0.25, 0.25, 0.25]])
#
# print(Geometric_Laspeyres_Index(pie[1], Weight(pie_weight[0]), pie[2]))

# def Geometric_Mean(iterable):
#     numpy_array=np.array(iterable)
#     return numpy_array.prod() ** (1.0 / len(numpy_array))





# Harmonic mean of price relatives
# The harmonic mean of the price relatives has the same kinds of
# axiomatic properties as the Carli but with opposite tendencies and biases.
# Fails the transitivity and time reversal tests.
# In addition it is very sensitive to “price bouncing,” as is the Carli index.
# As it can be viewed conceptually as the complement, or rough mirror image, of the Carli
# index, it has been argued that a suitable elementary index would be provided by a geometric mean of the two.

def Harmonic_Mean_of_Prices(
        price, t2_price
):
    array = []
    for i, item in enumerate(price):
        array.append(1/(price[i] / t2_price[i]))

    result = len(price)/np.sum(array)

    return result

# print(Harmonic_Mean_of_Price_Relvatives([6, 7, 2, 5], [6, 7, 3, 5]))

def IMF_Harmonic_Mean_of_Price_Relvatives(
        price, t2_price
):
    array = []
    for i, item in enumerate(price):
        array.append((price[i] / t2_price[i]))

    result = 1/((1/len(price))*(np.sum(array)))

    return result

# print(IMF_Harmonic_Mean_of_Price_Relvatives([6, 7, 2, 5], [6, 7, 3, 5]))

# def IMF_Harmonic_Mean_of_Price_Relvatives(
#         price, t2_price
# ):
#     array = []
#
#
#
#     for i, item in enumerate(price):
#         array.append(price[i] / t2_price[i])
#     print(array)
#
#     result = (1/len(price))*(np.sum(price)/np.sum(t2_price))
#     print('lemon')
#     print(result)
#     result = 1 / result
#
#     return result
#


def Weighted_Harmonic_Mean_of_Price_Relvatives(
        price, t2_price, weight
):
    array = []
    for i, item in enumerate(price):
        array.append(weight[i]/(price[i] / t2_price[i]))

    result = np.sum(weight)/np.sum(array)

    return result


def Ratio_of_Harmonic_Mean_Prices(
        price, t2_price
):
    t1 = []
    t2 = []
    for i, item in enumerate(price):
        t1.append(len(price)/price[i])
        t2.append(len(price)/t2_price[i])

    t1 = np.sum(t1)
    t2 = np.sum(t2)

    return t1/t2

# print(Ratio_of_Harmonic_Mean_Prices([6, 7, 2, 5], [6, 7, 3, 5]))



def Arithmetic_Geometric_Mean(
        number_1, number_2, decimal_places
):
    a = number_1
    g = number_2
    
    while a != g:
        getcontext().prec = decimal_places

        a1 = Decimal(Decimal(1/2)*(a+g))
        g1 = Decimal(np.sqrt(a*g))


        a = a1
        g = g1
    
    return a

def Root_Mean_Squre(
        list
):
    array = []
    for i, item in enumerate(list):
        array.append(item**2)

    return np.sqrt(1/len(list)*(np.sum(array)))

def Golden_Ratio(
        decimal_places
):
    getcontext().prec=decimal_places
    return (Decimal(1)+Decimal(np.sqrt(5)))/Decimal(2)


# Carruthers, Sellwood, Ward, Dalén Index
# Fails transitivity test
# Empirically observed to be close to Jevons Index
def C_S_W_D_Price_Index(
        Carli_Index, Harmonic_Mean
):
    return np.sqrt((Carli_Index*Harmonic_Mean))


#
def Lloyd_Moulton_Unweighted(
        price, t2_price, elasticity_of_substitution
):
    es = 1-elasticity_of_substitution

    array = []
    for i, item in enumerate(price):
        array.append(t2_price[i]/price[i])

    array_2 = []
    for i, item in enumerate(array):
        array_2.append((array[i]**es)/len(array))

    result = (np.sum(array_2))**(1/es)

    return result

# pie=np.array(
#     [[6, 7, 2, 5], [6, 7, 3, 5], [7, 6, 4, 5], [6, 7, 5, 4], [6, 7, 2, 5], [6, 7.2, 3, 5], [6.6, 7.7, 2.2, 5.5]])
# 
# print(Lloyd_Moulton(pie[0], pie[1], 0))
# print(Lloyd_Moulton(pie[0], pie[1], 0.99999999))

def Lloyd_Moulton_Weighted(
        price, t2_price, elasticity_of_substitution, weight
):
    es = 1-elasticity_of_substitution

    first_tier_brackets = []
    for i, item in enumerate(price):
        first_tier_brackets.append(t2_price[i]/price[i])

    second_tier_brackets = []
    for i, item in enumerate(first_tier_brackets):
        second_tier_brackets.append((first_tier_brackets[i]**es)*weight[i])

    result = (np.sum(second_tier_brackets))**(1/es)

    return result

# #
# def (
#
# ):
#     return

# --------  Bit2al Formulae








# #
# def _Price_Index(
#
# ):
#     return


# ------------  GDP / GVA / RSI / INFLATION / ETC

"""The Expenditure Approach to GDP"""


def Household_Consumption(
        avg_shopping_basket, house_rent, holidays, other_consumables
):
    return


def Shopping_Basket():
    return


def Consumer_Price_Index_Housing(
        consumer_price_index, occupiers_housing_cost, council_tax
):
    return consumer_price_index+occupiers_housing_cost+council_tax


"""
The below RPI is not considered a national statistic, for details discussed: 

"""


def Retail_Price_Index(

):
    return


"""The Income Approach to GDP"""


# Employment Income
def Employee_compensation(
        salaries, pensions, NI_contributions, bonuses, estimated_benefits
):
    return salaries+pensions+NI_contributions+bonuses+estimated_benefits


# Company Profit
def Gross_Trading_Profits(
        internal_GVA, labour_cost
):
    return internal_GVA-labour_cost


# Profits
def Gross_Operating_Surplus(
        gross_trading_profits, rental_income
):
    return gross_trading_profits+rental_income


# Self-Employed Income
def Mixed_Income(
        self_employed_employee_compensation, self_employed_gross_operating_surplus
):
    return self_employed_employee_compensation+self_employed_gross_operating_surplus


# The total value added t1d on income
def Gross_Value_Added_Income(
        employee_comp, gross_opp_surplus, mixed_income
):
    return employee_comp+gross_opp_surplus+mixed_income


def Gross_Value_Added_Income_Basic(
        gross_value_added_income, taxes_on_production, subsidies_on_production
):
    return gross_value_added_income+taxes_on_production-subsidies_on_production


def Gross_Domestic_Product_Income_Market(
        gross_value_added_basic, tax_on_products, subsidies_on_products
):
    return gross_value_added_basic+tax_on_products-subsidies_on_products

# Aggregate Supply
# Output = Y
# Imports = M
# Taxes - Product_Subsidies) = T

# Aggregate Demand
# Intermediate_Consumption = Z (That which is consumed in production)
# Household_consumption = C
# Government_spending = G
# Capital Formation (Investment) = I
# Exports = X

def Gross_Domestic_Product(
        output,
        imports,
        taxes,
        subsidies,
        intermediate_consumption,
        household_consumption,
        government_spending,
        investment,
        exports
):
    # output + imports + (taxes - product_subsidies) =
    # intermediate_consumption + household_consumption + government_spending + investment + exports

    value_added = output - intermediate_consumption
    gross_domestic_product_2 = value_added + (taxes - subsidies)
    gross_domestic_product_3 = household_consumption + government_spending + investment + exports - imports

    return gross_domestic_product_2

class Resident_Institutional_Unit:
    def __init__(self, title):
        self.title = title
        self.productive_assets = []

# child of resident_institutional_unit --- how to do this?
# Also known as a local kind of activity unit
class Establishment:
    def __init__(self, title):
        self.title = title
        self.costs = []
        self.output = []
        self.location = []

# page 267




resident_institutional_units = ['non-financial corporations',
                               'financial corporations',
                               'general government',
                               'households',
                               'non-profit institutions serving households']





def Prices_Indices_For_An_Elementary_Aggregate(
        data, reference_column
):
    if isinstance(data, pd.DataFrame):
        data = data.to_numpy()

    result=np.copy(data)
    # print(np.array([[i] for i in Current_to_Current_Index('C', data)]))
    # for i, item in enumerate(data):
    result=np.concatenate((data, np.array([[i] for i in Arithmetic_Mean_Series(data)]),
                           np.array([[i] for i in Geometric_Mean_Series('O', data)]),
                           np.array(Current_to_Previous_Price_Relatives(data)),
                           np.array(Current_to_Reference_Price_Relatives(data, reference_column)),
                           np.array([[i] for i in Current_to_Current_Index('C', data)]),
                           np.array([[i] for i in Chained_Elementary_Aggregates('C', data)]),
                           np.array([[i] for i in Direct_Index_On_t1('C', data)]),
                           np.array([[i] for i in Current_to_Current_Index('D', data)]),
                           np.array([[i] for i in Chained_Elementary_Aggregates('D', data)]),
                           np.array([[i] for i in Direct_Index_On_t1('D', data)]),
                           np.array([[i] for i in Current_to_Current_Index('J', data)]),
                           np.array([[i] for i in Chained_Elementary_Aggregates('J', data)]),
                           np.array([[i] for i in Direct_Index_On_t1('J', data)])),
                          axis=1)

    return result


#
# pie=np.array(
#     [[6, 7, 2, 5], [6, 7, 3, 5], [7, 6, 4, 5], [6, 7, 5, 4], [6, 7, 2, 5], [6, 7.2, 3, 5], [6.6, 7.7, 2.2, 5.5]])
#
# pie=np.array(
#     [[1,1,1,1,1,1], [1.2, 3, 1.3, 0.7, 1.4, 0.8], [1, 1, 1.5, 0.5, 1.7, 0.6], [0.8, 0.5, 1.6, 0.3, 1.9, 0.4], [1, 1, 1.6, 0.1, 2, 0.2]])
#
# # Export to CSV
#
# pizza= np.rot90(Prices_Indices_For_An_Elementary_Aggregate(pie, 0))
# pizza= np.rot90(pizza)
# pizza= np.rot90(pizza)
# pizza= np.fliplr(pizza)
#
# cols = ['Period 0', 'Period 1', 'Period 2', 'Period 3', 'Period 4']
# index = ['Product A: Price',
#          'Product B: Price',
#          'Product C: Price',
#          'Product D: Price',
#          'Product E: Price',
#          'Product F: Price',
#          'Arithmetic Mean Prices',
#          'Geometric Mean Prices',
#          'Product A: Period to Period Price Relatives',
#          'Product B: Period to Period Price Relatives',
#          'Product C: Period to Period Price Relatives',
#          'Product D: Period to Period Price Relatives',
#          'Product E: Period to Period Price Relatives',
#          'Product F: Period to Period Price Relatives',
#          'Product A: Current to Reference Price Relatives',
#          'Product B: Current to Reference Price Relatives',
#          'Product C: Current to Reference Price Relatives',
#          'Product D: Current to Reference Price Relatives',
#          'Product E: Current to Reference Price Relatives',
#          'Product F: Current to Reference Price Relatives',
#          'Carli: Period to Period Index',
#          'Carli: Chained Period to Period Index',
#          'Carli: Direct Index on Reference',
#          'Dutot: Period to Period Index',
#          'Dutot: Chained Period to Period Index',
#          'Dutot: Direct Index on Reference',
#          'Jevons: Period to Period Index',
#          'Jevons: Chained Period to Period Index',
#          'Jevons: Direct Index on Reference',
#          ]
#
# dataset = pd.DataFrame(data=pizza[0:, 0:],  # values
#              index=index,  # 1st column as index
#              columns=cols)
# print(dataset)
#
# dataset.to_csv('test.csv')

# #The social welfare function (SWF) methodology is a systematic framework for assessing governmental policy. It represents a major step beyond cost-benefit analysis (CBA), currently the dominant policy-assessment tool. The SWF framework is well established in certain parts of the economics literature — such as theoretical welfare economics, optimal tax theory, and climate economics — but unlike CBA is not yet used by governments. While CBA quantifies well-being impacts in monetary units (via the construct of willingness to pay/accept), the SWF framework does so using an interpersonally comparable well-being measure.
#
# "Measuring Social Welfare: An Introduction" provides a rigorous but accessible overview and defense of the SWF framework. This interdisciplinary work is grounded not only in economics but also in philosophy; it draws from philosophical scholarship concerning well-being, consequentialism, distributive justice, and utilitarianism.
#
# The SWF framework has three components:
#
# (1) The well-being measure, which converts each possible outcome of policy choice into a list (vector) of well-being numbers, measuring the well-being of each person in the population in that outcome.
#
# (2) The SWF proper, which is a rule for ranking these vectors (for example, the utilitarian SWF, which sums up the numbers; or a prioritarian SWF, which sums up a concave transformation of well-being, and thereby gives priority to those at lower well-being levels).
#
# (3) An uncertainty module for the chosen SWF, for ranking policies understood as probability distributions over well-being vectors.
#
# Chapter 1 provides an overview of the methodology and its ethical grounding, and contrasts the SWF approach with CBA. Chapter 2 discusses the construction of the well-being measure. Following in the footsteps of John Harsanyi, this chapter shows how von Neumann-Morgenstern utility theory can be used to construct an interpersonally comparable well-being measure that accommodates heterogeneous preferences. Chapters 3 and 4 discuss the functional form of the SWF and application under uncertainty. Salient possibilities include the utilitarian SWF, prioritarian SWFs, “sufficientist" SWFs, egalitarian SWFs, and the leximin SWF. These chapters aim specifically to make the case for prioritarianism. Chapter 5 is a detailed case study of the application of the SWF format to environmental policy (specifically, fatality risk regulation), contrasting that approach with CBA. (Because CBA ignores the diminishing marginal utility of money, it is biased towards the rich in valuing risk reduction — even more so than utilitarianism, let alone prioritarianism — and is insensitive to the distribution of the material costs of reduction.) Chapter 6 discusses the potential implementation of the SWF approach in government, and Chapter 7 addresses research frontiers (variable population and responsibility).
#
# https://ec.europa.eu/environment/beyond_gdp/news_en.html
