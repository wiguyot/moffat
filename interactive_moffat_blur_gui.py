import numpy as np
from astropy.io import fits
from scipy.signal import fftconvolve
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import os
import sys

def moffat_kernel(shape, fwhm, beta):
    ny, nx = shape
    y, x = np.mgrid[0:ny, 0:nx]
    x -= nx // 2
    y -= ny // 2
    alpha = fwhm / (2 * np.sqrt(2**(1 / beta) - 1))
    r2 = x**2 + y**2
    kernel = (1 + (r2 / alpha**2)) ** (-beta)
    return kernel / np.sum(kernel)

def apply_blur_and_update(ax, img_orig, fwhm, beta):
    kernel = moffat_kernel((21, 21), fwhm, beta)
    blurred = fftconvolve(img_orig, kernel, mode='same')
    ax.clear()
    vmin, vmax = np.percentile(img_orig, [5, 99.5])
    ax.imshow(blurred, cmap='gray', origin='lower', vmin=vmin, vmax=vmax)
    ax.set_title(f"Flou Moffat (FWHM={fwhm:.2f}, β={beta:.2f})")
    plt.draw()
    return blurred

def interactive_gui(fits_file):
    # Charger image
    with fits.open(fits_file) as hdul:
        data = hdul[0].data
        header = hdul[0].header

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6))
    plt.subplots_adjust(bottom=0.25)

    # Image originale
    vmin, vmax = np.percentile(data, [5, 99.5])
    ax1.imshow(data, cmap='gray', origin='lower', vmin=vmin, vmax=vmax)
    ax1.set_title("Image d'origine")

    # Valeurs initiales
    init_fwhm = 3.0
    init_beta = 3.0

    blurred = apply_blur_and_update(ax2, data, init_fwhm, init_beta)

    # Curseurs
    ax_fwhm = plt.axes([0.25, 0.15, 0.65, 0.03])
    ax_beta = plt.axes([0.25, 0.1, 0.65, 0.03])
    s_fwhm = Slider(ax_fwhm, 'FWHM', 0.5, 10.0, valinit=init_fwhm)
    s_beta = Slider(ax_beta, 'β', 1.0, 10.0, valinit=init_beta)

    def update(val):
        fwhm = s_fwhm.val
        beta = s_beta.val
        nonlocal blurred
        blurred = apply_blur_and_update(ax2, data, fwhm, beta)

    s_fwhm.on_changed(update)
    s_beta.on_changed(update)

    # Bouton pour sauvegarder
    ax_save = plt.axes([0.8, 0.025, 0.1, 0.04])
    btn_save = Button(ax_save, 'Enregistrer')

    def save(event):
        base, ext = os.path.splitext(fits_file)
        if ext == ".gz":
            base, ext2 = os.path.splitext(base)
            ext = ext2 + ext
        output_file = f"{base}_moffat_gui.fit"
        hdu = fits.PrimaryHDU(blurred, header=header)
        hdu.writeto(output_file, overwrite=True)
        print(f"Image sauvegardée : {output_file}")

    btn_save.on_clicked(save)

    plt.show()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Utilisation : python interactive_moffat_blur_gui.py image.fit")
        sys.exit(1)
    fits_file = sys.argv[1]
    interactive_gui(fits_file)
