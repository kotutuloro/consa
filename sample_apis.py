import json

clipping_search_json = """{
  "artists" : {
    "href" : "https://api.spotify.com/v1/search?query=clipping&type=artist&market=US&offset=0&limit=20",
    "items" : [ {
      "external_urls" : {
        "spotify" : "https://open.spotify.com/artist/5HJ2kX5UTwN4Ns8fB5Rn1I"
      },
      "followers" : {
        "href" : null,
        "total" : 37249
      },
      "genres" : [ "alternative hip hop", "escape room" ],
      "href" : "https://api.spotify.com/v1/artists/5HJ2kX5UTwN4Ns8fB5Rn1I",
      "id" : "5HJ2kX5UTwN4Ns8fB5Rn1I",
      "images" : [ {
        "height" : 849,
        "url" : "https://i.scdn.co/image/96f3fd452d3871eea1ba9ba9cab63b002d8360bb",
        "width" : 960
      }, {
        "height" : 566,
        "url" : "https://i.scdn.co/image/0106dfdbd971940d5d086193793ffdff3f879f8e",
        "width" : 640
      }, {
        "height" : 177,
        "url" : "https://i.scdn.co/image/78735dcbb6433f5dd385df001ba7310e8251bd70",
        "width" : 200
      }, {
        "height" : 57,
        "url" : "https://i.scdn.co/image/d5b963a2d7f8ae014ff41777d5d007ff6646d977",
        "width" : 64
      } ],
      "name" : "clipping.",
      "popularity" : 48,
      "type" : "artist",
      "uri" : "spotify:artist:5HJ2kX5UTwN4Ns8fB5Rn1I"
    }, {
      "external_urls" : {
        "spotify" : "https://open.spotify.com/artist/7iUaTsRiiEVbslUcOs5mpd"
      },
      "followers" : {
        "href" : null,
        "total" : 88
      },
      "genres" : [ ],
      "href" : "https://api.spotify.com/v1/artists/7iUaTsRiiEVbslUcOs5mpd",
      "id" : "7iUaTsRiiEVbslUcOs5mpd",
      "images" : [ {
        "height" : 640,
        "url" : "https://i.scdn.co/image/1a08ba0b21ca3a1a9e9c1a460c6ced7e1fcdc4ef",
        "width" : 640
      }, {
        "height" : 300,
        "url" : "https://i.scdn.co/image/90d14a557979095113b36fb3522ed6ac4f9352db",
        "width" : 300
      }, {
        "height" : 64,
        "url" : "https://i.scdn.co/image/608e28aef8a31c5d1bfea6af5234edfc2fb97a08",
        "width" : 64
      } ],
      "name" : "Clipping",
      "popularity" : 0,
      "type" : "artist",
      "uri" : "spotify:artist:7iUaTsRiiEVbslUcOs5mpd"
    }, {
      "external_urls" : {
        "spotify" : "https://open.spotify.com/artist/1eaN7fgBEU7woIGZ7uAKIZ"
      },
      "followers" : {
        "href" : null,
        "total" : 14
      },
      "genres" : [ ],
      "href" : "https://api.spotify.com/v1/artists/1eaN7fgBEU7woIGZ7uAKIZ",
      "id" : "1eaN7fgBEU7woIGZ7uAKIZ",
      "images" : [ ],
      "name" : "clipping. feat. baseck",
      "popularity" : 13,
      "type" : "artist",
      "uri" : "spotify:artist:1eaN7fgBEU7woIGZ7uAKIZ"
    }],
    "limit" : 20,
    "next" : null,
    "offset" : 0,
    "previous" : null,
    "total" : 8
  }
}"""

top_artists_json = """{
  "items" : [ {
    "external_urls" : {
      "spotify" : "https://open.spotify.com/artist/4RnBFZRiMLRyZy0AzzTg2C"
    },
    "followers" : {
      "href" : null,
      "total" : 264026
    },
    "genres" : [ "alternative hip hop", "escape room", "hip hop", "pop rap", "rap", "underground hip hop" ],
    "href" : "https://api.spotify.com/v1/artists/4RnBFZRiMLRyZy0AzzTg2C",
    "id" : "4RnBFZRiMLRyZy0AzzTg2C",
    "images" : [ {
      "height" : 640,
      "url" : "https://i.scdn.co/image/7195c290c3d01d6aa5ed38e586b7507844febba3",
      "width" : 640
    }, {
      "height" : 320,
      "url" : "https://i.scdn.co/image/7566df19db79c5ef1d83d7d4595871f96a41e428",
      "width" : 320
    }, {
      "height" : 160,
      "url" : "https://i.scdn.co/image/b189456130865fa15c236cba8ed12d06a4ce93cb",
      "width" : 160
    } ],
    "name" : "Run The Jewels",
    "popularity" : 69,
    "type" : "artist",
    "uri" : "spotify:artist:4RnBFZRiMLRyZy0AzzTg2C"
  }, {
    "external_urls" : {
      "spotify" : "https://open.spotify.com/artist/59pWgeY26Q6yJy37QvJflh"
    },
    "followers" : {
      "href" : null,
      "total" : 149674
    },
    "genres" : [ "alternative dance", "brooklyn indie", "chillwave", "dance-punk", "dream pop", "escape room", "folk-pop", "indie christmas", "indie pop", "indie r&b", "indie rock", "indietronica", "neo-psychedelic", "new rave", "noise pop", "nu gaze", "pop christmas", "shimmer pop", "synthpop" ],
    "href" : "https://api.spotify.com/v1/artists/59pWgeY26Q6yJy37QvJflh",
    "id" : "59pWgeY26Q6yJy37QvJflh",
    "images" : [ {
      "height" : 640,
      "url" : "https://i.scdn.co/image/8d58760b9be85beb2ff1a3064dd36c593367e328",
      "width" : 640
    }, {
      "height" : 320,
      "url" : "https://i.scdn.co/image/6bc4b5baf2a4bc126643a5e73bd90982488a4be4",
      "width" : 320
    }, {
      "height" : 160,
      "url" : "https://i.scdn.co/image/9754757c9753ede069c630202baac58d82d0e485",
      "width" : 160
    } ],
    "name" : "Sleigh Bells",
    "popularity" : 52,
    "type" : "artist",
    "uri" : "spotify:artist:59pWgeY26Q6yJy37QvJflh"
  }, {
    "external_urls" : {
      "spotify" : "https://open.spotify.com/artist/4m0HRALRlPxbZp5SwvktFX"
    },
    "followers" : {
      "href" : null,
      "total" : 5309
    },
    "genres" : [ "escape room", "underground hip hop", "vaporwave" ],
    "href" : "https://api.spotify.com/v1/artists/4m0HRALRlPxbZp5SwvktFX",
    "id" : "4m0HRALRlPxbZp5SwvktFX",
    "images" : [ {
      "height" : 416,
      "url" : "https://i.scdn.co/image/ce7acdb32325551442fa884d23b962a95d60ae85",
      "width" : 974
    }, {
      "height" : 273,
      "url" : "https://i.scdn.co/image/fcb4466cb7cf252331c1413a9fe81ce44f771e32",
      "width" : 639
    }, {
      "height" : 85,
      "url" : "https://i.scdn.co/image/83b14e80d7067c55c075ac5295b7a974a5ab99d4",
      "width" : 199
    }, {
      "height" : 27,
      "url" : "https://i.scdn.co/image/11fb53b56b8eb23b63440199a23a03cc75ee1e8a",
      "width" : 63
    } ],
    "name" : "Cities Aviv",
    "popularity" : 29,
    "type" : "artist",
    "uri" : "spotify:artist:4m0HRALRlPxbZp5SwvktFX"
  } ],
  "total" : 50,
  "limit" : 3,
  "offset" : 0,
  "href" : "https://api.spotify.com/v1/me/top/artists?limit=3&offset=0",
  "previous" : null,
  "next" : "https://api.spotify.com/v1/me/top/artists?limit=3&offset=3"
}"""


