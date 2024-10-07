# OnlineShop Django Projekto Aprašymas

## Apie projektą

Šis projektas yra internetinės parduotuvės pavyzdys, sukurtas naudojant Django framework'ą. Tai apima pagrindines el. komercijos funkcijas, tokias kaip produktų katalogas, vartotojų valdymas, krepšelio sistema, užsakymų valdymas ir apmokėjimo būdai. Projektas pritaikytas Lietuvos rinkai.

## Projektas sukomponuotas iš šių Django aplikacijų

- **Store**: Produktų ir kategorijų valdymas.
- **Users**: Vartotojų registracija ir profilio valdymas.
- **Orders**: Užsakymų, krepšelio ir pristatymo informacijos valdymas.
- **API**: REST API paslaugos su Django REST Framework.


### Pagrindinės funkcijos

- **Produktų katalogas**: Produktų sąrašas pagal kategorijas ir subkategorijas su išsamiais aprašymais.
- **Vartotojų registracija ir valdymas**: Vartotojai gali registruotis, prisijungti ir valdyti savo paskyras.
- **Krepšelis ir užsakymų valdymas**: Galimybė pridėti produktus į krepšelį, redaguoti krepšelio turinį bei atlikti užsakymus.
- **Pristatymo informacijos pridėjimas**: Pildoma pristatymo informacija atskirame formos lange.
- **Mokėjimo būdai**: Integruoti keli bankiniai apmokėjimo būdai, tarp kurių yra Paysera, Swedbank, SEB ir kiti.

### Administratorius

- **Admin panelė**: Lengvas produktų, kategorijų, užsakymų valdymas.
- **Produktų redagavimas**: Galima keisti produktų informaciją, kainas, likučius ir kt.
- **Užsakymų stebėjimas**: Galimybė stebėti užsakymus bei jų būsenas.

## Projekto diegimas

### Priklausomybių diegimas

Įsitikinkite, kad turite įdiegtą `Python` ir `pip` paketų tvarkyklę. Visas projekto priklausomybes galite įdiegti iš `requirements.txt` failo, naudodami šią komandą:

```bash
pip install -r requirements.txt



