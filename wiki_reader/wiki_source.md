# DEC_capstone
Wikimedia events real-time analysis

### Wiki create

```json
{
  "$schema": "/mediawiki/revision/create/2.0.0",
  "meta": {
    "uri": "https://commons.wikimedia.org/wiki/File:Recueil._%22La_proie_du_mort%22_film_de_W._S._Van_Dyke_-_btv1b10520780m_(08_of_29).jpg",
    "request_id": "4e3a97d8-717c-49ef-b675-ac583df9c5a1",
    "id": "7ec61881-722a-43c5-b969-ec0abf09bc8c",
    "dt": "2023-11-08T14:05:02Z",
    "domain": "commons.wikimedia.org",
    "stream": "mediawiki.page-create",
    "topic": "codfw.mediawiki.page-create",
    "partition": 0,
    "offset": 33112041
  },
  "database": "commonswiki",
  "page_id": 140418514,
  "page_title": "File:Recueil._\"La_proie_du_mort\"_film_de_W._S._Van_Dyke_-_btv1b10520780m_(08_of_29).jpg",
  "page_namespace": 6,
  "rev_id": 819709846,
  "rev_timestamp": "2023-11-08T14:05:02Z",
  "rev_sha1": "gvkmsmcr1xqrolstwer5omqngi6l6sq",
  "rev_minor_edit": false,
  "rev_len": 1220,
  "rev_content_model": "wikitext",
  "rev_content_format": "text/x-wiki",
  "performer": {
    "user_text": "Gzen92Bot",
    "user_groups": [
      "bot",
      "*",
      "user",
      "autoconfirmed"
    ],
    "user_is_bot": true,
    "user_id": 5142080,
    "user_registration_dt": "2015-08-19T06:25:04Z",
    "user_edit_count": 3656714
  },
  "page_is_redirect": false,
  "comment": "Gallica btv1b10520780m",
  "parsedcomment": "Gallica btv1b10520780m",
  "dt": "2023-11-08T14:05:02Z",
  "rev_slots": {
    "main": {
      "rev_slot_content_model": "wikitext",
      "rev_slot_sha1": "gvkmsmcr1xqrolstwer5omqngi6l6sq",
      "rev_slot_size": 1220,
      "rev_slot_origin_rev_id": 819709846
    }
  }
}
```

### Wiki recentchange
```json
{
  "$schema": "/mediawiki/recentchange/1.0.0",
  "meta": {
    "uri": "https://de.wikipedia.org/wiki/Natalja_Andrejewna_Gerbulowa",
    "request_id": "ca815c5d-3189-47e7-a79f-efe5c64afbaf",
    "id": "2bfdf58c-0765-4769-a176-7fd1a21571b3",
    "dt": "2023-11-08T14:03:39Z",
    "domain": "de.wikipedia.org",
    "stream": "mediawiki.recentchange",
    "topic": "codfw.mediawiki.recentchange",
    "partition": 0,
    "offset": 751383542
  },
  "id": 343665103,
  "type": "edit",
  "namespace": 0,
  "title": "Natalja Andrejewna Gerbulowa",
  "title_url": "https://de.wikipedia.org/wiki/Natalja_Andrejewna_Gerbulowa",
  "comment": "Bot: [[Kategorie:Universiadeteilnehmer (Russland)]] umbenannt in [[Kategorie:Teilnehmer an den World University Games (Russland)]]: laut [[Wikipedia:WikiProjekt Kategorien/Diskussionen/2023/April/27#Unterkategorien der Kategorie:Teilnehmer an den World University Games (erl.)|Diskussion]]",
  "timestamp": 1699452219,
  "user": "TaxonKatBot",
  "bot": true,
  "notify_url": "https://de.wikipedia.org/w/index.php?diff=238921719&oldid=238464706",
  "minor": true,
  "length": {
    "old": 8511,
    "new": 8530
  },
  "revision": {
    "old": 238464706,
    "new": 238921719
  },
  "server_url": "https://de.wikipedia.org",
  "server_name": "de.wikipedia.org",
  "server_script_path": "/w",
  "wiki": "dewiki",
  "parsedcomment": "Bot: <a href=\"/w/index.php?title=Kategorie:Universiadeteilnehmer_(Russland)&amp;action=edit&amp;redlink=1\" class=\"new\" title=\"Kategorie:Universiadeteilnehmer (Russland) (Seite nicht vorhanden)\">Kategorie:Universiadeteilnehmer (Russland)</a> umbenannt in <a href=\"/wiki/Kategorie:Teilnehmer_an_den_World_University_Games_(Russland)\" title=\"Kategorie:Teilnehmer an den World University Games (Russland)\">Kategorie:Teilnehmer an den World University Games (Russland)</a>: laut <a href=\"/wiki/Wikipedia:WikiProjekt_Kategorien/Diskussionen/2023/April/27#Unterkategorien_der_Kategorie:Teilnehmer_an_den_World_University_Games_(erl.)\" title=\"Wikipedia:WikiProjekt Kategorien/Diskussionen/2023/April/27\">Diskussion</a>"
}
```

### Wiki delete
```json
{
   "$schema":"/mediawiki/page/delete/1.0.0",
   "meta":{
      "uri":"https://he.wikipedia.org/wiki/%D7%94%D7%9C%D7%99%D7%92%D7%94_%D7%94%D7%A4%D7%A9%D7%99%D7%A1%D7%98%D7%99%D7%AA_%D7%94%D7%90%D7%99%D7%9E%D7%A4%D7%A8%D7%99%D7%90%D7%9C%D7%99%D7%AA",
      "request_id":"830455d1-f4af-43ee-9688-183194437c9e",
      "id":"f620b9f3-8210-4467-bc28-21c39d0c3fa0",
      "dt":"2023-11-08T14:13:49Z",
      "domain":"he.wikipedia.org",
      "stream":"mediawiki.page-delete",
      "topic":"codfw.mediawiki.page-delete",
      "partition":0,
      "offset":4875668
   },
   "database":"hewiki",
   "performer":{
      "user_text":"דזרט",
      "user_groups":[
         "ipblock-exempt",
         "patroller",
         "sysop",
         "*",
         "user",
         "autoconfirmed"
      ],
      "user_is_bot":false,
      "user_id":605750,
      "user_registration_dt":"2020-02-05T14:07:03Z",
      "user_edit_count":101199
   },
   "page_id":2017885,
   "page_title":"הליגה_הפשיסטית_האימפריאלית",
   "page_namespace":0,
   "page_is_redirect":false,
   "rev_id":36404848,
   "rev_count":23,
   "comment":"אני עוד אעבוד על הערך, כרגע הוא במצב לא משהו וספק אם יש לו חשיבות",
   "parsedcomment":"אני עוד אעבוד על הערך, כרגע הוא במצב לא משהו וספק אם יש לו חשיבות"
}
```
