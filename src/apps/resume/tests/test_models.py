from os import urandom

import delorean
from django.test import TestCase

from apps.resume.models import Organization
from apps.resume.models import Responsibility
from apps.resume.models import ResumePage
from project.utils.xdatetime import DateDelta


class Test(TestCase):
    def test_organization(self):
        placeholder = urandom(4).hex()

        start = delorean.parse("2020-01-01").date
        finish = delorean.parse("2021-03-03").date

        organization = Organization(name=placeholder)

        kw = {
            "name": placeholder,
            "organization": organization,
            "started_at": start,
        }

        org = Organization(**kw)
        self.assertEqual(org.actual_name, placeholder)
        self.assertTrue(org.on_air)
        self.assertEqual(str(org), f"{placeholder!r} @ {placeholder} ({org.pk})")

        org = Organization(nda_name=f"nda_{placeholder}", **kw)
        self.assertEqual(org.actual_name, placeholder)

        org = Organization(nda_name=f"nda_{placeholder}", is_under_nda=True, **kw)
        self.assertEqual(org.actual_name, f"nda_{placeholder}")

        org = Organization(position_text="a\nb\nc\n", **kw)
        self.assertSetEqual(set(org.position), set("abc"))

        org = Organization(finished_at=finish, **kw)
        self.assertEqual(org.duration, DateDelta(years=1, months=2))
        self.assertFalse(org.on_air)

        org = Organization(achievements_text="a\nb\nc\n", **kw)
        self.assertSetEqual(set(org.achievements), set("abc"))

        org = Organization(achievements_text="a\nb\nc\n", **kw)
        self.assertSetEqual(set(org.achievements), set("abc"))

        org = Organization(link_text="a\nb\nc\n", **kw)
        self.assertSetEqual(set(org.link), set("abc"))


    def test_responsibility(self):
        placeholder = urandom(4).hex()

        responsibility = Responsibility(name=placeholder)
        self.assertEqual(str(responsibility), f"{placeholder}")


    def test_resumepage(self):
        placeholder = urandom(4).hex()
        resumepage = ResumePage(title=placeholder)
        self.assertEqual(str(resumepage), f"ResumePage [id_{resumepage.pk}]")
