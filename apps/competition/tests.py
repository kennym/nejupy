from django.test import TestCase

from datetime import datetime

from competition.models import Competition, COMPETITION_STATS


class CompetitionTestCase(TestCase):
    competition = None

    def _get_or_create_competition(self):
        if self.competition:
            return self.competition.reset()

        competition = Competition.objects.create(title="Test Competition",
                                                 description="Just a test.")
        competition.save()

        return competition
        
    def test_create_competition(self):
        """ Create a sample competition. """
        competition = Competition.objects.create(title="Test Competition",
                                                 description="Just a test.")
        competition.save()
        
    def test_start_competition(self):
        """ Start a competition. """
        competition = self._get_or_create_competition()
        
        # Make sure competition hasn't started yet
        self.assertEquals(competition.status, 0)
        self.assertEquals(competition.start_time, None)

        competition.start()

        # Competition is now started
        self.assertEquals(competition.status, 1)
        self.assertAlmostEqual(competition.start_time.toordinal(),
                               datetime.now().toordinal())
        
    def test_stop_competition(self):
        """ Test stopping a competition. """
        competition = self._get_or_create_competition()
        competition.start()
        
        # ... now stop it.
        competition.stop()

        self.assertEquals(competition.status, 2)
        self.assertLessEqual(competition.end_time, datetime.now())
        self.assertGreaterEqual(competition.end_time, competition.start_time)
        
    def test_stop_not_started_competition(self):
        """ Test stopping a not started competition.

        Should not modify the object in any way. """
        competition = self._get_or_create_competition()

        self.assertEquals(competition.status, 0)
        
        # ... now stop it.
        competition.stop()

        self.assertEquals(competition.status, 0)
        self.assertEquals(competition.start_time, None)
        self.assertEquals(competition.end_time, None)

    def test_start_already_finished_competition(self):
        """ Test starting already finished competition. """
        competition = self._get_or_create_competition()
        competition.start()
        competition.stop()
       
        # Now, start again...
        competition.start()
        
        # ...which should have done nothing to the model
        self.assertEquals(competition.status, 2)

    def test_reset_competition(self):
        """ Test resetting competition. """
        competition = self._get_or_create_competition()
        competition.start()
        competition.reset()
 
        self.assertIsNone(competition.start_time)
        self.assertIsNone(competition.end_time)
        self.assertEquals(competition.status, COMPETITION_STATS[0][0])

    def test_not_started(self):
        """ Test `not_started` property. """
        competition = self._get_or_create_competition()
        self.assertTrue(competition.not_started())

        competition.start()
        self.assertFalse(competition.not_started())

        competition.stop()
        self.assertFalse(competition.not_started())

    def test_in_progress(self):
        """ Test `in_progress` property. """
        competition = self._get_or_create_competition()
        self.assertFalse(competition.in_progress())

        competition.start()
        self.assertTrue(competition.in_progress())

        competition.stop()
        self.assertFalse(competition.in_progress())

    def test_ended(self):
        """ Test `ended` property. """
        competition = self._get_or_create_competition()
        self.assertFalse(competition.ended())

        competition.start()
        self.assertFalse(competition.ended())

        competition.stop()
        self.assertTrue(competition.ended())

    def test_unicode_representation(self):
        """ Test the unicode representation.
        
        Assert that it returns the competition title. """
        competition = self._get_or_create_competition()

        self.assertEquals(competition.__unicode__(), competition.title)
