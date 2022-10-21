import pytest

from crochet.application.services import ProjectService
from crochet.infrastructure.event_store import MemoryEventStore


@pytest.mark.parametrize(
    "name",
    [
        "test project",
        "another test project",
    ],
)
def test_create_new_project(name):
    project_service = ProjectService(event_store=MemoryEventStore())

    project = project_service.create_new_project(project_name=name)

    assert project.name == name
