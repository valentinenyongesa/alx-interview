#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movieId>');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

console.log('API URL:', apiUrl); // Debugging output

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch movie data. Status code: ${response.statusCode}`);
    return;
  }

  try {
    const filmData = JSON.parse(body);
    const charactersUrls = filmData.characters;

    if (!charactersUrls || charactersUrls.length === 0) {
      console.error('No characters found for this movie.');
      return;
    }

    // Function to fetch and print character names
    const printCharacterNames = async () => {
      for (const characterUrl of charactersUrls) {
        try {
          const characterResponse = await fetch(characterUrl);
          const characterData = await characterResponse.json();
          console.log(characterData.name);
        } catch (fetchError) {
          console.error('Error fetching character:', fetchError);
        }
      }
    };

    printCharacterNames();
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});
