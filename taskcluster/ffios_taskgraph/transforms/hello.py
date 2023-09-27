import copy
from taskgraph.transforms.base import TransformSequence

transforms = TransformSequence()

@transforms.add
def create_hello(config, tasks):
    for task in tasks:
        terms = task.pop("terms")
        for term in terms:
            new_task = copy.deepcopy(task)
            new_task["run"]["command"] = f"Hello {term}!"
            new_task["label"] = f"hello-{term.replace(' ', '_')}"
            yield new_task
