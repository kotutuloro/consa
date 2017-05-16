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
    }, {
      "external_urls" : {
        "spotify" : "https://open.spotify.com/artist/68oIILqspVnekLF9lk0szn"
      },
      "followers" : {
        "href" : null,
        "total" : 0
      },
      "genres" : [ ],
      "href" : "https://api.spotify.com/v1/artists/68oIILqspVnekLF9lk0szn",
      "id" : "68oIILqspVnekLF9lk0szn",
      "images" : [ ],
      "name" : "Clipping Pounders",
      "popularity" : 0,
      "type" : "artist",
      "uri" : "spotify:artist:68oIILqspVnekLF9lk0szn"
    }, {
      "external_urls" : {
        "spotify" : "https://open.spotify.com/artist/4ZTFj2meuyjmk74UUjJ1V0"
      },
      "followers" : {
        "href" : null,
        "total" : 7
      },
      "genres" : [ ],
      "href" : "https://api.spotify.com/v1/artists/4ZTFj2meuyjmk74UUjJ1V0",
      "id" : "4ZTFj2meuyjmk74UUjJ1V0",
      "images" : [ ],
      "name" : "clipping. feat. jalene goodwin",
      "popularity" : 9,
      "type" : "artist",
      "uri" : "spotify:artist:4ZTFj2meuyjmk74UUjJ1V0"
    }, {
      "external_urls" : {
        "spotify" : "https://open.spotify.com/artist/4atNL7GkDnZEfD20oz5oMn"
      },
      "followers" : {
        "href" : null,
        "total" : 3
      },
      "genres" : [ ],
      "href" : "https://api.spotify.com/v1/artists/4atNL7GkDnZEfD20oz5oMn",
      "id" : "4atNL7GkDnZEfD20oz5oMn",
      "images" : [ ],
      "name" : "clipping. feat. kill rogers",
      "popularity" : 8,
      "type" : "artist",
      "uri" : "spotify:artist:4atNL7GkDnZEfD20oz5oMn"
    }, {
      "external_urls" : {
        "spotify" : "https://open.spotify.com/artist/0TtJyTEX7fq8j2jbXZ9ZsT"
      },
      "followers" : {
        "href" : null,
        "total" : 6
      },
      "genres" : [ ],
      "href" : "https://api.spotify.com/v1/artists/0TtJyTEX7fq8j2jbXZ9ZsT",
      "id" : "0TtJyTEX7fq8j2jbXZ9ZsT",
      "images" : [ ],
      "name" : "clipping. feat. ezra buchla",
      "popularity" : 7,
      "type" : "artist",
      "uri" : "spotify:artist:0TtJyTEX7fq8j2jbXZ9ZsT"
    }, {
      "external_urls" : {
        "spotify" : "https://open.spotify.com/artist/2PuU523omVAOhEjVrlaQRv"
      },
      "followers" : {
        "href" : null,
        "total" : 4
      },
      "genres" : [ ],
      "href" : "https://api.spotify.com/v1/artists/2PuU523omVAOhEjVrlaQRv",
      "id" : "2PuU523omVAOhEjVrlaQRv",
      "images" : [ ],
      "name" : "clipping. feat. kill rogers & TiVO",
      "popularity" : 11,
      "type" : "artist",
      "uri" : "spotify:artist:2PuU523omVAOhEjVrlaQRv"
    } ],
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
                      "date": "2010-02-17"
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


clipping_search = json.loads(clipping_search_json)
top_artists = json.loads(top_artists_json)
related_1 = json.loads(related_1_json)
related_2 = json.loads(related_2_json)
vw_concerts = json.loads(vw_concerts_json)
