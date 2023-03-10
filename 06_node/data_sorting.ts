import { readdirSync } from 'fs';

/**
 * Q: Write a function / code snippet that does the following:
 *
 * Given a folder `/tmp/files` that contains audio and video files,
 * record the trackTitle, genre, full filePath
 * in the db, each under the correct category based on media type (audio or video).
 *
 * The following assumptions can be made:
 *  - the files are currently sorted in folders based on genre
 *  - the name of the file is also the trackTitle
 *  - if you listed the contents of `/tmp/files` it would look something like this:
 *      /tmp/files/rock/title1.mp3
 *      /tmp/files/soul/title2.mp4
 *      /tmp/files/rock/title5.mp4
 *      /tmp/files/pop/title4.mp3
 *      /tmp/files/pop/title6.mp3
 *      /tmp/files/country/title7.mp3
 *      /tmp/files/country/title8.mp4
 *      /tmp/files/pop/title9.mp4
 *      /tmp/files/jazz/title10.mp3
 *      /tmp/files/pop/title11.mp3
 */

/**
 * Stubbed out function that would theoretically save `data` to the db
 * under the provided category
 * @param dbCollection - should be the media type (audio | video)
 * @param data - data about the song or video: trackTitle, filePath, genre
 * @returns empty Promises
 */
const saveToDb = async (
  category: 'audio' | 'videos',
  data: {
    trackTitle: string;
    filePath: string;
    genre: string;
  },
) => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      console.log(
        `Pretend I'm saving file data ${JSON.stringify(
          data,
        )} to a DB under category ${category}`,
      );
      if (!data.trackTitle || !data.filePath || !data.genre)
        reject('invalid data');
      else resolve('empty');
    }, 500);
  });
};

/**
 * Write your code here. Feel free to use `saveToDb` as the API/function that does "save to the database"
 */
