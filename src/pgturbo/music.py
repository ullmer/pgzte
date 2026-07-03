from pygame.mixer import music as _music
from .loaders import ResourceLoader
from . import constants


_music.set_endevent(constants.MUSIC_END)


class _MusicObject:
    """Small object wrapper to allow the music builtin to be used like the
    other resource loaders are.
    """
    def __init__(self, loader, path):
        self._loader = loader
        self._path = path

    def _play(self, loop):
        _music.load(self._path)
        # Since volume is reset whenever new music is played by pygame, we
        # have to set it before starting a track each time.
        _music.set_volume(self._loader._volume)
        _music.play(loop)
        self._loader._paused = False

    def play(self):
        """Play and loop a music file from the music/ directory."""
        self._play(-1)

    def play_once(self):
        """Play a music file from the music/ directory."""
        self._play(0)

    def queue(self):
        _music.queue(self.path)


class _MusicLoader(ResourceLoader):
    """Pygame's music API acts as a singleton with one 'current' track.

    It doesn't itself return music objects, so we use our own light wrapper
    class to align the usage of the music loader with the usage of the images
    or sounds loader.

    Recommended usage is as follows: music.filename.play()
    For backwards compatibility however, the previous functions are all
    preserved like so: music.play("filename")
    """
    EXTNS = ['mp3', 'ogg', 'oga']
    TYPE = 'music'

    def __init__(self, subpath):
        super().__init__(subpath)
        # This is just used to be able to tell when music is paused instead of
        # there simply being no music loaded in at all.
        self._paused = False
        self._volume = 1.0

    def _load(self, path):
        return _MusicObject(self, path)

    # The functions play, play_once and queue are here to preserve backwards
    # compatibility. They should not be used for fresh projects.
    def play(self, name):
        """Play and loop a music file from the music/ directory."""
        self.load(name).play()

    def play_once(self, name):
        """Play a music file from the music/ directory."""
        self.load(name).play_once()

    def queue(self, name):
        """Queue a music file to follow the current track."""
        self.load(name).queue()

    # The following functions are user facing and seen as intended use.
    def stop(self):
        """Stop all playback."""
        _music.stop()

    def pause(self):
        """Pause playback."""
        _music.pause()
        self._paused = True

    def unpause(self):
        """Resume playback of the music stream after it has been paused."""
        _music.unpause()
        self._paused = False

    def is_playing(self):
        """Return True if the music is playing and not paused."""
        return _music.get_busy()

    def is_paused(self):
        """Return whether playback is currently paused."""
        return self._paused

    def fadeout(self, seconds):
        """Fade out and eventually stop the music playback."""
        _music.fadeout(int(seconds * 1000))

    def get_volume(self):
        """Return the current volume level in inclusive range 0.0 to 1.0."""
        # We return the internally tracked volume here since pygame's own
        # get_volume will return None instead of 1.0 if the volume hadn't been
        # set before. This also avoids the conversion issues stemming from
        # how pygame stores the volume value internally, meaning the internal
        # volume value is more stable.
        return self._volume

    def set_volume(self, value):
        """Set the volume level to anywhere from 0.0 to 1.0. Clamp the value if
        the range is exceeded.
        """
        # Clamp the volume to the range 0.0 to 1.0.
        clamped_value = max(min(1.0, value), 0.0)
        self._volume = clamped_value
        _music.set_volume(clamped_value)


music = _MusicLoader("music")