related_1_json = """{
  "artists" : [ {
    "external_urls" : {
      "spotify" : "https://open.spotify.com/artist/3nf2EaHj8HikLNdaiW3v73"
    },
    "followers" : {
      "href" : null,
      "total" : 12848
    },
    "genres" : [ "alternative hip hop", "escape room", "hip hop", "indie r&b", "underground hip hop" ],
    "href" : "https://api.spotify.com/v1/artists/3nf2EaHj8HikLNdaiW3v73",
    "id" : "3nf2EaHj8HikLNdaiW3v73",
    "images" : [ {
      "height" : 640,
      "url" : "https://i.scdn.co/image/e16b15ec612ceb07ed5296bb2644dd677d13bfa3",
      "width" : 640
    }, {
      "height" : 300,
      "url" : "https://i.scdn.co/image/84b334edd7ba60ea34dfbd6d29c10748fbca8115",
      "width" : 300
    }, {
      "height" : 64,
      "url" : "https://i.scdn.co/image/cfad2244ba596a7e8c49cf5ac042ab5ee32213d6",
      "width" : 64
    } ],
    "name" : "Injury Reserve",
    "popularity" : 48,
    "type" : "artist",
    "uri" : "spotify:artist:3nf2EaHj8HikLNdaiW3v73"
  }, {
    "external_urls" : {
      "spotify" : "https://open.spotify.com/artist/5RADpgYLOuS2ZxDq7ggYYH"
    },
    "followers" : {
      "href" : null,
      "total" : 153316
    },
    "genres" : [ "alternative hip hop", "escape room", "hip hop", "indie r&b", "indietronica", "noise pop", "underground hip hop", "vaporwave" ],
    "href" : "https://api.spotify.com/v1/artists/5RADpgYLOuS2ZxDq7ggYYH",
    "id" : "5RADpgYLOuS2ZxDq7ggYYH",
    "images" : [ {
      "height" : 750,
      "url" : "https://i.scdn.co/image/b4421731b1edda8b8cc56bd74059305e3d3d3baf",
      "width" : 750
    }, {
      "height" : 640,
      "url" : "https://i.scdn.co/image/6cf74eae3b622bdd8c8cbcb944a0cbb5abc1f337",
      "width" : 640
    }, {
      "height" : 200,
      "url" : "https://i.scdn.co/image/44e99eba7959eb2855af390113e7f91ec5fb6280",
      "width" : 200
    }, {
      "height" : 64,
      "url" : "https://i.scdn.co/image/c273232d77a9aa0d880e99e690021c2ed153f0f3",
      "width" : 64
    } ],
    "name" : "Death Grips",
    "popularity" : 58,
    "type" : "artist",
    "uri" : "spotify:artist:5RADpgYLOuS2ZxDq7ggYYH"
  } ]
}"""


related_2_json = """{
  "artists" : [ {
    "external_urls" : {
      "spotify" : "https://open.spotify.com/artist/5RADpgYLOuS2ZxDq7ggYYH"
    },
    "followers" : {
      "href" : null,
      "total" : 153316
    },
    "genres" : [ "alternative hip hop", "escape room", "hip hop", "indie r&b", "indietronica", "noise pop", "underground hip hop", "vaporwave" ],
    "href" : "https://api.spotify.com/v1/artists/5RADpgYLOuS2ZxDq7ggYYH",
    "id" : "5RADpgYLOuS2ZxDq7ggYYH",
    "images" : [ {
      "height" : 750,
      "url" : "https://i.scdn.co/image/b4421731b1edda8b8cc56bd74059305e3d3d3baf",
      "width" : 750
    }, {
      "height" : 640,
      "url" : "https://i.scdn.co/image/6cf74eae3b622bdd8c8cbcb944a0cbb5abc1f337",
      "width" : 640
    }, {
      "height" : 200,
      "url" : "https://i.scdn.co/image/44e99eba7959eb2855af390113e7f91ec5fb6280",
      "width" : 200
    }, {
      "height" : 64,
      "url" : "https://i.scdn.co/image/c273232d77a9aa0d880e99e690021c2ed153f0f3",
      "width" : 64
    } ],
    "name" : "Death Grips",
    "popularity" : 58,
    "type" : "artist",
    "uri" : "spotify:artist:5RADpgYLOuS2ZxDq7ggYYH"
  }, {
    "external_urls" : {
      "spotify" : "https://open.spotify.com/artist/0J6PhnVD21GSFoJ9HoadLH"
    },
    "followers" : {
      "href" : null,
      "total" : 27860
    },
    "genres" : [ "abstract hip hop", "alternative hip hop", "escape room", "underground hip hop" ],
    "href" : "https://api.spotify.com/v1/artists/0J6PhnVD21GSFoJ9HoadLH",
    "id" : "0J6PhnVD21GSFoJ9HoadLH",
    "images" : [ {
      "height" : 640,
      "url" : "https://i.scdn.co/image/1ba457e0633ac15ac52e329055784412511bf4fa",
      "width" : 640
    }, {
      "height" : 300,
      "url" : "https://i.scdn.co/image/799921f3632462fc0ae3e684ba0f8ec47a071802",
      "width" : 300
    }, {
      "height" : 64,
      "url" : "https://i.scdn.co/image/e59a93b1780c0ee7a48da19dcb2c99fdf8b9233e",
      "width" : 64
    } ],
    "name" : "Milo",
    "popularity" : 48,
    "type" : "artist",
    "uri" : "spotify:artist:0J6PhnVD21GSFoJ9HoadLH"
  } ]
}"""


