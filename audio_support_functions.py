#support functions

import matplotlib
import matplotlib.pyplot as plt
from IPython.display import display, Audio
import librosa

def plot_waveform(waveform):
  waveform_numpy = waveform.t().numpy()
  plt.plot(waveform_numpy);
  plt.show(block=False)

def plot_spectrogram(spec, ylabel='freq_bin', aspect='auto', xmax=None):
  fig, axs = plt.subplots(1, 1)
  axs.set_title('Spectrogram (db)')
  axs.set_ylabel(ylabel)
  axs.set_xlabel('frame')
  im = axs.imshow(librosa.power_to_db(spec), origin='lower', aspect=aspect)
  if xmax:
    axs.set_xlim((0, xmax))
  fig.colorbar(im, ax=axs)
  plt.show(block=False)

def play_audio(waveform, sample_rate):
  waveform = waveform.numpy()

  num_channels, num_frames = waveform.shape
  if num_channels == 1:
    display(Audio(waveform[0], rate=sample_rate)) # for stereo audio (two channels)
  elif num_channels == 2:
    display(Audio((waveform[0], waveform[1]), rate=sample_rate))
  else:
    raise ValueError("Only mono or stereo files")