import numpy as np
import pandas as pd
import math

def normal_distribution(n):
    return np.random.normal(0, 1, n)

def cauchy_distribution(n):
    return np.random.standard_cauchy(n)

def student_distribution(n):
    return np.random.standard_t(3, n)

def poisson_distribution(n):
    return np.random.poisson(10, n)

def uniform_distribution(n):
    return np.random.uniform(-math.sqrt(3), math.sqrt(3), n)

distributions = [
    ('normal', normal_distribution, -10, 10),
    ('cauchy', cauchy_distribution, -10, 10),
    ('student', student_distribution, -10, 10),
    ('poisson', poisson_distribution, -50, 50),
    ('uniform', uniform_distribution, -10, 10),
]

def mean(x):
    return x.mean()

def median(x):
    return np.median(x)

def z_R(x):
    return (x.min() + x.max()) / 2


def z_Q(x):
    return (np.quantile(x, 0.25) + np.quantile(x, 0.75)) / 2

def z_tr(x):
    r = round(len(x) / 4)
    return x[r:-r].mean()

metrics = [
    ('mean', mean),
    ('median', median),
    ('z_R', z_R),
    ('z_Q', z_Q),
    ('z_tr', z_tr),
]

def E(z):
    return z.mean()

def D(z):
    return (z ** 2).mean() - z.mean() ** 2
ns = np.array([10, 100, 1000])

for distribution_name, distribution_f, min_value, max_value in distributions:
    result_df = pd.DataFrame(columns=[
        'n',
        *list(map(lambda metric: f'E(z) {metric[0]}', metrics)),
        *list(map(lambda metric: f'D(z) {metric[0]}', metrics)),
    ])
    
    table = str(distribution_name) + "\n\\hline\n"
    for n in ns:
        metric_values = {}
        
        for i in range(1000):
            x = distribution_f(n)
            x = x[(x >= min_value) & (x <= max_value)]

            for metric_name, metric_f in metrics:
                if not metric_name in metric_values:
                    metric_values[metric_name] = np.array([])

                metric_values[metric_name] = np.append(metric_values[metric_name], metric_f(x))

        data_row = {'n': [n]}
        table = table + f'n = {n} & & & & & \\\\\n'
        table = table + "\\hline \n"
        table = table + "& \\(\\overline{x}\\) & \\(med \\ x\\) & \\(z_R\\) & \\(z_Q\\) & \\(z_{tr}\\) \\\\\n"
        table = table + "\\hline \n"
        Ez = "\\(E(z)\\) "
        Dz = "\\(D(z)\\) "
        for metric_name, values in metric_values.items():
            Ez = Ez + f' & {E(values): .2e}'
            Dz = Dz + f' & {D(values): .2e}'
            data_row[f'E(z) {metric_name}'] = [E(values)]
            data_row[f'D(z) {metric_name}'] = [D(values)]
        Ez = Ez + ' \\\\\n \\hline \n'
        Dz = Dz + ' \\\\\n \\hline \n'
        table = table + Ez + Dz
        result_df = pd.concat([result_df, pd.DataFrame(data_row)])
    print(table)
    print('\n')
    result_df.to_csv(f'{distribution_name}.csv', index=False)