london_json = """{"resultsPage":
    {"results":
      {"location":[{
        "city":{"displayName":"London",
                "country":{"displayName":"UK"},
                "lng":-0.128,"lat":51.5078},
        "metroArea":{"uri":"http://www.songkick.com/metro_areas/24426-uk-london",
                     "displayName":"London",
                     "country":{"displayName":"UK"},
                     "id":24426,
                     "lng":-0.128,"lat":51.5078}},
        {"city":{"displayName":"London",
                "country":{"displayName":"UK"},
                "lng":-0.128,"lat":51.5078},
        "metroArea":{"uri":"http://www.songkick.com/metro_areas/24426-uk-london",
                     "displayName":"London",
                     "country":{"displayName":"UK"},
                     "id":24426,
                     "lng":-0.128,"lat":51.5078}},
        {"city":{"displayName":"London",
                 "country":{"displayName":"US"},
                 "lng":null,"lat":null,
                 "state":{"displayName":"KY"}},
        "metroArea":{"uri":"http://www.songkick.com/metro_areas/24580",
                     "displayName":"Lexington",
                     "country":{"displayName":"US"},
                     "id":24580,
                     "lng":-84.4947,"lat":38.0297,
                     "state":{"displayName":"KY"}}}
    ]},
    "totalEntries":2,"perPage":10,"page":1,"status":"ok"}}"""


houston_json = """{"resultsPage": {"page": 1,
                  "perPage": 50,
                  "results": {"location": [{"city": {"country": {"displayName": "US"},
                                                        "displayName": "Houston",
                                                        "lat": 29.7629,
                                                        "lng": -95.3832,
                                                        "state": {"displayName": "TX"}},
                                              "metroArea": {"country": {"displayName": "US"},
                                                             "displayName": "Houston",
                                                             "id": 15073,
                                                             "lat": 29.7629,
                                                             "lng": -95.3832,
                                                             "state": {"displayName": "TX"},
                                                             "uri": "http://www.songkick.com/metro_areas/15073-us-houston?utm_source=39427&utm_medium=partner"}},
                                             {"city": {"country": {"displayName": "US"},
                                                        "displayName": "Houston",
                                                        "lat": 43.7632995,
                                                        "lng": -91.5684764,
                                                        "state": {"displayName": "MN"}},
                                              "metroArea": {"country": {"displayName": "US"},
                                                             "displayName": "Winona",
                                                             "id": 57612,
                                                             "lat": 44.0513,
                                                             "lng": -91.6386,
                                                             "state": {"displayName": "MN"},
                                                             "uri": "http://www.songkick.com/metro_areas/57612-us-winona?utm_source=39427&utm_medium=partner"}},
                                             {"city": {"country": {"displayName": "US"},
                                                        "displayName": "Houston",
                                                        "lat": 38.91853,
                                                        "lng": -75.505058,
                                                        "state": {"displayName": "DE"}},
                                              "metroArea": {"country": {"displayName": "US"},
                                                             "displayName": "Houston",
                                                             "id": 83951,
                                                             "lat": 38.91853,
                                                             "lng": -75.505058,
                                                             "state": {"displayName": "DE"},
                                                             "uri": "http://www.songkick.com/metro_areas/83951-us-houston?utm_source=39427&utm_medium=partner"}},
                                             {"city": {"country": {"displayName": "Canada"},
                                                        "displayName": "Houston",
                                                        "lat": 54.400639,
                                                        "lng": -126.647049,
                                                        "state": {"displayName": "BC"}},
                                              "metroArea": {"country": {"displayName": "Canada"},
                                                             "displayName": "Houston",
                                                             "id": 50347,
                                                             "lat": 54.400639,
                                                             "lng": -126.647049,
                                                             "state": {"displayName": "BC"},
                                                             "uri": "http://www.songkick.com/metro_areas/50347-canada-houston?utm_source=39427&utm_medium=partner"}},
                                             {"city": {"country": {"displayName": "US"},
                                                        "displayName": "Houston",
                                                        "lat": 38.16386,
                                                        "lng": -89.783302,
                                                        "state": {"displayName": "IL"}},
                                              "metroArea": {"country": {"displayName": "US"},
                                                             "displayName": "Houston",
                                                             "id": 83956,
                                                             "lat": 38.16386,
                                                             "lng": -89.783302,
                                                             "state": {"displayName": "IL"},
                                                             "uri": "http://www.songkick.com/metro_areas/83956-us-houston?utm_source=39427&utm_medium=partner"}},
                                             {"city": {"country": {"displayName": "US"},
                                                        "displayName": "Houston",
                                                        "lat": 30.549999,
                                                        "lng": -92.807503,
                                                        "state": {"displayName": "LA"}},
                                              "metroArea": {"country": {"displayName": "US"},
                                                             "displayName": "Houston",
                                                             "id": 83961,
                                                             "lat": 30.549999,
                                                             "lng": -92.807503,
                                                             "state": {"displayName": "LA"},
                                                             "uri": "http://www.songkick.com/metro_areas/83961-us-houston?utm_source=39427&utm_medium=partner"}}]},
                  "status": "ok",
                  "totalEntries": 6}}"""


nowhere_json = """{"resultsPage": {"page": 1,
                  "perPage": 50,
                  "results": {},
                  "status": "ok",
                  "totalEntries": 0}}"""


vw_concerts_json = """{
      "resultsPage": {
          "page": 1,
          "totalEntries": 2,
          "perPage": 50,
          "results": {
              "event": [{
                  "displayName": "Vampire Weekend at O2 Academy Brixton (February 16, 2010)",
                  "type": "Concert",
                  "uri": "http://www.songkick.com/concerts/3037536-vampire-weekend-at-o2-academy-brixton?utm_medium=partner&utm_source=PARTNER_ID",
                  "venue": {
                      "lng": -0.1187418,
                      "displayName": "O2 Academy Brixton",
                      "lat": 51.4681089,
                      "id": 17522
                  },
                  "location": {
                      "lng": -0.1187418,
                      "city": "London, UK",
                      "lat": 51.4681089
                  },
                  "start": {
                      "time": "19:30:00",
                      "date": "2010-02-16",
                      "datetime": "2010-02-16T19:30:00+0000"
                  },
                  "performance": [{
                      "artist": {
                          "uri": "http://www.songkick.com/artists/288696-vampire-weekend",
                          "displayName": "Vampire Weekend",
                          "id": 288696,
                          "identifier": [{"mbid": "af37c51c-0790-4a29-b995-456f98a6b8c9"}]
                      },
                     "displayName": "Vampire Weekend",
                     "billingIndex": 1,
                     "id": 5380281,
                     "billing": "headline"
                  }],
                  "id": 3037536
              },
              {
                  "displayName": "Vampire Weekend at O2 Academy Brixton (February 17, 2010)",
                  "type": "Concert",
                  "uri": "http://www.songkick.com/concerts/3078766-vampire-weekend-at-o2-academy-brixton?utm_medium=partner&utm_source=PARTNER_ID",
                  "venue": {
                      "lng": -0.1187418,
                      "displayName": "O2 Academy Brixton",
                      "lat": 51.4681089,
                      "id": 17522
                  },
                  "location": {
                      "lng": -0.1187418,
                      "city": "London, UK",
                      "lat": 51.4681089
                  },
                  "start": {
                      "date": "2010-02-17",
                      "datetime": null
                  },
                  "performance": [{
                      "artist": {
                          "uri": "http://www.songkick.com/artists/288696-vampire-weekend",
                          "displayName": "Vampire Weekend",
                          "id": 288696,
                          "identifier": [{"mbid": "af37c51c-0790-4a29-b995-456f98a6b8c9"}]
                      },
                      "displayName": "Vampire Weekend",
                      "billingIndex": 1,
                      "id": 5468321,
                      "billing": "headline"
                  }],
                  "id": 3078766
              }]
          }
      }
  }"""

