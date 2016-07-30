import fresh_tomatoes
import media

# List of My Favorite Movies
law_abiding_citizen = media.Movie("Law Abiding Citizen",
                                  "A frustrated man decides to take justice \
                                  into his own hands after a plea bargain \
                                  sets one of his family's killers free.",
                                  "http://www.reviewstl.com/wp-content/uploads/2009/10/law-abiding-citizen-movie-poster.jpg", # noqa  
                                  "https://www.youtube.com/watch?v=LX6kVRsdXW4"
                                  ,media.Movie.VALID_RATINGS[3])

guardians_of_the_galaxy = media.Movie("Guardians of the Galaxy",
                                      "Brash space adventurer Peter Quill, \
                                      finds himself the quarry of relentless \
                                      bounty hunters after he steals an orb \
                                      coveted by Ronan, a powerful villain.",
                                      "http://smartbitchestrashybooks.com/images/uploads/GuardiansGalaxe.jpg", # noqa  
                                      "https://www.youtube.com/watch?v=2LIQ2-PZBC8"
                                      ,media.Movie.VALID_RATINGS[2])  

dark_knight = media.Movie("The Dark Knight",
                          "With the help of allies Lt. Jim Gordon, and DA \
                          Harvey Dent, Batman has been able to keep a tight \
                          lid on crime in Gotham City. But when a vile young \
                          criminal calling himself the Joker, suddenly throws \
                          the town into chaos.",
                          "http://host.trivialbeing.org/up/tdk-jul1-dark-knight-poster-stupidbats.jpg", # noqa  
                          "https://www.youtube.com/watch?v=EXeTwQWrcwY",
                          media.Movie.VALID_RATINGS[2])

finding_nemo = media.Movie("Finding Nemo",
                           "Marlin, a clown fish, is overly cautious with his \
                           son, Nemo, who has a foreshortened fin. When Nemo \
                           swims too close to the surface to prove himself, \
                           he is caught by a diver, and horrified Marlin must \
                           set out to find him.",
                           "http://i.huffpost.com/gen/636781/original.jpg", 
                           "https://www.youtube.com/watch?v=2zLkasScy7A",
                           media.Movie.VALID_RATINGS[1])

the_wolf_of_wall_street = media.Movie("The Wolf of Wall Street",
                                      "In 1987, Jordan Belfore takes an \
                                      entry-level job at a Wall Street \
                                      brokerage firm. By the early 1990s, \
                                      while still in his 20s, Belfort founds \
                                      his own firm, Stratton Oakmont. \
                                      Together with his trusted lieutenant \
                                      and a merry band of brokers.",
                                      "http://cdn2.gbtimes.com/cdn/farfuture/7ioYXeoP0jyN23yX7PM0Bu7wi0A-YBwhSbkwUtH2wFA/mtime:1390289000/sites/default/files/styles/1280_wide/public/2014/01/20/thewolfofwallstreet.jpg?itok=gHJUwj_1", # noqa
                                      "https://www.youtube.com/watch?v=iszwuX1AK6A", # noqa  
                                      media.Movie.VALID_RATINGS[3])

creed = media.Movie("Creed",
                    "Adonis Johnson never knew his famous father, boxing \
                    champion Apollo Creed, who died before Adonis was born.\
                    However, boxing is in his blood, so he seeks out Rocky  \
                    Balboa  and asks the retired champ to be his trainer.56",
                    "http://cdn2-www.comingsoon.net/assets/uploads/gallery/creed/creedpostersmall.jpg", # noqa  
                    "https://www.youtube.com/watch?v=Uv554B7YHk4",
                    media.Movie.VALID_RATINGS[2])

# Recall all listed movies via HTML Page
movies = [law_abiding_citizen, guardians_of_the_galaxy, dark_knight,
          finding_nemo, the_wolf_of_wall_street, creed]
fresh_tomatoes.open_movies_page(movies)




