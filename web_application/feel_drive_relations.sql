create table relations
(
  title    varchar(150) not null,
  username varchar(100) not null,
  feeling  varchar(20)  null,
  primary key (title, username),
  constraint relations_songs_title_fk
    foreign key (title) references songs (title),
  constraint relations_users_username_fk
    foreign key (username) references users (username)
);

INSERT INTO `feel&drive`.relations (title, username, feeling) VALUES ('Ascension - Flatbush ZOMBIES.mp3', 'admin', 'Motivational');
INSERT INTO `feel&drive`.relations (title, username, feeling) VALUES ('Boombastic - Shaggy.mp3', 'admin', 'Happiness');
INSERT INTO `feel&drive`.relations (title, username, feeling) VALUES ('Happy - Pharrell Williams.mp3', 'admin', 'Happiness');
INSERT INTO `feel&drive`.relations (title, username, feeling) VALUES ('Stir It Up - Bob Marley and the Wailers.mp3', 'admin', 'Happiness');
INSERT INTO `feel&drive`.relations (title, username, feeling) VALUES ('Superman - Roberto Molinaro.mp3', 'admin', 'Party');
create table songs
(
  title   varchar(100) not null
    primary key,
  feeling varchar(50)  not null
);

INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('1 Train - ASAP Rocky ft Kendrick Lamar, Joey Badass, YelaWolf, Danny Brown, Action Bronson.mp3', 'Motivational');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Ascension - Flatbush ZOMBIES.mp3', 'Motivational');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Be Quiet And Drive Far Away - Deftones.mp3', 'Motivational');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Bla Bla Bla - Gigi D''Agostino.mp3', 'Party');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Bollicine - Vasco Rossi.mp3', 'Happiness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Boombastic - Shaggy.mp3', 'Happiness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Born Slippy Trainspotting - Underworld.mp3', 'Party');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Bounce - Flatbush ZOMBiES.mp3', 'Motivational');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Break Stuff - Limp Bizkit.mp3', 'Motivational');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Buffalo Soldier - Bob Marley and the Wailers.mp3', 'Happiness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Bum Bum Tam Tam - Mc Fioti Future J Balvin Stefflon Don Juan Magan.mp3', 'Party');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Camorra - Nicky Romero.mp3', 'Party');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Check yo Self Remix - Ice Cube.mp3', 'Happiness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Chill Bill Remix ft DRAM Denzel Curry and Cousin Stizz.mp3', 'Motivational');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Chunky - FormatB.mp3', 'Party');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('City of Angels - 30 Seconds to Mars.mp3', 'Sadness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Claudia Lewis - M83.mp3', 'Happiness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Completamente - Thegiornalisti.mp3', 'Sadness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Could You Be Loved - Bob Marley and the Wailers.mp3', 'Happiness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Crapling Bonfire.mp3', 'Relax');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Dancing Queen - Abba.mp3', 'Happiness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Dead Bodies Everywhere - Korn.mp3', 'Motivational');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Deviazioni - Vasco Rossi.mp3', 'Happiness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Disperato - Thegiornalisti.mp3', 'Sadness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Dont Stop Me Now - Queen.mp3', 'Happiness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Down With The Sickness - Disturbed.mp3', 'Motivational');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Elephant - Tame Impala.mp3', 'Motivational');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Everybody hurts - REM.mp3', 'Sadness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Exodus - Bob Marley and the Wailers.mp3', 'Happiness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Fatto Di Te - Thegiornalisti.mp3', 'Sadness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Fegato, Fegato Spappolato - Vasco Rossi.mp3', 'Happiness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Gli Alberi - Thegiornalisti.mp3', 'Sadness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Guaranteed - Eddie Vedder.mp3', 'Sadness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Happy - Pharrell Williams.mp3', 'Happiness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Here Comes The Hotstepper - Ini Kamoze.mp3', 'Happiness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Hostile - Erick Sermon Ft Keith Murray.mp3', 'Happiness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Hurt - Johnny Cash.mp3', 'Sadness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('I Still Haven''t Found What I''m Looking For - U2.mp3', 'Sadness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('I''m Gonna Be 500 Miles  -The Proclaimers.mp3', 'Happiness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Il Tuo Maglione Mio - Thegiornalisti.mp3', 'Sadness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('In The End - Linkin Park.mp3', 'Motivational');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Inner Peace.mp3', 'Relax');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Intro - M83.mp3', 'Sadness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Is This Love - Bob Marley and the Wailers.mp3', 'Happiness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Jamming - Bob Marley and the Wailers.mp3', 'Happiness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Killing In the Name - Rage Against The Machine.mp3', 'Motivational');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('L''Ultimo Grido Della Notte - Thegiornalisti.mp3', 'Sadness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('La Vie En Rose - Cristin Milioti.mp3', 'Sadness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Lord Pretty Flacko Jodye 2 - A$AP Rocky.mp3', 'Motivational');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Losing It - Fisher.mp3', 'Party');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Lovers in Japan - Coldplay.mp3', 'Sadness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Mad World - Gary Jules.mp3', 'Sadness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Midnight - Coldplay.mp3', 'Sadness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Midnight City - M83.mp3', 'Happiness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Mont Blanc - Boris Brejcha.mp3', 'Party');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('My My Hey Hey - Neil Young.mp3', 'Sadness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Night Lovell - Still Cold (Prod Dylan Brady).mp3', 'Motivational');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('No Woman No Cry [Live] - Bob Marley and the Wailers.mp3', 'Happiness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Numb - Linkin Park.mp3', 'Motivational');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Nuvole Bianche -Ludovico Einaudi.mp3', 'Relax');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Ogni Volta - Vasco Rossi.mp3', 'Sadness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('One Love - Bob Marley and the Wailers.mp3', 'Happiness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('One Love - Nas.mp3', 'Happiness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('One Step Closer - Linkin Park.mp3', 'Motivational');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Papa Roach - Scars.mp3', 'Motivational');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Platypus (I hate you) - Green Day.mp3', 'Motivational');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Punky Reggae Party - Bob Marley & the Wailers.mp3', 'Happiness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Raconte moi une histoire - M83.mp3', 'Happiness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Redemption Song - Bob Marley and the Wailers.mp3', 'Happiness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Relaxing Piano.mp3', 'Relax');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Revolte - Paul Kalkbrenner.mp3', 'Party');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Round and Round - Imagine Dragons.mp3', 'Happiness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Satisfy My Soul - Bob Marley and the Wailers.mp3', 'Happiness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Sbagliare A Vivere - Thegiornalisti.mp3', 'Sadness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Sea Waves.mp3', 'Relax');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('September - Earth Wind & Fire.mp3', 'Happiness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Shook Ones Part II - Mobb Deep.mp3', 'Motivational');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Smells Like Teen Spirit - Nirvana.mp3', 'Motivational');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Smile - David Gilmour.mp3', 'Sadness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('So Whatcha Sayin - EPMD.mp3', 'Happiness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Society - Eddie Vedder.mp3', 'Sadness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Sold Out - Thegiornalisti.mp3', 'Sadness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Soon, my friend - M83.mp3', 'Sadness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Stir It Up - Bob Marley and the Wailers.mp3', 'Happiness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('SUMO - Denzel Curry.mp3', 'Motivational');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Sun Is Shining - Funkstar De Luxe (Firebeatz Remix).mp3', 'Party');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Sundress - ASAP Rocky.mp3', 'Happiness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Superman - Roberto Molinaro.mp3', 'Party');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Survival Of The Fittest - Mobb Deep.mp3', 'Motivational');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('The Forest Awakens.mp3', 'Relax');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('The Octopuss - Len Faki & Johannes Heil.mp3', 'Party');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('The Sky Is The Limit - Boris Brejcha.mp3', 'Party');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('The Sound of Silence - Simon & Garfunkel.mp3', 'Sadness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('This bright flash - M83.mp3', 'Happiness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Three Little Birds  - Bob Marley and the Wailers.mp3', 'Happiness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Till I Collapse - Eminem.mp3', 'Motivational');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Tra La Strada E Le Stelle - Thgiornalisti.mp3', 'Sadness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('ULT - Denzel Curry.mp3', 'Motivational');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Ultimate - Denzel Curry.mp3', 'Motivational');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Up in Flames - Coldplay.mp3', 'Sadness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Uptown Girl - Billy Joel.mp3', 'Happiness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Vacaciones en Chile - Ilario Alicante.mp3', 'Party');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Vieni E Cambiami La Vita - Thegiornalisti.mp3', 'Sadness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Wait - M83.mp3', 'Sadness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Waiting In Vain - Bob Marley & the Wailers.mp3', 'Happiness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Welcome To The Jungle - Guns ''N Roses.mp3', 'Motivational');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('What I''ve Done - Linkin Park.mp3', 'Motivational');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Wide Open - DJ Hyperactive (Len Faki DJ Edit).mp3', 'Party');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Xavier Rudd - Follow The Sun.mp3', 'Sadness');
INSERT INTO `feel&drive`.songs (title, feeling) VALUES ('Ya Kidding - Fisher.mp3', 'Party');
create table users
(
  username varchar(100) not null,
  password varchar(50)  not null,
  color    int          null,
  constraint users_username_uindex
    unique (username)
);

alter table users
  add primary key (username);

INSERT INTO `feel&drive`.users (username, password, color) VALUES ('a', 'a', 8000);
INSERT INTO `feel&drive`.users (username, password, color) VALUES ('admin', 'admin', 0);
INSERT INTO `feel&drive`.users (username, password, color) VALUES ('marco', 'marco', 8000);
INSERT INTO `feel&drive`.users (username, password, color) VALUES ('pietro', 'pietro', 0);
INSERT INTO `feel&drive`.users (username, password, color) VALUES ('simone', 'simone', 22000);