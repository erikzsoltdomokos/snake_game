import pygame
import array
import math
import random

class SoundManager:
    def __init__(self):
        self.enabled = True
        try:
            # Ensure mixer is initialized with specific settings for our buffer generation
            if not pygame.mixer.get_init():
                pygame.mixer.init(frequency=44100, size=-16, channels=1)
            self.sounds = self._generate_sounds()
        except Exception as e:
            print(f"Sound initialization failed: {e}")
            self.enabled = False
            self.sounds = {}

    def _generate_wave(self, frequency, duration, volume=0.3, wave_type='sine', decay=False):
        sample_rate = 44100
        n_samples = int(sample_rate * duration)
        buf = array.array('h')  # signed short (16-bit)
        amplitude = int(32767 * volume)
        
        for i in range(n_samples):
            t = float(i) / sample_rate
            
            # Apply decay envelope if requested
            current_amp = amplitude
            if decay:
                current_amp = int(amplitude * (1.0 - (i / n_samples)))

            if wave_type == 'sine':
                val = int(current_amp * math.sin(2 * math.pi * frequency * t))
            elif wave_type == 'square':
                period = 1.0 / frequency
                val = current_amp if (t % period) < (period / 2) else -current_amp
            elif wave_type == 'sawtooth':
                period = 1.0 / frequency
                val = int(current_amp * (2 * ((t % period) / period) - 1))
            elif wave_type == 'noise':
                val = random.randint(-current_amp, current_amp)
            else:
                val = 0
            
            buf.append(val)
            
        return pygame.mixer.Sound(buffer=buf)

    def _generate_sounds(self):
        sounds = {}
        # Eat: High pitched short beep (Coin-like)
        sounds['eat'] = self._generate_wave(1200, 0.1, 0.2, 'sine', decay=True)
        
        # Bonus: Two tone sequence
        # We can't easily sequence in one buffer without more logic, so just a distinct sound
        sounds['bonus'] = self._generate_wave(1800, 0.15, 0.2, 'square', decay=True)
        
        # Die: Low pitched noise/sawtooth
        sounds['die'] = self._generate_wave(150, 0.4, 0.3, 'sawtooth', decay=True)
        
        # Move (Menu): Short tick
        sounds['menu_move'] = self._generate_wave(400, 0.05, 0.1, 'square', decay=True)
        
        # Select (Menu): Higher tick
        sounds['menu_select'] = self._generate_wave(800, 0.1, 0.15, 'sine', decay=True)
        
        return sounds

    def play(self, name):
        if not self.enabled:
            return
        sound = self.sounds.get(name)
        if sound:
            try:
                sound.play()
            except:
                pass
