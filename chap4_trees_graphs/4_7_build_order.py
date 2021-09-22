from typing import List, Tuple

import pytest
from collections import defaultdict, deque


def determine_build_order(
    projects: List[str], dependencies: List[Tuple[str, str]]
):
    graph = defaultdict(list)
    in_degree = {project: 0 for project in projects}

    for dep in dependencies:
        parent, child = dep
        graph[parent].append(child)
        in_degree[child] += 1

    queue = deque()
    for project, dep in in_degree.items():
        if dep == 0:
            queue.append(project)
    result = []
    while len(queue) > 0:
        node = queue.popleft()
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
        result.append(node)
    if len(result) != len(projects):
        raise NoValidBuildOrderError("No valid order exists.")
    return result


def determine_build_order_v2(projects, dependencies):
    dependency_tree = {p: set() for p in projects}
    build_order = []
    unbuilt_projects = set(projects)
    for dependency, project in dependencies:
        dependency_tree[project].add(dependency)

    while unbuilt_projects:
        something_built = False
        for project in list(unbuilt_projects):
            dependencies = dependency_tree[project]
            if not unbuilt_projects.intersection(dependencies):
                build_order.append(project)
                unbuilt_projects.remove(project)
                something_built = True
        if not something_built:
            raise NoValidBuildOrderError("No valid build order exists")

    return build_order


class NoValidBuildOrderError(Exception):
    pass


def test_determine_build_order():
    projects = ["a", "b", "c", "d", "e", "f", "g"]
    dependencies = [
        ("d", "g"),
        ("a", "e"),
        ("b", "e"),
        ("c", "a"),
        ("f", "a"),
        ("b", "a"),
        ("f", "c"),
        ("f", "b"),
    ]
    build_order = determine_build_order(projects, dependencies)
    for dependency, project in dependencies:
        assert build_order.index(dependency) < build_order.index(project)


def test_impossible_build_order():
    projects = ["a", "b"]
    dependencies = [("a", "b"), ("b", "a")]
    with pytest.raises(NoValidBuildOrderError):
        determine_build_order(projects, dependencies)


if __name__ == "__main__":
    test_determine_build_order()
    test_impossible_build_order()
