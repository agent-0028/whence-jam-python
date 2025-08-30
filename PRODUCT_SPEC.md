# Product Specification

## Value Statement

As someone who gets lots of music recommendations from friends, I want a way to keep track of who recommended what so I can give them positive vibes when I like the music.

## Milestones

### Phase One

* There is a command line application that can be run locally by checking out this repository
* The user can specify the name of a song or album and a person recommending it
* The song or album title will be used to search the Spotify music database
* The application will store
  * a link to the song or album on Spotify
  * the name of the person who recommended it
  * the current date
* The user can list all previously stored jams, sorted by date descending

### Phase Two

* There is a simple web site
* The web site has a form with a field for a song title and a person that recommended it
* When the form is submitted the song or album title will be used to search the Spotify music database
* The application will store
  * a link to the song or album on Spotify
  * the name of the person who recommended it
  * the current date
* A list will be shown below the form with all previous entries, sorted by date descending

### Phase Three

* There is a REST API
* The REST API has an end point that accepts a song or album name and the name of a person that recommended it
* When end point is called the song or album title will be used to search the Spotify music database
* The application will store
  * a link to the song or album on Spotify
  * the name of the person who recommended it
  * the current date
* There is an end point that lists all previous entries, sorted by date descending
