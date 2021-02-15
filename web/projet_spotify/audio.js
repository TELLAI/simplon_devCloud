let playButton = document.querySelector(".play");
let suivantButton = document.querySelector(".suivant");
let precedentButton = document.querySelector(".precedent");
let imageTrack = document.querySelector(".track_image");
let artist = document.querySelector(".artist");
let title = document.querySelector(".title");
let volume_show = document.querySelector("#volume_show");
let recent_volume = document.querySelector("#volume");
let show_duration = document.querySelector("#show_duration");
let slider = document.querySelector("#duration_slider");
let track_duration = document.querySelector("#track_duration");
var seekSlider = document.getElementById("#duration_slider");
let currentTimeContainer = document.getElementById("#current-time");
let totalTimeContainer = document.getElementById("#total-time");

let track = document.createElement("audio");
track.setAttribute("id", "myAudio");

let num_index = 0;
let playing_song = false;

let all_song = [
  {
    name: "Chacun ses raisons",
    path: "music/chacun-ses-raisons.mp3",
    picture: "img/niro.png",
    singer: "NIRO",
  },
  {
    name: "500€",
    path: "music/rimk-500-eur.mp3",
    picture: "img/rimk.jpg",
    singer: "RIMK",
  },
  {
    name: "La fierté des nôtres",
    path: "music/fierte.mp3",
    picture: "img/rohff.jpg",
    singer: "ROHFF",
  },
  {
    name: "La tête dans les nuages",
    path: "music/nuage.mp3",
    picture: "img/jul2.jpg",
    singer: "JUL",
  },
  {
    name: "Esmeralda",
    path: "music/ezzahi.mp3",
    picture: "img/ammar_ezzahi.jpeg",
    singer: "AMMAR EZZAHI",
  },
  {
    name: "California love",
    path: "music/california-love.mp3",
    picture: "img/tupac2.jpg",
    singer: "TUPAC",
  },
  {
    name: "Temps d'avant",
    path: "music/temps-davant.mp3",
    picture: "img/jul2.jpg",
    singer: "JUL",
  },
  {
    name: "Imagine",
    path: "music/imagine.mp3",
    picture: "img/john_lennon.jpg",
    singer: "JOHN LENNON",
  },
  {
    name: "Hotel California",
    path: "music/hotel-california-2013-remaster.mp3",
    picture: "img/eagles.jpg",
    singer: "EAGLES",
  },
  {
    name: "Reflets D'esprit",
    path: "music/smala.mp3",
    picture: "img/smala.jpg",
    singer: "LA SMALA",
  },
  {
    name: "Californication",
    path: "music/californication.mp3",
    picture: "img/red2.jpg",
    singer: "RED HOT CHILI PEPPERS",
  },
  {
    name: "Pour ceux",
    path: "music/pour-ceux.mp3",
    picture: "img/mafia.jpeg",
    singer: "MAFIA K1 FRY",
  },
  {
    name: "Du fond du coeur",
    path: "music/coeur.mp3",
    picture: "img/rohff.jpg",
    singer: "ROHFF",
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
  if (playing_song == false) {
    playSong();
  } else {
    pauseSong();
  }
}

function playSong() {
  track.play();
  playing_song = true;
  playButton.innerHTML = '<i class="fas fa-pause"></i>';
}

function pauseSong() {
  track.pause();
  playing_song = false;
  playButton.innerHTML = '<i class="fas fa-play"></i>';
}

function nextSong() {
  if (num_index < all_song.length - 1) {
    num_index += 1;
    player(num_index);
    playSong();
  } else {
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
  } else {
    num_index = all_song.length - 1;
    player(num_index);
    playSong();
  }
}
function mute_sound() {
  track.volume = 0;
  volume.value = 0;
  volume_show.innerHTML = 0;
}
function volume_change() {
  volume_show.innerHTML = recent_volume.value;
  track.volume = recent_volume.value / 100;
}
function reset_slider() {
  slider.value = 0;
}

function convertElapsedTime(inputSeconds) {
  var secondes = Math.floor(inputSeconds % 60);
  if (secondes < 10) {
    secondes = "0" + secondes;
  }
  var minutes = Math.floor(inputSeconds / 60);
  return minutes + ":" + secondes;
}

myAudio.addEventListener("loadedmetadata", function () {
  totalTimeContainer.innerHTML = convertElapsedTime(track.duration);
  currentTimeContainer.innerHTML = convertElapsedTime(track.currentTime);
  seekSlider.max = track.duration;
  seekSlider.setAttribute("value", track.currentTime);
});

myAudio.addEventListener("timeupdate", function () {
  currentTimeContainer.innerHTML = convertElapsedTime(track.currentTime);
  seekSlider.setAttribute("value", track.currentTime);
  seekSlider.value = track.currentTime;
});
