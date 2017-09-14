# Liikennemerkkinumerot

Tieliikenneasetuksen [luvun 3](http://finlex.fi/fi/laki/ajantasa/1982/19820182#L3) tietojen mukainen 
kuvaus merkin numerosta merkin nimeen. 

JSON-tiedostoissa on data esitettynä kahdella eri tavalla avain/arvo-pareina arrayssä ja oliona, josta voi suoraan 
merkin numerolla hakea merkin kuvauksen. Js-tiedostoissa data on JSONP-muodossa. Kovakoodattu
callbackfunktio JSONP-datalle on `liikennemerkitCallback`.

## Huomioita

Cyclorama-datassa nopeusrajoituksien(merkit 361-364) tyyppitiedot sisältävät tiedon kilven nopeusrajoituksesta. 
Esim `314_40` tarkoittaa nopeusrajoitusta 40 km/h. Nopeutta ei ole merkin tekstikentässä Turun eikä Helsingin datoissa. 
Näitä variantteja ei ole lisätty tähän dataan, joten implementaation täytyy tarkistaa merkit 361-326 erikseen.

Esimerkiksi merkit 411-415("pakollinen ajosuunta) ja 417ja 418 "liikententeenjakaja") vaativat lisädataa numeron 
lisäksi merkin suunnasta. Cycloramadatassa tai muussa lähteessä voi olle selitteenä merkin suunta. Monen muun
merkin kohdalla on samanlainen ongelma. Pelkällä numerolla ei pysty täydellisesti replikoimaan merkkiä.

Merkit 424 ja 425 ovat molemmat nimellä "Pyörätie ja jalkakäytävä rinnakkain".

Osaan merkkien numeroita on lisätty kirjaintunniste. Esim. merkit 521 a - 421 c. 
Tässä datassa välissä olevat tyhjä merkki on poistettu datan saamiseksi samanmuotoiseksi kuin cyloramadatoissa

## Lisenssi
Python-koodi datan päivittämiseksi ja data lisenssillä [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)
