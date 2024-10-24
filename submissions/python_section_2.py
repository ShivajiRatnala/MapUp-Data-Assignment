import pandas as pd
import numpy as np
from datetime import time


#solution9

def calculate_distance_matrix(df)->pd.DataFrame:
    ids = pd.unique(df[['id_start', 'id_end']].values.ravel())
    id_to_index = {id_: idx for idx, id_ in enumerate(ids)}
    
    distance_matrix = np.full((len(ids), len(ids)), np.inf)
    np.fill_diagonal(distance_matrix, 0)

    for _, row in df.iterrows():
        i, j = id_to_index[row['id_start']], id_to_index[row['id_end']]
        distance_matrix[i, j] = row['distance']
        distance_matrix[j, i] = row['distance']  # assuming undirected

    for k in range(len(ids)):
        for i in range(len(ids)):
            for j in range(len(ids)):
                if distance_matrix[i, j] > distance_matrix[i, k] + distance_matrix[k, j]:
                    distance_matrix[i, j] = distance_matrix[i, k] + distance_matrix[k, j]

    distance_matrix_df= pd.DataFrame(distance_matrix, index=ids, columns=ids)
    return distance_matrix_df

# Example usage:
file_path = 'dataset-2.csv'
dff = pd.read_csv(file_path)
distance_matrix_df = calculate_distance_matrix(dff)
print(distance_matrix_df)


#solution10
def unroll_distance_matrix(df)->pd.DataFrame:
    
    rows = []
    for id_start in distance_matrix.index:
        for id_end in distance_matrix.columns:
            if id_start != id_end:
                rows.append({'id_start':id_start,'id_end':'id_end','distance':distance_matrix.loc[id_start,id_end]})
    df = pd.DataFrame(rows)
    return df
file_path = 'dataset-2.csv'
dff = pd.read_csv(file_path)

distance_matrix = calculate_distance_matrix(dff)

unrolled_df = unroll_distance_matrix(distance_matrix_df)
print(unrolled_df)


#solution11
def find_ids_within_ten_percentage_threshold(df, reference_id)->pd.DataFrame:
    ref_avg_distance = df[df['id_start'] == reference_id]['distance'].mean()
    
    lower_bound = ref_avg_distance * 0.9
    upper_bound = ref_avg_distance * 1.1
    
    avg_distances = df.groupby('id_start')['distance'].mean().reset_index()
    
    filtered_ids = avg_distances[(avg_distances['distance'] >= lower_bound) & (avg_distances['distance'] <= upper_bound)]
    
    return filtered_ids.sort_values(by='id_start')

file_path = 'dataset-2.csv'
dff = pd.read_csv(file_path)
distance_matrix_df = calculate_distance_matrix(dff)
unrolled_df = unroll_distance_matrix(distance_matrix_df)
reference_id = 1
result_df = find_ids_within_ten_percentage_threshold(unrolled_df, reference_id)

print(result_df)

#solution12
def calculate_toll_rate(df)->pd.DataFrame:
    rate_coefficients = {
        'moto': 0.8,
        'car': 1.2,
        'rv': 1.5,
        'bus': 2.2,
        'truck': 3.6
    }
    for vehicle, rate in rate_coefficients.items():
        df[vehicle] = df['distance'] * rate
    
    return df
result_df = calculate_toll_rate(unrolled_df)
print(result_df)

#solution13
def calculate_time_based_toll_rates(df)->pd.DataFrame:
    def get_discount_factor(day, start_time):
        if day in ['Saturday', 'Sunday']:
            return 0.7
        if time(0, 0) <= start_time < time(10, 0):
            return 0.8
        if time(10, 0) <= start_time < time(18, 0):
            return 1.2
        return 0.8
    
    vehicle_columns = ['moto', 'car', 'rv', 'bus', 'truck']
    
    time_based_df = df.copy()
    time_based_rows = []

    for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
        for hour in range(24):
            start_time = time(hour, 0)
            end_time = time(hour, 59)
            discount_factor = get_discount_factor(day, start_time)

            for _, row in df.iterrows():
                time_based_row = row.to_dict()
                time_based_row['start_day'] = day
                time_based_row['start_time'] = start_time
                time_based_row['end_day'] = day
                time_based_row['end_time'] = end_time
                for vehicle in vehicle_columns:
                    time_based_row[vehicle] = row[vehicle] * discount_factor
                time_based_rows.append(time_based_row)
    
    time_based_df = pd.DataFrame(time_based_rows)
    return time_based_df
result_df = calculate_time_based_toll_rates(result_df)
print(result_df) 