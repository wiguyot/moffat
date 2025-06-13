# Le profil de Moffat

## Quand on prend une photo d’une étoile...

Normalement, une étoile est un point minuscule dans le ciel. Mais sur une photo, même avec un bon télescope, elle apparaît un peu floue, comme une tache lumineuse.
Ce flou, ce « halo de lumière » autour du centre de l’étoile, on appelle ça sa forme d’éclat, ou en langage pro : PSF (Point Spread Function).

## Alors qu'est-ce que le  “profil de Moffat” ?

Le profil de Moffat, c’est une formule mathématique qui décrit comment la lumière d’une étoile se répartit dans cette petite tache floue sur ta photo.

C'est une recette qui dit  :

    « Au centre, c’est très lumineux, et plus on s’éloigne du centre, plus ça devient sombre. Mais pas trop vite, on garde un peu de lumière autour. »

C’est plus réaliste que d’autres formules, car il imite mieux ce qu’on voit vraiment, surtout quand le ciel n’est pas parfait.


## Comparaison avec la "gaussienne" (la fameuse cloche)

La gaussienne (ou "courbe en cloche") dit que la lumière tombe très vite quand on s’éloigne du centre.

Le Moffat, lui, dit que ça tombe plus doucement → donc les bords (ou ailes) sont plus lumineux.

Imagine une lampe de poche dans la brume :

- Gaussienne : tu ne vois que le centre bien éclairé.

- Moffat : tu vois aussi un halo lumineux autour.

⚙️ Et le fameux β ?

C’est un bouton magique dans la formule.
Il permet de dire à quelle vitesse la lumière s’atténue autour du centre.

- Si β est petit (genre 2) → les ailes sont larges, il y a plein de lumière autour.

- Si β est grand (genre 10 ou plus) → le profil ressemble à une gaussienne (ça devient pointu au centre, et sombre très vite autour).

📏 Dans la réalité, les astronomes trouvent que β entre 2 et 5 représente bien ce qu’on observe quand le ciel fait "danser" la lumière des étoiles (ce qu’on appelle le seeing).

## Pourquoi c’est utile ?

Parce que si tu veux améliorer une image d’astrophotographie (la rendre plus nette), il faut comprendre exactement comment l’étoile est floutée. Et pour ça, le profil de Moffat est une des meilleures approximations dans les vrais cas d’observation, mieux que la cloche gaussienne.

### ✨ Résumé visuel (imagé)

| Type de flou         | Centre lumineux | Bords (ailes) lumineux | Réaliste pour astro ?        |
|----------------------|------------------|--------------------------|-------------------------------|
| Gaussienne           | Oui              | Non                      | Moins                         |
| Moffat (β = 3)       | Oui              | Un peu oui               | ✅ Oui                        |
| Moffat (β grand)     | Oui              | Non                      | Presque une gaussienne        |


## Formule mathématique

### 📐 Profil de Moffat

Le profil de Moffat est défini par :

$$
I(r) = I_0 \left[ 1 + \left( \frac{r}{\alpha} \right)^2 \right]^{-\beta}
$$

- \( I(r) \) : intensité lumineuse à une distance \( r \) du centre
- \( I_0 \) : intensité maximale (au centre)
- \( \alpha \) : paramètre d’échelle (lié à la largeur du profil)
- \( \beta \) : paramètre de forme (contrôle l'épaisseur des ailes)

#### 🎯 Relation entre \( \alpha \) et la FWHM

La FWHM (Full Width at Half Maximum) est donnée par :

$$
\text{FWHM} = 2 \alpha \sqrt{2^{1/\beta} - 1}
$$

Cela permet de fixer \( \alpha \) à partir d'une FWHM mesurée ou souhaitée.

