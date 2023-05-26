def attach_results_to_name(names: list[str], results: list[int]):
    return [f"{names[i]} ({results[i]})" for i in range(len(names))]