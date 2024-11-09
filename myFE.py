import pandas as pd

def update_df(df:pd.DataFrame):
    df = df.copy()

    # Общий показатель всех опылителей, чтобы оценить их совокупное воздействие на урожайность.
    # df['total_pollinators'] = df['honeybee'] + df['bumbles'] + df['andrena'] + df['osmia']
    
    # Доля медоносных пчел среди всех опылителей, чтобы увидеть их значимость в опылении.
    # df['honeybee_ratio'] = df['honeybee'] / (df['total_pollinators'] + 1e-6)

    # Суммарное количество диких пчел для анализа их вклада в опыление.
    # df['wild_bees'] = df['bumbles'] + df['andrena'] + df['osmia']

    # Количество дождливых дней на одного опылителя, что может помочь понять, насколько опыление зависит от дождя.
    # df['rain_per_pollinator'] = df['RainingDays'] / (df['total_pollinators'] + 1e-6)

    # Количество семян на единицу завязей, что может помочь понять, насколько плодовитое растение.
    df['seed_per_fruit'] = df['seeds'] / (df['fruitset'] + 1e-6)

    # Оценка потенциальной продуктивности на основе массы плодов и количества семян.
    df['yield_factor'] = df['fruitmass'] * df['seeds']

    # Показатель, чтобы понять, как размер клонов влияет на эффективность опыления.
    # df['clone_to_pollinator_ratio'] = df['clonesize'] / (df['total_pollinators'] + 1e-6)

    # Среднее количество плодов на один клон, что может указать на эффективность размножения в зависимости от размера клона.
    df['fruit_per_clone'] = df['fruitset'] / (df['clonesize'] + 1e-6)


    if 'yield' in df.columns:
        df = df[['fruitset', 'yield_factor', 'fruit_per_clone', 'seed_per_fruit', 'yield']]
    else:
        df = df[['fruitset', 'yield_factor', 'fruit_per_clone', 'seed_per_fruit']]

    return df
