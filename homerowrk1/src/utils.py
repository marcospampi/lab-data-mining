def top_dict_pairs(src: dict, count: int) -> dict:
    return {
        key: value  for key, value in list(sorted(src.items(), key = lambda tup: tup[1], reverse=True ))[:count]
    }