outside_lands_json = """{"resultsPage":{"status":"ok","results":{"event":[{"venue":{"metroArea":{"country":{"displayName":"US"},"displayName":"SF Bay Area","uri":"http://www.songkick.com/metro_areas/26330-us-sf-bay-area?utm_source=39427&utm_medium=partner","id":26330,"state":{"displayName":"CA"}},"lat":37.7822891,"displayName":"Golden Gate Park","uri":"http://www.songkick.com/venues/5832-golden-gate-park?utm_source=39427&utm_medium=partner","lng":-122.463708,"id":5832},"type":"Festival","status":"ok","start":{"time":null,"datetime":null,"date":"2017-08-11"},"end":{"time":null,"datetime":null,"date":"2017-08-13"},"popularity":0.436318,"location":{"city":"San Francisco, CA, US","lat":37.7822891,"lng":-122.463708},"series":{"displayName":"Outside Lands Music & Arts Festival"},"displayName":"Outside Lands Music & Arts Festival 2017","ageRestriction":null,"uri":"http://www.songkick.com/festivals/91266-outside-lands-music-arts/id/29781594-outside-lands-music--arts-festival-2017?utm_source=39427&utm_medium=partner","performance":[{"artist":{"displayName":"Metallica","uri":"http://www.songkick.com/artists/331163-metallica?utm_source=39427&utm_medium=partner","id":331163,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:65f4f0c5-ef9e-490c-aee3-909e7ae6b2ab.json","mbid":"65f4f0c5-ef9e-490c-aee3-909e7ae6b2ab"}]},"displayName":"Metallica","billingIndex":1,"billing":"headline","id":57743054},{"artist":{"displayName":"Gorillaz","uri":"http://www.songkick.com/artists/68043-gorillaz?utm_source=39427&utm_medium=partner","id":68043,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:e21857d5-3256-4547-afb3-4b6ded592596.json","mbid":"e21857d5-3256-4547-afb3-4b6ded592596"}]},"displayName":"Gorillaz","billingIndex":2,"billing":"headline","id":57743064},{"artist":{"displayName":"Lorde","uri":"http://www.songkick.com/artists/6715369-lorde?utm_source=39427&utm_medium=partner","id":6715369,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:8e494408-8620-4c6a-82c2-c2ca4a1e4f12.json","mbid":"8e494408-8620-4c6a-82c2-c2ca4a1e4f12"},{"href":"http://api.songkick.com/api/3.0/artists/mbid:14cd21f6-df8e-4bff-af75-0dcfeb307c5d.json","mbid":"14cd21f6-df8e-4bff-af75-0dcfeb307c5d"}]},"displayName":"Lorde","billingIndex":3,"billing":"headline","id":57743139},{"artist":{"displayName":"alt-J","uri":"http://www.songkick.com/artists/4555533-altj?utm_source=39427&utm_medium=partner","id":4555533,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:fc7bbf00-fbaa-4736-986b-b3ac0266ca9b.json","mbid":"fc7bbf00-fbaa-4736-986b-b3ac0266ca9b"}]},"displayName":"alt-J","billingIndex":4,"billing":"headline","id":57743149},{"artist":{"displayName":"The Who","uri":"http://www.songkick.com/artists/69685-who?utm_source=39427&utm_medium=partner","id":69685,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:9fdaa16b-a6c4-4831-b87c-bc9ca8ce7eaa.json","mbid":"9fdaa16b-a6c4-4831-b87c-bc9ca8ce7eaa"}]},"displayName":"The Who","billingIndex":5,"billing":"headline","id":57743059},{"artist":{"displayName":"Empire of the Sun","uri":"http://www.songkick.com/artists/1911769-empire-of-the-sun?utm_source=39427&utm_medium=partner","id":1911769,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:ac7e838c-3d95-47c2-92a9-81767ad7c217.json","mbid":"ac7e838c-3d95-47c2-92a9-81767ad7c217"}]},"displayName":"Empire of the Sun","billingIndex":6,"billing":"headline","id":57743169},{"artist":{"displayName":"Fleet Foxes","uri":"http://www.songkick.com/artists/592267-fleet-foxes?utm_source=39427&utm_medium=partner","id":592267,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:fa97dd36-1b82-43d7-a6e4-2adeafd59cef.json","mbid":"fa97dd36-1b82-43d7-a6e4-2adeafd59cef"}]},"displayName":"Fleet Foxes","billingIndex":7,"billing":"headline","id":57743164},{"artist":{"displayName":"Queens of the Stone Age","uri":"http://www.songkick.com/artists/479466-queens-of-the-stone-age?utm_source=39427&utm_medium=partner","id":479466,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:7dc8f5bd-9d0b-4087-9f73-dc164950bbd8.json","mbid":"7dc8f5bd-9d0b-4087-9f73-dc164950bbd8"}]},"displayName":"Queens of the Stone Age","billingIndex":8,"billing":"headline","id":57743154},{"artist":{"displayName":"ScHoolboy Q","uri":"http://www.songkick.com/artists/3929726-schoolboy-q?utm_source=39427&utm_medium=partner","id":3929726,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:bce6d667-cde8-485e-b078-c0a05adea36d.json","mbid":"bce6d667-cde8-485e-b078-c0a05adea36d"}]},"displayName":"ScHoolboy Q","billingIndex":9,"billing":"headline","id":57743194},{"artist":{"displayName":"Young the Giant","uri":"http://www.songkick.com/artists/2905251-young-the-giant?utm_source=39427&utm_medium=partner","id":2905251,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:7fe96b15-5608-430e-ad25-77a01353c5d9.json","mbid":"7fe96b15-5608-430e-ad25-77a01353c5d9"}]},"displayName":"Young the Giant","billingIndex":10,"billing":"headline","id":57743199},{"artist":{"displayName":"Tove Lo","uri":"http://www.songkick.com/artists/7561184-tove-lo?utm_source=39427&utm_medium=partner","id":7561184,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:56756959-1e78-429c-b897-e1d056cb0225.json","mbid":"56756959-1e78-429c-b897-e1d056cb0225"}]},"displayName":"Tove Lo","billingIndex":11,"billing":"headline","id":57743229},{"artist":{"displayName":"Vance Joy","uri":"http://www.songkick.com/artists/6148694-vance-joy?utm_source=39427&utm_medium=partner","id":6148694,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:df36f6db-5987-46ed-9d02-0cf36ed4e060.json","mbid":"df36f6db-5987-46ed-9d02-0cf36ed4e060"}]},"displayName":"Vance Joy","billingIndex":12,"billing":"headline","id":57743214},{"artist":{"displayName":"Belle and Sebastian","uri":"http://www.songkick.com/artists/140046-belle-and-sebastian?utm_source=39427&utm_medium=partner","id":140046,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:e5c7b94f-e264-473c-bb0f-37c85d4d5c70.json","mbid":"e5c7b94f-e264-473c-bb0f-37c85d4d5c70"}]},"displayName":"Belle and Sebastian","billingIndex":13,"billing":"headline","id":57743179},{"artist":{"displayName":"A Tribe Called Quest","uri":"http://www.songkick.com/artists/90666-a-tribe-called-quest?utm_source=39427&utm_medium=partner","id":90666,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:9689aa5a-4471-4fb4-9721-07cecda0fa9f.json","mbid":"9689aa5a-4471-4fb4-9721-07cecda0fa9f"}]},"displayName":"A Tribe Called Quest","billingIndex":14,"billing":"headline","id":57743144},{"artist":{"displayName":"The Avett Brothers","uri":"http://www.songkick.com/artists/348455-avett-brothers?utm_source=39427&utm_medium=partner","id":348455,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:0a176d0a-ef46-4e7f-b018-9f4d65614668.json","mbid":"0a176d0a-ef46-4e7f-b018-9f4d65614668"}]},"displayName":"The Avett Brothers","billingIndex":15,"billing":"headline","id":57743174},{"artist":{"displayName":"Little Dragon","uri":"http://www.songkick.com/artists/2561-little-dragon?utm_source=39427&utm_medium=partner","id":2561,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:c8a9ae11-63bf-409b-8bf3-a96b3712a2ff.json","mbid":"c8a9ae11-63bf-409b-8bf3-a96b3712a2ff"}]},"displayName":"Little Dragon","billingIndex":16,"billing":"headline","id":57743209},{"artist":{"displayName":"Sleigh Bells","uri":"http://www.songkick.com/artists/145291-sleigh-bells?utm_source=39427&utm_medium=partner","id":145291,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:95f7536d-b2f7-4087-8668-a663ec201f5a.json","mbid":"95f7536d-b2f7-4087-8668-a663ec201f5a"}]},"displayName":"Sleigh Bells","billingIndex":17,"billing":"headline","id":57743239},{"artist":{"displayName":"James Vincent McMorrow","uri":"http://www.songkick.com/artists/2446716-james-vincent-mcmorrow?utm_source=39427&utm_medium=partner","id":2446716,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:3b7b1fd3-6952-4aa8-9467-40b105d1039b.json","mbid":"3b7b1fd3-6952-4aa8-9467-40b105d1039b"}]},"displayName":"James Vincent McMorrow","billingIndex":18,"billing":"headline","id":57743299},{"artist":{"displayName":"Real Estate","uri":"http://www.songkick.com/artists/658329-real-estate?utm_source=39427&utm_medium=partner","id":658329,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:2ff0dfc6-0542-4bbc-a44a-60605c074ba6.json","mbid":"2ff0dfc6-0542-4bbc-a44a-60605c074ba6"}]},"displayName":"Real Estate","billingIndex":19,"billing":"headline","id":57743289},{"artist":{"displayName":"Warpaint","uri":"http://www.songkick.com/artists/715080-warpaint?utm_source=39427&utm_medium=partner","id":715080,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:cf82a38f-9413-4333-bacb-ca5b6db95794.json","mbid":"cf82a38f-9413-4333-bacb-ca5b6db95794"}]},"displayName":"Warpaint","billingIndex":20,"billing":"headline","id":57743269},{"artist":{"displayName":"Above & Beyond","uri":"http://www.songkick.com/artists/81224-above-and-beyond?utm_source=39427&utm_medium=partner","id":81224,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:370bd5a3-4abf-4356-8576-3a8fc0c11d65.json","mbid":"370bd5a3-4abf-4356-8576-3a8fc0c11d65"}]},"displayName":"Above & Beyond","billingIndex":21,"billing":"headline","id":57743159},{"artist":{"displayName":"Future Islands","uri":"http://www.songkick.com/artists/508989-future-islands?utm_source=39427&utm_medium=partner","id":508989,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:74963434-dcb6-4b14-98cc-99873b06db66.json","mbid":"74963434-dcb6-4b14-98cc-99873b06db66"}]},"displayName":"Future Islands","billingIndex":22,"billing":"headline","id":57743189},{"artist":{"displayName":"Action Bronson","uri":"http://www.songkick.com/artists/4276611-action-bronson?utm_source=39427&utm_medium=partner","id":4276611,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:031bc934-28c9-491a-8648-c078450187dc.json","mbid":"031bc934-28c9-491a-8648-c078450187dc"}]},"displayName":"Action Bronson","billingIndex":23,"billing":"headline","id":57743234},{"artist":{"displayName":"Rebelution","uri":"http://www.songkick.com/artists/405316-rebelution?utm_source=39427&utm_medium=partner","id":405316,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:bf225245-fce7-4d30-b648-887cb33529e4.json","mbid":"bf225245-fce7-4d30-b648-887cb33529e4"}]},"displayName":"Rebelution","billingIndex":24,"billing":"headline","id":57743204},{"artist":{"displayName":"Royal Blood","uri":"http://www.songkick.com/artists/1421389-royal-blood?utm_source=39427&utm_medium=partner","id":1421389,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:52c2b5d4-8f0e-4423-ab4d-ace68227ad44.json","mbid":"52c2b5d4-8f0e-4423-ab4d-ace68227ad44"}]},"displayName":"Royal Blood","billingIndex":25,"billing":"headline","id":57743249},{"artist":{"displayName":"RAC","uri":"http://www.songkick.com/artists/301329-rac?utm_source=39427&utm_medium=partner","id":301329,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:73c23fbe-88d3-46fc-a303-f4259b03defe.json","mbid":"73c23fbe-88d3-46fc-a303-f4259b03defe"},{"href":"http://api.songkick.com/api/3.0/artists/mbid:4b75fd73-dddf-4220-96bb-0e595cc03297.json","mbid":"4b75fd73-dddf-4220-96bb-0e595cc03297"},{"href":"http://api.songkick.com/api/3.0/artists/mbid:52ae1bd5-6596-4d71-818a-cd2dc592158c.json","mbid":"52ae1bd5-6596-4d71-818a-cd2dc592158c"}]},"displayName":"RAC","billingIndex":26,"billing":"headline","id":57743294},{"artist":{"displayName":"Solange","uri":"http://www.songkick.com/artists/131614-solange?utm_source=39427&utm_medium=partner","id":131614,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:410e7fd3-b865-4fa0-bb18-1b7fd53382ca.json","mbid":"410e7fd3-b865-4fa0-bb18-1b7fd53382ca"},{"href":"http://api.songkick.com/api/3.0/artists/mbid:ff7103c5-da9e-434d-b8aa-037424ba45ad.json","mbid":"ff7103c5-da9e-434d-b8aa-037424ba45ad"},{"href":"http://api.songkick.com/api/3.0/artists/mbid:6d09a977-af24-4bbb-868b-508886d9e2f8.json","mbid":"6d09a977-af24-4bbb-868b-508886d9e2f8"}]},"displayName":"Solange","billingIndex":27,"billing":"headline","id":57743184},{"artist":{"displayName":"Electric Guest","uri":"http://www.songkick.com/artists/4392868-electric-guest?utm_source=39427&utm_medium=partner","id":4392868,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:01202233-d155-4cfa-83bf-55dc776bc309.json","mbid":"01202233-d155-4cfa-83bf-55dc776bc309"}]},"displayName":"Electric Guest","billingIndex":28,"billing":"headline","id":57743344},{"artist":{"displayName":"Dawes","uri":"http://www.songkick.com/artists/2335213-dawes?utm_source=39427&utm_medium=partner","id":2335213,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:59bc9caa-5700-4c77-9ab7-f089aa7a357f.json","mbid":"59bc9caa-5700-4c77-9ab7-f089aa7a357f"}]},"displayName":"Dawes","billingIndex":29,"billing":"headline","id":57743264},{"artist":{"displayName":"SOHN","uri":"http://www.songkick.com/artists/6174334-sohn?utm_source=39427&utm_medium=partner","id":6174334,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:8014af67-1b04-4123-8b02-6ca85840c514.json","mbid":"8014af67-1b04-4123-8b02-6ca85840c514"}]},"displayName":"SOHN","billingIndex":30,"billing":"headline","id":57743339},{"artist":{"displayName":"Kaytranada","uri":"http://www.songkick.com/artists/6699424-kaytranada?utm_source=39427&utm_medium=partner","id":6699424,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:e56aee57-d90e-40cf-a70d-beb70f6f3c69.json","mbid":"e56aee57-d90e-40cf-a70d-beb70f6f3c69"}]},"displayName":"Kaytranada","billingIndex":31,"billing":"headline","id":57743219},{"artist":{"displayName":"Bleachers","uri":"http://www.songkick.com/artists/1535267-bleachers?utm_source=39427&utm_medium=partner","id":1535267,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:1ccd1da1-f6e0-42a7-b222-81051dae89ad.json","mbid":"1ccd1da1-f6e0-42a7-b222-81051dae89ad"}]},"displayName":"Bleachers","billingIndex":32,"billing":"headline","id":57743224},{"artist":{"displayName":"How to Dress Well","uri":"http://www.songkick.com/artists/3011016-how-to-dress-well?utm_source=39427&utm_medium=partner","id":3011016,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:50a5520c-454a-4d5d-ab74-d442b58e7304.json","mbid":"50a5520c-454a-4d5d-ab74-d442b58e7304"}]},"displayName":"How to Dress Well","billingIndex":33,"billing":"headline","id":57743334},{"artist":{"displayName":"Foxygen","uri":"http://www.songkick.com/artists/4469688-foxygen?utm_source=39427&utm_medium=partner","id":4469688,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:913e6848-6865-4717-ac5e-3bd9c22826be.json","mbid":"913e6848-6865-4717-ac5e-3bd9c22826be"}]},"displayName":"Foxygen","billingIndex":34,"billing":"headline","id":57743329},{"artist":{"displayName":"Thundercat","uri":"http://www.songkick.com/artists/4143636-thundercat?utm_source=39427&utm_medium=partner","id":4143636,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:044fd265-79dd-43eb-afc4-8b20becf7e17.json","mbid":"044fd265-79dd-43eb-afc4-8b20becf7e17"}]},"displayName":"Thundercat","billingIndex":35,"billing":"headline","id":57743259},{"artist":{"displayName":"Temples","uri":"http://www.songkick.com/artists/1688790-temples?utm_source=39427&utm_medium=partner","id":1688790,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:3514578c-402a-4825-bd97-a525f31004e6.json","mbid":"3514578c-402a-4825-bd97-a525f31004e6"}]},"displayName":"Temples","billingIndex":36,"billing":"headline","id":57743304},{"artist":{"displayName":"Goldroom","uri":"http://www.songkick.com/artists/1959719-goldroom?utm_source=39427&utm_medium=partner","id":1959719,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:73d91e4c-88f7-4da5-8d18-06fbb4bfcca3.json","mbid":"73d91e4c-88f7-4da5-8d18-06fbb4bfcca3"}]},"displayName":"Goldroom","billingIndex":37,"billing":"headline","id":57743349},{"artist":{"displayName":"Shovels & Rope","uri":"http://www.songkick.com/artists/981579-shovels-and-rope?utm_source=39427&utm_medium=partner","id":981579,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:7f426331-11c0-4c66-aec1-719abe5dd86f.json","mbid":"7f426331-11c0-4c66-aec1-719abe5dd86f"}]},"displayName":"Shovels & Rope","billingIndex":38,"billing":"headline","id":57743254},{"artist":{"displayName":"K.Flay","uri":"http://www.songkick.com/artists/1893389-kflay?utm_source=39427&utm_medium=partner","id":1893389,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:d1fc999f-6184-41a6-bcb1-7c59bf74a6e1.json","mbid":"d1fc999f-6184-41a6-bcb1-7c59bf74a6e1"}]},"displayName":"K.Flay","billingIndex":39,"billing":"headline","id":57743309},{"artist":{"displayName":"Hundred Waters","uri":"http://www.songkick.com/artists/4958983-hundred-waters?utm_source=39427&utm_medium=partner","id":4958983,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:49d461f0-3abf-422e-9569-8813e90074d7.json","mbid":"49d461f0-3abf-422e-9569-8813e90074d7"}]},"displayName":"Hundred Waters","billingIndex":40,"billing":"headline","id":57743354},{"artist":{"displayName":"Bomba Estereo","uri":"http://www.songkick.com/artists/1071095-bomba-estereo?utm_source=39427&utm_medium=partner","id":1071095,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:aea8576d-7ad5-4430-bf2e-63725d80f05c.json","mbid":"aea8576d-7ad5-4430-bf2e-63725d80f05c"}]},"displayName":"Bomba Estereo","billingIndex":41,"billing":"headline","id":57743284},{"artist":{"displayName":"Louis the Child","uri":"http://www.songkick.com/artists/6441739-louis-the-child?utm_source=39427&utm_medium=partner","id":6441739,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:a56f9cc3-1569-4205-8514-9c5c545d724d.json","mbid":"a56f9cc3-1569-4205-8514-9c5c545d724d"}]},"displayName":"Louis the Child","billingIndex":42,"billing":"headline","id":57743244},{"artist":{"displayName":"Lee Fields & The Expressions","uri":"http://www.songkick.com/artists/2435006-lee-fields-and-the-expressions?utm_source=39427&utm_medium=partner","id":2435006,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:1a4c8b49-4a55-4299-b1c8-82e33e319f33.json","mbid":"1a4c8b49-4a55-4299-b1c8-82e33e319f33"}]},"displayName":"Lee Fields & The Expressions","billingIndex":43,"billing":"headline","id":57743399},{"artist":{"displayName":"Rag'n'Bone Man","uri":"http://www.songkick.com/artists/6252829-ragnbone-man?utm_source=39427&utm_medium=partner","id":6252829,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:37993cdf-f61a-488f-8cca-07e03b8aaa02.json","mbid":"37993cdf-f61a-488f-8cca-07e03b8aaa02"}]},"displayName":"Rag'n'Bone Man","billingIndex":44,"billing":"headline","id":57743279},{"artist":{"displayName":"Kali Uchis","uri":"http://www.songkick.com/artists/7338694-kali-uchis?utm_source=39427&utm_medium=partner","id":7338694,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:d0c7656d-8169-4f77-9dbe-b8f24e40105d.json","mbid":"d0c7656d-8169-4f77-9dbe-b8f24e40105d"}]},"displayName":"Kali Uchis","billingIndex":45,"billing":"headline","id":57743379},{"artist":{"displayName":"Noname","uri":"http://www.songkick.com/artists/386403-noname?utm_source=39427&utm_medium=partner","id":386403,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:3425b422-8c43-4fe4-8689-badb6aa139d0.json","mbid":"3425b422-8c43-4fe4-8689-badb6aa139d0"},{"href":"http://api.songkick.com/api/3.0/artists/mbid:9393cc98-b014-493c-bdf1-a643a088f662.json","mbid":"9393cc98-b014-493c-bdf1-a643a088f662"}]},"displayName":"Noname","billingIndex":46,"billing":"headline","id":57743359},{"artist":{"displayName":"Dr. Octagon","uri":"http://www.songkick.com/artists/230923-dr-octagon?utm_source=39427&utm_medium=partner","id":230923,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:3eba5e02-780b-4acd-befb-d23a0c6708dd.json","mbid":"3eba5e02-780b-4acd-befb-d23a0c6708dd"}]},"displayName":"Dr. Octagon","billingIndex":47,"billing":"headline","id":57743274},{"artist":{"displayName":"The Japanese House","uri":"http://www.songkick.com/artists/8552784-japanese-house?utm_source=39427&utm_medium=partner","id":8552784,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:5db88fae-df24-490e-971a-1b3fe8d373ea.json","mbid":"5db88fae-df24-490e-971a-1b3fe8d373ea"}]},"displayName":"The Japanese House","billingIndex":48,"billing":"headline","id":57743394},{"artist":{"displayName":"Frenship","uri":"http://www.songkick.com/artists/8061398-frenship?utm_source=39427&utm_medium=partner","id":8061398,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:b9f0dfa1-7cf1-4e3c-8770-c8bc660c000a.json","mbid":"b9f0dfa1-7cf1-4e3c-8770-c8bc660c000a"}]},"displayName":"Frenship","billingIndex":49,"billing":"headline","id":57743434},{"artist":{"displayName":"Hamilton Leithauser","uri":"http://www.songkick.com/artists/4812378-hamilton-leithauser?utm_source=39427&utm_medium=partner","id":4812378,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:6b82c839-ea15-4d3b-96f1-d1be924e9cb7.json","mbid":"6b82c839-ea15-4d3b-96f1-d1be924e9cb7"}]},"displayName":"Hamilton Leithauser","billingIndex":50,"billing":"headline","id":57743314},{"artist":{"displayName":"Jacob Banks","uri":"http://www.songkick.com/artists/5496118-jacob-banks?utm_source=39427&utm_medium=partner","id":5496118,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:ca4d7350-e835-4af6-9cbd-1e012e597de4.json","mbid":"ca4d7350-e835-4af6-9cbd-1e012e597de4"}]},"displayName":"Jacob Banks","billingIndex":51,"billing":"headline","id":57743444},{"artist":{"displayName":"Porches","uri":"http://www.songkick.com/artists/593368-porches?utm_source=39427&utm_medium=partner","id":593368,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:40a6d66b-8a96-45c8-838c-dd0c346c45ce.json","mbid":"40a6d66b-8a96-45c8-838c-dd0c346c45ce"}]},"displayName":"Porches","billingIndex":52,"billing":"headline","id":57743424},{"artist":{"displayName":"Maggie Rogers","uri":"http://www.songkick.com/artists/5815959-maggie-rogers?utm_source=39427&utm_medium=partner","id":5815959,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:dde26295-8cd4-474c-8740-3edb801b2776.json","mbid":"dde26295-8cd4-474c-8740-3edb801b2776"}]},"displayName":"Maggie Rogers","billingIndex":53,"billing":"headline","id":57743319},{"artist":{"displayName":"Kamaiyah","uri":"http://www.songkick.com/artists/8757604-kamaiyah?utm_source=39427&utm_medium=partner","id":8757604,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:c344fb50-2f55-4dd3-879b-b07f0e5387e1.json","mbid":"c344fb50-2f55-4dd3-879b-b07f0e5387e1"}]},"displayName":"Kamaiyah","billingIndex":54,"billing":"headline","id":57743369},{"artist":{"displayName":"Khruangbin","uri":"http://www.songkick.com/artists/4558473-khruangbin?utm_source=39427&utm_medium=partner","id":4558473,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:aea4c9b9-9f8d-49dc-b2ca-57d6f26e8634.json","mbid":"aea4c9b9-9f8d-49dc-b2ca-57d6f26e8634"}]},"displayName":"Khruangbin","billingIndex":55,"billing":"headline","id":57743364},{"artist":{"displayName":"Grace Mitchell","uri":"http://www.songkick.com/artists/8626209-grace-mitchell?utm_source=39427&utm_medium=partner","id":8626209,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:39dda82d-bdd5-4cd1-88f5-124311340661.json","mbid":"39dda82d-bdd5-4cd1-88f5-124311340661"}]},"displayName":"Grace Mitchell","billingIndex":56,"billing":"headline","id":57743419},{"artist":{"displayName":"Lawrence","uri":"http://www.songkick.com/artists/508423-lawrence?utm_source=39427&utm_medium=partner","id":508423,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:e1a0bbf2-ab13-4edf-8a56-c7ca76338375.json","mbid":"e1a0bbf2-ab13-4edf-8a56-c7ca76338375"},{"href":"http://api.songkick.com/api/3.0/artists/mbid:819a9744-627b-4bf5-92e9-f894b0f252e6.json","mbid":"819a9744-627b-4bf5-92e9-f894b0f252e6"},{"href":"http://api.songkick.com/api/3.0/artists/mbid:cf8e5830-85d0-4afe-92ac-9582eca437bd.json","mbid":"cf8e5830-85d0-4afe-92ac-9582eca437bd"},{"href":"http://api.songkick.com/api/3.0/artists/mbid:a86ee70d-2840-4290-adaf-0456611cd6f9.json","mbid":"a86ee70d-2840-4290-adaf-0456611cd6f9"},{"href":"http://api.songkick.com/api/3.0/artists/mbid:9a2e7212-1f32-4389-9a14-9a7691a8bfa7.json","mbid":"9a2e7212-1f32-4389-9a14-9a7691a8bfa7"}]},"displayName":"Lawrence","billingIndex":57,"billing":"headline","id":57743459},{"artist":{"displayName":"JOSEPH","uri":"http://www.songkick.com/artists/2744746-joseph?utm_source=39427&utm_medium=partner","id":2744746,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:34237319-960f-4d0c-aac8-1b928f93557b.json","mbid":"34237319-960f-4d0c-aac8-1b928f93557b"},{"href":"http://api.songkick.com/api/3.0/artists/mbid:7da82a8d-596b-417b-ba76-f1c36a1c30c8.json","mbid":"7da82a8d-596b-417b-ba76-f1c36a1c30c8"}]},"displayName":"JOSEPH","billingIndex":58,"billing":"headline","id":57743389},{"artist":{"displayName":"Sam Dew","uri":"http://www.songkick.com/artists/8305718-sam-dew?utm_source=39427&utm_medium=partner","id":8305718,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:63df1f4c-5f3e-48f5-8050-c59b5ddebe78.json","mbid":"63df1f4c-5f3e-48f5-8050-c59b5ddebe78"}]},"displayName":"Sam Dew","billingIndex":59,"billing":"headline","id":57743449},{"artist":{"displayName":"MUNA","uri":"http://www.songkick.com/artists/8299488-muna?utm_source=39427&utm_medium=partner","id":8299488,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:93787d7d-f03b-43c9-be65-032941a0932e.json","mbid":"93787d7d-f03b-43c9-be65-032941a0932e"}]},"displayName":"MUNA","billingIndex":60,"billing":"headline","id":57743409},{"artist":{"displayName":"Sofi Tukker","uri":"http://www.songkick.com/artists/8796259-sofi-tukker?utm_source=39427&utm_medium=partner","id":8796259,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:4ac723f4-8be8-4a0d-a3ae-d5dda20f0a9a.json","mbid":"4ac723f4-8be8-4a0d-a3ae-d5dda20f0a9a"}]},"displayName":"Sofi Tukker","billingIndex":61,"billing":"headline","id":57743324},{"artist":{"displayName":"John Moreland","uri":"http://www.songkick.com/artists/2812586-john-moreland?utm_source=39427&utm_medium=partner","id":2812586,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:c62ea4fb-b303-463b-a2a1-ff1cea9b1de5.json","mbid":"c62ea4fb-b303-463b-a2a1-ff1cea9b1de5"}]},"displayName":"John Moreland","billingIndex":62,"billing":"headline","id":57743439},{"artist":{"displayName":"S U R V I V E","uri":"http://www.songkick.com/artists/4789813-s-u-r-v-i-v-e?utm_source=39427&utm_medium=partner","id":4789813,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:9e26116a-2d3b-4765-855f-734e9453a45e.json","mbid":"9e26116a-2d3b-4765-855f-734e9453a45e"}]},"displayName":"S U R V I V E","billingIndex":63,"billing":"headline","id":57743374},{"artist":{"displayName":"The Lemon Twigs","uri":"http://www.songkick.com/artists/8344013-lemon-twigs?utm_source=39427&utm_medium=partner","id":8344013,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:f32d94e8-8d55-4ee2-9077-53d1c024a03b.json","mbid":"f32d94e8-8d55-4ee2-9077-53d1c024a03b"}]},"displayName":"The Lemon Twigs","billingIndex":64,"billing":"headline","id":57743404},{"artist":{"displayName":"Mon Laferte","uri":"http://www.songkick.com/artists/7433509-mon-laferte?utm_source=39427&utm_medium=partner","id":7433509,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:ab966c0f-e526-46ae-b492-82c27b87f81f.json","mbid":"ab966c0f-e526-46ae-b492-82c27b87f81f"}]},"displayName":"Mon Laferte","billingIndex":65,"billing":"headline","id":57743414},{"artist":{"displayName":"mondo cozmo","uri":"http://www.songkick.com/artists/8917484-mondo-cozmo?utm_source=39427&utm_medium=partner","id":8917484,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:9c8cbbb3-aa96-41f3-8e52-3c238c944ad4.json","mbid":"9c8cbbb3-aa96-41f3-8e52-3c238c944ad4"}]},"displayName":"mondo cozmo","billingIndex":66,"billing":"headline","id":57743429},{"artist":{"displayName":"She's","uri":"http://www.songkick.com/artists/2305893-shes?utm_source=39427&utm_medium=partner","id":2305893,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:908e4d54-4971-4d87-be68-3cda457e7a27.json","mbid":"908e4d54-4971-4d87-be68-3cda457e7a27"}]},"displayName":"She's","billingIndex":67,"billing":"headline","id":57743464},{"artist":{"displayName":"Oliver Tree","uri":"http://www.songkick.com/artists/9060964-oliver-tree?utm_source=39427&utm_medium=partner","id":9060964,"identifier":[{"href":"http://api.songkick.com/api/3.0/artists/mbid:1fa3bded-908f-47be-9784-3c9ef850682b.json","mbid":"1fa3bded-908f-47be-9784-3c9ef850682b"}]},"displayName":"Oliver Tree","billingIndex":68,"billing":"headline","id":57743454},{"artist":{"displayName":"Goldroom (Live Set)","uri":"http://www.songkick.com/artists/8606954-goldroom-live-set?utm_source=39427&utm_medium=partner","id":8606954,"identifier":[]},"displayName":"Goldroom (Live Set)","billingIndex":69,"billing":"headline","id":57813754},{"artist":{"displayName":"San Fermin (US)","uri":"http://www.songkick.com/artists/7901684-san-fermin-us?utm_source=39427&utm_medium=partner","id":7901684,"identifier":[]},"displayName":"San Fermin (US)","billingIndex":70,"billing":"headline","id":57743384}],"id":29781594}]},"perPage":50,"page":1,"totalEntries":1}}"""


clipping_search = json.loads(clipping_search_json)
top_artists = json.loads(top_artists_json)
related_1 = json.loads(related_1_json)
related_2 = json.loads(related_2_json)

london = json.loads(london_json)
houston = json.loads(houston_json)
nowhere = json.loads(nowhere_json)
vw_concerts = json.loads(vw_concerts_json)
outside_lands = json.loads(outside_lands_json)
