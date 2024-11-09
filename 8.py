def format_table(benchmarks, algos, results):
    header = ["Benchmark"] + algos

    column_widths = [
        max(len(str(benchmark)) for benchmark in benchmarks),  # Первая колонка "Benchmark"
        *[max(len(str(algo)), *(len(f"{result[i]:.2f}") for result in results)) for i, algo in enumerate(algos)]
    ]

    row_format = "| " + " | ".join(f"{{:<{w}}}" for w in column_widths) + " |"

    print(row_format.format(*header))

    print("|" + "-" * (sum(column_widths) + len(column_widths) * 3 - 1) + "|")

    for benchmark, result in zip(benchmarks, results):
        row = [benchmark] + [f"{value:.2f}" for value in result]
        print(row_format.format(*row))


format_table(
    ["best case", "the worst case"],
    ["quick sort", "merge sort", "bubble sort"],
    [[1.23, 1.56, 2.0], [3.3, 2.9, 3.9]]
)
