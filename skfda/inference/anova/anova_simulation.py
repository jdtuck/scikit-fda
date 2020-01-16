from skfda import FDataGrid
import numpy as np
from skfda.inference.anova.anova_oneway import func_oneway, func_oneway_usc
from skfda.datasets import make_gaussian_process


def generate_samples_independent(mean, sigma, n_samples):
    return [mean + np.random.normal(0, sigma, len(mean)) for _ in range(n_samples)]


grid = np.linspace(0, 1, 25)
n_levels = 3
sigmas = np.array([0, 0.2, 1, 1.8, 2.6, 3.4, 4.2, 5])
sigmas_star = sigmas * 25
# Case M2
mean1 = np.vectorize(lambda t: t * (1 - t) ** 5)(grid)
mean2 = np.vectorize(lambda t: t ** 2 * (1 - t) ** 4)(grid)
mean3 = np.vectorize(lambda t: t ** 3 * (1 - t) ** 3)(grid)

fd_means = FDataGrid([mean1, mean2, mean3])

samples1 = generate_samples_independent(mean1, sigmas_star[4], 10)
samples2 = generate_samples_independent(mean2, sigmas_star[4], 10)
samples3 = generate_samples_independent(mean3, sigmas_star[4], 10)

# Storing in FDataGrid
fd_1 = FDataGrid(samples1, sample_points=grid, dataset_label="Process 1")
fd_2 = FDataGrid(samples2, sample_points=grid, dataset_label="Process 2")
fd_3 = FDataGrid(samples3, sample_points=grid, dataset_label="Process 3")
fd_total = fd_1.concatenate(fd_2.concatenate(fd_3))

# print(func_oneway_usc(fd_1, fd_2, fd_3, n_sim=2000)[:-1])
print(func_oneway(fd_1, fd_2, fd_3, n_sim=2000)[:-1])