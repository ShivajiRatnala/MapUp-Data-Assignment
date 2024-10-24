from typing import Dict, List
import re
import pandas as pd


#solution1
def reverse_by_n_elements(lst: List[int], n: int) -> List[int]:
    results = []
    for i in range(0,len(lst),n):
        sublist = lst[i:i+n]
        sublist.reverse()
        results.extend(sublist)
    return results
lst = [1,2,3,4,5,6,7,8]
n = int(input("Enter a Number of elements reversed: "))
print(reverse_by_n_elements(lst,n))


#solution2
def group_by_length(lst: List[str]) -> Dict[int, List[str]]:
    group_elements = {}
    for i in lst:
        length = length(i)
        if length in group_elements:
            group_elements[length].append(i)
        else:
            group_by_length[length] = i 
    return dict(group_elements)


# solution3
def flatten_dict(nested_dict: Dict, sep: str = '.') -> Dict:
    """
    Flattens a nested dictionary into a single-level dictionary with dot notation for keys.
    
    :param nested_dict: The dictionary object to flatten
    :param sep: The separator to use between parent and child keys (defaults to '.')
    :return: A flattened dictionary
    """
    
    return dict


#solution4
def unique_permutations(nums: List[int]) -> List[List[int]]:
    def outputs(start,path):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(start,len(nums)):
            if i>start and nums[i] == nums[i-1]:
                continue
            path.append(nums[i])
            outputs(i+1,path)
            path.pop()
    result = []
    outputs(0,[])
    return result


#solution5
def find_all_dates(text: str) -> List[str]:
   
    pattern = r'\b\d{2}-\d{2}-\d{4}\b|\b\d{2}/\d{2}/\d{4}\b|\b\d{4}\.\d{2}\.\d{2}\b'
    match = re.findall(pattern,text)
    return match


#solution6
def polyline_to_dataframe(polyline_str: str) -> pd.DataFrame:
    """
    Converts a polyline string into a DataFrame with latitude, longitude, and distance between consecutive points.
    
    Args:
        polyline_str (str): The encoded polyline string.

    Returns:
        pd.DataFrame: A DataFrame containing latitude, longitude, and distance in meters.
    """
    return pd.Dataframe()


#solution7
def rotate_and_multiply_matrix(matrix: List[List[int]]) -> List[List[int]]:
    n = len(matrix)
    rotated_matrix = [[matrix[n-j-1][i] for j in range(n)]for i in range(n)]

    sum_matrix = []
    for i in range(n):
        sum_row = []
        for j in range(n):
            row_sum = sum(rotated_matrix[i])
            column_sum = sum(rotated_matrix[k][j] for k in range(n))

            new_values = row_sum +column_sum - 2*rotated_matrix[i][j]
            sum_row.append(new_values)
        sum_matrix.append(sum_row)
    return sum_matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = rotate_and_multiply_matrix(matrix)
print(result)


#solution8
def time_check(df) -> pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here

    return pd.Series()
