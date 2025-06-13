import numpy as np
import matplotlib.pyplot as plt

def moffat_psf(r, alpha=1.0, beta=2.5, I0=1.0):
    return I0 * (1 + (r / alpha)**2) ** (-beta)

# Créer une grille radiale
r = np.linspace(0, 5, 500)
alpha = 1.0
beta = 2.5
I0 = 1.0
intensity = moffat_psf(r, alpha, beta, I0)

# Calcul de la FWHM
fwhm = 2 * alpha * np.sqrt(2**(1/beta) - 1)

# Préparer le tracé
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(r, intensity, label=f"PSF de Moffat (β = {beta})")
ax.axhline(I0/2, color='red', linestyle='--', label='I₀ / 2 (demi-hauteur)')
ax.axvline(fwhm/2, color='green', linestyle='--', label='± FWHM/2')
ax.axvline(-fwhm/2, color='green', linestyle='--')
ax.set_xlabel("Distance au centre (r)")
ax.set_ylabel("Intensité I(r)")
ax.set_title("Profil de Moffat et FWHM")
ax.legend()
ax.grid(True)

plt.tight_layout()
plt.show()
