import pytest
from mock import Mock


class CustomIterable:
    def __init__(self, objs):
        self._objs = objs

    def __iter__(self):
        yield from self._objs


@pytest.fixture(params=[list, tuple, CustomIterable],
                ids=['list', 'tuple', 'custom'])
def multicls(request):
    return request.param


@pytest.fixture()
def pykube_object(pykube):
    obj = pykube.objects.CronJob(Mock(), {
        'metadata': {},
        'spec': {
            'jobTemplate': {},
        },
    })
    return obj


@pytest.fixture()
def kubernetes_model(kubernetes):
    # The most tricky class -- with attribute-to-key mapping (jobTemplate).
    obj = kubernetes.client.V1CronJob(
        metadata=kubernetes.client.V1ObjectMeta(),
        spec=kubernetes.client.V1CronJobSpec(
            schedule='* * * * *',
            job_template=kubernetes.client.V1JobTemplateSpec(),
        ),
    )
    return obj
