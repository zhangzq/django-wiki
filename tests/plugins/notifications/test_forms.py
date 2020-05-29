from django.test import TestCase
<<<<<<< HEAD
from wiki.plugins.notifications.forms import SettingsFormSet

from tests.base import RequireSuperuserMixin
=======
from django_nyt.forms import SettingsForm

from tests.base import RequireSuperuserMixin
from wiki.plugins.notifications.forms import SettingsFormSet
>>>>>>> udpate to 3.0


class SettingsFormTests(RequireSuperuserMixin, TestCase):
    def test_formset(self):
<<<<<<< HEAD
        SettingsFormSet(user=self.superuser1)
=======
        formset = SettingsFormSet(user=self.superuser1)
>>>>>>> udpate to 3.0
