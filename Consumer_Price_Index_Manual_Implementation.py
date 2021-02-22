import pandas as pd
import numpy as np
from decimal import *

import asyncio

import calcs as c


def LPCDJ_Indices(
        price_data,
        quantity_data,
        period_list,
):

    Laspeyres = [1]
    Paasche=[1]
    Carli = [1]
    Dutot = [1]
    Jevons = [1]

    for i, period in enumerate(period_list):
        if i+1 != len(period_list):

            # Laspeyres
            price_list=price_data['Period 1'].tolist()
            quantity_list=quantity_data['Period 1'].tolist()
            price_2_list=price_data[period_list[i+1]].tolist()
            Laspeyres.append(c.Laspeyres_Price_Index(price_list, quantity_list, price_2_list))

            # Paasche
            price_list=price_data['Period 1'].tolist()
            quantity_2_list=quantity_data[period_list[i+1]].tolist()
            price_2_list=price_data[period_list[i+1]].tolist()
            Paasche.append(c.Paasche_Price_Index(price_list, price_2_list, quantity_2_list))

            # Carli
            price_list=price_data['Period 1'].tolist()
            price_2_list=price_data[period_list[i+1]].tolist()
            Carli.append(c.Carli_Price_Index(price_list, price_2_list))

            # Dutot
            price_list=price_data['Period 1'].tolist()
            price_2_list=price_data[period_list[i+1]].tolist()
            Dutot.append(c.Dutot_Price_Index(price_list, price_2_list))

            # Jevons
            price_list=price_data['Period 1'].tolist()
            price_2_list=price_data[period_list[i+1]].tolist()
            Jevons.append(c.Jevons_Price_Index(price_list, price_2_list))

    result = pd.DataFrame({'Laspeyres':Laspeyres,
                           'Paasche': Paasche,
                           'Carli': Carli,
                           'Dutot': Dutot,
                           'Jevons': Jevons})

    print(result)

    return result

price=pd.read_csv('Price.csv')
quantity=pd.read_csv('Quantity.csv')

period_list=price.columns.values
period_list=period_list[1:]

# LPCDJ_Indices(price, quantity, period_list).to_csv('pie.csv')

def Chain_Period_to_Period_LPCDJ_Indices(
        price_data,
        quantity_data,
        period_list,
):
    Laspeyres=[1]
    Paasche=[1]
    Carli=[1]
    Dutot=[1]
    Jevons=[1]

    for i, period in enumerate(period_list):

        if i+1 != len(period_list):
            # Laspeyres
            price_list=price_data[period_list[i]].tolist()
            quantity_list=quantity_data[period_list[i]].tolist()
            price_2_list=price_data[period_list[i+1]].tolist()
            Laspeyres.append(c.Laspeyres_Price_Index(price_list, quantity_list, price_2_list))

            # Paasche
            price_list=price_data[period_list[i]].tolist()
            quantity_2_list=quantity_data[period_list[i+1]].tolist()
            price_2_list=price_data[period_list[i+1]].tolist()
            Paasche.append(c.Paasche_Price_Index(price_list, price_2_list, quantity_2_list))

            # Carli
            price_list=price_data[period_list[i]].tolist()
            price_2_list=price_data[period_list[i+1]].tolist()
            Carli.append(c.Carli_Price_Index(price_list, price_2_list))

            # Dutot
            price_list=price_data[period_list[i]].tolist()
            price_2_list=price_data[period_list[i+1]].tolist()
            Dutot.append(c.Dutot_Price_Index(price_list, price_2_list))

            # Jevons
            price_list=price_data[period_list[i]].tolist()
            price_2_list=price_data[period_list[i+1]].tolist()
            Jevons.append(c.Jevons_Price_Index(price_list, price_2_list))

        Laspeyres_final = []
        Paasche_final = []
        Carli_final = []
        Dutot_final = []
        Jevons_final = []

        for i, item in enumerate(Carli):
            Laspeyres_final.append(np.prod(Laspeyres[0:i+1]))

            Paasche_final.append(np.prod(Paasche[0:i+1]))
            Carli_final.append(np.prod(Carli[0:i+1]))
            Dutot_final.append(np.prod(Dutot[0:i+1]))
            Jevons_final.append(np.prod(Jevons[0:i+1]))

    result=pd.DataFrame({'Period_to_Period_Laspeyres': Laspeyres,
                         'Chain_Laspeyres': Laspeyres_final,
                         'Period_to_Period_Paasche': Paasche,
                         'Chain_Paasche': Paasche_final,
                         'Period_to_Period_Carli': Carli,
                         'Chain_Carli': Carli_final,
                         'Period_to_Period_Dutot': Dutot,
                         'Chain_Dutot': Dutot_final,
                         'Period_to_Period_Jevons': Jevons,
                         'Chain_Jevons': Jevons_final})

    print(result)

    return result
# Chain_Period_to_Period_LPCDJ_Indices(price, quantity, period_list).to_csv('pizza.csv')



async def Asymet_Weighted_Indices(
        dataframe
):
    result_df=pd.DataFrame([],
                           columns=['Period',
                                    'Palgrave',
                                    'Geometric_Paasche',
                                    'Geometric_Laspeyres',
                                    'Harmonic_laspeyres'])



    return result_df


async def Asymet_Weighted_Chain_Indices(
        dataframe
):
    result_df=pd.DataFrame([],
                           columns=['Period',
                                    'Chain_Palgrave',
                                    'Chain_Geometric_Paasche',
                                    'Chain_Geometric_Laspeyres',
                                    'Chain_Harmonic_Laspeyres'])

    return result_df


