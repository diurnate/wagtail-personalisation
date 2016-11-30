import datetime

import factory
from personalisation import models

class SegmentFactory(factory.DjangoModelFactory):
    name = 'TestSegment'
    status = 'enabled'

    class Meta:
        model = models.Segment

    @factory.post_generation
    def create_rules(self, create, extracted, **kwargs):
        if not create:
            return
        self.time_rule = TimeRuleFactory(segment=self)
        self.referral_rule = ReferralRuleFactory(segment=self)


class TimeRuleFactory(factory.DjangoModelFactory):
    start_time = datetime.time(8,0,0)
    end_time = datetime.time(23,0,0)

    class Meta:
        model = models.TimeRule

class ReferralRuleFactory(factory.DjangoModelFactory):
    regex_string = "test.test"

    class Meta:
        model = models.ReferralRule
