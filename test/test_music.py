from unittest import TestCase
from unittest.mock import patch
from pgturbo.music import music, _MusicObject
# Needed to patch pygame.mixer.music.play().
import pygame

class MusicTest(TestCase):
    def test_load_music(self):
        """We can access present music files."""
        self.assertIsInstance(music.powerup, _MusicObject)

    def test_non_present_music_errors(self):
        """If a nonexistent music file is specified, we get an error."""
        with self.assertRaises(AttributeError):
            music.powerside

    @patch("pygame.mixer.music.play")
    def test_play_music(self, pg_music_play):
        """We can play music through the pygame mixer."""
        music.powerup.play()
        pg_music_play.assert_called_once_with(-1)

    @patch("pygame.mixer.music.play")
    def test_play_music_once(self, pg_music_play):
        """We can play music through the pygame mixer."""
        music.powerup.play_once()
        pg_music_play.assert_called_once_with(0)

    @patch("pygame.mixer.music.play")
    @patch("pygame.mixer.music.queue")
    def test_queue_music(self, pg_music_queue, pg_music_play):
        """We can queue up something to play after a piece of music."""
        music.powerup.play_once()
        music.powerdown.queue()
        pg_music_queue.assert_called_once()

    @patch("pygame.mixer.music.play")
    def test_play_music_backward_compat(self, pg_music_play):
        """The old way of interacting with music still works without
        regressions."""
        music.play("powerup")
        pg_music_play.assert_called_once_with(-1)

    @patch("pygame.mixer.music.play")
    def test_play_music_once_backward_compat(self, pg_music_play):
        music.play_once("powerup")
        pg_music_play.assert_called_once_with(0)

    @patch("pygame.mixer.music.play")
    @patch("pygame.mixer.music.queue")
    def test_queue_music_backward_compat(self, pg_music_queue, pg_music_play):
        music.play_once("powerup")
        music.queue("powerdown")
        pg_music_queue.assert_called_once()

    @patch("pygame.mixer.music.play")
    @patch("pygame.mixer.music.stop")
    def test_stop_music(self, pg_music_stop, pg_music_play):
        """Music playback can be interrupted."""
        music.powerup.play()
        music.stop()
        pg_music_stop.assert_called_once()

    @patch("pygame.mixer.music.play")
    @patch("pygame.mixer.music.pause")
    def test_pause_music(self, pg_music_pause, pg_music_play):
        """Music playback can be interrupted."""
        music.powerup.play()
        music.pause()
        pg_music_pause.assert_called_once()

    @patch("pygame.mixer.music.play")
    @patch("pygame.mixer.music.unpause")
    def test_unpause_music(self, pg_music_unpause, pg_music_play):
        """Music playback can be interrupted."""
        music.powerup.play()
        music.pause()
        music.unpause()
        pg_music_unpause.assert_called_once()

    @patch("pygame.mixer.music.play")
    @patch("pygame.mixer.music.get_busy")
    def test_is_playing(self, pg_music_get_busy, pg_music_play):
        """We can check if music is currently playing."""
        pg_music_get_busy.return_value = False
        self.assertFalse(music.is_playing())
        music.play("powerup")
        pg_music_get_busy.return_value = True
        self.assertTrue(music.is_playing())

    @patch("pygame.mixer.music.play")
    def test_is_paused(self, pg_music_play):
        """We can check if music playback is currently paused."""
        music.powerup.play()
        self.assertFalse(music.is_paused())
        music.pause()
        self.assertTrue(music.is_paused())

    @patch("pygame.mixer.music.play")
    @patch("pygame.mixer.music.fadeout")
    def test_fadeout(self, pg_music_fadeout, pg_music_play):
        """We can let the current music fadeout over a duration."""
        music.powerup.play()
        music.fadeout(2.0)
        pg_music_fadeout.assert_called_once_with(int(2.0 * 1000))

    def test_get_volume(self):
        """We can check our current volume settings."""
        # Volume starts at 75% by default.
        self.assertEqual(music.get_volume(), 0.75)

    @patch("pygame.mixer.music.play")
    @patch("pygame.mixer.music.set_volume")
    def test_set_volume(self, pg_music_set_volume, pg_music_play):
        """We can change the volume level."""
        music.set_volume(1.0)
        self.assertEqual(music.get_volume(), 1.0)
        pg_music_set_volume.assert_called_once_with(1.0)
