import pandas as pd
import numpy as np
from decimal import *

import asyncio


async def LPCJ_Indices(
        dataframe
):
    result_df=pd.DataFrame([],
                           columns=['Period',
                                    'Laspeyres',
                                    'Paasche',
                                    'Carli',
                                    'Jevons'])

    return result_df


async def Chain_LPCJ_Indices(
        dataframe
):
    result_df=pd.DataFrame([],
                           columns=['Period',
                                    'Chain_Laspeyres',
                                    'Chain_Paasche',
                                    'Chain_Carli',
                                    'Chain_Jevons'])

    return result_df


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
