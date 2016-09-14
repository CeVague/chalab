from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404, render

from chalab import errors
from wizard.models import ChallengeModel
from .models import BundleTaskModel
from .tasks import bundle


def err(request, template, status, **kwargs):
    return render(request, template, status=status, context=kwargs)


@login_required
def build(request, pk):
    c = get_object_or_404(ChallengeModel, created_by=request.user, pk=pk)

    if not c.is_ready:
        return err(request, 'wizard/http400.html', 400,
                   challenge=c,
                   message='The challenge is not ready to be bundled.')

    b = BundleTaskModel.objects.filter(challenge=c).first()

    if b is None or b.state in {BundleTaskModel.FINISHED,
                                BundleTaskModel.CANCELLED,
                                BundleTaskModel.FAILED}:
        b = BundleTaskModel.create(c)
        bundle.delay(b)
    else:
        raise errors.HTTP400Exception('wizard/challenge/error.html', 'build is in progress',
                                      """The bundle is already being built.""",
                                      challenge=c)

    return redirect(c.get_absolute_url())


@login_required
def download(request, pk):
    c = get_object_or_404(ChallengeModel, created_by=request.user, pk=pk)
    b = get_object_or_404(BundleTaskModel, state=BundleTaskModel.FINISHED, challenge=c)
    return redirect(b.output.url)
