let playButton = document.querySelector(".play");
let pauseButton = document.querySelector(".pause");
let suivantButton = document.querySelector(".suivant");
let precedentButton = document.querySelector(".precedent");
let imageTrack = document.querySelector(".track_image");
let artist = document.querySelector(".artist");
let title = document.querySelector(".title");
let volume_show = document.querySelector("#volume_show");
let track = document.createElement("audio");

let num_index = 1;
let playing_song = false;

let all_song = [
  {
    name: "Chacun ses raisons",
    path: "music/chacun-ses-raisons.mp3",
    picture: "img/NIRO.jpg",
    singer: "NIRO",
  },
  {
    name: "500euros",
    path: "music/rimk-500-eur.mp3",
    picture: "img/rimk.jpg",
    singer: "RIMK",
  },
  {
    name: "California love",
    path: "music/california-love.mp3",
    picture: "img/tupac.jpg",
    singer: "TUPAC",
  },
  {
    name: "Temps d'avant",
    path: "music/temps-davant.mp3",
    picture: "img/jul.jpg",
    singer: "JUL",
  },
  {
    name: "Californication",
    path: "music/californiacation.mp3",
    picture: "img/red_hill.jpg",
    singer: "RED HOT CHILI PEPPERS",
  },
  {
    name: "Pour ceux",
    path: "music/pour-ceux.mp3",
    picture: "img/Mafia-k1-fry-logo.jpg",
    singer: "MAFIA K1 FRY",
  },
  {
    name: "Je commence tout doux",
    path: "music/je-commence.mp3",
    picture: "img/misteryou.jpg",
    singer: "MISTERYOU",
  },
];

function player(num_index) {
  track.src = all_song[num_index].path;
  title.innerHTML = all_song[num_index].name;
  imageTrack.src = all_song[num_index].picture;
  artist.innerHTML = all_song[num_index].singer;
  track.load();
  console.log(all_song[num_index].name);
}
player(num_index);

function justPlay() {
    if (playing_song == false){
        playSong();
    }
    else{
        pauseSong();
    }
}

function playSong() {
  track.play();
  playing_song = true;
}

function pauseSong() {
  track.pause();
  playing_song = false;
}

function nextSong() {
  if (num_index < all_song.length - 1) {
    num_index += 1;
    player(num_index);
    playSong();
  }
  else{
      num_index = 0;
      player(num_index);
      playSong();
  }
}

function backSong() {
    if (num_index > 0) {
        num_index -= 1;
        player(num_index);
        playSong();
    }
    else{
        num_index = all_song.length - 1;
        player(num_index);
        playSong();
    }
}