async def Asymet_Weighted_Fixed_Base_Indices(
        dataframe
):
    result_df=pd.DataFrame([],
                           columns=['Period',
                                    'Palgrave',
                                    'Geometric_Paasche',
                                    'Geometric_Laspeyres',
                                    'Harmonic_laspeyres'])

    return result_df


async def Asymet_Weighted_Fixed_Base_Chain_Indices(
        dataframe
):
    result_df=pd.DataFrame([],
                           columns=['Period',
                                    'Chain_Palgrave',
                                    'Chain_Geometric_Paasche',
                                    'Chain_Geometric_Laspeyres',
                                    'Chain_Harmonic_Laspeyres'])

    return result_df


async def Symet_Weighted_Fixed_Base_Indices(
        dataframe
):
    result_df=pd.DataFrame([],
                           columns=['Period',
                                    'Tornqvist-Theil',
                                    'Impilict_Walsh',
                                    'Walsh',
                                    'Fisher',  # Fisher Ideal
                                    'Drobisch',
                                    'Marshall-Edgeworth'])

    return result_df


async def Symet_Weighted_Fixed_Base_Chain_Indices(
        dataframe
):
    result_df=pd.DataFrame([],
                           columns=['Period',
                                    'Chain_Tornqvist-Theil',
                                    'Chain_Impilict_Walsh',
                                    'Chain_Walsh',
                                    'Chain_Fisher',  # Fisher Ideal
                                    'Chain_Drobisch',
                                    'Chain_Marshall-Edgeworth'])

    return result_df


async def Fixed_Base_Superlative_Single_Two_Stage_Indices(
        dataframe
):
    result_df=pd.DataFrame([],
                           columns=['Period',
                                    'Tornqvist-Theil',
                                    'Tornqvist-Theil_2',
                                    'Impilict_Walsh',
                                    'Impilict_Walsh_2',
                                    'Walsh',
                                    'Walsh_2',
                                    'Fisher',  # Fisher Ideal
                                    'Fisher_2',  # Fisher Ideal
                                    # 'Drobisch',
                                    # 'Drobisch_2',
                                    ])

    return result_df


async def Fixed_Base_Superlative_Single_Two_Stage_Chain_Indices(
        dataframe
):
    result_df=pd.DataFrame([],
                           columns=['Period',
                                    'Chain_Tornqvist-Theil',
                                    'Chain_Tornqvist-Theil_2',
                                    'Chain_Impilict_Walsh',
                                    'Chain_Impilict_Walsh_2',
                                    'Chain_Walsh',
                                    'Chain_Walsh_2',
                                    'Chain_Fisher',  # Fisher Ideal
                                    'Chain_Fisher_2',  # Fisher Ideal
                                    # 'Chain_Drobisch',
                                    # 'Chain_Drobisch_2',
                                    ])

    return result_df


async def Fixed_Base_Lloyd_Moulton_Indices(
        dataframe
):
    result_df=pd.DataFrame([],
                           columns=['Period',
                                    'Lloyd_Moulton_0',
                                    'Lloyd_Moulton_.2',
                                    'Lloyd_Moulton_.3',
                                    'Lloyd_Moulton_.4',
                                    'Lloyd_Moulton_.5',
                                    'Lloyd_Moulton_.6',
                                    'Lloyd_Moulton_.7',
                                    'Lloyd_Moulton_.8',
                                    'Lloyd_Moulton_1',
                                    ])

    return result_df


async def Chained_Lloyd_Moulton_Index(
        dataframe
):
    result_df=pd.DataFrame([],
                           columns=['Period',
                                    'Chain_Lloyd_Moulton_0',
                                    'Chain_Lloyd_Moulton_.2',
                                    'Chain_Lloyd_Moulton_.3',
                                    'Chain_Lloyd_Moulton_.4',
                                    'Chain_Lloyd_Moulton_.5',
                                    'Chain_Lloyd_Moulton_.6',
                                    'Chain_Lloyd_Moulton_.7',
                                    'Chain_Lloyd_Moulton_.8',
                                    'Chain_Lloyd_Moulton_1',
                                    ])

    return result_df


async def Diewert_Add_Per_Cha_Decomp_Fisher_Index(
        dataframe
):
    result_df=pd.DataFrame([],
                           columns=['Period',
                                    'Percent_Change_t_t',
                                    ])

    return result_df


async def Van_Ijzeren_Decomp_Fisher_Index(
        dataframe
):
    result_df=pd.DataFrame([],
                           columns=['Period',
                                    'Percent_Change_t_t',
                                    ])

    return result_df


async def Lowe_Young_Indices(
        dataframe
):
    result_df=pd.DataFrame([],
                           columns=['Period',
                                    'Lowe',
                                    'Young',
                                    ])

    return result_df


async def Five_Lowe_Indices(
        dataframe
):
    result_df=pd.DataFrame([],
                           columns=['Period',
                                    'Lowe_1',
                                    'Lowe_2',
                                    'Lowe_3',
                                    'Lowe_4',
                                    'Lowe_5',
                                    ])

    return result_df


async def Five_Young_Indices(
        dataframe
):
    result_df=pd.DataFrame([],
                           columns=['Period',
                                    'Young_1',
                                    'Young_2',
                                    'Young_3',
                                    'Young_4',
                                    'Young_5',
                                    ])

    return result_df
