import re

import pytest
import responses

from pyblizzard.common.enum.locale import Locale
from pyblizzard.common.enum.region import Region
from pyblizzard.diablo.diablo import Diablo
from pyblizzard.diablo.enum.artisan import Artisan
from pyblizzard.diablo.enum.follower import Follower

TEST_API_KEY = 'abc123'
TEST_REGION = Region.US
TEST_LOCALE = Locale.US
TEST_TIMEOUT = 1.0

TEST_ITEM_ID = 'Unique_CombatStaff_2H_001_x1'
TEST_BATTLE_TAG = 'Spittles-1502'
TEST_HERO_ID = '94825371'
TEST_FOLLOWER = Follower.ENCHANTRESS
TEST_ARTISAN = Artisan.BLACKSMITH

@pytest.fixture()
def stub_request_empty_json():
    responses.add(responses.GET, re.compile('.+'), json={})

@pytest.mark.usefixtures("stub_request_empty_json")
class TestDiablo:

    @staticmethod
    def create_test_diablo_instance():
        return Diablo(TEST_API_KEY, TEST_REGION, TEST_LOCALE, TEST_TIMEOUT)

    @responses.activate
    def test_get_career_profile(self):
        """get_career_profile sends a request with the expected URL."""
        diablo = self.create_test_diablo_instance()
        diablo.get_career_profile(TEST_BATTLE_TAG)

        expected_url = 'https://us.api.battle.net/d3/profile/Spittles-1502/?locale=en_US&apikey=abc123'
        request = responses.calls[0].request
        assert request.url == expected_url

    @responses.activate
    def test_get_hero_profile(self):
        """get_hero_profile sends a request with the expected URL."""
        diablo = self.create_test_diablo_instance()
        diablo.get_hero_profile(TEST_BATTLE_TAG, TEST_HERO_ID)

        expected_url = 'https://us.api.battle.net/d3/profile/Spittles-1502/hero/94825371?locale=en_US&apikey=abc123'
        request = responses.calls[0].request
        assert request.url == expected_url

    @responses.activate
    def test_get_item_data(self):
        """get_item_data sends a request with the expected URL."""
        diablo = self.create_test_diablo_instance()
        diablo.get_item_data(TEST_ITEM_ID)

        expected_url = 'https://us.api.battle.net/d3/data/item/Unique_CombatStaff_2H_001_x1?locale=en_US&apikey=abc123'
        request = responses.calls[0].request
        assert request.url == expected_url

    @responses.activate
    def test_get_follower_data(self):
        """get_follower_data sends a request with the expected URL."""
        diablo = self.create_test_diablo_instance()
        diablo.get_follower_data(TEST_FOLLOWER)

        expected_url = 'https://us.api.battle.net/d3/data/follower/enchantress?locale=en_US&apikey=abc123'
        request = responses.calls[0].request
        assert request.url == expected_url

    @responses.activate
    def test_get_artisan_data(self):
        """get_artisan_data sends a request with the expected URL."""
        diablo = self.create_test_diablo_instance()
        diablo.get_artisan_data(TEST_ARTISAN)

        expected_url = 'https://us.api.battle.net/d3/data/artisan/blacksmith?locale=en_US&apikey=abc123'
        request = responses.calls[0].request
        assert request.url == expected_url
