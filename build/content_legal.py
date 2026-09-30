# Páginas legales (EU / ES).
# {TITULAR} y {NIF} son datos pendientes del cliente: se muestran resaltados hasta rellenarlos en DATA.
# Borrador de trabajo: debe revisarlo un asesor legal antes de publicar.

DATA = {
    "TITULAR": None,   # p. ej. "Nombre Apellido Apellido" o "Hiru Fisioterapia S.L."
    "NIF": None,       # NIF / CIF
}

UPDATED = ("2026ko iraila", "septiembre de 2026")

CONTACT = [
    ("Izen komertziala: Hiru Fisioterapia Zentrua", "Nombre comercial: Hiru Fisioterapia Zentrua"),
    ("Titularra: {TITULAR}", "Titular: {TITULAR}"),
    ("IFZ: {NIF}", "NIF: {NIF}"),
    ("Helbidea: Plazaola kalea 4, 20230 Legazpi (Gipuzkoa)", "Dirección: Plazaola kalea 4, 20230 Legazpi (Gipuzkoa)"),
    ("Telefonoa: 943 049 797", "Teléfono: 943 049 797"),
    ("Posta elektronikoa: hiru@fisiohiru.com", "Email: hiru@fisiohiru.com"),
]

LEGAL = [
# ------------------------------------------------------------------ AVISO LEGAL
{
 "file": "lege-oharra.html",
 "title": ("Lege oharra", "Aviso legal"),
 "lead": ("Webgune honen titularraren datuak eta erabilera baldintzak.", "Datos del titular de este sitio web y condiciones de uso."),
 "sections": [
  {"id": "titularra", "title": ("Titularra", "Titular"),
   "blocks": [
    ("p", ("Informazioaren gizarteko zerbitzuei eta merkataritza elektronikoari buruzko 34/2002 Legearen 10. artikulua betez, hauek dira webgune honen titularraren datuak:",
           "En cumplimiento del artículo 10 de la Ley 34/2002, de servicios de la sociedad de la información y de comercio electrónico, estos son los datos del titular de este sitio web:")),
    ("ul", CONTACT),
   ]},
  {"id": "lanbidea", "title": ("Lanbide araututa", "Profesión regulada"),
   "blocks": [
    ("p", ("Zentroko fisioterapeutek fisioterapiako unibertsitate titulua dute (Espainia) eta Euskadiko Fisioterapeuten Elkargo Ofizialean (COFPV) daude kolegiatuta. Lanbidea Fisioterapeuten Elkargoaren estatutuek eta kode deontologikoak arautzen dute.",
           "Los fisioterapeutas del centro cuentan con el título universitario de Fisioterapia (España) y están colegiados en el Colegio Oficial de Fisioterapeutas del País Vasco (COFPV). La profesión se rige por los estatutos del Colegio y su código deontológico.")),
   ]},
  {"id": "erabilera", "title": ("Erabilera baldintzak", "Condiciones de uso"),
   "blocks": [
    ("p", ("Webgune hau erabiltzeak lege ohar hau onartzea dakar. Erabiltzaileak webgunea legearen eta fede onaren arabera erabiltzeko konpromisoa hartzen du.",
           "El uso de este sitio web implica la aceptación de este aviso legal. La persona usuaria se compromete a hacer un uso del sitio conforme a la ley y a la buena fe.")),
    ("p", ("Webguneko edukiak informazio orokorrekoak dira eta ez dute ordezten profesional baten balorazio pertsonalizatua. Tratamendu bat hasi aurretik, zure kasua baloratuko dugu.",
           "Los contenidos de la web son de carácter informativo y no sustituyen la valoración personalizada de un profesional. Antes de iniciar cualquier tratamiento, valoraremos tu caso.")),
   ]},
  {"id": "jabetza", "title": ("Jabetza intelektuala", "Propiedad intelectual"),
   "blocks": [
    ("p", ("Webguneko testuak, diseinua, logotipoa eta irudiak titularrarenak dira edo erabiltzeko baimena du. Ezin dira kopiatu, banatu edo eraldatu baimen espresurik gabe.",
           "Los textos, el diseño, el logotipo y las imágenes de la web son propiedad del titular o cuenta con autorización para su uso. No se permite su copia, distribución o transformación sin autorización expresa.")),
    ("p", ("Webguneko argazki batzuk ilustratiboak dira eta ez dute zentroko pertsonarik edo instalaziorik erakusten.",
           "Algunas fotografías de la web son ilustrativas y no muestran personas ni instalaciones reales del centro.")),
   ]},
  {"id": "erantzukizuna", "title": ("Erantzukizuna eta estekak", "Responsabilidad y enlaces"),
   "blocks": [
    ("p", ("Titularrak ahalegina egiten du informazioa eguneratuta eta zuzen mantentzeko, baina ez du erantzukizunik hartzen akats edo etenaldi puntualengatik.",
           "El titular procura mantener la información actualizada y correcta, pero no se hace responsable de errores u omisiones puntuales ni de interrupciones del servicio.")),
    ("p", ("Webgunean kanpoko webguneetarako estekak egon daitezke (adibidez, Google Maps). Titularrak ez du haien edukien gaineko kontrolik ezta erantzukizunik ere.",
           "La web puede contener enlaces a sitios externos (por ejemplo, Google Maps). El titular no controla ni se responsabiliza de sus contenidos.")),
   ]},
  {"id": "legeria", "title": ("Legeria eta jurisdikzioa", "Legislación y jurisdicción"),
   "blocks": [
    ("p", ("Lege ohar hau Espainiako legeriak arautzen du. Edozein gatazkatarako, legeak ezartzen dituen epaitegiak izango dira eskudunak.",
           "Este aviso legal se rige por la legislación española. Para cualquier controversia serán competentes los juzgados y tribunales que correspondan conforme a la ley.")),
   ]},
 ]},

# ------------------------------------------------------------------ PRIVACIDAD
{
 "file": "pribatutasun-politika.html",
 "title": ("Pribatutasun politika", "Política de privacidad"),
 "lead": ("Nola tratatzen ditugun zure datu pertsonalak, eta zein eskubide dituzun.", "Cómo tratamos tus datos personales y qué derechos tienes."),
 "sections": [
  {"id": "arduraduna", "title": ("Tratamenduaren arduraduna", "Responsable del tratamiento"),
   "blocks": [("ul", CONTACT)]},
  {"id": "datuak", "title": ("Zer datu jasotzen ditugu", "Qué datos recogemos"),
   "blocks": [
    ("p", ("Webgune honek ez du formulariorik, ez erregistrorik, ez analitika tresnarik. Telefonoz edo posta elektronikoz jartzen zarenean gurekin harremanetan, zuk ematen dizkiguzun datuak baino ez ditugu jasotzen: izena, harremanetarako datuak eta kontsultarako kontatzen diguzuna.",
           "Esta web no tiene formularios, registro de usuarios ni herramientas de analítica. Cuando nos contactas por teléfono o email, solo recogemos los datos que tú nos das: nombre, datos de contacto y lo que nos cuentes para tu consulta.")),
    ("p", ("Kontsultan osasunari buruzko informazioa partekatzen baduzu, datu mota berezitzat hartzen dugu eta konfidentzialtasun osoz tratatzen dugu.",
           "Si en tu consulta compartes información sobre tu salud, la consideramos una categoría especial de datos y la tratamos con total confidencialidad.")),
   ]},
  {"id": "helburua", "title": ("Helburua eta oinarri juridikoa", "Finalidad y base jurídica"),
   "blocks": [
    ("ul", [
      ("Zure kontsultei erantzutea eta hitzorduak kudeatzea. Oinarria: zure baimena eta, hala badagokio, tratamendu bat kontratatu aurreko neurriak (DBEO 6.1.a eta 6.1.b art.).",
       "Responder a tus consultas y gestionar citas. Base: tu consentimiento y, en su caso, las medidas precontractuales para prestarte un tratamiento (art. 6.1.a y 6.1.b RGPD)."),
      ("Osasun datuak: zure baimen esplizitua eta osasun laguntza ematea (DBEO 9.2.a eta 9.2.h art.).",
       "Datos de salud: tu consentimiento explícito y la prestación de asistencia sanitaria (art. 9.2.a y 9.2.h RGPD)."),
    ]),
    ("p", ("Ez dugu erabaki automatizaturik hartzen ezta profilik egiten ere.", "No tomamos decisiones automatizadas ni elaboramos perfiles.")),
   ]},
  {"id": "epea", "title": ("Kontserbazio epea", "Plazo de conservación"),
   "blocks": [
    ("p", ("Kontsulten datuak erantzuteko behar den denboran gordetzen ditugu. Paziente bihurtzen bazara, historia klinikoa osasun arloko legeriak ezartzen duen epean gordeko da.",
           "Conservamos los datos de las consultas el tiempo necesario para responderlas. Si pasas a ser paciente, la historia clínica se conservará durante el plazo que establece la normativa sanitaria.")),
   ]},
  {"id": "hartzaileak", "title": ("Hartzaileak", "Destinatarios"),
   "blocks": [
    ("p", ("Ez diegu zure datuak hirugarrenei lagatzen, legezko betebeharrik ez badago. Zerbitzu teknikoak ematen dizkiguten hornitzaileek (ostatatzea eta posta elektronikoa) gure izenean tratatu ditzakete datuak, dagokion kontratuarekin.",
           "No cedemos tus datos a terceros salvo obligación legal. Los proveedores que nos prestan servicios técnicos (alojamiento web y correo electrónico) pueden tratarlos por nuestra cuenta, con el contrato correspondiente.")),
   ]},
  {"id": "eskubideak", "title": ("Zure eskubideak", "Tus derechos"),
   "blocks": [
    ("p", ("Edozein unetan eska dezakezu:", "Puedes solicitar en cualquier momento:")),
    ("ul", [
      ("Zure datuetara sartzea, zuzentzea edo ezabatzea", "Acceder a tus datos, rectificarlos o suprimirlos"),
      ("Tratamendua mugatzea edo aurka egitea", "Limitar su tratamiento u oponerte a él"),
      ("Datuen eramangarritasuna", "La portabilidad de tus datos"),
      ("Emandako baimena kentzea", "Retirar el consentimiento que hayas dado"),
    ]),
    ("p", ("Idatzi hiru@fisiohiru.com helbidera edo etorri zentrora. Zure eskubideak errespetatu ez ditugula uste baduzu, erreklamazioa aurkez dezakezu Datuak Babesteko Espainiako Agentzian (aepd.es).",
           "Escríbenos a hiru@fisiohiru.com o acércate al centro. Si consideras que no hemos respetado tus derechos, puedes presentar una reclamación ante la Agencia Española de Protección de Datos (aepd.es).")),
   ]},
 ]},

# ------------------------------------------------------------------ COOKIES
{
 "file": "cookie-politika.html",
 "title": ("Cookie politika", "Política de cookies"),
 "lead": ("Laburbilduz: webgune honek ez du cookierik erabiltzen.", "En resumen: esta web no utiliza cookies."),
 "sections": [
  {"id": "zer-dira", "title": ("Zer dira cookieak", "Qué son las cookies"),
   "blocks": [
    ("p", ("Cookieak webgune bat bisitatzean zure gailuan gordetzen diren fitxategi txikiak dira. Nabigazioa gogoratzeko, estatistikak egiteko edo publizitatea erakusteko erabil daitezke.",
           "Las cookies son pequeños archivos que se guardan en tu dispositivo al visitar una web. Pueden servir para recordar tu navegación, hacer estadísticas o mostrar publicidad.")),
   ]},
  {"id": "erabilera", "title": ("Webgune honetan", "En esta web"),
   "blocks": [
    ("ul", [
      ("Ez dugu ez analitikako ez publizitateko cookierik erabiltzen.", "No usamos cookies de análisis ni de publicidad."),
      ("Letra-tipoak eta ikonoak gure zerbitzaritik kargatzen dira, hirugarrenei datuak bidali gabe.", "Las fuentes y los iconos se cargan desde nuestro propio servidor, sin enviar datos a terceros."),
      ("Aukeratzen duzun hizkuntza (EU/ES) zure nabigatzailean gordetzen dugu (localStorage), hurrengo bisitan gogoratzeko. Ez da gurera bidaltzen eta nabigatzailetik ezaba dezakezu.",
       "Guardamos el idioma que eliges (EU/ES) en tu navegador (localStorage) para recordarlo en tu próxima visita. No se nos envía y puedes borrarlo desde el navegador."),
    ]),
   ]},
  {"id": "mapa", "title": ("Google Maps", "Google Maps"),
   "blocks": [
    ("p", ("Kontaktu ataleko mapa ez da berez kargatzen. \"Mapa ikusi\" sakatzen baduzu bakarrik kargatzen da Google Maps, eta orduan Googlek bere cookieak erabil ditzake, bere pribatutasun politikaren arabera (policies.google.com/privacy).",
           "El mapa de la sección de contacto no se carga por defecto. Solo si pulsas \"Ver mapa\" se carga Google Maps, y entonces Google puede usar sus propias cookies según su política de privacidad (policies.google.com/privacy).")),
   ]},
  {"id": "aldaketak", "title": ("Aldaketak", "Cambios"),
   "blocks": [
    ("p", ("Etorkizunean cookieak erabiltzen dituen tresnaren bat gehitzen badugu, politika hau eguneratuko dugu eta, behar denean, zure baimena eskatuko dizugu.",
           "Si en el futuro añadimos alguna herramienta que use cookies, actualizaremos esta política y, cuando sea necesario, te pediremos tu consentimiento.")),
   ]},
 ]},
]
