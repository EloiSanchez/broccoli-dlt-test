from sqlmesh import macro


@macro()
def union_multiple(_, table_names: list[str]):
    def select_start(table_name: str):
        return f"select * from {table_name}"

    clauses = []
    for table_name in table_names:
        clauses.append(select_start(table_name))

    return " union ".join(clauses)
