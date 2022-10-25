import numpy as np

if __name__ == "__main__":
    array_1 = np.zeros(10)
    array_2 = np.arange(10)
    array_3 = np.random.rand(10)


def matrix_multiplication(matrix_1, matrix_2):
    return np.matmul(matrix_1, matrix_2)


def multiplication_check(list_of_matrices):
    multiplication_capability = True
    for i in range(len(list_of_matrices) - 1):
        rows_count_1, columns_count_1 = list_of_matrices[i].shape
        rows_count_2, columns_count_2 = list_of_matrices[i + 1].shape
        if columns_count_1 != rows_count_2:
            multiplication_capability = False
            break
    return multiplication_capability


def multiply_matrices(list_of_matrices):
    if multiplication_check(list_of_matrices):
        first_matrix = list_of_matrices[0]
        for i in range(len(list_of_matrices) - 1):
            second_matrix = list_of_matrices[i + 1]
            first_matrix = np.matmul(first_matrix, second_matrix)
        return first_matrix
    else:
        return None


def compute_2d_distance(unidimensional_array_1, unidimensional_array_2):
    array_of_difference = unidimensional_array_1 - unidimensional_array_2
    sum_of_squares = np.sum(np.square(array_of_difference))
    return np.sqrt(sum_of_squares)


compute_multidimensional_distance = compute_2d_distance


def compute_pair_distances(two_d_array):
    number_of_observation = np.shape(two_d_array)[0]
    pairwise_distances = np.zeros((number_of_observation, number_of_observation))
    for i in range(number_of_observation):
        for j in range(number_of_observation):
            observation_1 = two_d_array[i]
            observation_2 = two_d_array[j]
            pairwise_distances[i][j] = compute_multidimensional_distance(observation_1, observation_2)
    return pairwise_distances
