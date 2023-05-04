from collections import deque

execute_results = deque()


def quote_literal(literal):
    return f"'{literal}'"


def execute(sql, lines=0):
    return execute_results.popleft() if len(execute_results) > 0 else []


def add_mock_result(result):
    execute_results.append(result)
