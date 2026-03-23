def get_type(value):
    if isinstance(value, str):
        return "str"
    elif isinstance(value, bool):
        return "bool"
    elif isinstance(value, int):
        return "int"
    elif isinstance(value, float):
        return "float"
    elif value is None:
        return "null"
    elif isinstance(value, list):
        return "list"
    elif isinstance(value, dict):
        return "object"
    return "unknown"


def merge_values(v1, v2):
    """Merge two values intelligently"""

    # If both are dicts → merge recursively
    if isinstance(v1, dict) and isinstance(v2, dict):
        return merge_structures([v1, v2])

    # If both are lists → merge their inner structure
    if isinstance(v1, list) and isinstance(v2, list):
        combined = v1 + v2

        # remove duplicates
        unique = []
        seen = set()

        for item in combined:
            rep = str(item)
            if rep not in seen:
                seen.add(rep)
                unique.append(item)

        return unique

    # Otherwise → treat as types
    types = set(str(v1).split(" | ")) | set(str(v2).split(" | "))
    return " | ".join(sorted(types))


def merge_structures(structs):
    # handle non-dict structures safely
    if not all(isinstance(s, dict) for s in structs):
        types = set()
        for s in structs:
            types.update(str(s).split(" | "))
        return " | ".join(sorted(types))

    result = {}
    key_count = {}
    total = len(structs)

    for struct in structs:
        for key, value in struct.items():
            key_count[key] = key_count.get(key, 0) + 1

            if key not in result:
                result[key] = value
            else:
                result[key] = merge_values(result[key], value)

    # mark optional keys
    final = {}
    for key, value in result.items():
        if key_count.get(key, 0) < total:
            final[f"{key}?"] = value
        else:
            final[key] = value

    return final


def is_uniform(structs):
    """Check if all structures are identical"""
    first = structs[0]
    return all(s == first for s in structs)


# detect structure type
def get_structure_type(s):
    if isinstance(s, dict):
        return "object"
    elif isinstance(s, list):
        return "list"
    else:
        return str(s)


# detect mixed types
def has_mixed_types(structures):
    types = set(get_structure_type(s) for s in structures)
    return len(types) > 1


def build_structure(data, mode="fast", sample_size=3, max_depth=10, depth=0):
    if depth > max_depth:
        return "..."

    # -------- dict --------
    if isinstance(data, dict):
        return {
            key: build_structure(value, mode, sample_size, max_depth, depth + 1)
            for key, value in data.items()
        }

    # -------- list --------
    elif isinstance(data, list):
        if not data:
            return []

        # decide how many items to inspect
        if mode == "fast":
            items = data[:1]
        elif mode == "sample":
            items = data[:sample_size]
        elif mode == "full":
            items = data
        else:
            items = data[:1]

        structures = [
            build_structure(item, mode, sample_size, max_depth, depth + 1)
            for item in items
        ]

        # handle mixed structure types
        if has_mixed_types(structures):
            unique = []
            seen = set()

            for s in structures:
                rep = str(s)
                if rep not in seen:
                    seen.add(rep)
                    unique.append(s)

            return unique

        merged = merge_structures(structures)

        # Uniform structure → compress
        if is_uniform(structures):
            if len(data) > 1:
                return [
                    merged,
                    f"... {len(data)-1} more items (same structure)"
                ]
            return [merged]

        # Non-uniform → just return merged (with optional keys)
        return [merged]

    # -------- primitive --------
    else:
        return get_type(data)